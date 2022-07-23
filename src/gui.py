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
out_of_cards = sprite_sheet.get_image(1, 5, 71, 96, 1.5)

# def deal_next_card(pos) -> None:
#     if pos is 



pygame.display.flip()

dealer = deck.Deck()
dealer.shuffle()

draw_cards = []

def deal_cards() -> None:
    try:
        draw_cards.append(dealer.deal())
        draw_cards[-1].x = 150
        draw_cards[-1].y = 20
        surface.blit(draw_cards[-1].frontside, (draw_cards[-1].x, draw_cards[-1].y))
        pygame.display.update()
    except:
        print("Out of cards")
 


while running: 

    surface.blit(empty_slot, (568, 20))

    try:
        surface.blit(dealer.card_deck[-1].backside, (20, 20))
        surface.blit(dealer.card_deck[-1].backside, (25, 20))
        surface.blit(dealer.card_deck[-1].backside, (30, 20))
    except:
        surface.blit(out_of_cards, (20, 20))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            print (pos)
            deal_cards()
            # if test_deck.card_deck[51].rect.collidepoint(pos):
            #     print ("Deal!")



    pygame.display.update()

pygame.quit()