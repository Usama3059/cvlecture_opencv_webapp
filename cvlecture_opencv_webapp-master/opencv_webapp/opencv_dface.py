from django.conf import settings
import numpy as np
import cv2
from django.contrib import messages
import Algorithmia
from django.conf import settings


def opencv_dface(path,Adr):
    img=cv2.imread(path,1)
    print(path)
    cv2.imwrite(path, img)
    print("Usama")
    path1="http://usama024.pythonanywhere.com/"
    imageURL = settings.MEDIA_URL + Adr








    input = path1+imageURL
    print(input)
    client = Algorithmia.client('simBELmBzPwtLZeK/XxdN/fd9dz1')
    algo = client.algo('LgoBE/CarMakeandModelRecognition/0.4.5')
    algo.set_options(timeout=300) # optional
    usa=algo.pipe(input).result

    #img1 = cv2.imread(path, 1)
    #print("usama")
    #print(path)

    if(type(img) is np.ndarray):
        #print(img.shape)
        #baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
        #print(baseUrl)
        #face_cascade = cv2.CascadeClassifier(
            #baseUrl+'haarcascade_frontalface_default.xml')
        #eye_cascade = cv2.CascadeClassifier(baseUrl+'haarcascade_eye.xml')
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #faces = face_cascade.detectMultiScale(gray, 1.05, 5)
        # x=40
        # y=100
        # w=40
        # h=40
        # th=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,10)

        #for(x, y, w, h) in faces:

            #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            #roi_gray = gray[y:y+h, x:x+w]
            #roi_color = img[y:y+h, x:x+w]
            #eyes = eye_cascade.detectMultiScale(roi_gray)
            #for(ex, ey, ew, eh) in eyes:
                #cv2.rectangle(roi_color, (ex, ey),
                              #(ex+ew, ey+eh), (0, 255, 0), 2)

        cv2.imwrite(path, img)
        #messages.success(request,"Yo did")
        #messages.add_message(request, messages.INFO, 'Post added.')
        #usama=3
        return usama    

    else:
        print('something error')
        print(path)
