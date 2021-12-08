"""Przyklad zastosowania metod iteracyjnych do rozwiazania zadanego ukladu
    oraz pomiaru czasu wykonywania sie operacji dla losowego ukladu"""

import time, numpy as np
import sortowania, wykresy, uklad, zadanie
import gauss, gaussjordan, cholesky, banachiewicz
import iteracjaprosta, iteracjaseidela

def testy(typ):
    if typ == 1:
        """Przyklad sortowania tablic o zadanej dlugosci"""
        n = 100
        test1 = sortowania.Sortowania(n)
        test1.losuj()
        print(test1)
        stoper = time.time()
        test1.sortuj_przez_wstawianie()     
        czas1 = (time.time()-stoper)        
        stoper = time.time()
        test1.sortuj_przez_wybieranie()
        czas2 = (time.time()-stoper)
        print("------"*10)
        print("Sortowanie przez wstawianie:")
        print(test1.wyswietl_liste1())      
        print("Czas sortowania:", czas1)
        print("------"*10)
        print("Sortowanie przez wybieranie:")
        print(test1.wyswietl_liste2())
        print("Czas sortowania przez wybieranie:", czas2)
    elif typ == 2:
        """Badanie zlozonosci obliczeniowej obu metod sortowania"""
        test2 = sortowania.Sortowania(
            n = 1000,
            lprob = 7,
            ldlugosci = 77,
            najkrotsza = 100
        )
        print("Sortowanie przez wstawianie:")
        test2.badaj_zlozonosc(1)
        print("Sortowanie przez wybieranie:")
        test2.badaj_zlozonosc(2)
    elif typ == 3:
        """Porownujemy obie metody"""
        test3 = sortowania.Sortowania(
            n = 1000,
            lprob = 7,
            ldlugosci = 77
        )
        test3.porownaj_metody()
    elif typ == 4:
        """Miejsce na rozwiazanie - przygotowanie"""

        # wykonaj kilka testów próbnych dla danej metody, by ustalić maksymalny 
        # rozmiar macierzy n (by obliczenia nie trwały zbyt długo – dla macierzy 
        # o największym rozmiarze czas powinien być poniżej 1 sekundy) – możesz 
        # wykorzystać w tym celu sekcję 4 pliku pracownia1.py (1 punkt)

        # tworzymy obiekt klasy Uklad
        ukladA = uklad.Uklad(wymiar = 1111)

        # losujemy odpowiedni uklad rownan
        ukladA.losuj_uklad()
        
        # tworzymy obiekt klasy odpowiadajacej metodzie
        iterProstaA = iteracjaprosta.IteracjaProsta(ukladA)
        
        czas = 0.0
        # uruchamiamy stoper
        stoper = time.time()

        # wywolujemy odpowiednie metody
        if iterProstaA.przygotuj() == 1:
            iterProstaA.iteruj_roznica(eps = 1e-10, norma = ukladA.norma_wektora(typ = 0), wyswietlaj = 1, X0 = None)
        
        # zatrzymujemy stoper
        czas += time.time() - stoper

        # wyswietlamy czas rozwiazywania ukladu
        print(f"Czas rozwiazywania ukladu metoda iteracji prostej: {czas}")

    elif typ == 5:
        """Miejsce na rozwiazanie Zadania 1"""
        # tworzymy obiekt klasy Zadanie i podajemy odpowiednie parametry
        zad1 = zadanie.Zadanie()
        # badamy zlozonosc obliczeniowa wybranej metody
        zad1.badaj_zlozonosc(
            metoda = 2,
            opis = "Metoda iteracji Seidela"
        )
    elif typ == 6:
        # porownujemy metody
        # tworzymy obiekt klasy Zadanie i podajemy odpowiednie parametry
        zad2 = zadanie.Zadanie()
        # badamy zlozonosc obliczeniowa wybranej metody
        zad2.porownaj_metody(
            nazwa_metody1 = "Metoda iteracji prostej",
            nazwa_metody2 = "Metoda iteracji Seidela"
        )
    elif typ == 7:
        """Miejsce na rozwiazanie - przygotowanie"""

        # wykonaj kilka testów próbnych dla danej metody, by ustalić maksymalny 
        # rozmiar macierzy n (by obliczenia nie trwały zbyt długo – dla macierzy 
        # o największym rozmiarze czas powinien być poniżej 1 sekundy) – możesz 
        # wykorzystać w tym celu sekcję 4 pliku pracownia1.py (1 punkt)

        # tworzymy obiekt klasy Uklad
        ukladA = uklad.Uklad(wymiar = 1111)

        # losujemy odpowiedni uklad rownan
        ukladA.losuj_uklad()
        
        # tworzymy obiekt klasy odpowiadajacej metodzie
        iterSeidelaA = iteracjaseidela.IteracjaSeidela(ukladA)
        
        # uruchamiamy stoper
        stoper = time.time()

        # wywolujemy odpowiednie metody
        if iterSeidelaA.przygotuj() == 1:
            iterSeidelaA.iteruj_roznica(eps = 1e-10, norma = ukladA.norma_wektora(typ = 0), wyswietlaj = 1, X0 = None)
        
        # zatrzymujemy stoper
        czas = time.time() - stoper

        # wyswietlamy czas rozwiazywania ukladu
        print(f"Czas rozwiazywania ukladu metoda iteracji seidela: {czas}")
        
if __name__ == '__main__':
    testy(6)