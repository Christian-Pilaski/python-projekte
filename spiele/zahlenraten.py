import random

running = True

def usereingabe_check(string):
    """
    Liest eine Ganzzahl vom Nutzer ein und wiederholt die Eingabe bei ungültigem Wert.

    Args:
    string (str): Anzeigetext für die Eingabeaufforderung
    Returns:
    int: Die eingegebene Ganzzahl
    """
    while True:
        try: return int(input(string))
        except ValueError: print("Keine Gültige eingabe") 

def check_zahl(zahl, rnd_zahl, Versuche):
    """
    Vergleicht die Nutzereingabe mit der Zufallszahl und gibt einen Spielzustand zurück.

    Args:
        zahl (int): Die eingegebene Zahl des Nutzers
        rnd_zahl (int): Die zu erratende Zufallszahl
        Versuche (int): Anzahl der bisherigen Versuche
    Returns:
        str: "beenden", oder "neustart" bei falschem Tipp
    """
    if zahl == rnd_zahl:
        print("Herzlichen Glückwunsch!\nDu hast die Zahl erraten!\n")
        print("Versuche: ",Versuche)
        neustarten = input("noch einmal ? y/n ") 
        if neustarten.lower() == "n":
            return "beenden"
        return "neustart"
    elif zahl > rnd_zahl:
        print("Zu hoch geschätzt, Versuch es gleich noch einmal.")
    elif zahl < rnd_zahl:
        print("Zu niedrig geschätzt, Versuch es gleich noch einmal.")


if __name__ == "__main__":
    while running:
        Versuche = 0
        rnd_zahl = random.randint(1,100)
        start_rating = True
        while start_rating:
            x = usereingabe_check("Bitte geb eine Ganzzahl ein: ")
            Versuche +=1
            y = check_zahl(x, rnd_zahl, Versuche)
            if y == "beenden":
                start_rating = False
                running = False
            if y == "neustart":
                start_rating = False
        