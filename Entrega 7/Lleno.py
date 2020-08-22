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
from scipy.sparse import lil_matrix, csr_matrix

#crea una funcion que genera matrices laplaceanas
def matriz_laplaceana(N, d=float32):
    L = -(np.eye(N, k=-1, dtype=d))+2*(np.eye(N, dtype=d))-(np.eye(N, k=+1, dtype=d))
    return L

def matriz_laplaciana_dispersa(N,dtype=float32):
    A=lil_matrix((N,N),dtype=dtype)
    
    for i in range (N):
        for j in range(N):
            if i==j:
                A[i,j]=2
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1
    return  csr_matrix(A)

#recorrido de dimensiones de matriz
NP = [2, 4, 8, 16,
      32, 64, 128, 256,
      512, 1024,2048, 4096,
      8192, 16384] #indice de dimension de matrices cuadradas que vamos a evaluar

NC=5

for i in range(NC):
    
    dts1 = [] #indice que almacena el tiempo que se demora en cada iteracion de matriz de dimension N en NP
    dts2 = [] #indice que almacena la memoria que se usa en cada iteracion de matriz de dimension N en NP
    
    dts3 = []
    dts4 = []
    
    dts5 = []
    dts6 = []
    
    name = (f"ens-sol{i}.txt")
    print(f"i={i}")
    fid = open(name, "w") #genera el archivo Matmul.txt
    for N in NP: #recorremos el indice NP para matrices aleatorias A y B de dimension N en NP
        #A_inv*b
        print(f"N = {N}") #imprime en consola lo que está pasando en la operacion, indicando en que elemento N en NP esta iterando.
        print("A_inv*b")
        t1 = perf_counter()
        A = matriz_laplaceana(N) #A_inv*B
        b = np.ones(N)
        t2 = perf_counter()
        x = sp.linalg.solve(A,b)
        t3 = perf_counter()
        dt1 = t2 - t1
        dt2 = t3 - t2
        dts1.append(dt1) #guarda en el indice dts creado el timepo de iteracion que se demoró para esa matriz e NxN
        dts2.append(dt2) #guarda en el indice mem creado lo que uso de memoria en la iteracion para esa matriz de NxN
        print(f"Tiempo ensamblado dt1= {dt1} s") #imprime en la consola para llevar un registro visual de lo que esta haciendo
        print(f"Tiempo solucion dt2= {dt2} s")
        #matmul
        print("MATMUL")
        t1 = perf_counter()
        A = matriz_laplaceana(N) #A_inv*B
        B = matriz_laplaceana(N)
        t2 = perf_counter()
        S = A@B
        t3 = perf_counter()
        dt3 = t2 - t1
        dt4 = t3 - t2
        dts3.append(dt3) #guarda en el indice dts creado el timepo de iteracion que se demoró para esa matriz e NxN
        dts4.append(dt4)
        print(f"Tiempo ensamblado dt3= {dt3} s") #imprime en la consola para llevar un registro visual de lo que esta haciendo
        print(f"Tiempo solucion dt4= {dt4} s")
        #INEVRSA
        print("INVERSA")
        t1 = perf_counter()
        A = matriz_laplaceana(N) #A_inv*B
        t2 = perf_counter()
        I = inv(A)
        t3 = perf_counter()
        dt5 = t2 - t1
        dt6 = t3 - t2
        dts5.append(dt5) #guarda en el indice dts creado el timepo de iteracion que se demoró para esa matriz e NxN
        dts6.append(dt6)
        print(f"Tiempo ensamblado dt5= {dt5} s") #imprime en la consola para llevar un registro visual de lo que esta haciendo
        print(f"Tiempo solucion dt6= {dt6} s")
        #               __A_inv*b__  ___A@B___   ___inv___    
        fid.write(f"{N} {dt1} {dt2} {dt3} {dt4} {dt5} {dt6} \n") #escribe en el archivo los datos almacenados
        
        
        fid.flush() #limpia lo almacenado que imprimio en el archivo de texto
    
    fid.close() #deja de escribir
    
    
