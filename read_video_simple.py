import cv2

cap = cv2.VideoCapture('video.MOV')

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
