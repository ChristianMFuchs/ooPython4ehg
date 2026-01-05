import numpy, pygame
#
#
class bomber(pygame.sprite.Sprite):
    #
    #
    #
    #
    def __init__(self, _screen, _color, _width, _height):
        #
        #
        super().__init__()
        #
        self.image = pygame.Surface([_width, _height])
        self.image.fill(_color)
        self.rect = self.image.get_rect()
        #
        self.left_boundary = 0
        self.right_boundary = _screen.get_width()
        self.top_boundary = 0
        self.bottom_boundary = _screen.get_height()
        #
        self.rect.x = 50
        self.rect.y = 50
        self.xDelta = 5
        self.yDelta = 0
        #
        self.myUpdate = False

    def update(self):
        myUpdate = self.updateBomber()
        return myUpdate
    
    def updateBomber(self):
        #
        # Update position
        #
        print(self.rect.x, self.xDelta)
        if self.rect.x < 20 or self.rect.x > self.right_boundary-20:
            self.xDelta *= -1
        self.rect.x += self.xDelta
        #
        #
        myUpdateSimpleObject = 1
        return myUpdateSimpleObject
        
