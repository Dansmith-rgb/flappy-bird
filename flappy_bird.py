import pygame
import sys, os, math, random

from bird import Bird
from pipes import Pipe, PipeBottom

clock = pygame.time.Clock()
FPS = 500
#screen = pygame.display.set_mode((1280, 838))
objects = []

class FlappyBird:
    def __init__(self):
        "Initialize the game and its resources"
        pygame.init()
    
        self.screen = pygame.display.set_mode((1280, 838))
        pygame.display.set_caption("flappy bird")
    
        self.bg = pygame.image.load('images/tree-736875_1280.jpg').convert_alpha()
        self.bgx = 0
        self.bgx2 = self.bg.get_width()

        self.bird = Bird(self)
        self.pipe = Pipe(self)
        self.pipeb = PipeBottom(self)

    #def objects(self):
        self.objects = []

    def redrawWindow(self):
        #objects = []
        self.screen.blit(self.bg, (self.bgx, 0))
        self.screen.blit(self.bg, (self.bgx2, 0))
        self.bird.blitme()
        
        for x in self.objects:
            #x.blitme(self)
            x.blitme(self.screen)
        

    def run_game(self):
        """Start the main loop for the game."""
        speed = 30
        #objects = []
        pygame.time.set_timer(pygame.USEREVENT+2, random.randrange(2000, 3500))
        while True:
            fb.redrawWindow()
            #redrawWindow()
            #self.bird.update()
                
            # Moving the backgrounds
            clock.tick(speed)
            self.bgx -= 1.4
            self.bgx2 -= 1.4

            if self.bgx < self.bg.get_width() * -1:
                self.bgx = self.bg.get_width()

            if self.bgx2 < self.bg.get_width() * -1:
                self.bgx2 = self.bg.get_width()

            for objectt in objects:
                objectt.rect.x -= 1
                objectt.rect.x -= 1
                objectt.rect.x -= 1
                objectt.blitme()
                objectt.blitme()
                objectt.blitme()
                if objectt.rect.x < -14:
                    #objectt.rect.right()
                    objects.pop(objects.index(objectt))

            
                
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.USEREVENT+2:
                    r = random.randrange(0,2)
                    if r == 0:
                        
                        objects.append(self.pipe)
                        print("Hi")
                        #self.pipe.rect.x -= 1.4
                        
                        
                    elif r == 1:
                        objects.append(self.pipeb)
                        print("Yo")
                        #self.pipeb.rect.x -= 1.4
            

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.bird.moving_up = True
                        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.bird.moving_up = False
            
            self.bird.update()
            #self.bird.blitme()
            
            #self.pipe.blitme()
            #self.pipe.rect.x -= 1
            #self.pipeb.blitme()
            #self.pipeb.rect.x -= 1
           
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    fb = FlappyBird()
    fb.run_game() 

