#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Modulos

import sys
import pygame
from pygame.locals import *

# Constantes

venx = 640
veny = 448

# Clases


class Pieza(pygame.sprite.Sprite):  # 64x64 px tamaño
    def __init__(self, tipo):
        pygame.sprite.Sprite.__init__(self)
        if tipo == 0:
            self.image = load_image("tablero.png", True)
        elif tipo == 1:
            self.image = load_image("laser.png", True)
        elif tipo == 2:
            self.image = load_image("diana.png", True)
        elif tipo == 3:
            self.image = load_image("diana_espejo.png", True)
        elif tipo == 4:
            self.image = load_image("espejo.png", True)
        elif tipo == 5:
            self.image = load_image("espejotraves.png", True)
        elif tipo == 6:
            self.image = load_image("tunel.png", True)
        elif tipo == 7:
            self.image = load_image("bloqueo.png", True)
        elif tipo == 8:
            self.image = load_image("bloqueo_g.png", True)
        elif tipo == 9:
            self.image = load_image("portal.png", True)
        else:
            tipo = 0
            self.image = load_image("tablero.png", True)

# Funciones


def load_image(filename, transparent=False):
    try:
        image = pygame.image.load(filename)
    except pygame.error:
        raise SystemExit
    image = image.convert()
    if transparent:
        color = image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    return image

#------------------------------------------


def main():
    screen = pygame.display.set_mode((venx, veny))
    pygame.display.set_caption("Laser Game")
    background_image = load_image('fondo.png')
    bola = Bola()
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        screen.blit(background_image, (0, 0))
        screen.blit(bola.image, bola.rect)
        pygame.display.flip()
    return 0

if __name__ == '__main__':
    pygame.init()
    main()
