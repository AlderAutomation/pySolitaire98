import pygame
import settings
import spritesheet
import card
import deck

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

# image = pygame.image.load("./assets/image/spritesheet.png").convert_alpha()
# sprite_sheet =  spritesheet.SpriteSheet(image)

pygame.display.flip()

test_deck = deck.Deck()
test_deck.shuffle()


while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.blit(test_deck.card_deck[0].image, (20, 20))


    pygame.display.update()

pygame.quit()