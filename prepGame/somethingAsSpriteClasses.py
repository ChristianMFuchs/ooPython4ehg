import pygame

class Block(pygame.sprite.Sprite):
    #
    # This class represents the ** block **.
    # It derives from the "Sprite" class in Pygame.
    #
 
    def __init__(self, _color, _width, _height):
        # Constructor. Pass in the color of the block,
        # and its size.
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([_width, _height])
        self.image.fill(_color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()


class Ellipse(pygame.sprite.Sprite):
    #
    # This class represents the ** block **.
    # It derives from the "Sprite" class in Pygame.
    #
 
    def __init__(self, _color, _width, _height):
        # Constructor. Pass in the color of the block,
        # and its size.
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([_width, _height])
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
 
    # Draw the ellipse
        pygame.draw.ellipse(self.image, _color, [0, 0, _width, _height])
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()


class Block2(pygame.sprite.Sprite):
    #
    # This class represents the ball
    # It derives from the "Sprite" class in Pygame
    #
 
    def __init__(self, _color, _width, _height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([_width, _height])
        self.image.fill(_color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
        # Instance variables that control the edges of where we bounce
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
 
        # Instance variables for our current speed and direction
        self.change_x = 0
        self.change_y = 0
 
    def update(self):
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y
 
        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1
 
        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1

class Player2(Block2):
    """ The player class derives from Block2, but overrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse. """
    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]