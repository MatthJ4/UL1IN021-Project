import RPi.GPIO as GPIO
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import time

SPEAKER = 12
FREQ_MIN = 261.63 #Hz (DO4)
DIST_MAX = 48 #cm
LARG_NOTE = 2
DELAY = 0.08 #sec
NB_NOTES = 24

class Instrument:
    """Capteur de distance + haut parleurs"""

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SPEAKER, GPIO.OUT)
        self.ultrasonic = GroveUltrasonicRanger(5)
        self.pwm = GPIO.PWM(SPEAKER, 500)
        self.pwm.start(0)
        self.distance = DIST_MAX #pour l'init seulement
        self.note_pot = None
        self.note = None
        self.depuis = 0.0
        self.mode = False

    def update(self):
        """Update de l'instrument toutes les frames"""
        dist_brut = self.ultrasonic.get_distance()
        self.distance = 0.8 * self.distance + 0.2 * dist_brut #lissage
        if self.mode:
            temps = time.monotonic()
            if self.distance > DIST_MAX:
                self.note_pot = None
                self.pwm.ChangeDutyCycle(0)
                self.note = None
                return
            
            note = min(int(self.distance // LARG_NOTE), NB_NOTES - 1)
            if note == self.note:
                self.note_pot = None
            elif note != self.note_pot:
                self.note_pot = note
                self.depuis = temps
            elif temps - self.depuis >= DELAY:
                self.pwm.ChangeFrequency(FREQ_MIN * 2 ** (note / 12))
                if self.note is None:
                    self.pwm.ChangeDutyCycle(50)
                self.note_pot = None
                self.note = note
        else:
            if self.distance > DIST_MAX:
            self.pwm.ChangeDutyCycle(0)
            return

            self.pwm.ChangeFrequency(FREQ_MIN * 2**((self.distance // LARG_NOTE) / 12))
            self.pwm.ChangeDutyCycle(50)

    def close(self):
        self.pwm.stop()
        GPIO.cleanup()


























        



