# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 12:45:32 2020

@author: Felipe Bravo
"""
#importa funciones
from time import perf_counter
import scipy as sp 
import numpy as np
from scipy.linalg import inv
from numpy import float32

#crea una funcion que genera matrices laplaceanas
def matriz_laplaceana(N, d=float32):
    L = -(np.eye(N, k=-1, dtype=d))+2*(np.eye(N, dtype=d))-(np.eye(N, k=+1, dtype=d))
    return L

#recorrido de dimensiones de matriz
NP = [2, 5, 10,
    12, 15, 20,
    30, 40, 45, 
    50, 55, 60, 
    75, 100, 125, 
    160, 200, 250, 
    350, 500, 600, 
    800, 1000, 2000,
    5000, 10000] #indice de dimension de matrices cuadradas que vamos a evaluar

#iteraciones sobre las mismas dimensiones
NC=5
#crea los archivos que va a guardar
archivos=["A_invB_inv.txt", "A_invB_npSolve.txt", "A_invB_spSolve.txt", "A_invB_spSolve_symetric.txt" , "A_invB_spSolve_pos.txt", "A_invB_spSolve_pos_overwrite.txt"]

#abre los archivos para escribir en ellos
files= [open(archivo, 'w') for archivo in archivos]
#recorre los NP       
for N in NP:
    dts=np.zeros((NC, len(files)))
    print(f"N={N}")
    #va recorriendo los casos que planeamos
    for i in range(NC):
        print(f"i={i}")
        A = matriz_laplaceana(N) #A_inv*B
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = A_inv*B
        t2 = perf_counter()
        dt= t2- t1
        dts[i][0] = dt
        
        A = matriz_laplaceana(N) #npSolve
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = np.linalg.solve(A, B)
        t2 = perf_counter()
        dt= t2- t1
        dts[i][1] = dt
        
        A = matriz_laplaceana(N) #spSolve
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = sp.linalg.solve(A, B)
        t2 = perf_counter()
        dt= t2- t1
        dts[i][2] = dt
        
        A = matriz_laplaceana(N) #spSolve_symetric
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = sp.linalg.solve(A, B, assume_a = 'sym')
        t2 = perf_counter()
        dt= t2- t1
        dts[i][3] = dt
        
        A = matriz_laplaceana(N) #spSolve_pos
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = sp.linalg.solve(A, B, assume_a = 'pos')
        t2 = perf_counter()
        dt= t2- t1
        dts[i][4] = dt
        
        A = matriz_laplaceana(N) #spSolve_pos_overwrite
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = sp.linalg.solve(A, B, assume_a = 'pos', overwrite_a=True, overwrite_b=True)
        t2 = perf_counter()
        dt= t2- t1
        dts[i][5] = dt
        
    print("dts: ", dts)#imprime los resultados de cada iteracion 
    
    dts_prom = [np.mean(dts[i,j]) for j in range(len(files))]
    #imprime los promedios de los resultados anteriores y repite el loop con otra dimension de matriz en NP
    print("dts_promedio: ", dts_prom)
    
    for j in range(len(files)): #escribe en los archivos segun una estructura definida
        files[j].write(f"{N} {dts_prom[j]}\n")
        files[j].flush()
        
[file.close() for file in files]#cierra los archivos