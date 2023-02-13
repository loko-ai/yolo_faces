from pathlib import Path

import numpy as np
from yoloface import face_analysis
import cv2
from PIL import Image

face=face_analysis()        #  Auto Download a large weight files from Google Drive.
                            #  only first time.
                            #  Automatically  create folder .yoloface on cwd.

img_path = Path('/home/cecilia/loko/data/yolo/articolo-1-900x450.png')
with open(img_path, 'rb') as f:
    im_b = f.read()

image_np = np.frombuffer(im_b, np.uint8)
img_np = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

# example 1
img,face_box,conf=face.face_detection(model='full', frame_arr=img_np)
print(face_box)                  # box[i]=[x,y,w,h]
print(conf)                 #  value between(0 - 1)  or probability
print(img)


img_output = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converting BGR to RGB
out = Image.fromarray(img_output)
out.save('prova.png')


font = cv2.FONT_HERSHEY_PLAIN
font_ = cv2.FONT_HERSHEY_COMPLEX
color = (255, 200, 200)
if len(face_box) > 0:
    for i in range(len(face_box)):
        box = face_box[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        print(x,y,w,h)
        label = "{}".format('face')
        roi = img[y:y+w, x:x+h]
        roi = cv2.GaussianBlur(roi, (17, 17), 30)
        img[y:y+roi.shape[0], x:x+roi.shape[1]] = roi
        cv2.rectangle(img, (x, y), (x + h, y + w), (255, 255, 255), 3)
        (text_width, text_height) = cv2.getTextSize(label, font, fontScale=1, thickness=1)[0]
        text_offset_x, text_offset_y = x, y - 10
        box_coords = (
        (text_offset_x, text_offset_y + 10), (text_offset_x + text_width + 10, text_offset_y - text_height - 10))
        cv2.rectangle(img, box_coords[0], box_coords[1], (0, 0, 0), cv2.FILLED)
        cv2.putText(img, label, (text_offset_x, text_offset_y), font, fontScale=1, color=color, thickness=1)


img_output = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converting BGR to RGB
out = Image.fromarray(img_output)
out.save('prova2.png')