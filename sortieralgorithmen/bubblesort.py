def bubblesort(liste: list) -> list:
    """
    Sortiert eine Liste aufsteigend mit dem Bubblesort-Algorithmus.
    
    Argumente:
        liste: Eine Liste mit vergleichbaren Elementen
    Returns:
        Die sortierte Liste
    """
    for n in range(len(liste), 1, -1):
        for i in range(0, n - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
    return liste


if __name__ == "__main__":
    messwerte = [9, 8, 7, 6, 1, 2, 3, 4, 11, 12, 19, 17]
    print(bubblesort(messwerte))