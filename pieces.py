"""
Author: Jack Lin
Date: May. 11, 2014
Description: Module for the Tetris game. Contains all the rotations of
             different pieces and the pieces themselves. Movenments of the blocks
             are also included.
"""
#Import all the necessary modules
import sprites, random, pygame
#load all the block pictures
blue = pygame.image.load("images/blue.jpg")
dark_blue = pygame.image.load("images/dark_blue.jpg")
orange = pygame.image.load("images/orange.jpg")
yellow = pygame.image.load("images/yellow.jpg")
green = pygame.image.load("images/green.jpg")
purple = pygame.image.load("images/purple.jpg")
red = pygame.image.load("images/red.jpg")

def T_block():
    """This function initilizes the T shaped block on the the screen, it returns
    all the individual blocks."""
    block1 = sprites.Block((207.5, 37.5), blue)
    block2 = sprites.Block((172.5, 72.5), blue)
    block3 = sprites.Block((242.5, 72.5), blue)
    block4 = sprites.Block((207.5, 72.5), blue)
    return block1, block2, block3, block4

def T_rotate(b1, b2, b3, b4, rotation):
    """This function take four blocks that make up one piece and the rotational
    number as paramters. This function rotates the T piece that is on the screen"""
    #If statements to check which rotation it is
    if rotation == 1:
        b2.change_XY(35, 35)
    elif rotation == 2:
        #If rotation 2 then it check to see if there are any special cases where
        #the piece might be right beside the left border
        if b1.rect.left == 50 and b2.rect.left == 50 and b4.rect.left == 50:
            b1.change_XY(0,35), b2.change_XY(35,0), b3.change_XY(35,0), b4.change_XY(35,0)
        else:
            b1.change_XY(-35, 35)
    elif rotation == 3:
        b3.change_XY(-35, -35)
    else:
        #Like ratotion 2, but this time it checks for the special cases beside
        #the right border
        if b2.rect.right == 400 and b3.rect.right == 400 and b4.rect.right == 400:
            b1.change_XY(0,-35), b2.change_XY(-70,-35), b3.change_XY(0,35),b4.change_XY(-35,0)
        else:
            b1.change_XY(35, -35), b2.change_XY(-35, -35), b3.change_XY(35, 35)

def L_block():
    """This function initilizes the L shaped block on the the screen, it returns
    all the individual blocks."""
    block1 = sprites.Block((172.5, 37.5), dark_blue)
    block2 = sprites.Block((172.5, 72.5), dark_blue)
    block3 = sprites.Block((207.5, 72.5), dark_blue)
    block4 = sprites.Block((242.5, 72.5), dark_blue)
    return block1, block2, block3, block4

def L_rotate(b1, b2, b3, b4, rotation):
    """This function take four blocks that make up one piece and the rotational
    number as paramters. This function rotates the L piece that is on the screen"""
    #If statements to check which rotation it is
    if rotation == 1:
        b1.change_XY(70,0), b2.change_XY(35,-35), b4.change_XY(-35,35)
    elif rotation == 2:
        #Check for special case on the left border
        if b2.rect.left == 50 and b3.rect.left == 50 and b4.rect.left == 50:
            b1.change_XY(35,70), b2.change_XY(70,35),b3.change_XY(35,0), b4.change_XY(0,-35)
        else:
            b1.change_XY(0,70), b2.change_XY(35,35), b4.change_XY(-35,-35)
    elif rotation == 3:
        b1.change_XY(-70,0), b2.change_XY(-35,35), b4.change_XY(35,-35)
    else:
        #Check for special case on the right border
        if b2.rect.right == 400 and b3.rect.right == 400 and b4.rect.right == 400:
            b1.change_XY(-35,-35), b2.change_XY(-70,0),b3.change_XY(-35,35), b4.change_XY(0,70)
        else:
            b1.change_XY(0,-70), b2.change_XY(-35,-35), b4.change_XY(35,35)

def J_block():
    """This function initilizes the J shaped block on the the screen, it returns
    all the individual blocks."""
    block1 = sprites.Block((242.5, 37.5), orange)
    block4 = sprites.Block((172.5, 72.5), orange)
    block3 = sprites.Block((207.5, 72.5), orange)
    block2 = sprites.Block((242.5, 72.5), orange)
    return block1, block2, block3, block4

def J_rotate(b1, b2, b3, b4, rotation):
    """This function take four blocks that make up one piece and the rotational
    number as paramters. This function rotates the J piece that is on the screen"""
    #If statements to check which rotation it is
    if rotation == 1:
        b1.change_XY(0,70), b2.change_XY(-35,35), b4.change_XY(35, -35)
    elif rotation == 2:
        if b2.rect.left == 50 and b3.rect.left == 50 and b4.rect.left == 50:
            #Checks for special case on left border
            b1.change_XY(-35,0), b2.change_XY(0,-35),b3.change_XY(35,0), b4.change_XY(70,35)
        else:
            b1.change_XY(-70,0), b2.change_XY(-35,-35), b4.change_XY(35,35)
    elif rotation == 3:
        b1.change_XY(0,-70), b2.change_XY(35,-35), b4.change_XY(-35,35)
    else:
        #Check for special case on the right border
        if b2.rect.right == 400 and b3.rect.right == 400 and b4.rect.right == 400:
            b1.change_XY(35,0), b2.change_XY(0,35),b3.change_XY(-35,0), b4.change_XY(-70,-35)
        else:
            b1.change_XY(70,0), b2.change_XY(35,35), b4.change_XY(-35,-35)

