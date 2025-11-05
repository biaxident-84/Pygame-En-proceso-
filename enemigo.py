import pygame
import random

class Enemigo:
    def __init__(self, image_path, pantalla_ancho, pantalla_alto):
        """Incializa un enemigo en una posición aleatoria"""
        self.image = pygame.image.load(image_path) # Cargar la imagen del objeto
        self.x = random.randint(0, pantalla_ancho - 64)
        self.y = random.randint(50, 150)
        self.x_velocidad = 3
        self.y_velocidad = 40
        self.pantalla_ancho = pantalla_ancho
        self.pantalla_alto = pantalla_alto

    def movimiento(self):
        """Mueve al enemigo horizontalmente y lo hace bajar al tocar los bordes"""
        self.x += self.x_velocidad # Mueve al enemigo independientemente de si llego a los bordes o no

        # Rebote en los bordes
        if self.x <= 0:
            self.x_velocidad = abs(self.x_velocidad) # Cambia el sentido de mov izq a der
            self.y += self.y_velocidad # Al llegar al borde baja el enemigo
        elif self.x >= self.pantalla_ancho - 64:
            self.x_velocidad = -abs(self.x_velocidad) # Cambia el sentido de mov de r a mov izq
            self.y += self.y_velocidad  #Al llegar al borde baja el enemigo

    # Dibujar la figura despues del update  
    def dibujar(self, surface):
        """Dibuja al enemigo en la pantalla"""
        surface.blit(self.image, (self.x, self.y))
