#
from schuelerschaftClass import schuelerschaft

def main():
    ehg = schuelerschaft()
    #
    ehg.neuerSchueler("x", "5", "010120000")
    ehg.neuerSchueler("Y", "5", "010120000")
    ehg.neuerSchueler("Z", "5", "010120000")
    #
    print(ehg.anzahlSchueler())
    return 1

main()