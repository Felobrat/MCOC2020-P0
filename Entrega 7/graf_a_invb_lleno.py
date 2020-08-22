# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 18:11:22 2020

@author: Felipe Bravo
"""
#FUNCIONES A USAR
from psutil import virtual_memory
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

#ROTULO DE LOS EJES
x     = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
y1    = [0.000001, 0.1e-3, 1e-3, 10e-3, 0.1, 1, 10, 60, 600]
y2    = [10**i for i in range(3, 11)]
y1val = ["0.01 ms", "0.1 ms","1 ms","10 ms","0,.1 s","1 s","10 s","1 min", "10 min"]
y2val = ["1 KB","10 KB","100 KB","1 MB","10 MB", "100 MB","1 GB", "10 GB"]

NP = [2, 4, 8, 16,
      32, 64, 128, 256,
      512, 1024,2048, 4096,
      8192, 16384]

#EMPEZAR A GRAFICAR
fig = plt.figure(figsize=(7,7))   

#CREAR PRIMER GRAFICO Y ORDENARLO EN EL PRIMER ESPACIO VERTICALMENTE
graf1 = fig.add_subplot(2,1,1)

#RECORRER LOS .txt CREADOS Y ALMACENAR LA INFORMACION PARA USARLA
for i in range(5):
    datos = np.loadtxt(f"lleno{i}.txt")
    graf1.plot(datos[:,0], datos[:,1],"o-", color='gray')
    
#AJUSTAR A ESCALA LOG-LOG EL GRAFICO 1
graf1.set_xscale("log")
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

#HACER QUE TENGA LOS ESPACIOS ENTREMEDIO, SEÑALANDO AL ESCALA LOG
graf1.minorticks_on()


#DARLE TITULO A LOS EJES
graf1.set_ylabel('Tiempo de ensamblado (s)')
graf1.set_title('Rendimiento Ax=b lleno')
graf1.plot([16384],[600], "w--")
graf1.plot([2, 16384],[max(datos[:,1]),max(datos[:,1])], linestyle='--', color='royalblue', label="constante" )
graf1.plot([2, 16384], [2*max(datos[:,1])/16384, 16384*max(datos[:,1])/16384], linestyle='--', color='gold', label="O(N)" ) 
graf1.plot([10, 16384], [10**2*max(datos[:,1])/16384**2, 16384**2*max(datos[:,1])/16384**2], linestyle='--', color='darkgreen', label="O(N^2)") 
graf1.plot([100, 16384], [100**3*max(datos[:,1])/16384**3, 16384**3*max(datos[:,1])/16384**3], linestyle='--', color='orangered', label="O(N^3)" ) 
graf1.plot([400, 16384], [400**4*max(datos[:,1])/16384**4, 16384**4*max(datos[:,1])/16384**4], linestyle='--', color='purple', label="O(N^4)")

#CREAR SEGUNDO GRAFICO Y ORDENARLO EN EL SEGUNDO ESPACIO VERTICALMENTE
graf2 = fig.add_subplot(2,1,2)

#REUSAR LOS DATOS ALMACENADOS PREVAIMENTE EN 'datos'
for i in range(5):
    datos = np.loadtxt(f"lleno{i}.txt")
    graf2.plot(datos[:,0], datos[:,2],"o-",color='gray')


#AJUSTAR A ESCALA LOG-LOG EL GRAFICO 2
graf2.set_yscale("log")
graf2.set_xscale("log")

#DARLE EL ESPACIADO ASIGNADO
graf2.set_xticks(x)
#HACER QUE TENGA LOS VALORES DE ITERACION 
graf2.set_xticklabels(x)
#ROTAR LAS ETIQUETAS COMO EL DE EJEMPLO
for tick in graf2.get_xticklabels():
    tick.set_rotation(45)

#DARLE ESPACIADO AL EJE 
graf2.set_yticks(y1)
#REASIGNAR LOS VALORES DE LOS EJES 
graf2.set_yticklabels(y1val)
#DEFINE UNA LINEA HORIZONTAL ACCEDIENDO A LA MEMORIA VIRTUAL DEL COMPUTADOR Y GRAFICANDOLA

#ACTIAR LA GRILLA
#HACER QUE TENGA LOS ESPACIOS ENTREMEDIO, SEÑALANDO AL ESCALA LOG
graf2.minorticks_on()
#LIMITE DE LOS EJES


#TITULO DE LOS EJES
graf2.set_xlabel("Tamaño Matriz N")
graf2.set_ylabel("Tiempo de solucion (s)")
graf2.plot([2, 16384],[max(datos[:,2]),max(datos[:,2])], linestyle='--', color='royalblue', label="Constante" )
graf2.plot([16384],[600], "w--")
graf2.plot([2, 16384], [2*max(datos[:,2])/16384, 16384*max(datos[:,2])/16384], linestyle='--', color='gold', label="O(N)" ) 
graf2.plot([2, 16384], [2**2*max(datos[:,2])/16384**2, 16384**2*max(datos[:,2])/16384**2], linestyle='--', color='darkgreen', label="O(N^2)" ) 
graf2.plot([50, 16384], [50**3*max(datos[:,2])/16384**3, 16384**3*max(datos[:,2])/16384**3], linestyle='--', color='orangered', label="O(N^3)" ) 
graf2.plot([200, 16384], [200**4*max(datos[:,2])/16384**4, 16384**4*max(datos[:,2])/16384**4], linestyle='--', color='purple', label="O(N^4)" )
graf2.legend()
plt.tight_layout()
#GUARDAR COMO IMAGEN EL GRAFICO
fig.savefig('DESEMPEÑO A_invb_lleno.png')