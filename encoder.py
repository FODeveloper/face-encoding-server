#!flask/bin/python

from facerecognizer import *
import numpy as np
import cv2

from flask import Flask, jsonify,request,Response
import jsonpickle

import requests


DB_URL = "http://127.0.0.1:8000/personapp/persons/"

app = Flask(__name__)

def save_person(data):
    response = requests.post(DB_URL, json=data)
    print(response)


def recognize_face_image(image):
    rectangles = face_locations(image)
    response = {
        'result': 'none or several faces in the input image'
    }
    encoded = False
    if len(rectangles) == 1:
        t, r, b, l = rectangles[0]
        face = image[t:b, l:r]
        encoding = face_encodings(face)
        if len(encoding)!=0:
            response['result'] = encoding[0].tolist()
            encoded = True
    return response, encoded


# route http posts to this method
@app.route('/encode/', methods=['POST'])
def inference():
    r = request
    uploaded_img = r.files['media']
    nparr = np.frombuffer(uploaded_img.read(), dtype=np.uint8)
    img = cv2.imdecode(nparr, flags=1)
    result, encoded = recognize_face_image(img)
    
    response = jsonpickle.encode(result)
    if encoded:
        data = {
            'permission': r.values['permission'],
            'first_name': r.values['first_name'],
            'last_name': r.values['last_name'],
            'photo_path': '/profile.png',
            'encoding': str(result['result'])
        }

        save_person(data)

    return Response(response=response, status=200, mimetype="application/json")
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
