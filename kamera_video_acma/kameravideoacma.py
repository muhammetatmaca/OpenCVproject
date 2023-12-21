import cv2
cap = cv2.VideoCapture(0)

#video boyutlarını belirleme

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#yazdırma referansı
writer=cv2.VideoWriter("ornekkayit.mp4",cv2.VideoWriter.fourcc(*"DIVX"),20,(width,height))

if not cap.isOpened():
    raise Exception("Kamera kullanılamıyor.")


#videyu kaydetmek ve ekranda acık tutmak için
while True:
    ret,frame=cap.read()
    cv2.imshow("video", frame)
    #kayıt
    writer.write(frame)
     
    if cv2.waitKey(1) & 0xFF == ord("q"):break


cap.release()
writer.release()
cv2.destroyAllWindows()  