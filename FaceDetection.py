import cv2

face_cascad = cv2.CascadeClassifier("C:\\Users\\Menoo\\PycharmProjects\\FaceDetection\\haarcascade_frontalface_alt2.xml")

cap = cv2.VideoCapture(0)
cap.open(0, cv2.CAP_DSHOW)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascad.detectMultiScale(gray, scaleFactor= 1.5, minNeighbors= 5)
    for(x, y, w, h) in face:
        print(x, y, w, h)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        #img = "image.png"
        #cv2.imwrite(img, roi_gray)

        color = (255, 0, 255)
        stroke = 3
        width = x + w
        height = y + h
        cv2.rectangle(frame, (x, y), (width, height), color, stroke)
    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
