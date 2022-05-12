import os
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from get_images_from_db import get_all_images_from_firebase
from video_stream import vid_str
from indentify import indentify_faces

MAINPATH = "DownloadedImages/"
IDENTIFIED_PATH ='Identify_faces/'

with st.sidebar:
    st.markdown("###")
    st.markdown('Choose type')
    selected_page = option_menu(None, ["Captured", "Identify"], 
        icons=['list-task', 'list-task',], 
        menu_icon="cast", default_index=0, orientation="vertical")

# vid_str()

if selected_page == "Captured":
    st.title("IMAGES FROM STORAGE !")
    # for image in image_list_from_storage:
    for image in os.listdir(MAINPATH):
        path = MAINPATH + image
        img = Image.open(path)
        st.image(img, caption=image)

else:
    st.title("INDENTIFIED IMAGES !")
    for i_image in os.listdir(IDENTIFIED_PATH):
        path = IDENTIFIED_PATH + i_image
        img = Image.open(path)
        st.image(img, caption=i_image)