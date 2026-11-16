from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import RPi.GPIO as GPIO
import time


SPEAKER = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(SPEAKER, GPIO.OUT)


ultrasonic = GroveUltrasonicRanger(5)

    
pwm = GPIO.PWM(SPEAKER, 500)
pwm.start(50)
distance = 20 # init de la distance pr 1er itération


while True:
    distance_brut = ultrasonic.get_distance()
    distance = (0.8 * distance + 0.2 * distance_brut) #lissage de la distance
    if distance > 40:
        continue
        pwm.stop()
    else:
        ratio = (distance/40)
        freq = ratio * 535.25
        pwm.ChangeFrequency(freq)
        time.sleep(0.03)



GPIO.cleanup()





























        



