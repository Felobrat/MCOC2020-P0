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

Se observa que para matrices de dimensión 2 a 10, se tiene un tiempo de procesamiento casi constante en LOG-LOG, lo que inidca que el tamaño no es relevante en la variabilidad del procesamiento de los datos en ese tramos, se observa que el más veloz en este tramo es la multiplicacion directa A_invb, y la inversion usando np.solve, mientras que la más lenta son las sp.solve; esto se debe a que la multilpicacion directa no necesit recursos adicionales, y al usarlos, se enlentece el proceso de iteracion dado el aumento de procesamiento y uso de memoria. Desde matrices de dimension 10 a 50, se tiene que hay un aumento sostenido de la demora casi lineal o potencial en la escala LOG-LOG, lo que indica un procesamiento más caotico y aprovechando recursos de optimizacion de memoria en algunos casos, pero se mantiene la optimalidad de procesamiento anterior. Para Matrices de dimension 50 a 200, se tiene que se empiza a notar la diferencia en el uso de recursos de optimizacion de las funciones de sp.solve, sobrepasando rapidamente a la multiplicacion directa a traves de np.solve, con la distincion que la funcion sp.solve sin añadiduras es menos eficiente a medida que se agregan sub funciones en ella y resolviendo de manera en tiempos ascendentes a medida que se agregan más subfunciones; todavia es más eficiente la multiplicacion directa de las matrices a traves del operador asterisco. Para dimensiones de matriz superiores a 200, se observa que las matrices tienen un comportamiento cada vez más parecido y tendencia asintotica, pero siendo levente superior en casi todos los casos la multiplicacion directa.

Se observa que para dimensiones superiores a 5.000, el algoritmo SciPy no logra mantener la precision necesaria, seguramente por la saturacion de la memoria. Lo que se puede observar en el grafico (2), donde se ve utilizada la memoria RAM casi en su totalidad y los procesadores ocupando peaks y se comniezan a saturar y des saturar a medida que procesa, lo que se puede ver que estan pasandose informacion de un lado a otro procesando información para no saturarse.

Se debe entonces, estudiar cual va a ser la dimension y la sensibilidad que se necesita en cada problema para decidir cual funcion de resolución es más adecuado utilizar.
