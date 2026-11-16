from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import RPi.GPIO as GPIO
import pygame
import os
pygame.init()
screen_info = pygame.display.Info()
s_width = screen_info.current_w
s_height = screen_info.current_h
scalex = s_width / 1920
scaley = s_height / 1080
screen = pygame.display.set_mode((s_width, s_height))
grey = (200, 200, 200)
SPEAKER = 12
""""""
GPIO.setmode(GPIO.BCM)
GPIO.setup(SPEAKER, GPIO.OUT)
ultrasonic = GroveUltrasonicRanger(5)
""""""
pwm = GPIO.PWM(SPEAKER, 500)
pwm.start(50)
distance = 20 # init de la distance pr 1er itération
""""""