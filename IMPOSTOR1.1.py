from random import randint
from time import sleep

Begriffe = [
    "Stift",
    "Schule",
    "Bob der Baumeister",
    "Virus",
    "Will of D.",
    "Goyim",
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
    "Gruppe",
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

def SpielerListe():
    AnzahlSpieler = int(input("Wie viele Spieler?: \n "))
    global Spieler
    Spieler = []
    for i in range(AnzahlSpieler):
        NickName = input("Wie heißt der " + str(i+1) + ". Spieler?: \n ")
        Spieler.append(NickName)
    return Spieler


def BegriffAuswahl():
    BVar = randint(0, BLen-1)
    return BVar

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
    if Nochmal == 1:
        SetUp()
    print("ES WAR", Spieler[ImpVar])
    return "Viel Glück."

def Start():
    SpielerListe()
    SetUp()
    return "Danke"

Start()