import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os
from collections import Counter
import math

st.set_page_config(layout="wide")
st.title('🤖 AI Fashion Trend Dashboard')

# --- Control Sidebar ---
st.sidebar.header("Data Pipeline")
if st.sidebar.button('Update Trend Data'):
    # Note: For the executable, these functions would be imported.
    # For now, we assume the files have been run manually.
    st.sidebar.info("Please run scraper.py and main.py manually for now.")

# --- Helper Function for Color Mapping ---
# This function converts a raw RGB value to its closest named color.
def get_color_name(rgb_tuple):
    # A simple color palette for mapping
    color_palette = {
        "Black": (0, 0, 0), "White": (255, 255, 255), "Red": (255, 0, 0),
        "Green": (0, 128, 0), "Blue": (0, 0, 255), "Yellow": (255, 255, 0),
        "Cyan": (0, 255, 255), "Magenta": (255, 0, 255), "Gray": (128, 128, 128),
        "Maroon": (128, 0, 0), "Olive": (128, 128, 0), "Navy": (0, 0, 128),
        "Purple": (128, 0, 128), "Teal": (0, 128, 128), "Brown": (165, 42, 42),
        "Beige": (245, 245, 220), "Pink": (255, 192, 203)
    }
    
    min_distance = float('inf')
    closest_color = "Unknown"
    for name, rgb in color_palette.items():
        # Calculate Euclidean distance
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(rgb_tuple, rgb)]))
        if distance < min_distance:
            min_distance = distance
            closest_color = name
    return closest_color

# --- Caching Function to Load Data ---
@st.cache_data
def load_data():
    if os.path.exists('fashion_trends.csv'):
        df = pd.read_csv('fashion_trends.csv', converters={'colors': json.loads})
        return df
    return None

df = load_data()

# --- Main Dashboard Display ---
if df is None:
    st.warning("Trend data file (fashion_trends.csv) not found. Please click 'Update Trend Data' in the sidebar to generate it.")
else:
    st.sidebar.header("Filters")
    # Make sure 'garment_type' column exists and is not empty before creating filter
    if 'garment_type' in df.columns and not df['garment_type'].empty:
        unique_garments = sorted(df['garment_type'].unique())
        selected_garment = st.sidebar.selectbox('Select a Garment Type', options=['All'] + unique_garments)

        if selected_garment != 'All':
            df_filtered = df[df['garment_type'] == selected_garment]
        else:
            df_filtered = df
    else:
        df_filtered = df # No filter applied if column is missing

    st.header(f"Showing Trends for: {selected_garment}")

    # --- Create two columns for the charts ---
    col1, col2 = st.columns(2)

    with col1:
        # 1. Garment Type Distribution
        st.subheader("Garment Type Distribution")
        if not df['garment_type'].empty:
            fig_garment = px.bar(df['garment_type'].value_counts(), 
                                 title="Most Common Garment Types",
                                 labels={'value': 'Count', 'index': 'Garment Type'})
            st.plotly_chart(fig_garment, use_container_width=True)

    with col2:
        # 2. Color Distribution (NEW IMPLEMENTATION)
        st.subheader("Dominant Color Trends")
        if not df_filtered['colors'].empty:
            # Flatten the list of lists of colors
            all_colors = [tuple(color) for sublist in df_filtered['colors'] for color in sublist]
            
            # Map RGB to color names
            color_names = [get_color_name(rgb) for rgb in all_colors]
            
            # Count the occurrences of each color name
            color_counts = pd.Series(color_names).value_counts()
            
            fig_color = px.bar(color_counts, 
                               title="Most Frequent Colors",
                               labels={'value': 'Count', 'index': 'Color Name'})
            st.plotly_chart(fig_color, use_container_width=True)

    # 3. Display Sample Images (NEW IMPLEMENTATION)
    st.subheader("Sample Images")
    if not df_filtered.empty:
        # Define number of columns for the grid
        num_columns = 4
        # Get up to 12 images to display
        image_files = df_filtered['filename'].head(12).tolist()
        
        # Create the grid
        cols = st.columns(num_columns)
        for i, image_file in enumerate(image_files):
            # Place each image in the next available column
            with cols[i % num_columns]:
                image_path = os.path.join('images', image_file)
                if os.path.exists(image_path):
                    st.image(image_path, caption=image_file, width=150)
    else:
        st.write("No images to display for this selection.")