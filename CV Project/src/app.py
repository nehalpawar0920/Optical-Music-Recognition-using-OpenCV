# streamlit_app.py

import os
import cv2
import streamlit as st
from PIL import Image

# Function to read images from the given folder path
def read_images_from_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(folder_path, filename)
            img = cv2.imread(img_path)
            images.append(img)
    return images

# Streamlit app title and description
st.title("Optical Music Note Recognition using OpenCV")
st.write("")

# Upload path of input folder
input_folder_path = st.sidebar.text_input("Input Folder Path")

if input_folder_path and os.path.exists(input_folder_path):
    # Read images from the input folder
    images_input = read_images_from_folder(input_folder_path)

    st.subheader("Input Images:")
    for idx, img in enumerate(images_input):
        # Convert BGR image to RGB format for displaying with PIL
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        st.image(Image.fromarray(img_rgb), caption=f"Input Image {idx + 1}", use_column_width=True)

# Upload path of output folder
output_folder_path = st.sidebar.text_input("Output Folder Path")

if output_folder_path and os.path.exists(output_folder_path):
    # Read images from the output folder
    images_output = read_images_from_folder(output_folder_path)

    st.subheader("Processed Images:")
    for idx, img in enumerate(images_output):
        # Convert BGR image to RGB format for displaying with PIL
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        st.image(Image.fromarray(img_rgb), caption=f"Processed Image {idx + 1}", use_column_width=True)
