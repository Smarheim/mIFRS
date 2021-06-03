import cv2
import time
print(cv2.__version__)
import numpy as np
 
def nothing(x):
    pass
 
cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1320,0)
 
cv2.createTrackbar('hueLower', 'Trackbars',80,179,nothing)
cv2.createTrackbar('hueUpper', 'Trackbars',150,179,nothing)
 

 
cv2.createTrackbar('satLow', 'Trackbars',40,255,nothing)
cv2.createTrackbar('satHigh', 'Trackbars',255,255,nothing)

cv2.createTrackbar('valLow','Trackbars',40,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)
 
 
dispW=640
dispH=480
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
 

while True:
    ret, orgframe = cam.read()
  
    frame=cv2.medianBlur(orgframe, 7)
    
    
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

    
 
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
 
    hueLow=cv2.getTrackbarPos('hueLower', 'Trackbars')
    hueUp=cv2.getTrackbarPos('hueUpper', 'Trackbars')
 
    hue2Low=cv2.getTrackbarPos('hue2Lower', 'Trackbars')
    hue2Up=cv2.getTrackbarPos('hue2Upper', 'Trackbars')
 
    Ls=cv2.getTrackbarPos('satLow', 'Trackbars')
    Us=cv2.getTrackbarPos('satHigh', 'Trackbars')
 
    Lv=cv2.getTrackbarPos('valLow', 'Trackbars')
    Uv=cv2.getTrackbarPos('valHigh', 'Trackbars')
 
    l_b=np.array([hueLow,Ls,Lv])
    u_b=np.array([hueUp,Us,Uv])
 
    l_b2=np.array([hue2Low,Ls,Lv])
    u_b2=np.array([hue2Up,Us,Uv])
 
    FGmask=cv2.inRange(hsv,l_b,u_b)
    FGmask2=cv2.inRange(hsv,l_b2,u_b2)
    FGmaskComp=cv2.add(FGmask,FGmask2)
    cv2.imshow('FGmaskComp',FGmaskComp)
    cv2.moveWindow('FGmaskComp',0,530)
 
    FG=cv2.bitwise_and(frame, frame, mask=FGmaskComp)
    cv2.imshow('FG',FG)
    cv2.moveWindow('FG',700,0)
 
    bgMask=cv2.bitwise_not(FGmaskComp)
    cv2.imshow('bgMask',bgMask)
    cv2.moveWindow('bgMask',700,530)
 
    BG=cv2.cvtColor(bgMask,cv2.COLOR_GRAY2BGR)
 
    final=cv2.add(FG,BG)
    cv2.imshow('final',final)
   
    cv2.moveWindow('final',1400,0)
    gray = cv2.cvtColor(FG,cv2.COLOR_HSV2RGB)


    edges=cv2.Canny(gray,0,30,3)
    cv2.imshow('edges',edges)
    cv2.moveWindow('edges',1400,530)

   
    lines2=cv2.HoughLines(edges, 1, np.pi/180, 50, 50,30)
    lines=cv2.HoughLinesP(edges, 1, np.pi/180, 50, 50,30)
    if lines is not None:
        for x1,y1,x2,y2 in lines[0]:

            frame=cv2.line(frame, (x1,y1), (x2,y2),(0, 0, 255),5)
        for theta in lines2[0]:
            
    
            print((theta*180)/np.pi)
         
        

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()