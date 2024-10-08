import os
import cv2
import time
camera=cv2.VideoCapture(0)
try:
    if not os.path.exists('ImageAttendance'):
        os.makedirs('ImageAttendance')
except OSError:
    print("directory not created")
  
current_frame_count=0
total_time=10
start_time=time.time()
while(int(time.time()-start_time)<total_time):
    name=input("Enter name :")
    ret,frame=camera.read()
    cv2.imshow("frame",frame)
    if ret:
        name='./ImageAttendance/'+str(name)+str(current_frame_count)+'.jpg'
        print(name)
        cv2.imwrite(name,frame)
        current_frame_count+=1
    else:
        break
    key=cv2.waitKey(1)
    if key == 27:
        break
camera.release()
cv2.destroyAllWindows()

