import os
import cv2
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendence-536e4-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendence-536e4.appspot.com"
})


# importing student img
# Images here contains my data(folders of various persons)

folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    # print(path).
    # extract the person id from the image path
    studentIds.append(os.path.splitext(path)[0])

    # uploading images to  the firebase storage
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


print(studentIds)
print(len(imgList))

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        # converting images color BGR to RGB cz face-recognition packages uses RGB and openCV uses BGR
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # compute the facial embedding for the face
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
        print(encode)

    return encodeList


# Encoding started and finding and then adding them to a list along with students ID
encodeListKnown = findEncodings(imgList)

# Which ID belongs to which Encoding fixing that
encodeListKnownWithIds = [encodeListKnown, studentIds]
print(encodeListKnownWithIds)

# use pickle to save data into a file for later use
file = open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownWithIds, file)
file.close()

# print("File Save...")

