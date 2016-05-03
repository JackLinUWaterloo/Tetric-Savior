"""
Author: Jack Lin
Date: May. 12, 2014
Description: This is a sprite module for the game Tetris.
"""

#Import/initialize pygame
import pygame
pygame.init()

class Display(pygame.sprite.Sprite):
    """This class defines the text displays for the game"""
    def __init__(self, message, xy_pos, font, font_size):
        """This initializer takes a text message, position, font, and font size
        of the message as parameters."""
        #Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        #Load the custom font, and initialize the starting text
        self.__font = pygame.font.Font(font, font_size)
        self.__font_size = font_size
        #Set the image rect and image attribute
        self.image = self.__font.render(message, 1, (0,0, 0))
        self.rect = self.image.get_rect()
        #Instantiate attributes
        self.__text = message
        self.__center = xy_pos
        
    def set_text(self, message):
        """This method changes the display text"""
        self.__text = message
    
    def set_font(self, font):
        """This method changes the font of the text"""
        self.__font = pygame.font.Font(font, self.__font_size)
        
    def update(self):
        """This method will be called automatically to display"""
        self.image = self.__font.render(self.__text, 1, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.__center
        
class Block(pygame.sprite.Sprite):
    """This class defines the blocks that will be generated in the game"""
    def __init__(self, xy_pos, block):
        """This initializer takes the position of the block, and the block image
        itself as parameters."""
        #Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        #Set the image and rect attributes for the block
        self.image = block     
        self.rect = self.image.get_rect()
        self.rect.center = xy_pos
        #Set the initial x and y vectors for the block
        self.__dx = 0
        self.__dy = 0
        
    def go_left(self):
        """This method causes the x direction of the block to decrease."""
        self.__dx = -35
        
    def go_right(self):
        """This method causes the x direction of the block to increase."""
        self.__dx = 35
        
    def go_down(self):
        """This method causes the y direction of the block to increase."""
        self.__dy = 35
        
    def change_XY(self, x, y):
        """This method changes the x and y position of the block directly, it
        takes in x and y position as parameters."""
        self.rect.left += x
        self.rect.bottom += y
                
    def update(self):
        """This method will be called automatically to reposition the block."""
        #Check if the block is within the borders
        if self.rect.left != 50 and self.__dx == -35:
            #If not beside left border or beyond then move left
            self.rect.left += self.__dx
            self.__dx = 0
        if self.rect.right != 400 and self.__dx == 35:
            #If not beisde right border and beyond then move right
            self.rect.left += self.__dx
            self.__dx = 0
        if self.rect.bottom <= 720:
            #If not on base border then drop
            self.rect.bottom += self.__dy
            self.__dy = 0

class Circle(pygame.sprite.Sprite):
    """This class defines the sprite for our player"""
    def __init__(self):
        """This initializer does not have a parameter, it initializes the image
        and rect attributes."""
        #Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        #Set the image and rect attributes for the player circle
        self.image = pygame.image.load("images/crosshair.png")
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center =((70, 50))
        
    def update(self):
        """This method will be called automatically to reposition the player
        circle"""
        self.rect.center = pygame.mouse.get_pos()

class EndZone(pygame.sprite.Sprite):
    """This class defines the sprite for the bottom end zone."""
    def __init__(self):
        """This initializer does not take any parameters, it initializes the
        image and image rect."""
        #Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        #Our endzone sprite will be 35 pixels high and 350 pixels wide
        self.image = pygame.image.load("images/lava.jpg")
        self.rect = self.image.get_rect()
        self.rect.left = 50
        self.rect.top = 685
        
    def move_up(self):
        """This method moves the endzone sprite up."""
        self.rect.top -= 35
        
    def reset(self):
        """This method resets the top position of the sprite."""
        self.rect.top = 685
        
class Screen(pygame.sprite.Sprite):
    """This class defines our a full size background screen."""
    def __init__(self, wallpaper):
        """This initailizer takes in an image as a parameter, it initilizes the
        the image and sets the image rect."""
        #Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        #Setting image and image rect
        self.image = wallpaper
        self.rect = self.image.get_rect()
        self.rect.center = ((300, 360))