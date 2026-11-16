import RPi.GPIO as GPIO
import time
from src.settings import distance, ultrasonic, pwm

def instrument():
    distance_brut = ultrasonic.get_distance()
    distance = (0.8 * distance + 0.2 * distance_brut) #lissage de la distance
    if distance > 40:
        pwm.stop()
    else:
        ratio = (distance/40)
        freq = ratio * 535.25
        pwm.ChangeFrequency(freq)
        time.sleep(0.03)

    GPIO.cleanup()





























        



