# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:33:13 2024

@author: marco
"""

MAX_ITER = 10

teta1 = 0.8
teta2 = 0.35  #SE LO ALZO, GradLagr DIMINUISCE, la DIMINUISCE, n_iter AUMENTA
teta3 = 0.7

EPS = [0.01, 0.01]

delta = 10**(-5)

eps = 10**(-5)

max_iter_penalita = 10**2

m = 9
p = 1

DIM = 2

#FILENAME_PROBLEM = "Funzione Test Prob1"
FILENAME_STAMPE = "Risultati_SimAnn_MarcoCasalbore_es4.txt"
file_stampe = open(FILENAME_STAMPE, "w")