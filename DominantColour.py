from PIL import Image
from sklearn.cluster import KMeans
import numpy as np

def get_dominant_colors(image_path, k=5):
    image = Image.open(image_path)
    image = image.resize((150, 150)) # Resize for speed
    pixels = np.array(image).reshape(-1, 3)

    kmeans = KMeans(n_clusters=k, n_init='auto')
    kmeans.fit(pixels)

    # Get the RGB values of the cluster centers
    colors = kmeans.cluster_centers_.astype(int)
    return colors.tolist()

# Example usage:
# colors = get_dominant_colors('images/product_0.jpg')
# print(colors)