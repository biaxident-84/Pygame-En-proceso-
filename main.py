import pygame
import sys
from nave import Nave_jugador

# Contanstes de pantalla
ANCHO = 800
ALTO = 600
VEL_NAVE = 5
 
# Inicialización del Pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Space Invaders - Fase 2")

clock = pygame.time.Clock()
COLOR = (0, 0, 0)

# Creamos la nave del jugador, centrada abajo
nave = Nave_jugador(
    x_inicial = ANCHO // 2 -25, # Centrad a 8 (50px de ancho)
    y_inicial = ALTO - 60, # Cerca del borde inferior
    velocidad = VEL_NAVE,
    limite_izq = 0,
    limite_der = ANCHO - 50 
)
# Game loop
while True:
    # Manejo de eventos ( tevclado, cerrar ventana, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Evento de disparo
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                nave.disparar()

    # Lógica del juego ( por ahora nada)
    nave.update()

    #Dibujar ( reubicar personajes)
    pantalla.fill(COLOR)  # Fondo
    nave.dibujar(pantalla) # Nave 

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)


