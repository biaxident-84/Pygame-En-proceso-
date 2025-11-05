import pygame

COLOR_BALA = (255, 255, 0) # Amarillo
ANCHO_BALA = 5
ALTO_BALA = 15

class Bala:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.rect = pygame.Rect(self.x, self.y, ANCHO_BALA, ALTO_BALA)

    def update(self):
        """Actualiza la posición de la bala"""
        self.y -= self.velocidad
        self.rect.topleft = (self.x, self.y)

    def dibujar(self, surface):
        """Dibujar la bala"""
        pygame.draw.rect(surface, COLOR_BALA, self.rect)

    def fuera_de_pantalla(self):
        """Indica si la bala ya salio de la pantalla (por arriba)"""
        return (self.y + ALTO_BALA) < 0
        
    
        