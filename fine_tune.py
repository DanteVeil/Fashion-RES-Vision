# fine_tune.py

import torch
from torch.utils.data import Dataset, DataLoader
from transformers import ViTImageProcessor, ViTForImageClassification, TrainingArguments, Trainer
from PIL import Image
import pandas as pd
import os
import kagglehub

# --- 1. Automated Dataset Download ---
print("Downloading fashion dataset from Kaggle Hub...")
# This will download and unzip the dataset, then return the path to the folder
try:
    dataset_path = kagglehub.dataset_download("paramaggarwal/fashion-product-images-small")
    print(f"Dataset downloaded to: {dataset_path}")
except Exception as e:
    print(f"Failed to download dataset. Error: {e}")
    print("Please ensure you have authenticated with Kaggle. This typically requires a 'kaggle.json' file in your user directory.")
    exit()

# --- 2. Create a Custom PyTorch Dataset Class ---
class FashionDataset(Dataset):
    """Custom dataset for loading fashion product images."""
    def __init__(self, csv_file, img_dir, processor, limit=None):
        try:
            self.img_labels = pd.read_csv(csv_file, on_bad_lines='skip')
        except FileNotFoundError:
            print(f"Error: The file {csv_file} was not found inside the downloaded dataset.")
            exit()
            
        if limit:
            self.img_labels = self.img_labels.sample(n=limit, random_state=42)

        self.img_dir = img_dir
        self.processor = processor
        
        # Create a mapping from category name to a unique integer ID
        self.labels = self.img_labels['masterCategory'].unique()
        self.label_to_id = {label: i for i, label in enumerate(self.labels)}
        self.id_to_label = {i: label for i, label in enumerate(self.labels)}

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        # Construct the image path
        img_id = self.img_labels.iloc[idx]['id']
        img_path = os.path.join(self.img_dir, f"{img_id}.jpg")
        
        try:
            image = Image.open(img_path).convert("RGB")
            label_name = self.img_labels.iloc[idx]['masterCategory']
            label_id = self.label_to_id[label_name]
            
            # Use the ViT processor to prepare the image for the model
            inputs = self.processor(images=image, return_tensors="pt")
            # The trainer expects a flat tensor, not a batch of one
            inputs['pixel_values'] = inputs['pixel_values'].squeeze(0)
            inputs['labels'] = torch.tensor(label_id)
            return inputs
        except (FileNotFoundError, UnboundLocalError):
            # If an image is missing from the dataset, just get the next one
            print(f"Warning: Image for ID {img_id} not found. Skipping.")
            return self.__getitem__((idx + 1) % len(self))

# --- 3. Set up and run the training ---
if __name__ == '__main__':
    # Define paths using the path returned by kagglehub
    CSV_PATH = os.path.join(dataset_path, 'styles.csv')
    IMG_DIR = os.path.join(dataset_path, 'images')
    
    # Load the image processor from the pre-trained model
    processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
    
    print("Loading and preparing dataset...")
    # Using a small sample of 1000 images for a quick example. Increase this for better accuracy.
    full_dataset = FashionDataset(csv_file=CSV_PATH, img_dir=IMG_DIR, processor=processor, limit=1000)

    print("Loading pre-trained Vision Transformer model...")
    model = ViTForImageClassification.from_pretrained(
        'google/vit-base-patch16-224-in21k',
        num_labels=len(full_dataset.labels),
        label2id=full_dataset.label_to_id,
        id2label=full_dataset.id_to_label,
        ignore_mismatched_sizes=True # This is crucial for transfer learning!
    )
    
    # Define the training arguments
    training_args = TrainingArguments(
        output_dir='./fashion_model_checkpoints', # Directory to save model checkpoints
        per_device_train_batch_size=16,
        num_train_epochs=3, # 3 epochs is a good starting point for fine-tuning
        save_steps=500,
        save_total_limit=2,
        logging_dir='./training_logs',
        report_to="none" # Disables online logging services like wandb
    )
    
    # A simple data collator to batch our items together
    def collate_fn(data):
        return {
            'pixel_values': torch.stack([f['pixel_values'] for f in data]),
            'labels': torch.stack([f['labels'] for f in data])
        }

    # Create the Trainer instance
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=full_dataset,
        data_collator=collate_fn
    )

    # Start the fine-tuning process
    print("Starting fine-tuning...")
    trainer.train()
    
    # Save the final, fine-tuned model
    final_model_path = './fashion_model_final'
    print(f"Training complete. Saving model to '{final_model_path}'")
    trainer.save_model(final_model_path)
    # Also save the processor to ensure it's bundled with the model
    processor.save_pretrained(final_model_path)