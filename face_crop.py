# -*- coding: utf-8 -*-
"""Face_Crop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19Svhu4ry5t5olQZJZDcp05IS7llyzZkI
"""

from google.colab import drive
drive.mount('/content/dirve')

import cv2
import glob
import os

input_dir = "/content/dirve/Shareddrives/Code-15/MBTI/INTP/INTP_Input" ## 사진이 들어있는 폴더
output_dir = "/content/dirve/Shareddrives/Code-15/MBTI/INTP/INTP_Output" ## 사진을 뱉는 폴더
files = os.listdir(input_dir)
print(files)
face_cascade = cv2.CascadeClassifier('/content/dirve/Shareddrives/Code-15/MBTI/haarcascade_frontalface.xml')

for el in files:
    splt = el.split(".") # 파일 이름
    ext = splt.pop() # 파일 확장자
    if ext in "jpg jpeg png bmp JPG JPEG PNG BMP":
    
      img_files = input_dir+'/'+ el
      img = cv2.imread(img_files)
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      
      faces = face_cascade.detectMultiScale(gray, 1.3, 5)
      for (x, y, w, h) in faces:
          cropped = img[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)]
          if cropped.size == 0:
            print(el+' 파일 출력실패')
            break
          # 이미지를 저장
          cv2.imwrite(output_dir+'/'+el, cropped)