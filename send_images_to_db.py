import os
import pyrebase

def send_images_to_firebase(f_name, path):
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
    storage.child(f_name).put(path)
