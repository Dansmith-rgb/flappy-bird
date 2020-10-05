import pygame
import math


clock = pygame.time.Clock()
class Bird:
    """A class to manage the ship."""

    def __init__(self, fb_game):
        """Initialize the ship and set its strating position."""
        self.screen = fb_game.screen
        self.screen_rect = fb_game.screen.get_rect()

        # Load the bird image and get its rect.
        self.image = pygame.image.load('images/new_bird.jpg').convert_alpha()
        self.rect = self.image.get_rect()

        # Start each new bird at the left handside of the screen
        self.rect.center = self.screen_rect.center

        # Movement flag.
        self.moving_up = False

    def update(self):
        """Update the birds position based on the movement flag."""
        pixels = 10
        Going_down = False
        
        if self.moving_up:
            self.rect.y -= 20
        if clock.tick_busy_loop(500):
            clock.get_time()
            self.rect.y += 10
            Going_down = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
