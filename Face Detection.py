
# coding: utf-8

# In[21]:


import cv2
import matplotlib.pyplot as plt
import time

haarc=cv2.CascadeClassifier('C:\\Users\home\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
def conversion(img):
    return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
def detect_faces(cascade,image,scaleFactor=0):
    
    copy=image.copy()
    grayimage=cv2.cvtColor(copy,cv2.COLOR_BGR2GRAY)
    faces=cascade.detectMultiScale(grayimage,scaleFactor=1.1, minNeighbors=5)
    print("Faces Found= ",len(faces))
    for (x,y,w,h) in faces:
        cv2.rectangle(copy,(x,y), (x+w, y+h), (0,255,0), 2)
    return copy
grp=cv2.imread('F:\group.jpg')

total_faces=detect_faces(haarc,grp)
plt.imshow(conversion(total_faces))




