# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 17:09:38 2020

@author: Felipe Bravo
"""
import numpy as np #para poder generar arrays 

def mimatmul(A,B):
    
    A, B = np.array(A), np.array(B) #reordena las variables contenidas en las matrices, ordenandolas como una lista y elementos manejables.
    f_A, c_A = A.shape #organiza en filas y columnas usando la funcion shape para mantener el orden de la matriz A original.
    f_B, c_B = B.shape ##organiza en filas y columnas usando la funcion shape para mantener el orden de la matriz A original.
    resultado = np.zeros([f_A, c_B]) #genera una matriz de ceros con dimension de filas de A y B columnas, dada la propiedad de multiplicacion de Matrices, en el caso que no sean cuadradas.
    
    for i in range(f_A): #avanza hasta la cantidad de filas de A
        for j in range(c_B): #avanza hasta la cantidad de columans de B
            for n in range(f_B): #avanza segun las filas de B
                resultado[i,j]+= A[i,n] * B[n,j] #genera la multilpicacion segun la coordenada para generar la mutiplicacion.
            
    return resultado