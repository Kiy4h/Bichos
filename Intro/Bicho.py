#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Bicho.py por:
#   Flavio Danesse <fdanesse@gmail.com>

import os
import pygame
from pygame.sprite import Sprite
import random
from math import sin, cos, radians

BASE_PATH = os.path.dirname(__file__)
BASE_PATH = os.path.dirname(BASE_PATH)

INDICE_ROTACION = 5


class Bicho(Sprite):

    def __init__(self, ancho, alto):

        Sprite.__init__(self)

        files = []
        dirpath = os.path.join(BASE_PATH, "Bichos")
        for archivo in os.listdir(dirpath):
            files.append(os.path.join(dirpath, archivo))

        random.seed()
        path = random.choice(files)
        imagen = pygame.image.load(path)
        imagen_escalada = pygame.transform.scale(imagen, (60, 50))
        self.imagen_original = imagen_escalada.convert_alpha()

        self.image = self.imagen_original.copy()
        self.rect = self.image.get_rect()

        sounds = []
        dirpath = os.path.join(BASE_PATH, "Sonidos")
        for archivo in os.listdir(dirpath):
            sounds.append(os.path.join(dirpath, archivo))

        random.seed()
        path = random.choice(sounds)
        self.sonido = pygame.mixer.Sound(path)

        random.seed()
        self.velocidad = random.randrange(3, 11, 1)

        self.contador = 0
        self.escena = pygame.Rect(35, 35, ancho - 70, alto - 70)

        self.angulo = 0
        self.dx = 0
        self.dy = 0
        self.__run()

    def __run(self):
        random.seed()
        self.angulo = random.randrange(0, 360, 5)
        x = self.escena.w / 2
        y = self.escena.h / 2
        self.rect.centerx, self.rect.centery = (x, y)
        self.dx, self.dy = self.__get_vector(self.angulo)
        self.__actualizar_posicion()
        #self.sonido.play(-1)

    def __get_vector(self, angulo):
        radianes = radians(angulo)
        x = int(cos(radianes) * self.velocidad)
        y = int(sin(radianes) * self.velocidad)
        return x, y

    def __actualizar_posicion(self):
        self.image = pygame.transform.rotate(
            self.imagen_original, -self.angulo)
        x = self.rect.centerx + self.dx
        y = self.rect.centery + self.dy
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        if self.rect.colliderect(self.escena):
            #if self.contador > 30:
            #    sent = random.randrange(1, 3, 1)
            #    if sent == 1:
            #        self.angulo -= int(0.7 * INDICE_ROTACION)
            #    elif sent == 2:
            #        self.angulo += int(0.7 * INDICE_ROTACION)
            #    self.contador = 0
            #self.contador += 1
            self.dx, self.dy = self.__get_vector(self.angulo)
            self.__actualizar_posicion()
        else:
            #self.sonido.stop()
            self.kill()
            return
