import settings

class Card:
    
    def __init__(self, number, suit:str, frontside:str, backside:str, face:str="down") -> None:
        self.number = number
        self.suit = suit
        self.face = face
        self.rotation = "portrait"
        self.frontside = frontside
        self.backside = backside
        self.top_x = 20
        self.top_y = 20
        self.is_clicked = False
        self.bottom_x = self.top_x + settings.card_width
        self.bottom_y = self.top_y + settings.card_height
        self.is_covered = True

        if suit == "hearts":
            self.colour = "red"
        elif suit == "diamonds":
            self.colour = "red"
        elif suit == "clubs":
            self.colour = "black"
        elif suit == "spades":
            self.colour = "black"


    def flip_card (self) -> None:
        if self.face == "up":
            self.face = "down"
        else:
            self.face = "up"


    def rotate_card (self) -> None:
        if self.rotation == "portrait":
            self.rotation = "landscape"
        else:
            self.rotation = "portrait"


    def set_is_clicked (self, pos:tuple) -> None:
        if pos[0] >= self.top_x and pos[0] <= self.top_x + settings.card_width:
            if pos[1] >= self.top_y and pos[1] <= self.top_y + settings.card_height:
                if self.face == "up" and self.is_covered == False:
                    print(f"{self.number}, {self.suit} has been clicked")
                    if self.is_clicked == False:
                        self.is_clicked = True
                    else:
                        self.is_clicked = False
                    print(f"is_clicked set to : {self.is_clicked}")
