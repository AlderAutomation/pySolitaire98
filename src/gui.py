from logging import exception
import pygame
import settings
import spritesheet
import deck

pygame.init()

width = settings.width1
height = settings.height1
color = settings.original_green


surface = pygame.display.set_mode((width, height))
surface.fill(color)
pygame.display.set_caption("pySolitaire98")

icon = pygame.image.load("./assets/image/icon.png")
pygame.display.set_icon(icon)


image = pygame.image.load("./assets/image/spritesheet.png")
sprite_sheet =  spritesheet.SpriteSheet(image)

empty_slot = sprite_sheet.get_image(0, 4, 71, 96, 1.5)
out_of_cards = sprite_sheet.get_image(1, 5, 71, 96, 1.5)

pygame.display.flip()

dealer = deck.Deck()
dealer.shuffle()

draw_cards = []

col0 = []
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []

cols = [col0, col1, col2, col3, col4, col5, col6]


def deal_cards() -> None:
    try:
        draw_cards.append(dealer.deal())
        draw_cards[-1].x = 150
        draw_cards[-1].y = 20
        surface.blit(draw_cards[-1].frontside, (draw_cards[-1].x, draw_cards[-1].y))
        pygame.display.update()
        print(f"Remaining cards: {len(dealer.card_deck)}")
    except:
        print("Out of cards")
 

def new_game_deal():

    while len(col6) < 7:
        
        for col in cols:
            col.append(dealer.deal())

        flipme = cols.pop(0)

        flipme[-1].flip_card()

        x_y_for_col(20,200,col0)
        deal_for_new_game(col0)
        x_y_for_col(166,200,col1)
        deal_for_new_game(col1)
        x_y_for_col(312,200,col2)
        deal_for_new_game(col2)
        x_y_for_col(458,200,col3)
        deal_for_new_game(col3)
        x_y_for_col(604,200,col4)
        deal_for_new_game(col4)
        x_y_for_col(750,200,col5)
        deal_for_new_game(col5)
        x_y_for_col(896,200,col6)
        deal_for_new_game(col6)


    
def x_y_for_col(x:int, y:int, col:object) -> None:
    temp_x = x
    temp_y = y

    for card in col:
        card.x = temp_x
        card.y = temp_y
    
        # temp_x = temp_x + 20
        temp_y = temp_y + 20


def deal_for_new_game(col:object) -> None:
    for card in col: 
        if card.face == "down":
            surface.blit(card.backside, (card.x, card.y))
        else:
            surface.blit(card.frontside, (card.x, card.y))


def main():
    running = True

    new_game_deal()

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



        pygame.display.update()

    pygame.quit()


if __name__=="__main__":
    main()