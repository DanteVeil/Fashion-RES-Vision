import pandas as pd
import os
# from your_other_files import get_dominant_colors, classify_garment

image_files = os.listdir('images')
results = []

for image_file in image_files:
    path = os.path.join('images', image_file)
    # In a real run, you'd call your actual functions here.
    # This is placeholder data for demonstration.
    colors = [[255,0,0], [0,0,0]] # get_dominant_colors(path) 
    garment_type = "T-Shirt"      # classify_garment(path)

    results.append({
        'filename': image_file,
        'colors': colors,
        'garment_type': garment_type
    })

df = pd.DataFrame(results)
df.to_csv('fashion_trends.csv', index=False)
print("Analysis complete. Data saved to fashion_trends.csv")