import logging
import pygame
import settings
import spritesheet
import deck

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="log.log", level=logging.DEBUG, format = LOG_FORMAT)
my_logger = logging.getLogger()

pygame.init()

# Surface setup
width = settings.width1
height = settings.height1
color = settings.original_green

surface = pygame.display.set_mode((width, height))
surface.fill(color)
pygame.display.set_caption("pySolitaire98")
icon = pygame.image.load("./assets/image/icon.png")
pygame.display.set_icon(icon)

# Spritesheet 
image = pygame.image.load("./assets/image/spritesheet.png")
sprite_sheet =  spritesheet.SpriteSheet(image)

empty_slot = sprite_sheet.get_image(0, 4, 71, 96, settings.scale)
out_of_cards = sprite_sheet.get_image(1, 5, 71, 96, settings.scale)

pygame.display.flip()

# game init'ing
dealer = deck.Deck()
dealer.shuffle()
waste_pile = []

col0 = []
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []

cols = [col0, col1, col2, col3, col4, col5, col6]

def deal_cards() -> None:
    if len(dealer.card_deck) > 0:
        waste_pile.append(dealer.deal())
        waste_pile[-1].top_x = 166
        waste_pile[-1].top_y = 20
        waste_pile[-1].face = "up"
        waste_pile[-1].is_covered = False
        if len(waste_pile) > 1:
            waste_pile[-2].is_covered = True
        surface.blit(waste_pile[-1].frontside, (waste_pile[-1].top_x, waste_pile[-1].top_y))
        pygame.display.update()
        print(f"Remaining cards: {len(dealer.card_deck)}")
        if len(dealer.card_deck) == 0 and dealer.is_out_of_cards == False:
            dealer.is_out_of_cards = True
            
            surface.fill(color)
            surface.blit(waste_pile[-1].frontside, (waste_pile[-1].top_x, waste_pile[-1].top_y))
            draw_colums()
            surface.blit(out_of_cards, (20, 20))
    elif len(dealer.card_deck) == 0 and dealer.is_out_of_cards == True:
        rebuild_stock_pile()
        surface.fill(color)
        draw_stock_pile()
        draw_colums()


def draw_stock_pile() -> None:
    surface.blit(dealer.card_deck[-1].backside, (20, 20))
    surface.blit(dealer.card_deck[-1].backside, (30, 20))
    surface.blit(dealer.card_deck[-1].backside, (40, 20))


def rebuild_stock_pile() -> None:
    my_logger.debug("Rebuilding Stock Pile")

    while len(waste_pile) > 0:
        dealer.rebuild_from_discard(waste_pile[0])
        waste_pile.pop(0)
    
    dealer.is_out_of_cards = False


def new_game_deal():
    draw_stock_pile()

    while len(col6) < 7:
        
        for col in cols:
            col.append(dealer.deal())

        flipme = cols.pop(0)

        flipme[-1].flip_card()
        flipme[-1].is_covered = False

        draw_colums()



def draw_colums() -> None:
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
    temp_y = y

    for card in col:
        card.top_x = x
        card.top_y = temp_y
    
        temp_y = temp_y + 20


def deal_for_new_game(col:object) -> None:
    for card in col: 
        if card.face == "down":
            surface.blit(card.backside, (card.top_x, card.top_y))
        else:
            surface.blit(card.frontside, (card.top_x, card.top_y))


def main():
    running = True
    
    new_game_deal()

    cols = []
    cols = [col0, col1, col2, col3, col4, col5, col6]


    while running: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for card in waste_pile:
                    card.set_is_clicked(pos)

                for col in cols:
                    for card in col:
                        card.set_is_clicked(pos)


            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                for card in waste_pile:
                    card.set_is_clicked(pos)

                for col in cols:
                    for card in col:
                        card.set_is_clicked(pos)

                try:
                    if pos[0] >= 20 and pos[0] <= 20 + settings.card_width:
                        if pos[1] >= 20 and pos[1] <= 20 + settings.card_height:
                            deal_cards()
                except:
                    deal_cards()


        pygame.display.update()

    pygame.quit()


if __name__=="__main__":
    main()