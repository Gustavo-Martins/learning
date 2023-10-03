# Opens and plays music
import pygame


pygame.init()
pygame.mixer.music.load("Intro_And_Tarantelle.mp3")
pygame.mixer.music.play()
pygame.event.wait()
