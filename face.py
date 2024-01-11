import threading

import cv2 
from deepface import DeepFace
# defined a camera object
cap = cv2.VideoCapture (0)
# set the proportions of the camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# set the counter to 0
counter = 0

face_match = False
# the reference image
reference_img = cv2.imread('image/SERGIOpy.jpg')
# function that verifys the face matches the reference image
def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError: 
        face_match = False

while True:
 ret, frame = cap.read()
 if ret:
    if counter % 38 == 8:
      try:
       threading. Thread(target=check_face, args=(frame.copy(),)).start() 
      except ValueError:
       pass
    counter += 1
    # if the face matches the reference image, the text will be green, if not, it will be red
    if face_match:
     cv2.putText(frame, "YOU ARE SERGIO", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    else: 
        cv2.putText(frame, "IMPOSTER!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
    cv2.imshow("video", frame)
# if the user presses q, the program will stop
 key = cv2.waitKey(1)
 if key == ord("q"):
    break

cv2.destroyAllWindows()