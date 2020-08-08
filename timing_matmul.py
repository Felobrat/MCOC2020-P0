# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 16:14:47 2020

@author: Felipe Bravo
"""

from scipy import matrix, rand #importar funiones 
from time import perf_counter 

NP = [2, 5, 10,
    12, 15, 20,
    30, 40, 45, 
    50, 55, 60, 
    75, 100, 125, 
    160, 200, 250, 
    350, 500, 600, 
    800, 1000, 2000, 
    5000, 10000] #indice de dimension de matrices cuadradas que vamos a evaluar

NC = 10 #corridas que vamos a repetir la medicion de rendimiento

for i in range(NC):
    
    dts = [] #indice que almacena el tiempo que se demora en cada iteracion de matriz de dimension N en NP
    mem = [] #indice que almacena la memoria que se usa en cada iteracion de matriz de dimension N en NP
    name = (f"Matmul{i}.txt")

    fid = open(name, "w") #genera el archivo Matmul.txt
    for N in NP: #recorremos el indice NP para matrices aleatorias A y B de dimension N en NP

        print(f"N = {N}") #imprime en consola lo que está pasando en la operacion, indicando en que elemento N en NP esta iterando.
        A = matrix(rand(N,N)) #genera la matriz A aleatoria de dimension NxN
        B = matrix(rand(N,N)) #genera la matriz B aleatoria de dimension NxN
        
        t1 = perf_counter() #empieza a contar cuando llega a esta parte de la iteracion
        C = A*B #hace la operacion de multiplicar matrices A y B de dimension NxN*NxN
        t2 = perf_counter() #deja de contar
        
        dt = t2 - t1 #mide cuando se demoro en multiplicar las matrices.

        size = 3 * (N**2) * 8 #calculo de cuanta memoria usa en alamcenar los datos de las matrices.
        dts.append(dt) #guarda en el indice dts creado el timepo de iteracion que se demoró para esa matriz e NxN
        mem.append(size) #guarda en el indice mem creado lo que uso de memoria en la iteracion para esa matriz de NxN
    
        fid.write(f"{N} {dt} {size}\n") #escribe en el archivo los datos almacenados
        
        print(f"Tiempo transcurrido = {dt} s") #imprime en la consola para llevar un registro visual de lo que esta haciendo
        print(f"memoria usada = {size} bytes")
        fid.flush() #limpia lo almacenado que imprimio en el archivo de texto
    
    fid.close() #deja de escribir
