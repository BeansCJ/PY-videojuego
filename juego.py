import pygame

pygame.init()

ANCHO = 800
ALTO = 600
VELOCIDAD = 5

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("PY VIDEOJUEGO")
reloj = pygame.time.Clock()

jugador = pygame.image.load("rocket.png").convert_alpha()
jugador_x = (ANCHO - jugador.get_width()) // 2
jugador_y = (ALTO - jugador.get_height()) // 2

jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]:
        jugador_x -= VELOCIDAD
    if teclas[pygame.K_d]:
        jugador_x += VELOCIDAD
    if teclas[pygame.K_w]:
        jugador_y -= VELOCIDAD
    if teclas[pygame.K_s]:
        jugador_y += VELOCIDAD

    jugador_x = max(0, min(jugador_x, ANCHO - jugador.get_width()))
    jugador_y = max(0, min(jugador_y, ALTO - jugador.get_height()))

    pantalla.fill((67, 10, 93))
    pantalla.blit(jugador, (jugador_x, jugador_y))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
