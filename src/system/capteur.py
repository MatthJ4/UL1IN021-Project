import RPi.GPIO as GPIO
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

SPEAKER = 12
FREQ_MIN = 261.63 #Hz (DO4)
DIST_MAX = 39 #cm
LARG_NOTE = 3

class Instrument:
    """Capteur de distance + haut parleurs"""

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SPEAKER, GPIO.OUT)
        self.ultrasonic = GroveUltrasonicRanger(5)
        self.pwm = GPIO.PWM(SPEAKER, 500)
        self.pwm.start(0)
        self.distance = 20 #pour l'init seulement

    def update(self):
        """Hyp: self.distance != 0"""
        dist_brut = self.ultrasonic.get_distance()
        self.distance = 0.8 * self.distance + 0.2 * dist_brut #lissage
        if self.distance > DIST_MAX:
            self.pwm.ChangeDutyCycle(0)
            return

        self.pwm.ChangeFrequency(FREQ_MIN * 2**((self.distance // LARG_NOTE) / 12))
        self.pwm.ChangeDutyCycle(50)

    def close(self):
        self.pwm.stop()
        GPIO.cleanup()


























        



