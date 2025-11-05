import pygame
import sys
import random
from nave import Nave_jugador
from enemigo import Enemigo

# Detecta la colision
def hay_colision(enemigo, bala):
    """Detectar colision usando rectangulosde Pygame"""
    enemigo_rect = pygame.Rect(enemigo.x, enemigo.y, enemigo.image.get_width(), enemigo.image.get_height())
    return enemigo_rect.colliderect(bala.rect)
    

# Contanstes de pantalla
ANCHO = 800
ALTO = 600
VEL_NAVE = 5
puntaje = 0
 
# Inicialización del Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("assets/sounds/fondo.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Space Invaders - Fase 5")
clock = pygame.time.Clock()
COLOR = (0, 0, 0)

# Creamos la nave del jugador, centrada abajo
nave = Nave_jugador(
    image_path= "assets/images/nave.png",
    x_inicial = ANCHO // 2 -25, # Centrada (50px de ancho)
    y_inicial = ALTO - 60, # Cerca del borde inferior
    velocidad = VEL_NAVE,
    limite_izq = 0,
    limite_der = ANCHO - 50 
)

# Crear enemigos
enemigos = []
for i in range(6):
    enemigo = Enemigo("assets/images/ovni.png", ANCHO, ALTO)
    enemigos.append(enemigo)

#Cargar el sonido (Una sola vez, fuera del bucle)
sonido_explosion = pygame.mixer.Sound("assets/sounds/colision.mp3")

# Game loop
while True:
    # Manejo de eventos (teclado, cerrar ventana, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Evento de disparo
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                nave.disparar()

    #Dibujar ( reubicar personajes)
    pantalla.fill(COLOR)  # Fondo
    #Logica del juego
    nave.update()
    nave.dibujar(pantalla) # Nave 
    
    for enemigo in enemigos:
        enemigo.movimiento()
        

        #Nueva detección de colisión con colliderect
        for bala in nave.balas:
            if hay_colision(enemigo, bala):
                sonido_explosion.play()
                puntaje += 1
                enemigo.x = random.randint(0, ANCHO - 64)
                enemigo.y = random.randint(50, 150)
                nave.balas.remove(bala)

        enemigo.dibujar(pantalla) # Enemigo

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)


