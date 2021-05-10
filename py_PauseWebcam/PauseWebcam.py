import cv2,time
video=cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = video.read()
    cc = cv2.imshow("Capturing",frame)
    key=cv2.waitKey(1)
 
    if key==ord('`'): 
        key=cv2.waitKey(-1)
    elif key==ord('x'):
        break
