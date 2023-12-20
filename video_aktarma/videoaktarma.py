import cv2
import time

video_name = "cadde.mp4"

cap=cv2.VideoCapture(video_name)


if cap.isOpened()==False:
    print("hata")

while True:
    ret,frame =cap.read()
    if ret ==True:
        time.sleep(0.01)
        cv2.imshow("video", frame)
        
    else:
        break
    
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
    
cap.release()

cv2.destroyAllWindows()