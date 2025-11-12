
import numpy as np

class itemA():
    #
    # itemA is a class, that allows the creation of objects that
    # can be polaced on the screen, move and rotate with a distinct
    # translational and rotational velociy. Both quantities can be changed 
    # on the value of offsets.
    #
    # The behviour is not physical, as no euqtion or motion (Newtons law, ...)
    # is used.
    #

    def __init__(self, usedScreen, polygonShape):
        self.xDim = 10
        self.yDim = 20
        self.polygonDefinition = polygonShape
        self.polygonPlacement  = polygonShape
        self.xCenter = usedScreen.get_width()/2
        self.yCenter = usedScreen.get_height()/2
        self.angle = 0
        self.rotVelociy = 0
        self.transVelocity = 0
        return None
    
    def placePolygon(self, screenHeight):
        self.polygonPlacement = []
        for k in self.polygonDefinition:
            pCart = (k[0]*np.cos(self.angle)- k[1]*np.sin(self.angle) + self.xCenter, 
                    (k[0]*np.sin(self.angle) + k[1]*np.cos(self.angle)) + self.yCenter )
            pGame = (pCart[0], screenHeight-pCart[1])
            self.polygonPlacement.append(pGame)
        return 1

    
    def updateVelocify(self, deltaVelocity):
        self.velocity += deltaVelocity
        if self.velocity < 0:
            self.velocity = 0
        elif self.velocity > 400:
            self.velocity = 400
        else:
            pass
        return 1
    
    def updateAngle(self, deltaRotVelocity):
        self.angle += deltaRotVelocity
        if self.angle < 0:
            self.angle += 2*np.pi
        elif self.angle > np.pi * 2:
            self.angle = 0
        else:
            pass
        return 1
    
    def updateLocation(self, deltaTime):
        self.xCenter += np.cos(self.angle)*self.velocity*deltaTime
        self.yCenter += np.sin(self.angle)*self.velocity*deltaTime
        return 1