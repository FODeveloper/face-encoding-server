# face-encoding-server
A face encoder service to send face embedding to mini-face app

# How to run it
1.  Ensure that miniface is running(check mini-face repo)
2.  Run encoder.py using the command:
```
python3 encoder.py
```
after installing cv2, numpy, requests and flask
3.  You can use postman to POST an image with the following body of the request:
```
{
  'permission': <permission> # <Authorized> or <Not Authorized>
  'first_name': <person-firstname>
  'last_name': <person-lastname>
  'media': photo
}
```
for media: in postman body tab, change the type from text to file, to be able to load your image.

4.  This server is running on 0.0.0.0 by default, you can change it in encoder main part
5.  It assumes that miniface app is running on localhost port 8000.
6.  the server detect and encode the face image, and send result to miniface app, to register new person.
7.  if there are many persons, or none in the image, the server will return 
```
{
  'result': 'none or several faces in the input image'
}
```
