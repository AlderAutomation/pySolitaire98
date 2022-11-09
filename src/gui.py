import logging
import pygame
import settings
import spritesheet
import deck
import my_logger


my_log = my_logger.Default().my_logger

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
clock = pygame.time.Clock()
FPS = 60

foundation_1 = []
foundation_2 = []
foundation_3 = []
foundation_4 = []

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
            draw_foundations()
            surface.blit(out_of_cards, (20, 20))
    elif len(dealer.card_deck) == 0 and dealer.is_out_of_cards == True:
        rebuild_stock_pile()
        redraw_all()


def switch_is_covered(card_to_cover:object, card_on_top:object) -> None: 
    card_on_top.is_covered = False
    card_to_cover.is_covered = True


def redraw_all():
    surface.fill(color)
    draw_foundations()
    draw_stock_pile()
    draw_colums()
    if len(waste_pile) > 1:
        draw_waste_pile(-1)


def draw_waste_pile(amount: int) -> None:
    surface.blit(waste_pile[amount].frontside, (waste_pile[amount].top_x, waste_pile[amount].top_y))


def draw_stock_pile() -> None:
    surface.blit(dealer.card_deck[-1].backside, (20, 20))
    surface.blit(dealer.card_deck[-1].backside, (30, 20))
    surface.blit(dealer.card_deck[-1].backside, (40, 20))


def draw_foundations() -> None:
    if len(foundation_1) == 0:
        surface.blit(empty_slot, (settings.col3_x, settings.row0_y))
    else:
        surface.blit(foundation_1[-1].frontside, (settings.col3_x, settings.row0_y))
    if len(foundation_2) == 0:
        surface.blit(empty_slot, (settings.col4_x, settings.row0_y))
    else:
        surface.blit(foundation_2[-1].frontside, (settings.col4_x, settings.row0_y))
    if len(foundation_3) == 0:
        surface.blit(empty_slot, (settings.col5_x, settings.row0_y))
    else:
        surface.blit(foundation_3[-1].frontside, (settings.col5_x, settings.row0_y))
    if len(foundation_4) == 0:
        surface.blit(empty_slot, (settings.col6_x, settings.row0_y))
    else:
        surface.blit(foundation_4[-1].frontside, (settings.col6_x, settings.row0_y))


def rebuild_stock_pile() -> None:
    my_log.debug("Rebuilding Stock Pile")

    while len(waste_pile) > 0:
        dealer.rebuild_from_discard(waste_pile[0])
        waste_pile.pop(0)
    
    dealer.is_out_of_cards = False


def new_game_deal():
    draw_stock_pile()
    draw_foundations()

    while len(col6) < 7:
        
        for col in cols:
            col.append(dealer.deal())

        flipme = cols.pop(0)

        flipme[-1].flip_card()
        flipme[-1].is_covered = False

        draw_colums()



def draw_colums() -> None:
        x_y_for_col(settings.col0_x, settings.row1_y, col0)
        deal_for_new_game(col0)
        x_y_for_col(settings.col1_x, settings.row1_y, col1)
        deal_for_new_game(col1)
        x_y_for_col(settings.col2_x, settings.row1_y, col2)
        deal_for_new_game(col2)
        x_y_for_col(settings.col3_x, settings.row1_y, col3)
        deal_for_new_game(col3)
        x_y_for_col(settings.col4_x, settings.row1_y, col4)
        deal_for_new_game(col4)
        x_y_for_col(settings.col5_x, settings.row1_y, col5)
        deal_for_new_game(col5)
        x_y_for_col(settings.col6_x, settings.row1_y, col6)
        deal_for_new_game(col6)

    
def x_y_for_col(x:int, y:int, col:object) -> None:
    temp_y = y

    for card in col:
        card.top_x = x
        card.top_y = temp_y
    
        temp_y = temp_y + settings.row0_y


