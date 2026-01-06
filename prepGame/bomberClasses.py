import numpy, pygame, random
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
        #
        #
        self.attackState = "READY"
        self.nCounter = 0
        self.nCounterLimit = 50
        self.nBombs = 5

    def update(self):
         # *** Override of the pre-defined update function ***
        myUpdate = self.updateBomber()
        return myUpdate
    
    def updateBomber(self):
        #
        # Update position
        #
        if self.rect.x < 20 or self.rect.x > self.right_boundary-20:
            self.xDelta *= -1
        self.rect.x += self.xDelta
        #
        # Work on bombin sequence
        #
        if self.attackState == "READY":
            if random.random() < 0.1 and 0 == 1:
                self.attackState = "LAUNCH_WAIT"
                self.nBombs = 5
                self.nCounter = 0
            elif self.attackState == "LAUNCH_WAIT":
                #
                if self.nCounter < 50: self.nCounter += 1
                else: 
                    self.attackState = "LAUNCH_THROW"
                    self.nBombs -= 1
            elif self.attackState == "LAUNCH_THROW_DONE":
                #
                if self.nBombs > 0:
                    self.attackState = "LAUNCH_WAIT"
                    self.nCounter = 0
                else:
                    self.attackState = "SUFFER"
                    self.nCounter = 0
            elif self.attackState == "SUFFER":
                #
                if self.nCounter < self.nCounterLimit:
                    self.nCounter += 1
                else:
                    self.attackState = "READY"
            else:
                pass
        #
        #
        #
        myUpdateSimpleObject = 1
        return myUpdateSimpleObject
        
class stupidBomb(pygame.sprite.Sprite):
    #
    #
    #
    #
    def __init__(self, _screenObj, _bomberObj, _color, _width, _height):
        #
        #
        super().__init__()
        #
        self.image = pygame.Surface([_width, _height])
        self.image.fill(_color)
        self.rect = self.image.get_rect()
        #
        self.left_boundary = 0
        self.right_boundary = _screenObj.get_width()
        self.top_boundary = 0
        self.bottom_boundary = _screenObj.get_height()
        #
        self.rect.x = _bomberObj.rect.x
        self.rect.y = _bomberObj.rect.y + 10
        self.xDelta = 0
        self.yDelta = 3
        #
        self.myUpdate = False

    def update(self):
         # *** Override of the pre-defined update function ***
        myUpdate = self.updateStupidBomb()
        return myUpdate
    
    def updateStupidBomb(self):
        #
        # Update position
        #
        if self.rect.y < self.bottom_boundary:
            self.rect.y += self.yDelta
        #
        #
        myUpdateSimpleObject = 1
        return myUpdateSimpleObject
    
#
#
#
class generalRectangle(pygame.sprite.Sprite):
    #
    # Sprite that allows the generation of static rectangles.
    #
    def __init__(self, _screen, _color, _width, _height, _x, _y):
        #
        #
        super().__init__()
        #
        self.image = pygame.Surface([_width, _height])
        self.image.fill(_color)
        self.rect = self.image.get_rect()
        #
        #
        self.rect.x = _x
        self.rect.y = _y
        #
        self.myUpdate = False
        #
    def update(self):
        # *** Override of the pre-defined update function ***
        myUpdate = self.updateRectangle()
        return myUpdate
    
    def updateRectangle(self):
        # Function defined just to have control.
        myUpdateSimpleObject = 1
        return myUpdateSimpleObject
