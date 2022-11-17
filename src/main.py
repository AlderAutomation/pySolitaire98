import deck 
import view
import settings
import my_logger

my_log = my_logger.Default().my_logger


class Controller():
    def __init__(self) -> None:
        # game init'ing
        self.stock = deck.Deck()
        self.stock.shuffle()
        self.talon = []

        self.foundation_1 = []
        self.foundation_2 = []
        self.foundation_3 = []
        self.foundation_4 = []

        self.foundations = [self.foundation_1, self.foundation_2, self.foundation_3, self.foundation_4]

        self.col0 = []
        self.col1 = []
        self.col2 = []
        self.col3 = []
        self.col4 = []
        self.col5 = []
        self.col6 = []

        self.cols = [self.col0, self.col1, self.col2, self.col3, self.col4, self.col5, self.col6]


    def deal_cards(self, gui) -> None:
        if len(self.stock.card_deck) > 0:
            self.talon.append(self.stock.deal())
            self.talon[-1].top_x = 166
            self.talon[-1].top_y = 20
            self.talon[-1].face = "up"
            self.talon[-1].is_covered = False
            if len(self.talon) > 1:
                self.talon[-2].is_covered = True
            gui.surface.blit(self.talon[-1].frontside, (self.talon[-1].top_x, self.talon[-1].top_y))
            my_log.debug(f"Remaining cards: {len(self.stock.card_deck)}")
            print(f"Remaining cards: {len(self.stock.card_deck)}")
            if len(self.stock.card_deck) == 0 and self.stock.is_out_of_cards == False:
                self.stock.is_out_of_cards = True
                
                gui.surface.fill(gui.color)
                gui.surface.blit(self.talon[-1].frontside, (self.talon[-1].top_x, self.talon[-1].top_y))
                gui.draw_colums(self.col0, self.col1, self.col2, self.col3, self.col4, self.col5, self.col6)
                gui.draw_foundations(self.foundations)
                gui.surface.blit(gui.out_of_cards, (20, 20))
                print ("draw out of cards")
        elif len(self.stock.card_deck) == 0 and self.stock.is_out_of_cards == True:
            self.rebuild_stock_pile()
            gui.redraw_all(self)

        
    def rebuild_stock_pile(self) -> None:
        my_log.debug("Rebuilding Stock Pile")

        while len(self.talon) > 0:
            self.stock.rebuild_from_discard(self.talon[0])
            self.talon.pop(0)
        
        self.stock.is_out_of_cards = False


    def new_game_deal(self, gui):
        gui.draw_stock_pile(self.stock)
        gui.draw_foundations(self.foundations)

        while len(self.col6) < 7:
            
            for col in self.cols:
                col.append(self.stock.deal())

            flipme = self.cols.pop(0)

            flipme[-1].flip_card()
            flipme[-1].is_covered = False

            gui.draw_colums(self.col0, self.col1, self.col2, self.col3, self.col4, self.col5, self.col6)

        self.cols = [self.col0, self.col1, self.col2, self.col3, self.col4, self.col5, self.col6]


    def card_placement(self, gui, pos:tuple, to_pile:list, x:int, from_pile: list):
        if pos[0] >= x and pos[0] <= x + settings.card_width:
            to_pile.append(from_pile.pop())
            gui.redraw_all(self)
            if len(from_pile) > 1:
                gui.surface.blit(from_pile[-1].backside, (from_pile[-1].top_x, from_pile[-1].top_y))
            if len(to_pile) > 1:
                self.switch_is_covered(to_pile[-2], to_pile[-1])


    def placement_checks(self, gui,  pos:tuple, from_pile:list ) -> None:

        if pos[1] < settings.row1_y:
            if pos[0] >= settings.col3_x and pos[0] <= settings.col3_x + settings.card_width:
                if self.foundation_checks(self.foundation_1, from_pile):
                    self.card_placement(gui, pos, self.foundation_1, settings.col3_x, from_pile)
            if pos[0] >= settings.col4_x and pos[0] <= settings.col4_x + settings.card_width:
                if self.foundation_checks(self.foundation_2, from_pile):
                    self.card_placement(gui, pos, self.foundation_2, settings.col4_x, from_pile)
            if pos[0] >= settings.col5_x and pos[0] <= settings.col5_x + settings.card_width:
                if self.foundation_checks(self.foundation_1, from_pile):
                    self.card_placement(gui, pos, self.foundation_1, settings.col5_x, from_pile)
            if pos[0] >= settings.col6_x and pos[0] <= settings.col6_x + settings.card_width:
                if self.foundation_checks(self.foundation_2, from_pile):
                    self.card_placement(gui, pos, self.foundation_2, settings.col6_x, from_pile)

        elif pos[1] >= settings.row1_y:
            if pos[0] >= settings.col0_x and pos[0] <= settings.col0_x + settings.card_width:
                if self.col_checks(self.col0, from_pile):
                    self.card_placement(gui, pos, self.col0, settings.col0_x, from_pile)
            if pos[0] >= settings.col1_x and pos[0] <= settings.col1_x + settings.card_width:
                if self.col_checks(self.col1, from_pile):
                    self.card_placement(gui, pos, self.col1, settings.col1_x, from_pile)
            if pos[0] >= settings.col2_x and pos[0] <= settings.col2_x + settings.card_width:
                if self.col_checks(self.col2, from_pile):
                    self.card_placement(gui, pos, self.col2, settings.col2_x, from_pile)
            if pos[0] >= settings.col3_x and pos[0] <= settings.col3_x + settings.card_width:
                if self.col_checks(self.col3, from_pile):
                    self.card_placement(gui, pos, self.col3, settings.col3_x, from_pile)
            if pos[0] >= settings.col4_x and pos[0] <= settings.col4_x + settings.card_width:
                if self.col_checks(self.col4, from_pile):
                    self.card_placement(gui, pos, self.col4, settings.col4_x, from_pile)
            if pos[0] >= settings.col5_x and pos[0] <= settings.col5_x + settings.card_width:
                if self.col_checks(self.col5, from_pile):
                    self.card_placement(gui, pos, self.col5, settings.col5_x, from_pile)
            if pos[0] >= settings.col6_x and pos[0] <= settings.col6_x + settings.card_width:
                if self.col_checks(self.col6, from_pile):
                    self.card_placement(gui, pos, self.col6, settings.col6_x, from_pile)


    def col_checks(self, col:list, from_pile:list) -> bool:
        can_place = False
        
        if len(col) == 0 and from_pile[-1].number == 13:
            can_place = True
        else:
            if len(col) > 0 and col[-1].colour != from_pile[-1].colour and col[-1].number - 1 == from_pile[-1].number:
                can_place = True

        return can_place


    def foundation_checks(self, foundation:list, from_pile: list) -> bool: 
        can_place = False

        if len(foundation) == 0:
            suit = from_pile[-1].suit
        else:
            suit = foundation[0].suit

        if len(foundation) == 0: 
            if from_pile[-1].number == 1:
                can_place = True
        
        if from_pile[-1].suit == suit:
            if from_pile[-1].number > 1 and (from_pile[-1].number - len(foundation)) == 1:
                can_place = True
        
        return can_place   


    def switch_is_covered(self, card_to_cover:object, card_on_top:object) -> None: 
        card_on_top.is_covered = False
        my_log.debug(f"{card_on_top.number} of {card_on_top.suit} is now uncovered and is face {card_on_top.face}")
        card_to_cover.is_covered = True
        my_log.debug(f"{card_to_cover.number} of {card_to_cover.suit} is now covered and is face {card_to_cover.face}")



def main():
    gui =  view.SolitaireGUI()
    game = Controller()

    gui.run(game)

    

if __name__=="__main__":
    main()