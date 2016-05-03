"""
Author: Jack Lin
Date: May. 11, 2014
Description: Tetris
"""

#IMPORT AND INITIALIZE
import pygame, sprites, pieces, random
pygame.init()
pygame.mixer.init()
    
def main():
    #Main game function
    #DISPLAY
    screen = pygame.display.set_mode((600, 720))
    pygame.display.set_caption("TETRIS SAVIOR")
    
    #ENTITIES
    #Create background
    background = pygame.Surface(screen.get_size())
    background.fill((0,128,255))
    screen.blit(background, (0,0))
    #Creating a borders  
    l_border = pygame.Surface((20, screen.get_height()-10))
    t_border = pygame.Surface((screen.get_width()-210, 20))
    l_border.fill((0, 51, 102))
    t_border.fill((0, 51, 102))
    #Load background music and all the sound effects
    pygame.mixer.music.load("sound/background_music.ogg")
    shoot = pygame.mixer.Sound("sound/shoot.wav")
    scoreSound = pygame.mixer.Sound("sound/score.wav")
    GG = pygame.mixer.Sound("sound/game_over.wav")
    levelUp = pygame.mixer.Sound("sound/level_up.flac")
    #Setting volumes of each sound effect and the background music
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    shoot.set_volume(0.6)
    scoreSound.set_volume(0.7)
    GG.set_volume(0.7)
    levelUp.set_volume(0.6)
    #Import text fonts
    startFont = "fonts/Bullpen.ttf"
    startFont3D = "fonts/Bullpen3D.ttf"
    font = "fonts/CFO.ttf"
    #Load images
    titlePicture = pygame.image.load("images/title_background.jpg")
    endPicture = pygame.image.load("images/end_background.jpg")
    #Create title screen sprites and sprite groups
    titleScreen = sprites.Screen(titlePicture)
    title = sprites.Display("TETRIS SAVIOR", (300, 100), font, 85)
    start_text = sprites.Display("START", (300, 650), startFont, 40)
    circle = sprites.Circle()
    #Put different sprites into separate groups
    circleGroup = pygame.sprite.Group(circle)
    titleSprites = pygame.sprite.Group(titleScreen,title,start_text,circle)
    #Create game screen sprites and game screen sprite groups
    scoreSprite = sprites.Display("Score: 0", (510, 70), font, 30)
    levelSprite = sprites.Display("Level: 1", (510, 120), font, 30)
    endZone = sprites.EndZone()
    piece, x = pieces.new_piece()
    #Put different sprites into separate groups
    blockGroup = pygame.sprite.Group(piece)
    allSprites = pygame.sprite.Group(scoreSprite,levelSprite,piece,endZone)
    #Create game over screen sprites and game over screen sprite groups
    GGScreen = sprites.Screen(endPicture)
    GGSprite = sprites.Display("GAME OVER", (300, 250), font, 100)
    finalScore = sprites.Display("", (300, 380), font, 40)
    restartSprite = sprites.Display("RESTART",(200,500),startFont,40)
    quitSprite = sprites.Display("QUIT",(400,500),startFont,40)
    #Put all the game over sprites into one group
    GGSprites = pygame.sprite.Group(quitSprite,GGScreen,finalScore,restartSprite,GGSprite)

    #ACTION - ASSIGN
    keepGoing = True
    clock = pygame.time.Clock()
    b1, b2, b3, b4 = piece
    random_int = random.randint(1,4)
    count = 0
    rotate = 0
    collision = 0
    score = 0
    level = 1
    fraps = 30
    GG_count = 0
    condition = False
    start_game = False
    game_over = False
    #Sets the mouse pointer to invisible
    pygame.mouse.set_visible(False)
    
    #LOOP
    while keepGoing:    
        #TIME
        clock.tick(30)
        
        #EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #If exit clicked, music fades out, game ends
                pygame.mixer.music.fadeout(1000)
                keepGoing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Checks the actions between the mouse and other sprites, if clicked
                #sound effect plays
                shoot.play()
                #If start button clicked, game starts
                if pygame.sprite.spritecollide(start_text, circleGroup, True):
                    start_game = True
                    
            if start_game:
                #checks if mouse collides with any blocks when clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #If collided, collided block disappears
                    if pygame.sprite.spritecollide(circle,blockGroup, True):
                        collision += 1
                        
            if game_over:
                #After game over, checks if player wants to restart the game or
                #quit the game and display score at the same time
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #If player clicks quit then music fades out, game ends
                    if pygame.sprite.spritecollide(quitSprite, circleGroup, True):
                        pygame.mixer.music.fadeout(1000)
                        keepGoing = False
                    elif pygame.sprite.spritecollide(restartSprite, circleGroup, True):
                        #Else if restart button clicked, reset everything
                        b1.kill(), b2.kill(), b3.kill(), b4.kill()
                        count = 0
                        score = 0
                        collision = 0
                        level = 1
                        fraps = 30
                        endZone.reset()
                        condition = False
                        start_game = True
                        GG_count = 1
        if game_over:
            #If game ended then sets the final score
            finalScore.set_text("FINAL SCORE: %s"%str(score))
            
        #Checks if player is hovering the mouse pointer over the text buttons
        #Changes font to 3D if mouse pointer collides with the diaplay message
        if pygame.sprite.spritecollide(start_text,circleGroup, False):
            start_text.set_font(startFont3D)
        else:
            start_text.set_font(startFont)
            
        #Changes font to 3D if mouse pointer collides with the diaplay message
        if pygame.sprite.spritecollide(quitSprite,circleGroup, False):
            quitSprite.set_font(startFont3D)
        else:
            quitSprite.set_font(startFont)
            
        #Changes font to 3D if mouse pointer collides with the diaplay message
        if pygame.sprite.spritecollide(restartSprite,circleGroup, False):
            restartSprite.set_font(startFont3D)
        else:
            restartSprite.set_font(startFont)
            
        if start_game:
            #starts the game
            count += 1
            levelSprite.set_text("Level: %s"%str(level))
            #Checks if all the blocks are still there, if all gone then generate
            #new block 
            if b1.alive() == False and b2.alive() == False and b3.alive() == False and b4.alive() == False:
                #Plays sound if new piece is generated
                scoreSound.play()
                #Checks if the loop is running right after restart, if true
                #then score will not be added
                if GG_count == 0:
                    score += 1
                else:
                    #If not then as long as game started, score is gained after
                    #each piece
                    if game_over:
                        score = 0
                        game_over = False
                    else:
                        score += 1
                #Sets score, generate new piece, adds new piece to block group
                #and allsprite group, resets some conditions and values
                scoreSprite.set_text("Score: %s"%(str(score)))
                piece, x = pieces.new_piece()
                b1, b2, b3, b4 = piece
                blockGroup.add(piece)
                allSprites.add(piece)
                rotate = 0
                collision = 0
                condition = True
                    
            if count == fraps:
                #for every set of frames ran, piece drops and is randomly moved
                #to the left, right, down, or rotated
                pieces.drop(b1, b2, b3, b4)
                count = 0
                #Checks which number was randomly genrated to match with a movement
                if random_int == 1:
                    pieces.move_left(b1, b2, b3, b4)
                elif random_int == 2:
                    pieces.move_right(b1, b2, b3, b4)
                elif random_int == 3:
                    pieces.drop(b1, b2, b3, b4)
                else:
                    rotate += 1
                    if x == 1:
                        #checks which piece to rotate
                        pieces.T_rotate(b1, b2, b3, b4, rotate)
                    elif x == 2:
                        pieces.L_rotate(b1, b2, b3, b4, rotate)
                    elif x == 3:
                        pieces.J_rotate(b1, b2, b3, b4, rotate)
                    elif x == 4:
                        pieces.S_rotate(b1, b2, b3, b4, rotate)
                    elif x == 5:
                        pieces.Z_rotate(b1, b2, b3, b4, rotate)
                    elif x == 6:
                        pieces.I_rotate(b1, b2, b3, b4, rotate)
                    count = 0
                #Regenerate another random number
                random_int = random.randint(1,4)

                if rotate == 4:
                    #Keeps track of the piece rotations in the game
                    rotate = 0
        
                if score%10 == 0 and score > 1 and condition:
                    #For every 10 points, lava rises up and pieces increases the
                    #drop speed
                    level += 1
                    fraps -= 3
                    condition = False
                    count = 0
                    levelUp.play()
                    if endZone.rect.bottom != 720:
                        #If lava is under the half way point of the screen, then
                        #it rises
                        endZone.move_up()

        if pygame.sprite.spritecollide(endZone, blockGroup, True):
            #If any pieces touches the lava, game over screen generated
            GG.play()
            start_game = False
            game_over = True
            circleGroup = pygame.sprite.Group(circle)

        #REFRESH
        if start_game:
            #Refreshes anything that is used for the game screen
            screen.blit(background, (0,0))
            screen.blit(l_border, (30,10))
            screen.blit(l_border, (400,10))
            screen.blit(t_border, (30,0))
            
            allSprites.add(circle)
            allSprites.clear(screen, background)
            allSprites.update()
            allSprites.draw(screen)
        elif game_over:
            #Refreshes anything used for game over screen
            GGSprites.add(circle)
            GGSprites.clear(screen, background)
            GGSprites.update()
            GGSprites.draw(screen)
        else:
            #Refreshes anything used for title screen
            titleSprites.clear(screen, background)
            titleSprites.update()
            titleSprites.draw(screen)
        #Displays the image
        pygame.display.flip()
    #Set mouset to visible
    pygame.mouse.set_visible(True)
    #Delay quit for music to fade out
    pygame.time.delay(1100)
    pygame.quit()

#Calls the main function
main()   