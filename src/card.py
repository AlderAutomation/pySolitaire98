class Card:
    
    def __init__(self, number, suit:str, frontside:str, backside:str, face:str="down") -> None:
        self.number = number
        self.suit = suit
        self.face = face
        self.rotation = "portrait"
        self.frontside = frontside
        self.backside = backside
        self.x = 20
        self.y = 20

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


    def set_x(self, x:int) -> None:
        print (f'Set X to {x}')
        self.x = x


    def set_x(self, y:int) -> None:
        print (f'Set Y to {y}')
        self.y = y
