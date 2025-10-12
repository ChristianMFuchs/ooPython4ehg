class schueler():
 
    def __init__(self, schuelerName: str, schuelerKlasse: str, schuelerLehrer: str, schuelerBday: str, schuelerDurchschnitt: float):
        self.schuelerName = schuelerName
        self.schuelerKlasse = schuelerKlasse
        self.schuelerLehrer = schuelerLehrer
        self.schuelerBday = schuelerBday
        self.schuelerDurchschnitt = schuelerDurchschnitt
        return None
   
    # get methods: methods to access the attribute.
    def getSchuelerName(self):
        return self.schuelerName
    def getSchuelerKlasse(self):
        return self.schuelerKlasse
    def getSchuelerLehrer(self):
        return self.schuelerLehrer
    def getSchuelerBday(self):
        return self.schuelerBday
    def getSchuelerDurchschnitt(self):
        return self.schuelerDurchschnitt
   
    #set methods: methods to modify values, in case meaningfull for the use case
    # change value of the price of the shoe
    def setSchuelerKlasse(self, newSchuelerKlasse: str):
        self.schuelerKlasse = newSchuelerKlasse
        return 1
    def setSchuelerLehrer(self, newSchuelerLehrer: str):
        self.schuelerLehrer = newSchuelerLehrer
        return 1
    def setSchuelerDurchschnitt(self, newSchuelerDurchschnitt: float):
        self.schuelerDurchschnitt = newSchuelerDurchschnitt
        return 1