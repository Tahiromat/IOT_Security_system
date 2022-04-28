import os
import pyrebase

def get_all_images_from_firebase():
  
  images_list = []

  firebaseConfig = {
    "apiKey": "AIzaSyBHtIh3LujbC_-usf7HwJyHn7-ovhBlh_0",
    "authDomain": "iotsecuritysystem.firebaseapp.com",
    "databaseURL": "https://iotsecuritysystem.firebaseapp.com",
    "projectId": "iotsecuritysystem",
    "storageBucket": "iotsecuritysystem.appspot.com",
    "messagingSenderId": "965747010830",
    "appId": "1:965747010830:web:6ffaa8e38b8c6cef837b5f",
    "measurementId": "G-F41WK5LJWT",
    "serviceAccount": "serviceAccountKey.json"
  }

  firebase_storage = pyrebase.initialize_app(firebaseConfig)
  storage = firebase_storage.storage()

  all_files = storage.list_files()

  for file in all_files:
    file.download_to_filename("DownloadedImages/"+file.name)


  for file in os.listdir("/home/tahir/Documents/DataScience/IOTProject/DownloadedImages"):
    images_list.append(file)

  return images_list
