"""To jest szablon do stworzenia rozwiazania"""

import time, numpy as np
import sortowania, wykresy, uklad
import gauss, gaussjordan, cholesky, banachiewicz
import iteracjaprosta, iteracjaseidela
from typing import List

class Zadanie:
    def __init__(self, n = 1111, M = 4, N = 22):
        """Konstruktor okreslajacy parametry eksperymentu"""
        self.n = n                          # maksymalny rozmiar macierzy
        self.M = M                          # liczba pomiarow
        self.N = N                          # liczba rozmiarow
        self.rozmiary = []                  # lista rozmiarow ukladow
        self.czasy: List[List] = [[], []]   # lista czasow rozwiazywania

    def mierz_czas(self, metoda, k):
        """Metoda mierzaca czas rozwiazywania problemu wybrana metoda
            k - rozmiar macierzy"""

        czas = 0.0
        macierzA = uklad.Uklad(wymiar = k)
        
        if metoda == 1:
            pomiary = 0
            while pomiary < self.M:
                macierzA.losuj_uklad()
                macierzAprosta = iteracjaprosta.IteracjaProsta(macierzA)
                stoper = time.time()
                if(macierzAprosta.przygotuj() == 1):
                    macierzAprosta.iteruj_roznica(eps = 1e-10, norma = 0, wyswietlaj = 0, X0 = None)
                    czas += time.time() - stoper
                    pomiary += 1

        if metoda == 2:
            pomiary = 0
            while pomiary < self.M:
                macierzA.losuj_uklad()
                macierzASeidela = iteracjaseidela.IteracjaSeidela(macierzA)
                stoper = time.time()
                if(macierzASeidela.przygotuj() == 1):
                    macierzASeidela.iteruj_roznica(eps = 1e-10, norma = 0, wyswietlaj = 0, X0 = None)
                    czas += time.time() - stoper
                    pomiary += 1
        
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