"""import pygame
pygame.init()
pygame.mixer.music.load('askin_you.wav')
pygame.mixer.music.play()
input()
pygame.event.wait()"""
import winsound
winsound.PlaySound('askin_you.wav', winsound.SND_FILENAME)