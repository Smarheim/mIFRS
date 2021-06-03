import RPi.GPIO as GPIO
import time, sys


ENA = 32
IN1 = 18
IN2 = 23
IN3 = 35
IN4 = 37

# set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)

GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(ENA,GPIO.OUT)


my_pwm=GPIO.PWM(ENA,100)

my_pwm.start(100)




GPIO.output(IN1, GPIO.LOW) 
GPIO.output(IN2, GPIO.HIGH)
time.sleep(1)





GPIO.output(IN3, GPIO.LOW) 
GPIO.output(IN4, GPIO.HIGH)
time.sleep(1)

timestart=time.time()

timecount=70

while time.time() < timestart + timecount:
        
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN1, GPIO.LOW)

    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    
    