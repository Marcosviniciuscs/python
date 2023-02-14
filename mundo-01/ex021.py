import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Wm21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
#'tem que iniciar o mixer primeiro'
