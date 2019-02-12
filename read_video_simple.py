import cv2

cap = cv2.VideoCapture(0)
//To use internal webcam, use 0 (e.g. cap = cv2.VideoCapture(0))
//To use external usb webcam, replace 0 with 1 (e.g. cap = cv2.VideoCapture(1))
//To play a saved video, just replace the 0 or 1 with the name of the video file.  (e.g. cap = cv2.VideoCapture('video.MOV))

while True:
    ref, frame = cap.read()
    if ref:
        cv2.imshow('Demo', frame)
    else:
        break

    k = cv2.waitKey(10)
    if k == ord('q'):
        break
cv2.destroyAllWindows()
