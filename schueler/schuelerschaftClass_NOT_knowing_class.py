#
from schuelerClass import schueler
#
#
class schuelerschaft():

    def __init__(self):
        self.alleSchueler = []
        return None

    def neuerSchueler(self, _neuerSchueler: schueler):
        self.alleSchueler.append(_neuerSchueler)
        return 1
    
    def anzahlSchueler(self):
        return len(self.alleSchueler)
    
    # Anzahl der Schueler mit einem bestimmten Name.

    # Position eines Schuelers in der Liste aller Schueler

    # Entlassen eines Schuelers

    # Ändern des Klassenlehrers für einen bestimmten Schüler (Name, Geburtstag)

    # Ändern des Notendurchschnitts für einen bestimmten Schüler.

    # Ändern des Klassenlehrers für alle Schüler einer bestimmten Klasse.

    # Schuljahresende - elle Schüler einer bestimmten Klasse weden versetzt und haben zunächst keinen Klassenlehrer.