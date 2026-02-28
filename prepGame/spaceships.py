
import numpy as np

class landingModuleA():
    #
    # LandingModuleA.
    #

    def __init__(self, xCenterInit, yCenterInit, polygonShape, dotsPerMeter):
        self.polygonDefinition = polygonShape # Polygon shape of the ship,
        self.xCenter = xCenterInit            # x coordinate of center of ship in Meter
        self.yCenter = yCenterInit            # y coordinate of center of ship in Meter
        self.xVelocity = 0                    # x Velocity in m/s
        self.yVelocity = 0                    # y velocity in m/s
        self.thrustForce = [0,0]              # thrust force (x,y) in Newton (N)
        self.rigidMass = 10000                # mass of ship without fuel in kg
        self.fuelMass = 0                     # fule load of ship in kg
        self.dotsPerMeter = dotsPerMeter
        return None
    
    def placePolygon(self, screenHeight):
        #
        # Proper placement of the ship's polygon-points on the screen.
        #
        polygonPlacement = []
        for k in self.polygonDefinition:
            pCart = (int((self.xCenter + k[0])*self.dotsPerMeter), int((self.yCenter + k[1])*self.dotsPerMeter)) 
            pGame = (pCart[0], screenHeight-pCart[1])
            polygonPlacement.append(pGame)
        return polygonPlacement

    
    def updateMotion(self, externalAccelerationGravitation, secondaryExternalForce, deltaTime):
        if self.yCenter > 50:
            #
            # externalAccelarationGravitation: accelecation due to gravitation including sign
            #
            totalForceX = externalAccelerationGravitation[0]*(self.rigidMass+self.fuelMass) 
            totalForceX += secondaryExternalForce[0]
            totalForceX += self.thrustForce[0]
            #
            totalForceY = externalAccelerationGravitation[1]*(self.rigidMass+self.fuelMass) 
            totalForceY += secondaryExternalForce[1]
            totalForceY += self.thrustForce[1]
            #
            self.xVelocity += totalForceX * deltaTime/(self.rigidMass+self.fuelMass)
            self.yVelocity += totalForceY * deltaTime/(self.rigidMass+self.fuelMass)
            #
            self.xCenter += deltaTime*self.xVelocity
            self.yCenter += deltaTime*self.yVelocity
            #
        return 1
    
    def updateThrustY(self, externalAccelerationGravitationY, changeThrustForceY):
        absValueAcceGravitation = abs(externalAccelerationGravitationY)
        newThrustForce = self.thrustForce[1] + changeThrustForceY
        if newThrustForce > 0 and newThrustForce < 1.5 * absValueAcceGravitation*self.rigidMass:
            self.thrustForce[1] = newThrustForce
        elif newThrustForce < 0:
            self.thrustForce[1] = 0
        else:
            pass 
        return 1
    
    def shutOffThrust(self):
        self.thrustForce = [0,0]
        return 1