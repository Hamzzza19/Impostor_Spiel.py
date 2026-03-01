from random import randint
from time import sleep

#Liste der möglichen Begriffe - ein Begriff und der dazugehörige Hilfsbegriff müssen den selben Index in der jeweiligen Liste haben um zu funktionieren.
Begriffe = [
    "Stift",
    "Schule",
    "Bob der Baumeister",
    "Virus",
    "Will of D.",
    "Pizza",
    "Wüste",
    "Computer",
    "Eis",
    "Gefängnis",
    "Drache",
    "Pyramide",
    "Zirkus",
    "Zeit",
    "Schatten",
    "Meer",
    "König",
    "Rakete",
    "Bibliothek",
    "Maske",
    "Schatz",
    "Roboter",
    "Dschungel",
    "Geist",
    "Turnier",
    "Magnet",
    "Tunnel",
    "Kompass",
    "Spiegel",
    "Arena",
    "Tempel",
    "Labor",
    "Insel",
    "Geheimnis",
    "Ritter",
    "Code",
    "Expedition",
    "Festival",
    "Stern",
    "Burg",
    "Karte",
    "Sturm",
    "Uhr",
    "Brücke",
    "Feuer",
    "Hafen",
    "Statue",
    "Maschine",
    "Krone"
]

Hbegriffe = [
    "Essentials",
    "Lernen",
    "Kinderserie",
    "Infektion",
    "One Piece",
    "Italien",
    "Heiß",
    "Technik",
    "Kalt",
    "Zellen",
    "Mythos",
    "Alt",
    "Show",
    "Vergangenheit",
    "Dunkel",
    "Salz",
    "Herrschaft",
    "Start",
    "Wissen",
    "Verbergen",
    "Gold",
    "Metall",
    "Natur",
    "Unsichtbar",
    "Wettkampf",
    "Anziehung",
    "Untergrund",
    "Richtung",
    "Reflexion",
    "Kampf",
    "Religion",
    "Forschung",
    "Abgeschieden",
    "Rätsel",
    "Mittelalter",
    "Verschlüsselung",
    "Reise",
    "Feier",
    "Nachthimmel",
    "Mauer",
    "Navigation",
    "Wind",
    "Tick",
    "Verbindung",
    "Hitze",
    "Schiffe",
    "Denkmal",
    "Mechanik",
    "Macht"
]

BLen = len(Begriffe)

#hier wird der Spieler gefragt wer mitspielt zw wie viele mitspielen. Dazu wird eine Liste erstellt
def SpielerListe():
    AnzahlSpieler = int(input("Wie viele Spieler?: \n "))
    global Spieler
    Spieler = []
    for i in range(AnzahlSpieler):
        NickName = input("Wie heißt der " + str(i+1) + ". Spieler?: \n ")
        Spieler.append(NickName)
    return Spieler

#aus den verfügbaren Begriffen oben wird zufällig ein Begriff ausgewählt. Oder eher der Index dieses Begriffes.
def BegriffAuswahl():
    BVar = randint(0, BLen-1)
    return BVar

#den spielern wird gesagt ob sie Impostor sind oder nicht (mit Spoiler-Schutz) - dementsprechend wird ihnen der begriff oder hilfsbegriff ausgegeben
#darauf folgend kann man entscheiden ob man mit den selben spielern weiterspielt (Setup() wird neugestartet) oder nicht - Funktion endet und Programm muss neugestartet werden.
def SetUp():
    SpLen = len(Spieler)
    ImpVar = randint(0, SpLen-1)
    Bvar = BegriffAuswahl()
    zaehler = 0
    for j in Spieler:
        if zaehler != ImpVar:
            confirm = input(str(j) + "... \nbist du bereit? Du hast 10 sek. Zeit ")
            print(Begriffe[Bvar])
        elif zaehler == ImpVar:
            confirm = input(str(j) + "... \nbist du bereit? Du hast 10 sek. Zeit ")
            print("Impostor.")
            print("Dein Hilfswort:", Hbegriffe[Bvar],".")
        zaehler += 1
        sleep(10)
        for _ in range(300):
            print("SCROLL NICHT HOCH")
    Nochmal = int(input("Nochmal? \n 1 = Ja \n 2 = Nein \n "))
    print("Viel Glück.")
    if Nochmal == 1:
        SetUp()
    elif Nochmal = 2:
        print("Schade")
    print("ES WAR", Spieler[ImpVar])
    return 

#damit bei wiederholtem Spielen die Spielerliste nicht erneut erstellt werden muss, wird müssen beide Funktionen getrennt sein aber beim Start nacheinander auslösen
def Start():
    SpielerListe()
    SetUp()
    return print("Danke für's Spielen!")


Start()
