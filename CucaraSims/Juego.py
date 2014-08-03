#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import gobject
import pygame
import gtk

from pygame.locals import HWSURFACE
#from BiblioJAM.JAMButton import JAMButton

#from Bicho import Bicho

RESOLUCION_INICIAL = (800, 600)
BASE_PATH = os.path.dirname(__file__)
BASE_PATH = os.path.dirname(BASE_PATH)

gobject.threads_init()


class CucaraSims(gobject.GObject):

    __gsignals__ = {
    "exit": (gobject.SIGNAL_RUN_LAST,
        gobject.TYPE_NONE, [])}

    def __init__(self):

        gobject.GObject.__init__(self)

        self.RESOLUCION_INICIAL = RESOLUCION_INICIAL
        self.resolucionreal = RESOLUCION_INICIAL
        self.ventana_real = False
        self.escenario = False
        self.ventana = False
        self.reloj = False
        self.estado = 0

        #self.sprites = pygame.sprite.RenderUpdates()
        #self.widgets = pygame.sprite.RenderUpdates()

    def __handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.emit("exit")
                    return
        pygame.event.clear()

    def run(self):
        print "Corriendo CucaraSims . . ."
        self.estado = 1
        self.ventana.blit(self.escenario, (0, 0))
        self.ventana_real.blit(pygame.transform.scale(self.ventana,
            self.resolucionreal), (0, 0))
        pygame.display.update()

        try:
            while self.estado:
                self.reloj.tick(35)
                while gtk.events_pending():
                    gtk.main_iteration()
                #if len(self.sprites.sprites()) < 5:
                #    gobject.idle_add(self.sprites.add,
                #        Bicho(RESOLUCION_INICIAL[0],
                #        RESOLUCION_INICIAL[1]))
                #self.sprites.clear(self.ventana, self.escenario)
                #self.widgets.clear(self.ventana, self.escenario)
                #self.sprites.update()
                #self.widgets.update()
                self.__handle_event()
                #self.sprites.draw(self.ventana)
                #self.widgets.draw(self.ventana)
                self.ventana_real.blit(pygame.transform.scale(
                    self.ventana, self.resolucionreal), (0, 0))
                pygame.display.update()
                pygame.time.wait(3)
        except:
            pass

    def stop(self):
        self.estado = 0
        pygame.quit()

    def salir(self, widget=False):
        self.estado = 0
        pygame.quit()

    def escalar(self, resolucion):
        self.resolucionreal = resolucion

    def config(self):
        pygame.init()
        self.reloj = pygame.time.Clock()

        from pygame.locals import MOUSEMOTION
        from pygame.locals import MOUSEBUTTONUP
        from pygame.locals import MOUSEBUTTONDOWN
        from pygame.locals import JOYAXISMOTION
        from pygame.locals import JOYBALLMOTION
        from pygame.locals import JOYHATMOTION
        from pygame.locals import JOYBUTTONUP
        from pygame.locals import JOYBUTTONDOWN
        from pygame.locals import VIDEORESIZE
        from pygame.locals import VIDEOEXPOSE
        from pygame.locals import USEREVENT
        from pygame.locals import QUIT
        from pygame.locals import ACTIVEEVENT
        from pygame.locals import KEYDOWN
        from pygame.locals import KEYUP

        pygame.event.set_blocked([
            JOYAXISMOTION, JOYBALLMOTION, JOYHATMOTION, JOYBUTTONUP,
            JOYBUTTONDOWN, ACTIVEEVENT, USEREVENT])
        pygame.event.set_allowed([QUIT, VIDEORESIZE, VIDEOEXPOSE,
            KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN])
        pygame.key.set_repeat(15, 15)

        pygame.display.set_mode(
            (0, 0), pygame.DOUBLEBUF | pygame.FULLSCREEN, 0)

        pygame.display.set_caption("CucaraSims")

        path = os.path.join(BASE_PATH, "CucaraSims", "Imagenes", "arena1.png")
        imagen = pygame.image.load(path)
        self.escenario = pygame.transform.scale(
            imagen, RESOLUCION_INICIAL).convert_alpha()

        self.ventana = pygame.Surface((RESOLUCION_INICIAL[0],
            RESOLUCION_INICIAL[1]), flags=HWSURFACE)
        self.ventana_real = pygame.display.get_surface()
