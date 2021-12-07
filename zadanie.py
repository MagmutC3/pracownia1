"""To jest szablon do stworzenia rozwiazania"""

import time, numpy as np
import sortowania, wykresy, uklad
import gauss, gaussjordan, cholesky, banachiewicz
import iteracjaprosta, iteracjaseidela
from typing import List

class Zadanie:
    def __init__(self, n = 1300, M = 4, N = 22):
        """Konstruktor okreslajacy parametry eksperymentu"""
        self.n = n                          # maksymalny rozmiar macierzy
        self.M = M                          # liczba pomiarow
        self.N = N                          # liczba rozmiarow
        self.rozmiary = []                  # lista rozmiarow ukladow
        self.czasy: List[List] = [[], []]   # lista czasow rozwiazywania
        
    def mierz_czas(self, metoda, k):
        """Metoda mierzaca czas rozwiazywania problemu wybrana metoda
            k - rozmiar macierzy"""

        # uzupełnij metodę mierz_czas w pliku zadanie.py tak, by wykonywała 
        # ona po M iteracji algorytmu, który masz zbadać – jej działanie ma 
        # być analogiczne do metody mierz_czas klasy Sortowania (możesz od 
        # razu tak ją skonstruować, by wewnątrz pojawiła się instrukcja 
        # warunkowa, która pozwoli Ci wykorzystywać obie metody, które 
        # masz porównać w zadaniu 2) (1 punkt)

        czas = 0.0
        
        # tworzymy obiekt klasy Uklad
        macierzA = uklad.Uklad(wymiar = k)
        
        # tworzymy petle, w ktorej bedziemy mierzyc czas rozwiazywania
        # ukladu n rownan self.pomiary razy
        for i in range(self.M):
            # dokonujemy 4 pomiarow na rozmiar chyba?
            # 22 rozmiary mierzymy ja nie wiem
            pass

        
        return czas/self.M
    
    def badaj_zlozonosc(self, metoda, opis):
        # okreslamy krok zmiany rozmiaru ukladu
        krok = self.n / self.N
        self.rozmiary = []
        self.czasy[metoda-1] = []
        for i in range(self.N):
            self.rozmiary.append(int((i+1)*krok))   
            self.czasy[metoda-1].append(
                self.mierz_czas(metoda, self.rozmiary[i])
            )
            print(self.rozmiary[i], self.czasy[metoda-1][i])
        wykres = wykresy.Wykresy(self.n)
        wykres.badaj_zlozonosc(
            rozmiary = self.rozmiary,
            czasy = self.czasy[metoda-1],
            nazwa = opis
        )
    
    def porownaj_metody(self, nazwa_metody1, nazwa_metody2):
        krok = self.n / self.N
        for i in range(self.N):
            k = int((i+1)*krok)
            self.rozmiary.append(k)
            t1 = self.mierz_czas(1, k)
            t2 = self.mierz_czas(2, k)
            self.czasy[0].append(t1)
            self.czasy[1].append(t2)
            print(f"{k} \t {t1:10.8f} \t {t2:10.8f}")
        wykres = wykresy.Wykresy(self.n)
        wykres.porownaj_algorytmy(
            self.rozmiary,
            self.czasy,
            nazwa_metody1,
            nazwa_metody2
        )