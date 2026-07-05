import json
DATEINAME = "Kontakte_Verwaltung.json"
kontakte = {}

def kontakt_anlegen(kontakte, name, vorname, telefon, email):
    """
    Legt einen neuen Kontakt in dem dict kontakte an und speichert ihn
    
    Args:
        Kontakte(dict): Das Kontakte Dictionary
        name(str): Nachname des Kontakts
        vorname(str): Vorname des Kontakts
        telefon(str): Telefonnummer
        email (str): Email-Adresse
    Returns: 
        None
    """    
    if kontakte:
        neue_id = max(int(k) for k in kontakte.keys()) + 1
    else:
        neue_id = 1
    kontakte[neue_id] = {
        "Vorname": vorname,
        "Nachname": name,
        "Telefon": telefon,
        "Email":email
    }
    kontakte_speichern(kontakte, DATEINAME)

def kontakte_anzeigen(kontakte):
    """
    Zeigt alle Kontakte an
    
    Args:
        kontakte (dict)
    Returns:
        None
    """    
    for k,v in kontakte.items():
        print(f"ID:  {k}")
        print(f"    Vorname:   {v['Vorname']}")
        print(f"    Nachname:  {v['Nachname']}")
        print(f"    Telefon:   {v['Telefon']}")
        print(f"    Email:     {v['Email']}")
        print("------------------------------------------")
        
def kontakt_suchen(kontakte, suchbegriff):
    """
    Sucht einen Kontakt aus den Kontakten anhand eines eingegebenen wertes
    
    Args:
        kontakte(dict)
        suchbegriff der im hauptprogramm eingegeben wurde
    Returns:
        Bei Erfolg key(ID) und value(Werte name tel etc.) 
        Bei misserfolg None
    """    
    for k,v in kontakte.items():
        if suchbegriff.lower() in [str(val).lower() for val in v.values()]:
            return k,v
    return None

def kontakt_aendern(kontakte, suchbegriff):
    """
    Ändert einen bestehenden Kontakt anhand eines eingegebenen feldes/wertes und speichert diesen
    
    Args:
        kontakte(dict)
        suchbegriff eingabe vom nutzer
    Returns:
        None
    """    
    ergebnis = kontakt_suchen(kontakte,suchbegriff)
    if ergebnis is None:
        print("Kontakt nicht gefunden")
        return
    else:
        k,v = ergebnis
        felder ={
            "1":"Vorname",
            "2":"Nachname",
            "3":"Telefon",
            "4":"Email"
            }
        feld = input("Welchen Wert möchtest du ändern? \n1.Vorname\n2.Nachname\n3.Telefon\n4.Email\n")
        if feld in felder:
            key = felder[feld]
            neuer_wert = input(f"Neuer {key}: ")
            kontakte[k][key]= neuer_wert
            kontakte_speichern(kontakte, DATEINAME)
             
def kontakt_loeschen(kontakte, suchbegriff):
    """
    Löscht einen bestehenden Kontakt anhand des eingegebenen suchbegriffes
    
    Args:
        kontakte(dict)
        suchbegriff
    Returns:
        None
    """    
    ergebnis = kontakt_suchen(kontakte,suchbegriff)
    if ergebnis is None:
        print("Kontakt nicht gefunden")
        return
    else:
        k,v = ergebnis
        print(f"Gefunden: {v['Vorname']} {v['Nachname']} {v['Telefon']} {v['Email']}")
        loeschen = input("wirklich löschen y/n?")
        if loeschen.lower() == "y":
            del kontakte[k]
            kontakte_speichern(kontakte, DATEINAME)

def kontakte_speichern(kontakte, dateiname):
    """
    Öffnet und Speichert das aktuelle Kontakte(dict) in eine Datei
    
    Args:
        kontakte(dict)
        Dateiname Name der festgelegten datei
    Returns:
        None
    """    
    with open(dateiname,"w",encoding="UTF-8")as datei:
        json.dump(kontakte, datei, indent=4, ensure_ascii=False)
        
def kontakte_laden(dateiname):
    """
    Öffnet und liest daten aus der datei
    
    Args:
        dateiname - Name der Datei der zu öffnenden Datei
    Returns:
        Bei Erfolg ein Dictionary mit bestehenden daten
        Bei Misserfolg ein leeres dict
    """    
    try:
        with open(dateiname,"r",encoding="UTF-8")as datei:
            return json.load(datei)
    except FileNotFoundError:
        return {}
    

if __name__== "__main__":
    kontakte = kontakte_laden(DATEINAME)
    running=True
    while running:
        eingabe = input("Was möchtest du tun? \n1.Kontakt_anlegen\n2.kontakte_anzeigen\n3.kontakt_suchen\n4.Kontakt_ändern\n5.Kontakte_löschen\n6.Beenden\n")
        if eingabe == "1":
            vorn=input("vorname:  ")
            nachn=input("nachname: ")
            tel=input("telefon:  ")
            mail=input("email:    ")
            kontakt_anlegen(kontakte,nachn,vorn,tel,mail)
        elif eingabe == "2":
            kontakte_anzeigen(kontakte)
        elif eingabe == "3":
            suchbegriff= input("Suchbegriff eingeben: ")
            ergebnis = kontakt_suchen(kontakte, suchbegriff)
            if ergebnis is None:
                print("Kontakt nicht gefunden")
            else:
                k, v = ergebnis
                print(f"Gefunden: ID {k}")
                print(f"    Vorname:  {v['Vorname']}")
                print(f"    Nachname: {v['Nachname']}")
                print(f"    Telefon:  {v['Telefon']}")
                print(f"    Email:    {v['Email']}")
        elif eingabe == "4":
            suchbegriff= input("Suchbegriff eingeben: ")
            kontakt_aendern(kontakte,suchbegriff)
        elif eingabe == "5":
            suchbegriff= input("Suchbegriff eingeben: ")
            kontakt_loeschen(kontakte,suchbegriff)
        elif eingabe == "6":
            running = False
        else: print("Ungültige eingabe")