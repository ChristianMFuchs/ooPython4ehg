#
def octaveSet():
    return {"subcontra", "contra"}

def lengthSet():
    return {"1", "1/2", "1/4", "1/8", "3/4", "3/8", "3/16"}

def nameSet():
    return {"c", "d", "e", "f", "g", "a", "h"}

def barTypeSet():
    return {"Default", "Intro", "End"}

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
    
class piece():

    def __init__(self):
        self.listOfVoices = []
        self.rhythm = 1
        self.timing = 0

    def appendVoice(self, newVoice):
        self.listOfVoices.append(newVoice)
        return 1
    
    def setRhythm(self, newRhythm):
        self.rhythm = newRhythm
        return 1
    
    def setTiming(self, newTiming):
        self.timing = newTiming
        return 1
    
    def getRhythm(self):
        return self.rhythm
    
    def getTiming(self):
        return self.timing
    
    def getListOfVoices(self):
        return self.listOfVoices
    

class voice():
    def __init__(self):
        self.listOfBars = []
        self.name = ""

    def appendBar(self, newBar):
        self.listOfBars.append(newBar)
        return 1
        
    def setName(self, newName):
        self.name = newName
        return 1
    
    def getName(self):
        return self.name
    
    def getListOfBars(self):
        return self.listOfBars


class bar():
    def __init__(self, initType = "Default"):
        if initType in barTypeSet():
            self.type = initType
        else:
            print("Bad init type. Terminate here")
            exit()
        self.listOfTunes = []

    def appendTune(self, newTune):
        self.listOfTunes.append(newTune)
        return 1
    
    def getListOfTunes(self):
        return self.listOfTunes
    
    def getType(self):
        return self.type
        
class player():
    def __init__(self):
        pass

    def play(self, musicPiece):
        return 1
        
    def dump(self, musicPiece: piece):
        aListOfVoices = musicPiece.getListOfVoices()
        print("* Number of voices: ", len(aListOfVoices))
        for someVoice in aListOfVoices:
            print("> Voice ", someVoice.getName())
            aListOfBars = someVoice.getListOfBars()
            print("** Number of bars: ", len(aListOfBars))
            for someBar in aListOfBars:
                print("Bar type ",  someBar.getType())
                aListOfTunes = someBar.getListOfTunes()
                print("*** Number of tunes ", len(aListOfTunes))
                for aTune in aListOfTunes:
                    print(">>> ", aTune.getName(), aTune.getRelativeLength(), aTune.getOctave())
            #for iBar in musicPiece[iVoice].:
            #    print(">> Bar number ", barCounter)
            #    for tune in bar:
            #        print(">>> ", tune.getName(), tune.getRelativeLength(), tune.getOctave())
        return 1