def deal_for_new_game(col:object) -> None:
    for card in col: 
        if card.face == "down":
            surface.blit(card.backside, (card.top_x, card.top_y))
        else:
            surface.blit(card.frontside, (card.top_x, card.top_y))


def move_card(mouse_pos:tuple, card:object)->None: 
    card.top_x = mouse_pos[0]
    card.top_y = mouse_pos [1]

    surface.blit(card.frontside, (card.top_x, card.top_y))


def placement_checks(pos:tuple, from_pile:list ) -> None:
    card_placement(pos, col0, settings.col0_x, from_pile)
    card_placement(pos, col1, settings.col1_x, from_pile)
    card_placement(pos, col2, settings.col2_x, from_pile)

    if pos[1] < settings.row1_y:
        card_placement(pos, foundation_1, settings.col3_x, from_pile)
    elif pos[1] >= settings.row1_y:
        card_placement(pos, col3, settings.col3_x, from_pile)

    if pos[1] < settings.row1_y:
        card_placement(pos, foundation_2, settings.col4_x, from_pile)
    elif pos[1] >= settings.row1_y:
        card_placement(pos, col4, settings.col4_x, from_pile)

    if pos[1] < settings.row1_y:
        card_placement(pos, foundation_3, settings.col5_x, from_pile)
    elif pos[1] >= settings.row1_y:
        card_placement(pos, col5, settings.col5_x, from_pile)

    if pos[1] < settings.row1_y:
        card_placement(pos, foundation_4, settings.col6_x, from_pile)
    elif pos[1] >= settings.row1_y:
        card_placement(pos, col6, settings.col6_x, from_pile)


def card_placement(pos:tuple, to_pile:list, x:int, from_pile: list):
    if pos[0] >= x and pos[0] <= x + settings.card_width:
        to_pile.append(from_pile.pop())
        redraw_all()
        if len(from_pile) > 1:
            surface.blit(from_pile[-1].frontside, (from_pile[-1].top_x, from_pile[-1].top_y))
        if len(to_pile) > 1:
            switch_is_covered(to_pile[-2], to_pile[-1])


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

                if len(waste_pile) > 0: 
                    waste_pile[-1].set_is_clicked(pos, True)

                
                for col in cols:
                    if len(col) > 0:
                        col[-1].set_is_clicked(pos, True)


            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                for col in cols:
                    for card in col:
                        if card.is_clicked:
                            if len(col) == 2:
                                col[-2].is_covered = False
                            elif len(col) > 2:
                                switch_is_covered(col[-3], col[-2])
                            placement_checks(pos, col)
                        card.set_is_clicked(pos, False)

                for card in waste_pile:
                    if card.is_clicked:                       
                        if len(waste_pile) == 2:
                            waste_pile[-2].is_covered = False
                        elif len(waste_pile) > 2:
                            switch_is_covered(waste_pile[-3], waste_pile[-2])
                        placement_checks(pos, waste_pile)
                    card.set_is_clicked(pos, False)
                     
                try:
                    if pos[0] >= settings.col0_x and pos[0] <= settings.col0_x + settings.card_width:
                        if pos[1] >= settings.row0_y and pos[1] <= settings.row0_y + settings.card_height:
                            deal_cards()
                except:
                    deal_cards()

            if event.type == pygame.MOUSEMOTION and len(waste_pile) > 0:
                if waste_pile[-1].is_clicked:
                    pos = pygame.mouse.get_pos()
                    redraw_all()
                    if len(waste_pile) > 1:
                        surface.blit(waste_pile[-2].frontside, (waste_pile[-2].top_x, waste_pile[-2].top_y))
                    move_card(pos, waste_pile[-1])

            for col in cols:
                if event.type == pygame.MOUSEMOTION and len(col) > 0:
                    if col[-1].is_clicked:
                        pos = pygame.mouse.get_pos()
                        redraw_all()
                        move_card(pos, col[-1])


        clock.tick(FPS)

        pygame.display.flip()

    pygame.quit()


if __name__=="__main__":
    main()