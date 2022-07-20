class Card:
    
    def __init__(self, number, suit, face="down", rotation="portrait" ) -> None:
        self.number = number
        self.suit = suit
        self.face = face
        self.rotation = rotation

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