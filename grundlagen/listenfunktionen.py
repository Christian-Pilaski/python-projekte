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
    for i in range(n):
        temp=liste.pop()
        liste.insert(0,temp)
    return liste

def liste_to_strings(liste):
    """
    Ändert jeden eintrag einer Liste zu einem String
    """
    liste2=[]
    for z in liste:
        liste2.append(str(z))
    return liste2