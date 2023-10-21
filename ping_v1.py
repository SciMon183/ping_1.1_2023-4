# Funkcja sprawdzająca, czy któryś z kandydatów uzyskał większość absolutną
def sprawdz_wiekszosc(glosy):
    suma_glosow = sum(glosy)
    for i, liczba_glosow in enumerate(glosy, 1):
        if liczba_glosow > suma_glosow // 2:
            return f"KANDYDAT {i}"
    return "DRUGA TURA"

# Wczytanie liczby przypadków testowych
t = int(input())

# Przetwarzanie każdego przypadku testowego
for _ in range(t):
    # Wczytanie liczby kandydatów n i liczby głosów dla każdego kandydata
    data = input().split()
    n = int(data[0])
    glosy = [int(x) for x in data[1:]]

    # Wywołanie funkcji sprawdzającej i wydruk wyniku
    wynik = sprawdz_wiekszosc(glosy)
    print(wynik)
