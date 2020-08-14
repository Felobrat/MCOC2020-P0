# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 12:45:32 2020

@author: Felipe Bravo
"""

from time import perf_counter
import scipy as sp 
import numpy as np
from scipy.linalg import inv
from numpy import float32

def matriz_laplaceana(N, d=float32):
    L = -(np.eye(N, k=-1, dtype=d))+2*(np.eye(N, dtype=d))-(np.eye(N, k=+1, dtype=d))
    return L

NP = [2, 5, 10,
    12, 15, 20,
    30, 40, 45, 
    50, 55, 60, 
    75, 100, 125, 
    160, 200, 250, 
    350, 500, 600, 
    800, 1000, 2000,
    5000, 10000] #indice de dimension de matrices cuadradas que vamos a evaluar

NC=10

archivos=["A_invB_inv.txt", "A_invB_npSolve.txt"]

files= [open(archivo, 'w') for archivo in archivos]
        
for N in NP:
    dts=np.zeros((NC, len(files)))
    print(f"N={N}")
    
    for i in range(NC):
        print(f"i={i}")
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = A_inv*B
        t2 = perf_counter()
        dt= t2- t1
        dts[i][0] = dt
        
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = np.linalg.solve(A, B)
        t2 = perf_counter()
        dt= t2- t1
        dts[i][1] = dt
        
    print("dts: ", dts)
    
    dts_prom = [np.mean(dts[i,j]) for j in range(len(files))]
    
    print("dts_promedio: ", dts_prom)
    
    for j in range(len(files)):
        files[j].write(f"{N} {dts_prom[j]}\n")
        files[j].flush()
        
[file.close() for file in files]