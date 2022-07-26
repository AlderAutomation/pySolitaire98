import pygame

class SpriteSheet():
    def __init__(self, image) -> None:
        self.sheet = image

    
    def get_image(self, wframe, hframe, width, height, scale=1) -> object:
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0,0), ((wframe * width), (hframe * height) , width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))

        return image