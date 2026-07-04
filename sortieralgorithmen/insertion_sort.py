def insert_sort(liste):    
    """
    Sortiert eine Liste von Zahlen in aufsteigender Reihenfolge mithilfe des Insertion-Sort-Algorithmus.  
    Parameter:
    liste (list): Eine Liste von Zahlen, die sortiert werden soll.
    Returns:
    list: Die sortierte Liste von Zahlen in aufsteigender Reihenfolge.
    """
    for i in range(1,len(liste)):     
        wert = liste[i]                 
        j = i                         
        while j>0 and liste[j-1] > wert:
            liste[j] = liste[j-1]     
            j = j-1                   
        liste[j] = wert                 
    return liste                      

def test_insert_sort():
    assert insert_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert insert_sort([3, 0, -1, 8, 7]) == [-1, 0, 3, 7, 8]
    assert insert_sort([]) == []
    assert insert_sort([1]) == [1]
    assert insert_sort([2, 1]) == [1, 2]
    assert insert_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

if __name__ == "__main__":
    test_insert_sort()
    print("Alle Tests bestanden!")