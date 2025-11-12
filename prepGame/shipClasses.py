
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

    def __init__(self, xCenterInit, yCenterInit, polygonShape):
        self.xDim = 10
        self.yDim = 20
        self.polygonDefinition = polygonShape
        self.xCenter = xCenterInit
        self.yCenter = yCenterInit
        self.angle = np.pi/2
        self.rotVelocity = 0
        self.transVelocity = 0
        return None
    
    def placePolygon(self, screenHeight):
        polygonPlacement = []
        for k in self.polygonDefinition:
            pCart = (k[0]*np.cos(self.angle)- k[1]*np.sin(self.angle) + self.xCenter, 
                    (k[0]*np.sin(self.angle) + k[1]*np.cos(self.angle)) + self.yCenter )
            pGame = (pCart[0], screenHeight-pCart[1])
            polygonPlacement.append(pGame)
        return polygonPlacement

    
    def updateVelocify(self, deltaVelocity):
        self.transVelocity += deltaVelocity
        if self.transVelocity < 0:
            self.transVelocity = 0
        elif self.transVelocity > 400:
            self.transVelocity = 400
        else:
            pass
        return 1
    
    def updateRotVelocity(self, deltaRotVelocity):
        self.rotVelocity += deltaRotVelocity
        if self.rotVelocity < -10:
            self.rotVelocity = -10
        elif self.rotVelocity > 10:
            self.rotVelocity = 10
        else:
            pass
        return 1
    
    def updateCoordinatesAndAngle(self, deltaTime):
        self.xCenter += np.cos(self.angle)*self.transVelocity*deltaTime
        self.yCenter += np.sin(self.angle)*self.transVelocity*deltaTime
        self.angle += self.rotVelocity*deltaTime
        return 1