# analysis.py

from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
from transformers import ViTImageProcessor, ViTForImageClassification
import os

# --- Model Loading (Updated to load YOUR fine-tuned model) ---
MODEL_PATH = './fashion_model_final'

if os.path.exists(MODEL_PATH):
    print("Loading fine-tuned fashion model...")
    processor = ViTImageProcessor.from_pretrained(MODEL_PATH)
    model = ViTForImageClassification.from_pretrained(MODEL_PATH)
else:
    print("Fine-tuned model not found. Falling back to generic ImageNet model.")
    processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
    model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224-in21k')

# --- Analysis Functions (The classify_garment function is now much more accurate) ---
def get_dominant_colors(image_path, k=5):
    # ... (this function remains the same) ...
    try:
        image = Image.open(image_path).convert('RGB')
        image = image.resize((150, 150))
        pixels = np.array(image).reshape(-1, 3)
        
        kmeans = KMeans(n_clusters=k, n_init='auto', random_state=0)
        kmeans.fit(pixels)
        
        colors = kmeans.cluster_centers_.astype(int)
        return colors.tolist()
    except Exception as e:
        print(f"Could not process colors for {image_path}: {e}")
        return []

def classify_garment(image_path):
    """
    Classifies the garment using your fine-tuned model.
    """
    try:
        image = Image.open(image_path).convert('RGB')
        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        # This will now return your custom labels like "Apparel", "Footwear", etc.
        return model.config.id2label[predicted_class_idx]
    except Exception as e:
        print(f"Could not classify {image_path}: {e}")
        return "Unknown"