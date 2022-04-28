"""
    Firebaseden gelen videolar üzerinde Algoritmik aramalar yapılacak 
        ML, DL algoritmalarından biri seçilecek.
"""

import streamlit as st
from PIL import Image
from get_images_from_db import get_all_images_from_firebase

st.title("Security System App !")

MAINPATH = "DownloadedImages/"

image_list = get_all_images_from_firebase()

print(image_list)

for image in image_list:
    path = MAINPATH + image

    img = Image.open(path)
    st.image(img, caption='TEST FRAMES')

