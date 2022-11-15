import pygame
import settings
import spritesheet
import deck
import my_logger

my_log = my_logger.Default().my_logger


class SolitaireGUI():
    def __init__(self) -> None:       
        pygame.init()

        # Surface setup
        width = settings.width1
        height = settings.height1
        self.color = settings.original_green

        self.surface = pygame.display.set_mode((width, height))
        self.surface.fill(self.color)
        pygame.display.set_caption("pySolitaire98")
        icon = pygame.image.load("./assets/image/icon.png")
        pygame.display.set_icon(icon)

        # Spritesheet 
        image = pygame.image.load("./assets/image/spritesheet.png")
        sprite_sheet =  spritesheet.SpriteSheet(image)

        self.empty_slot = sprite_sheet.get_image(0, 4, 71, 96, settings.scale)
        out_of_cards = sprite_sheet.get_image(1, 5, 71, 96, settings.scale)

        pygame.display.flip()

        self.clock = pygame.time.Clock()
        self.FPS = 60


    def redraw_all(self, game):
        self.surface.fill(self.color)
        self.draw_foundations(game.foundations)
        self.draw_stock_pile(game.stock)
        self.draw_colums(game.col0, game.col1, game.col2, game.col3, game.col4, game.col5, game.col6)
        if len(game.talon) > 1:
            self.draw_talon(-1, game.talon)


    def draw_talon(self, amount: int, talon:list) -> None:
        self.surface.blit(talon[amount].frontside, (talon[amount].top_x, talon[amount].top_y))


    def draw_stock_pile(self, stock:list) -> None:
        self.surface.blit(stock.card_deck[-1].backside, (20, 20))
        self.surface.blit(stock.card_deck[-1].backside, (30, 20))
        self.surface.blit(stock.card_deck[-1].backside, (40, 20))


    def draw_foundations(self, foundations:list) -> None:
        x = settings.col3_x

        for foundation in foundations:
            if len(foundation) == 0:
                self.surface.blit(self.empty_slot, (x, settings.row0_y))
            else:
                self.surface.blit(foundation[-1].frontside, (x, settings.row0_y))
            x = x + 146


    def draw_colums(self, col0, col1, col2, col3, col4, col5, col6) -> None:
        # x = settings.col0_x

        # for col in cols:
        #     self.x_y_for_col(x, settings.row1_y, col)
        #     self.deal_for_new_game(col)
        #     x = x + 146

        self.x_y_for_col(settings.col0_x, settings.row1_y, col0)
        self.deal_for_new_game(col0)
        self.x_y_for_col(settings.col1_x, settings.row1_y, col1)
        self.deal_for_new_game(col1)
        self.x_y_for_col(settings.col2_x, settings.row1_y, col2)
        self.deal_for_new_game(col2)
        self.x_y_for_col(settings.col3_x, settings.row1_y, col3)
        self.deal_for_new_game(col3)
        self.x_y_for_col(settings.col4_x, settings.row1_y, col4)
        self.deal_for_new_game(col4)
        self.x_y_for_col(settings.col5_x, settings.row1_y, col5)
        self.deal_for_new_game(col5)
        self.x_y_for_col(settings.col6_x, settings.row1_y, col6)
        self.deal_for_new_game(col6)






    def deal_for_new_game(self, col:object) -> None:
        for card in col: 
            if card.face == "down":
                self.surface.blit(card.backside, (card.top_x, card.top_y))
            else:
                self.surface.blit(card.frontside, (card.top_x, card.top_y))


    def x_y_for_col(self, x:int, y:int, col:object) -> None:
        temp_y = y

        for card in col:
            card.top_x = x
            card.top_y = temp_y
        
            temp_y = temp_y + settings.row0_y

    def move_card(self, mouse_pos:tuple, card:object)->None: 
        # Card Dragging and drawing function
        card.top_x = mouse_pos[0]
        card.top_y = mouse_pos [1]

        self.surface.blit(card.frontside, (card.top_x, card.top_y))

    def col_flip_check(self, col: list):
        if len(col) == 0:
            return False
        elif col[-1].face == "down" and col[-1].is_covered == False:
            return  True


    def run(self, game):
        running = True
        
        game.new_game_deal(self)


        while running: 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if len(game.talon) > 0: 
                        game.talon[-1].set_is_clicked(pos, True)

                    print(game.cols)
                    
                    for col in game.cols:
                        if len(col) > 0:
                            
                            col[-1].set_is_clicked(pos, True)


                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()


                    for col in game.cols:
                        if self.col_flip_check(col):
                            col[-1].flip_card()
                            my_log.debug(f"{col[-1].number} of {col[-1].suit} has been flipped")
                        for card in col:
                            if card.is_clicked: 
                                if len(col) == 2:
                                    col[-2].is_covered = False
                                elif len(col) > 2:
                                    game.switch_is_covered(col[-3], col[-2])
                                game.placement_checks(self, pos, col)
                            card.set_is_clicked(pos, False)
                        self.redraw_all(game)

                    for card in game.talon:
                        if card.is_clicked:                       
                            if len(game.talon) == 2:
                                game.talon[-2].is_covered = False
                            elif len(game.talon) > 2:
                                game.switch_is_covered(game.talon[-3], game.talon[-2])
                            game.placement_checks(self, pos, game.talon)
                        card.set_is_clicked(pos, False)
                        
                    try:
                        if pos[0] >= settings.col0_x and pos[0] <= settings.col0_x + settings.card_width:
                            if pos[1] >= settings.row0_y and pos[1] <= settings.row0_y + settings.card_height:
                                game.deal_cards(self)
                    except:
                        game.deal_cards(self)

                if event.type == pygame.MOUSEMOTION and len(game.talon) > 0:
                    if game.talon[-1].is_clicked:
                        pos = pygame.mouse.get_pos()
                        self.redraw_all(game)
                        if len(game.talon) > 1:
                            self.surface.blit(game.talon[-2].frontside, (game.talon[-2].top_x, game.talon[-2].top_y))
                        self.move_card(pos, game.talon[-1])

                for col in game.cols:
                    if event.type == pygame.MOUSEMOTION and len(col) > 0:
                        if col[-1].is_clicked:
                            pos = pygame.mouse.get_pos()
                            self.redraw_all(game)
                            self.move_card(pos, col[-1])


            self.clock.tick(self.FPS)

            pygame.display.flip()

        pygame.quit()









