running = True

    
def addition(a,b):
    """
    Addiert Zahlen 
    Args:
        a: Erste Zahl
        b: Zweite Zahl
    Return c (Ergebnis)
    """
    c = a+b
    return c
   
def subtraktion(a,b):
    """
    Subtrahiert Zahlen 
    Args:
        a: Erste Zahl
        b: Zweite Zahl
    Return c (Ergebnis)
    """
    c = a-b
    return c
        
def multiplikation(a,b):
    """
    Multipliziert Zahlen 
    Args:
        a: Erste Zahl
        b: Zweite Zahl
    Return c (Ergebnis)
    """
    c = a*b
    return c

def division(a,b):
    """
    Dividiert Zahlen und fängt teilen durch 0 ab
    Args:
        a: Erste Zahl
        b: Zweite Zahl
    Return: Ergebnis der Berechnung als float, oder None bei Division durch 0
    """
    try:
        c= a/b  
    except ZeroDivisionError:
        print("Ein Fehler ist Aufgetreten: Division durch 0")  
        c= None
    return c
        
def eingabe_float(eingabe):
    while True:
        try:
            return float(input(eingabe))
        except ValueError:
            print("Keine gültige Eingabe, Probiere es erneut.")

if  __name__== "__main__": 
    while running:
        eins = eingabe_float("1.Zahl: ")
        operator = input("Bitte wähle deine Rechenart(+-*/): ")
        zwei = eingabe_float("2.Zahl: ")
        if operator == "+":
            print("Addition: ", addition(eins,zwei))
        elif operator == "-":
            print("Subtraktion: ", subtraktion(eins,zwei))
        elif operator == "*":
            print("Multiplikation: ", multiplikation(eins,zwei))
        elif operator == "/":
            print("Division: ", division(eins,zwei))
        else:
            print("Ungültige eingabe!")
        x = input("Abbrechen ? Press y:  ").lower()
        if x == "y":
            running = False