import RPi.GPIO as GPIO
import time, sys
import copy
from threading import Thread

f = open("Encoder2.txt", "w+")

GPIO.setmode(GPIO.BOARD)

ENA = 33
IN1 = 31
IN2 = 15

print("how long do you want to run the motor?")
st=input()

st=int(st)





def thread1(self):
    global s
    
    s=0
    while s<=st:
    

        time.sleep(1)
        s+=1
        
 

def motor(self):
   
    global s 
    
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)

    GPIO.setup(ENA,GPIO.OUT)
    my_pwm=GPIO.PWM(ENA,100)
    my_pwm.start(50)


    GPIO.output(IN1, GPIO.LOW) 
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(1) 


    a_pin =21
    b_pin =22



    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.IN)

    outcome = [0,-1,1,0,-1,0,0,1,1,0,0,-1,0,-1,1,0]
    last_AB = 0b00
    counter = 0

    timestart=time.time()

    timecount=st
    

    while time.time() < timestart + timecount:
        
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN1, GPIO.LOW)
    
            

        A = GPIO.input(a_pin)
        B = GPIO.input(b_pin)
        
        current_AB = (A << 1) | B
        position = (last_AB << 2) | current_AB
        counter  += outcome[position]
        last_AB = current_AB
        f.write(str((counter/s)*(60/36)))
            
        
        for i in range (1,round(st/5)):  

        
            while s >i*5  and s <i*5+2 :
        


                print((counter/s)*(60/36),"RPM")
                time.sleep(1.1)
            
                i+=1
            
GPIO.setmode(GPIO.BOARD)

ENA = 33
IN1 = 31
IN2 = 15
            
        
      

if __name__=="__main__":


    motor = Thread( target=motor, args=("Thread-2", ) )
    motor.start()

    thread1 = Thread( target=thread1, args=("Thread-1", ) )
    thread1.start()

    motor.join()
    thread1.join()

        
    

GPIO.cleanup()                                                                                     
