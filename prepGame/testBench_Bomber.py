import pygame, random, bomberClasses, numpy  

def main():

    # Define some colors
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    RED   = (255,   0,   0)
    # Initialize Pygame
    pygame.init()
    
    # Set the height and width of the screen
    screen_width = 700
    screen_height = 400
    screen = pygame.display.set_mode([screen_width, screen_height])
    
    # This is a list of 'sprites.' Each block in the program is
    # added to this list. The list is managed by a class called 'Group.'
    # block_list = pygame.sprite.Group()
    
    # This is a list of every sprite. All blocks and the player block as well.
    all_sprites_list = pygame.sprite.Group()
    all_bombs_list = pygame.sprite.Group()
    
    myBomber = bomberClasses.bomber(screen, RED, 10, 10)
    myBottom = bomberClasses.generalRectangle(screen, BLACK, 690, 5, 5, 390)
    
    all_sprites_list.add(myBomber)
    all_sprites_list.add(myBottom)

    # Loop until the user clicks the close button.
    done = False
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while not done:
        #
        # Evaluate Mouse commands
        #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    
        # Clear the screen
        screen.fill(WHITE)
    
        # Update bomber
        all_sprites_list.update()

        # Draw all the spites
        all_sprites_list.draw(screen)
    
        # Limit to 60 frames per second
        clock.tick(60)
    
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
    pygame.quit()

main()