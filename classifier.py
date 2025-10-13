from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image

# Load the pre-trained model and processor
processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224-in21k')

def classify_garment(image_path):
    image = Image.open(image_path)
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    # The model predicts one of 21,843 ImageNet classes. 
    # You'd need to map these to fashion categories, or fine-tune the model.
    predicted_class_idx = logits.argmax(-1).item()
    predicted_class = model.config.id2label[predicted_class_idx]
    return predicted_class

# For a more accurate model, you would fine-tune this on a fashion-specific dataset 
# like DeepFashion, mapping its categories to your own simple ones (e.g., 'Top', 'Trousers', 'Coat').