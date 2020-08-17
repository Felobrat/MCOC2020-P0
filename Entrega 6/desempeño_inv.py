# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 18:43:30 2020

@author: Felipe Bravo
"""

#FUNCIONES A USAR

import matplotlib.pyplot as plt
import numpy as np

#ROTULO DE LOS EJES
x     = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
y1    = [0.000001, 0.1e-3, 1e-3, 10e-3, 0.1, 1, 10, 60, 600]
y2    = [10**i for i in range(3, 11)]
y1val = [".","0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min", "10 min"]
y2val = ["1 KB","10 KB","100 KB","1 MB","10 MB", "100 MB","1 GB", "10 GB"]



#EMPEZAR A GRAFICAR
fig = plt.figure(figsize=(10,10))  

#CREAR PRIMER GRAFICO Y ORDENARLO EN EL PRIMER ESPACIO VERTICALMENTE
graf1 = fig.add_subplot(1,1,1)
#RECORRER LOS .txt CREADOS Y ALMACENAR LA INFORMACION PARA USARLA
datos = np.loadtxt('A_invB_inv.txt')
graf1.plot(datos[:,0], datos[:,1],"o-", label='A_invB_inv')
datos = np.loadtxt('A_invB_npSolve.txt')
graf1.plot(datos[:,0], datos[:,1],"o-", label='A_invB_npSolve')
datos = np.loadtxt('A_invB_spSolve.txt')
graf1.plot(datos[:,0], datos[:,1],"o-", label='A_invB_spSolve')
datos = np.loadtxt('A_invB_spSolve_symetric.txt')
graf1.plot(datos[:,0], datos[:,1],"o-", label='A_invB_spSolve_symetric')
datos = np.loadtxt('A_invB_spSolve_pos.txt')
graf1.plot(datos[:,0], datos[:,1],"o-", label='A_invB_spSolve_pos')
datos = np.loadtxt('A_invB_spSolve_pos_overwrite.txt')
graf1.plot(datos[:,0], datos[:,1],"o-", label='A_invB_spSolve_pos_overwrite')

#AJUSTAR A ESCALA LOG-LOG EL GRAFICO 1
graf1.set_xscale('log')
graf1.set_yscale("log")

#DARLE EL ESPACIADO ASIGNADO
graf1.set_xticks(x)
#HACER QUE NO TENGA VALORES
graf1.set_xticklabels(x)
for tick in graf1.get_xticklabels():
    tick.set_rotation(45)

#DARLE ESPACIADO Y VALORES AL EJE 'Y' SEGUN EL PRINCIPIO
graf1.set_yticks(y1)
#AJUSTAR LOS VALORES DEL EJE PARA MOSTRAR EN KB, MB, GB
graf1.set_yticklabels(y1val)
#ACTIVAR LA GRILLA DEL GRAFICO
graf1.grid()
#HACER QUE TENGA LOS ESPACIOS ENTREMEDIO, SEÑALANDO AL ESCALA LOG
graf1.minorticks_on()
graf1.legend()

#DARLE TITULO A LOS EJES
graf1.set_xlabel('Tamaño Matriz $N$')
graf1.set_ylabel('Tiempo Transcurrido (s)')

plt.tight_layout()



#GUARDAR COMO IMAGEN EL GRAFICO
fig.savefig('RENDIMIENTO_inv.png')