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


image = pygame.image.load("./assets/image/spritesheet.png")
sprite_sheet =  spritesheet.SpriteSheet(image)



empty_slot = sprite_sheet.get_image(0, 4, 71, 96, 1.5)






pygame.display.flip()

test_deck = deck.Deck()
test_deck.shuffle()



while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.blit(empty_slot, (568, 20))

    surface.blit(test_deck.card_deck[51].backside, (20, 20))
    surface.blit(test_deck.card_deck[51].backside, (25, 20))
    surface.blit(test_deck.card_deck[51].backside, (30, 20))
    surface.blit(test_deck.card_deck[0].frontside, (20, 175))


    pygame.display.update()

pygame.quit()