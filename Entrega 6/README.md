# Rendimiento Ax=b

En esta entrega, se evalua el desempeño de distintas funciones para resolver un sistema lineal Ax=B a través de distintos métodos; multiplicacion directa, herramientas NumPy y SciPy ccon distintos formatos de manejo en este ultimo. Se analizara el desempeño de éstas y como se comporta el rendimiento de mi computador.

* Observaciones:
  
    * El correr el programa, se observa que se generan los archivos, pero al llegar a la matriz 10.000x10.000, tiene problamas en la funcion SciFy, la cual no logra iterar de forma  correcta la matriz y advirtiendo de fallas en la sensibilidad. Se adjunta imagen a  continuación.
  
  ![warning10000](https://user-images.githubusercontent.com/69157203/90408904-7f9d4f00-e076-11ea-95a2-de1a94912e4e.png)

     Los errores se encuentran en la subfuncion POS y SYM de la funcion SCIPY.

   * El rendimiento del CPU (1) y Memoria RAM (2) usada, se observa en los graficos a continuación.
  
  (1) 
  
  ![cpu2](https://user-images.githubusercontent.com/69157203/90409161-cd19bc00-e076-11ea-9945-8193cce19058.png)

  (2) 
  
  ![ram2](https://user-images.githubusercontent.com/69157203/90409167-cee37f80-e076-11ea-98de-b31951696f02.png)

   Se comentará más adelante.
   
* Resultado del Rendimiento de distintas Funciones Ax=b

![RENDIMIENTO_inv](https://user-images.githubusercontent.com/69157203/90411674-1ae3f380-e07a-11ea-8a7d-b609f4fe53a7.png)
