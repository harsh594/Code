
# coding: utf-8

# In[11]:


import cv2
import os
import numpy as np

subjects=["", "Elvis Presley", "Chester Charles Bennington"]

def detect_faces(image):
    
    copy=image.copy()
    grayimage=cv2.cvtColor(copy,cv2.COLOR_BGR2GRAY)
    face_cascade=cv2.CascadeClassifier('C:\\Users\home\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\cv2\data\lbp\lbpcascade_frontalface.xml')
    faces=face_cascade.detectMultiScale(grayimage,scaleFactor=1.2, minNeighbors=5)
    if(len(faces)==0):
        return None, None
    (x,y,w,h)=faces[0]
    #print("Faces Found= ",len(faces))
    return grayimage[y:y+h, x:x+h], faces[0]



def prepare_training_data(folder_path):
    dirs=os.listdir(folder_path)
    faces=[]
    labels=[]
    for dir_name in dirs:
        if not dir_name.startswith("s"):
            continue
        label=int(dir_name.replace("s",""))
        subject_dir_path=folder_path + "/" + dir_name
        subject_images_name=os.listdir(subject_dir_path)
        for image_name in subject_images_name:
            if image_name.startswith("."):
                continue
            image_path=subject_dir_path + "/" + image_name
            image=cv2.imread(image_path)
            cv2.imshow("Training on image.......", image)
            cv2.waitKey(100)
            face, rect=detect_faces(image)
            if face is not None:
                faces.append(face)
                labels.append(label)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    return  faces, labels
print("Preparing Data.....")
faces, labels=prepare_training_data("F:/training-data")
print("Data Prepared")
print("Total Faces: " ,len(faces))
print("Total Labels: " ,len(labels))
face_recognizer =cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces,np.array(labels))

def draw_rectangle(img, rect):
    (x,y,w,h)=rect
    cv2.rectangle(img, (x,y),(x+w, y+h), (0,255,0),2)

def draw_text(img,text,x,y):
    cv2.putText(img, text, (x,y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,255,0), 2)

def predict(img_test):
    img=img_test.copy()
    face, rect=detect_faces(img)
    label,confidence=face_recognizer.predict(face)
    label_text=subjects[label]
    draw_rectangle(img, rect)
    draw_text(img,label_text,rect[0],rect[1]-5)
    return img

print("Predicting images......")
test_img1=cv2.imread('F:\Elvis.jpg')
test_img2=cv2.imread('F:\Chester.jpg')
predicted_img1=predict(test_img1)
predicted_img2=predict(test_img2)
print("Prediction Complete!!")

cv2.imshow(subjects[2], predicted_img1)
cv2.imshow(subjects[1], predicted_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




