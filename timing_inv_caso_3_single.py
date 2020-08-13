# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:20:02 2020

@author: Felipe Bravo
"""

 
from time import perf_counter 
from scipy.linalg import inv
import numpy as np

NP = [2, 5, 10,
    12, 15, 20,
    30, 40, 45, 
    50, 55, 60, 
    75, 100, 125, 
    160, 200, 250, 
    350, 500, 600, 
    800, 1000, 2000,
    5000, 10000] #indice de dimension de matrices cuadradas que vamos a evaluar

dts = [] #indice que almacena el tiempo que se demora en cada iteracion de matriz de dimension N en NP
mem = [] #indice que almacena la memoria que se usa en cada iteracion de matriz de dimension N en NP
name = (f"timing_inv_caso_3_np.single.txt")
fid = open(name, "w") #genera el archivo Matmul.txt
for N in NP: #recorremos el indice NP para matrices aleatorias A y B de dimension N en NP
    print(f"N = {N}") #imprime en consola lo que está pasando en la operacion, indicando en que elemento N en NP esta iterando.
    A = 2*(np.eye(N, dtype=np.single)) #genera la matriz A diagonal con valores 2 de dimension NxN
    for m in range(N):
        for n in range(N):
            if m==n+1:
                A[m,n]+=-1
                if m==n-1:
                    A[m,n]+=-1
    print(A.dtype)                 
    t1 = perf_counter() #empieza a contar cuando llega a esta parte de la iteracion
    Ainv = inv(A, overwrite_a=False) #hace la operacion de multiplicar matrices A y B de dimension NxN*NxN
    t2 = perf_counter() #deja de contar
    dt = t2 - t1 #mide cuando se demoro en multiplicar las matrices.
    print(Ainv.dtype)
    size=(Ainv.itemsize+A.itemsize)*(N**2) #calculo de cuanta memoria usa en alamcenar los datos de las matrices.
    print(Ainv.itemsize) #calculo de cuanta memoria usa en alamcenar los datos de las matrices.
    dts.append(dt) #guarda en el indice dts creado el timepo de iteracion que se demoró para esa matriz e NxN
    mem.append(size) #guarda en el indice mem creado lo que uso de memoria en la iteracion para esa matriz de NxN

    fid.write(f"{N} {dt} {size}\n") #escribe en el archivo los datos almacenados
        
    print(f"Tiempo transcurrido = {dt} s") #imprime en la consola para llevar un registro visual de lo que esta haciendo
    print(f"memoria usada = {size} bytes")
    fid.flush() #limpia lo almacenado que imprimio en el archivo de texto
    
fid.close() #deja de escribir