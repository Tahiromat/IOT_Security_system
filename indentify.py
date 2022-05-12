import face_recognition
from PIL import Image, ImageDraw
from datetime import datetime
import os


def indentify_faces(image_name):
  image_of_tahir = face_recognition.load_image_file('known/Tahir Mat.jpeg')
  tahir_face_encoding = face_recognition.face_encodings(image_of_tahir)[0]

  #  Create arrays of encodings and names
  known_face_encodings = [
    tahir_face_encoding,
  ]

  known_face_names = [
    "Tahir Mat",
  ]

  # Load test image to find faces in
  test_image = face_recognition.load_image_file(image_name)

  # Find faces in test image
  face_locations = face_recognition.face_locations(test_image)
  face_encodings = face_recognition.face_encodings(test_image, face_locations)

  # Convert to PIL format
  pil_image = Image.fromarray(test_image)

  # Create a ImageDraw instance
  draw = ImageDraw.Draw(pil_image)

  # Loop through faces in test image
  for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown Person"
    # If match
    if True in matches:
      first_match_index = matches.index(True)
      name = known_face_names[first_match_index]
    # Draw box
    draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))
    # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))
    now = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    f_name = now + ".jpg"
    # Save image
    pil_image.save('Identify_faces/'+ f_name)

  del draw
  # Display image
  # pil_image.show()
  


# for image_name in os.listdir('DownloadedImages/'):
#   indentify_faces(image_name)



# import face_recognition
# from PIL import Image, ImageDraw
# from  datetime import  datetime
# import os



# def identify_faces(image_p):

  
#   image_of_tahir = face_recognition.load_image_file('known/Tahir Mat.jpeg')
#   tahir_face_encoding = face_recognition.face_encodings(image_of_tahir)[0]


#   #  Create arrays of encodings and names
#   known_face_encodings = [
#     tahir_face_encoding,
#   ]

#   known_face_names = [
#     "Tahir Mat",
#   ]

  
#     # Load test image to find faces in
#   test_image = face_recognition.load_image_file('DownloadedImages/'+ image_p)
#   # Find faces in test image
#   face_locations = face_recognition.face_locations(test_image)
#   face_encodings = face_recognition.face_encodings(test_image, face_locations)
#   # Convert to PIL format
#   pil_image = Image.fromarray(test_image)
#   # Create a ImageDraw instance
#   draw = ImageDraw.Draw(pil_image)
#   # Loop through faces in test image
#   for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#     matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#     name = "Unknown Person"
#     # If match
#     if True in matches:
#       first_match_index = matches.index(True)
#       name = known_face_names[first_match_index]
#     # Draw box
#     draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))
#     # Draw label
#     text_width, text_height = draw.textsize(name)
#     draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
#     draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))
#   del draw

#   # Display image
#   pil_image.show()

#   now = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
#   f_name = now + ".jpg"

#   # Save image
#   pil_image.save('RecognitionFaces/Identify_faces/'+f_name)


# for image_name in os.listdir('DownloadedImages/'):
#   print(image_name)
#   identify_faces(image_name)

