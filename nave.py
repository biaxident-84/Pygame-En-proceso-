import pygame
from bala import Bala

COLOR_NAVE = (0, 255, 0) # verde para verla fácil
ANCHO_NAVE = 50
ALTO_NAVE = 50

class Nave_jugador:
    # Como nace el objeto
    def __init__(self, image_path, x_inicial, y_inicial, velocidad, limite_izq, limite_der):
        # Estado interno (atributos)
        self.image = pygame.image.load(image_path)
        self.x = x_inicial
        self.y = y_inicial
        self.velocidad = velocidad
        self.limite_izq = limite_izq
        self.limite_der = limite_der
        # Rectangulo para representar la nave
        #self.rect = pygame.Rect(self.x, self.y, ANCHO_NAVE, ALTO_NAVE)
        self.balas = [] # Lista para almacenar balas activas
    
    def manejar_input(self):
        """Lee el teclado y ajustar la posición de la nave"""
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidad
        
        # Disparo
        # pygame.key.get_pressed() no detecta  " tecla recien presionada"
        # asi que esto lo manejaremos desde el lopp principal


        # limites de pantalla ( no salirse)
        if self.x < self.limite_izq:
            self.x = self.limite_izq
        if self.x > self.limite_der:
            self.x = self.limite_der

        # Actualizar el rect para que siga en x. y
        #self.rect.topleft = (self.x, self.y)

    # Dibujar la figura despues del update
    def dibujar(self, surface):
        """Dibuja la nave como un rectángulo"""
        #pygame.draw.rect(surface, COLOR_NAVE, self.rect)
        surface.blit(self.image, (self.x, self.y))
        # Mas adelante esto será una imagen
        for bala in self.balas:
            bala.dibujar(surface)

    # Se ejecuta en cada frame
    def update(self):
        """Punto central de actualización  por frame"""
        self.manejar_input()
        # Mas comportamiento a futuro: disparar, animaciones, etc.

        # Actualizar y limpiar balas
        for bala in self.balas[:]:
            bala.update()
            if bala.fuera_de_pantalla():
                self.balas.remove(bala)

    def disparar(self):
        """Crear una nueva bala desde el centro superior de la nave"""
        x_bala = self.x + ANCHO_NAVE // 2 - 2
        y_bala = self.y
        nueva_bala = Bala(x_bala, y_bala, velocidad=8)
        self.balas.append(nueva_bala)
        
        
