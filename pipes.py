import pygame

class Pipe:
    """Store all the data and stuff in this class."""
    def __init__(self, fb_game):
        """Initialize the game resurces."""
        self.screen = fb_game.screen
        self.screen_rect = fb_game.screen.get_rect()

        # Load the image and get it's rect.
        self.pipe1 =  pygame.image.load('images/pipe1.jpg').convert_alpha()
        self.rect = self.pipe1.get_rect()

        # Start each pole at the right handside of the screen
        self.rect.right = self.screen_rect.right

        #self.x = float(self.rect.x)

    #def update(self):
        #self.x += self.settings
    

    def blitme(self):
        """Draw the poles at its current location."""
        self.screen.blit(self.pipe1, self.rect)
        
class PipeBottom:
    """Store all the data and stuff for all the bottom pipes."""
    def __init__(self, fb_game):
        """Initialize the pipe resources."""
        
        self.screen = fb_game.screen
        self.screen_rect = fb_game.screen.get_rect()

        # Load the images and get it's rect.
        self.pipeb = pygame.image.load('images/pipeb.jpg').convert_alpha()
        self.rect = self.pipeb.get_rect()

        # Start each pole at the bottom right handside of the screen.
        self.rect.bottomright = self.screen_rect.bottomright


    def blitme(self):
        """Draw the poles at it's current location."""
        
        self.screen.blit(self.pipeb, self.rect)
