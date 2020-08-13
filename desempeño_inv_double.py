# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 19:44:08 2020

@author: Felipe Bravo
"""

from psutil import virtual_memory
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

#ROTULO DE LOS EJES
x     = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
y1    = [0.000001, 0.1e-3, 1e-3, 10e-3, 0.1, 1, 10, 60, 600]
y2    = [10**i for i in range(3, 11)]
y1val = [".","0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min", "10 min"]
y2val = ["1 KB","10 KB","100 KB","1 MB","10 MB", "100 MB","1 GB", "10 GB"]



#EMPEZAR A GRAFICAR
fig = plt.figure()  

#CREAR PRIMER GRAFICO Y ORDENARLO EN EL PRIMER ESPACIO VERTICALMENTE
graf1 = fig.add_subplot(2,1,1)

#RECORRER LOS .txt CREADOS Y ALMACENAR LA INFORMACION PARA USARLA
datos = np.loadtxt('timing_inv_caso_1_np.double.txt')
graf1.plot(datos[:,0], datos[:,1],"o-", label='double_C1')
datos = np.loadtxt('timing_inv_caso_2_np.double.txt')
graf1.plot(datos[:,0], datos[:,1],"o-", label='double_C2')
datos = np.loadtxt('timing_inv_caso_3_np.double.txt')
graf1.plot(datos[:,0], datos[:,1],"o-", label='double_C3')


#AJUSTAR A ESCALA LOG-LOG EL GRAFICO 1
graf1.set_xscale('log')
graf1.set_yscale("log")

#DARLE EL ESPACIADO ASIGNADO
graf1.set_xticks(x)
#HACER QUE NO TENGA VALORES
graf1.set_xticklabels(['' for _ in range(len(x))])

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
graf1.set_ylabel('Tiempo Transcurrido (s)')
graf1.set_title('Comparacion rendimiento Rendimiento INV (double)')


#CREAR SEGUNDO GRAFICO Y ORDENARLO EN EL SEGUNDO ESPACIO VERTICALMENTE
graf2 = fig.add_subplot(2,1,2)

#REUSAR LOS DATOS ALMACENADOS PREVAIMENTE EN 'datos'
datos = np.loadtxt('timing_inv_caso_1_np.double.txt')
graf2.plot(datos[:,0], datos[:,2],"o-", label='double_C1')
datos = np.loadtxt('timing_inv_caso_2_np.double.txt')
graf2.plot(datos[:,0], datos[:,2],"o-", label='double_C2')
datos = np.loadtxt('timing_inv_caso_3_np.double.txt')
graf2.plot(datos[:,0], datos[:,2],"o-", label='double_C3')

#AJUSTAR A ESCALA LOG-LOG EL GRAFICO 2
graf2.set_yscale("log")
graf2.set_xscale("log")

#DARLE EL ESPACIADO ASIGNADO
graf2.set_xticks(x)
#HACER QUE TENGA LOS VALORES DE ITERACION 
graf2.set_xticklabels(x)
#ROTAR LAS ETIQUETAS COMO EL DE EJEMPLO
for tick in graf2.get_xticklabels():
    tick.set_rotation(60)

#DARLE ESPACIADO AL EJE 
graf2.set_yticks(y2)
#REASIGNAR LOS VALORES DE LOS EJES 
graf2.set_yticklabels(y2val)
#DEFINE UNA LINEA HORIZONTAL ACCEDIENDO A LA MEMORIA VIRTUAL DEL COMPUTADOR Y GRAFICANDOLA
graf2.axhline(virtual_memory().total, linestyle='--', color='black')


#ACTIAR LA GRILLA
graf2.grid()
#HACER QUE TENGA LOS ESPACIOS ENTREMEDIO, SEÑALANDO AL ESCALA LOG
graf2.minorticks_on()
graf2.legend()
#LIMITE DE LOS EJES


graf2.set_ylim([10, 10**11])
#TITULO DE LOS EJES
graf2.set_xlabel("Tamaño Matriz N")
graf2.set_ylabel("Uso memoria")


#GUARDAR COMO IMAGEN EL GRAFICO
fig.savefig('Comparacion RENDIMIENTO_double.png')