#
from schuelerClass import schueler
#
#
class schuelerschaft():

    def __init__(self):
        self.alleSchueler = []
        return None

    # Hinzufügernneines Schülers.
    def neuerSchueler(self, _name: str, _Klasse:str, _Geburtstag:str):
        #
        # Neue Objekte werden innerhalb der Klassen Schuelerschaft erzeugt.
        #
        neuerSChueler = schueler(_name, _Klasse, "-", _Geburtstag, -1)
        self.alleSchueler.append(neuerSChueler)
        return 1
    
    # Anzahl aller Schueler
    def anzahlSchueler(self):
        return len(self.alleSchueler)
    
    #Anzahl der Schueler mit einem bestimmten Name.
    def zahlSchueler(self, _name: str):
        anzahl = 0
        for i in self.alleSchueler:
            if i.schuelerName == _name:
                anzahl += 1
        return anzahl
    
    #Position eines Schuelers in der Liste aller Schueler
    def indexSchueler(self, _name: str, _Bday: str):
        anzahl = self.zahlSchueler(_name)
        indexLocation = -1
        if anzahl > 0:
            for i in self.alleSchueler:
                if i.schuelerName == _name and i.schuelerBday == _Bday:
                    indexLocation = self.alleSchueler.index(i)
                    pass
                else:
                    pass
        else:
            pass
        return indexLocation
    
    # Entlassen eines Schuelers
    def entlasseSchueler(self, _name:str, _bday: str):
        indexLocation = self.indexSchueler(_name, _bday)
        if indexLocation > -1:
            self.alleSchueler.remove(self.alleSchueler[indexLocation])
        else:
            pass
        return indexLocation
    
    # Ändern des Klassenlehrers für einen bestimmten Schüler (Name, Geburtstag)

    # Ändern des Notendurchschnitts für einen bestimmten Schüler.

    # Ändern des Klassenlehrers für alle Schüler einer bestimmten Klasse.

    # Schuljahresende - elle Schüler einer bestimmten Klasse weden versetzt und haben zunächst keinen Klassenlehrer.

    # Bestimmen des Notendurchschnitt für eine bestimmte Schulklasse.