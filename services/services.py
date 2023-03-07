import json
import os

import sanic
from loguru import logger
from loko_extensions.business.decorators import extract_value_args
from loko_extensions.model.components import Component, Input, Arg, save_extensions, Dynamic
from sanic import Sanic, json as sjson
from sanic.exceptions import NotFound
from sanic_cors import CORS
import numpy as np
import cv2
from loko_client.business.fs_client import FSClient

from doc.doc import yolofaces_doc
from yoloface import face_analysis

gw = 'http://gateway:8080/routes/'
fsclient = FSClient(gateway=gw)

comp = Component("Faces", inputs=[Input(id="image")], description=yolofaces_doc,
args=[Arg(name="threshold", type='number', value='0'),
      Arg(name='blur', value=False, description='Whether objects have to be blurred', type='boolean'),
      Dynamic(name='file_path', dynamicType='directories', parent='blur', condition="{parent}")], icon="RiEmotionHappyLine")

save_extensions([comp])

app = Sanic("yolo")
app.static("/web", "/frontend/dist")
CORS(app)

face = face_analysis()

@app.post("/")
@extract_value_args(file=True)
def extract(file, args):
    logger.info(f'ARGS: {args}')
    file = file[0]
    image_np = np.frombuffer(file.body, np.uint8)
    img_np = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    blur = args.get('blur', False)
    threshold = json.loads(args.get('threshold', '0'))
    img,boxes,scores = face.face_detection(model='full', frame_arr=img_np)
    labels = ['face']*len(scores)
    ret = []
    logger.info(boxes)
    for label, score, box in zip(labels, scores, boxes):
        x,y,h,w = box
        box = [x,y,w,h]
        temp = dict(label=label, score=score, bbox=box)
        logger.info(f'RES: {temp}')
        if temp['score']>threshold:
            ret.append(temp)
    if blur:
        file_path = args.get('file_path')['path']
        fname = file.name
        ext = '.'+fname.split('.')[1]

        blur_img = img_np.copy()
        for obj in ret:
            bbox = [round(el) for el in obj['bbox']]
            x, y, w, h = bbox
            roi = blur_img[y:y + h, x:x + w]
            roi = cv2.GaussianBlur(roi, (51, 51), 0)
            blur_img[y:y + roi.shape[0], x:x + roi.shape[1]] = roi
        img_byte_arr = cv2.imencode(ext, blur_img)[1].tobytes()
        fsclient.save(os.path.join(file_path, fname), img_byte_arr)

    return sjson(ret)

@app.exception(Exception)
async def manage_exception(request, exception):
    logger.error(exception)
    if isinstance(exception, NotFound):
        return sanic.json(str(exception), status=404)
    logger.exception('ERROR')
    return sanic.json(str(exception), status=500)


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, single_process=True)