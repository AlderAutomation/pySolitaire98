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

image = pygame.image.load("./assets/image/spritesheet.png").convert_alpha()
sprite_sheet =  spritesheet.SpriteSheet(image)

frame_0 = sprite_sheet.get_image(0, 0, 71, 96)
frame_1 = sprite_sheet.get_image(0, 1, 71, 96)
frame_2 = sprite_sheet.get_image(0, 2, 71, 96)
frame_3 = sprite_sheet.get_image(0, 3, 71, 96)



pygame.display.flip()


while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # test_card = card.Card("a", "clubs", frame_0)
    # surface.blit(test_deck.image[0], (5, 5))
    
    test_deck = deck.Deck()
    test_deck.shuffle
    hand = []
    hand.append(test_deck.deal())

    for card in hand:
        surface.blit(card.image, (5, 5))

    pygame.display.update()

pygame.quit()