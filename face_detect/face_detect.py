import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

file_path="이미지 파일 경로"
file_names=os.listdir(file_path)
print(file_names)

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
for file_name in file_names:
	src = '저장할 경로'
	src = src+'\\'+file_name
	if not os.path.exists(src):
		os.makedirs(src)
	img_path = file_path+"/"+file_name
	img_names = os.listdir(img_path)
	i = 0
	for img_name in img_names:
		try:
			face_dec_img_path = img_path+'/'+img_name
			image = cv2.imread(face_dec_img_path)
			grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(image, 1.03, 5)
			try:
				for (x,y,w,h) in faces:
					ropped = image[y-int(h/4):y+h+int(h/4),x-int(w/4):x+w+int(w/4)]
					cv2.imwrite(src+'//'+file_name+' '+str(i)+".png",ropped)
					i += 1
			except:
				print(img_name+'에서 얼굴을 찾을 수 없습니다.')
		except:
			print(img_name+'에서 알수 없는 오류')
cv2.waitKey(0)
cv2.destroyAllWindows()