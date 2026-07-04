def verdoppeln(liste):
    """
    Verdoppelt jeden Wert in der gegebenen Liste.

    :parameter liste: Eine Liste von Zahlen.
    :return: Eine neue Liste mit verdoppelten Werten.
    """
    liste2 = []
    for x in liste:
        liste2.append(x * 2)
    return liste2

def rotieren(liste,n):
    """
    Rotiert die gegebene Liste um var:n Positionen nach rechts.

    :parameter liste: Eine Liste von Zahlen.
    :return: Eine neue Liste, die um eine Position nach rechts rotiert wurde.
    """   
    liste = liste[:]
    for i in range(n):
        temp=liste.pop()
        liste.insert(0,temp)
    return liste

def liste_to_strings(liste):
    """
    Ändert jeden eintrag einer Liste zu einem String
    
    :parameter liste: Eine Liste mit inhalt
    :returns: Eine neue Liste mit den Typen Strings 
    """
    liste2=[]
    for z in liste:
        liste2.append(str(z))
    return liste2

def ueber_durchschnitt(liste):
    """
    Berechnet den durchschnit und speichert alle die 
    über dem durschnitt liegenden Zahlen in einer neuen Liste
    
    :parameter liste: Eine Liste von Zahlen
    :returns: Eine neue Liste mit Zahlen über dem durchschnitt
    """   
    liste2 =[]
    durchschnitt = sum(liste) / len(liste)
    for i in liste:
        if i > durchschnitt:
            liste2.append(i)
    return liste2

def ist_sortiert(liste):
    """
    Prüft ob eine Liste Sortiert ist 
    parameter: liste
    returns: Boolscher Wert
    """
    return liste == sorted(liste)

def unique(liste):
    """
    Entfernt doppelte Werte aus einer Liste
    Hinweis: Die Reihenfolge der Elemente wird nicht garantiert.
    parameter: Eine liste mit Werten
    returns: Eine Liste mit uniquen Werten
    """
    return list(set(liste))

