#
def octaveSet():
    return {"subcontra", "contra"}

def lengthSet():
    return {"1", "1/2", "1/4", "1/8", "3/4", "3/8", "3/16"}

def nameSet():
    return {"c", "d", "e", "f", "g", "a", "h"}

class tune():
    def __init__(self, initLength = "1", initOctave = "subcontra", initName = "a"):
        if initLength in lengthSet():
            self.relativeLength = initLength
        else:
            print("Instantiation falied, bad length ...")
            exit()
        if initOctave in octaveSet():
            self.octave = initOctave
        else:
            print("Instantiation falied, bad octave name")
            exit()
        if initName in nameSet():
            self.name = initName
        else:
            print("Instantiation failed, bad name ...")
            exit()

    def setRelativeLength(self, valueLength):
        if valueLength in lengthSet():
            self.relativeLength = valueLength
            return 1
        else:
            return 0
    
    def getRelativeLength(self):
        return self.relativeLength
    
    def setOctave(self, valueOctave):
        if valueOctave in octaveSet():
            self.octave = valueOctave
            return 1
        else:
            return 0
    
    def getOctave(self):
        return self.octave
    
    def setName(self, valueName):
        if valueName in nameSet():
            self.name = valueName
            return 1
        else:
            return 0
    
    def getName(self):
        return self.name    