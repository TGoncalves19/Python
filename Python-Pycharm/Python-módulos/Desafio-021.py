# Desafio 021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input()'''

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()