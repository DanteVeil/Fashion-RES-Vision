# dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
import json # <--- IMPORT THIS

st.set_page_config(layout="wide")
st.title('🤖 AI Fashion Trend Dashboard')

# Use a converter to parse the color string back into a list
try:
    df = pd.read_csv(
        'fashion_trends.csv', 
        converters={'colors': json.loads} # <--- CHANGE THIS
    )
except FileNotFoundError:
    st.error("fashion_trends.csv not found. Please run main.py first.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while reading the CSV: {e}")
    st.stop()

# ... (the rest of your dashboard code remains the same) ...

# --- Sidebar Filters ---
st.sidebar.header("Filters")
selected_garment = st.sidebar.selectbox('Select a Garment Type', options=['All'] + sorted(df['garment_type'].unique()))

if selected_garment != 'All':
    df_filtered = df[df['garment_type'] == selected_garment]
else:
    df_filtered = df

# --- Main Page Visualizations ---
st.header(f"Showing Trends for: {selected_garment}")

# 1. Garment Type Distribution
st.subheader("Garment Type Distribution")
fig_garment = px.bar(df['garment_type'].value_counts(), 
                     title="Most Common Garment Types",
                     labels={'value': 'Count', 'index': 'Garment Type'})
st.plotly_chart(fig_garment)

# 2. Color Distribution (requires some data processing)
st.subheader("Dominant Color Trends")
st.write("Color distribution chart would go here.")

# 3. Display Sample Images
st.subheader("Sample Images")
if not df_filtered.empty:
    st.image([f"images/{fname}" for fname in df_filtered['filename'].head(5)], width=150)
else:
    st.write("No images to display for this selection.")