def S_block():
    """This function initilizes the S shaped block on the the screen, it returns
    all the individual blocks."""
    block1 = sprites.Block((242.5, 37.5), yellow)
    block2 = sprites.Block((207.5, 37.5), yellow)
    block3 = sprites.Block((207.5, 72.5), yellow)
    block4 = sprites.Block((172.5, 72.5), yellow)
    return block1, block2, block3, block4

def S_rotate(b1, b2, b3, b4, rotation):
    """This function take four blocks that make up one piece and the rotational
    number as paramters. This function rotates the S piece that is on the screen"""
    #If statements to check which rotation it is
    if rotation == 1 or rotation == 3:
        b1.change_XY(0,70), b2.change_XY(35,35), b4.change_XY(35, -35)
    else:
        #Check for special case on the left border
        if b4.rect.left == 50 and b3.rect.left == 50:
            b1.change_XY(35,-70), b2.change_XY(0,-35),b3.change_XY(35,0), b4.change_XY(0,35)
        else:
            b1.change_XY(0,-70), b2.change_XY(-35,-35), b4.change_XY(-35, 35)
            
def Z_block():
    """This function initilizes the Z shaped block on the the screen, it returns
    all the individual blocks."""
    block1 = sprites.Block((172.5, 37.5), green)
    block2 = sprites.Block((207.5, 37.5), green)
    block3 = sprites.Block((207.5, 72.5), green)
    block4 = sprites.Block((242.5, 72.5), green)
    return block1, block2, block3, block4

def Z_rotate(b1, b2, b3, b4, rotation):
    """This function take four blocks that make up one piece and the rotational
    number as paramters. This function rotates the Z piece that is on the screen"""
    #If statements to check which rotation it is
    if rotation == 1 or rotation == 3:
        b1.change_XY(70,0), b2.change_XY(35,35), b4.change_XY(-35, 35)
    else:
        #Checks for special case on left border
        if b4.rect.left == 50 and b3.rect.left == 50:
            b1.change_XY(-35,0), b2.change_XY(0,-35),b3.change_XY(35,0), b4.change_XY(70,-35)
        else:
            b1.change_XY(-70,0), b2.change_XY(-35,-35), b4.change_XY(35,-35)
            
def I_block():
    """This function initilizes the I shaped block on the the screen, it returns
    all the individual blocks."""
    block1 = sprites.Block((207.5, 37.5), purple)
    block2 = sprites.Block((207.5, 72.5), purple)
    block3 = sprites.Block((207.5, 107.5), purple)
    block4 = sprites.Block((207.5, 142.5), purple)
    return block1, block2, block3, block4

def I_rotate(b1, b2, b3, b4, rotation):
    """This function take four blocks that make up one piece and the rotational
    number as paramters. This function rotates the I piece that is on the screen"""
    #If statements to check which rotation it is
    if rotation == 1 or rotation == 3:
        #Checks for special case on left border and right border
        if b1.rect.left == 50 and b2.rect.left == 50:
            b1.change_XY(0,70), b2.change_XY(35,35),b3.change_XY(70,0), b4.change_XY(105,-35)
        elif b1.rect.left == 85 and b2.rect.left == 85:
            b1.change_XY(-35,70), b2.change_XY(0,35),b3.change_XY(35,0), b4.change_XY(70,-35)
        elif b1.rect.right == 400 and b2.rect.right == 400:
            b1.change_XY(-105,70), b2.change_XY(-70,35),b3.change_XY(-35,0), b4.change_XY(0,-35)
        else:
            b1.change_XY(-70,70), b2.change_XY(-35,35), b4.change_XY(35,-35)
    else:
        b1.change_XY(70,-70), b2.change_XY(35,-35), b4.change_XY(-35,35)

def O_block():
    """This function initilizes the O shaped block on the the screen, it returns
    all the individual blocks."""
    block1 = sprites.Block((207.5, 37.5), red)
    block2 = sprites.Block((207.5, 72.5), red)
    block3 = sprites.Block((242.5, 37.5), red)
    block4 = sprites.Block((242.5, 72.5), red)
    return block1, block2, block3, block4

def new_piece():
    """Create a new piece to be on the screen, returns the piece created and the
    piece number x."""
    x = random.randint(1,7)
    if x == 1:
        piece = T_block()
    elif x == 2:
        piece = L_block()
    elif x == 3:
        piece = J_block()
    elif x == 4:
        piece = S_block()
    elif x == 5:
        piece = Z_block()
    elif x == 6:
        piece = I_block()
    else:
        piece = O_block()
    return piece, x

def drop(b1, b2, b3, b4):
    """This function drops the piece down by 35 pixels, and it takes in the 4
    blocks that form a piece as parameters."""
    b1.go_down(), b2.go_down(), b3.go_down(), b4.go_down()

def move_left(b1, b2, b3, b4):
    """This function moves the piece to the left by 35 pixels, and it takes the 4
    blocks that form a piece as parameters."""
    #Only moves if it's beyond the left border
    if b1.rect.left > 50 and b2.rect.left > 50 and b3.rect.left > 50 and \
       b4.rect.left > 50:
        b1.go_left(), b2.go_left(), b3.go_left(), b4.go_left()
        
def move_right(b1, b2, b3, b4):
    """This function moves the piece to the right by 35 pixels, and it takes the 4
    blocks that form a piece as parameters."""
    #Only moves if it's below the right border
    if b1.rect.right < 400 and b2.rect.right < 400 and b3.rect.right < 400 and \
       b4.rect.right < 400:
        b1.go_right(), b2.go_right(), b3.go_right(), b4.go_right()