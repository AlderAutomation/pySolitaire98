import pygame

class SpriteSheet():
    def __init__(self, image) -> None:
        self.sheet = image

    
    def get_image(self, wframe, hframe, width, height, scale=1) -> object:
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((wframe * width), (hframe * height) , width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        # image.set_colorkey(colour)

        return image


# , colour=(0,0,0)