import pygame
import settings

pygame.init()
running = True

width = settings.width1
height = settings.height1
color = settings.original_green


surface = pygame.display.set_mode((width, height))
surface.fill(color)
pygame.display.set_caption("pySolitaire98")

icon_name = pygame.image.load("./assets/image/icon.png")
pygame.display.set_icon(icon_name)

image = pygame.load_ ("./assets/image/spritesheet.png")

pygame.display.flip()


while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.blit(image, (0,0))

    pygame.display.update()