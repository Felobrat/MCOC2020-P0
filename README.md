# MCOC2020-P0

# Mi Computador
* Tipo: Notebook
* Año: 2015
* Marca: ASUS
* Modelo: X556UAK
* Sistema Operativo: Windows 10 Home

* Hardware
  - Procesador: Intel(R) Core(TM) i5-7200U CPU @2.50Hz 2.71Hz 
  - Frecuencia Base: 2.50 GHz 
  - Frecuencia Turbo Máxima: 3.10 GHz
  - Nucleos: 2
  - Hilos: 4
  - Arquitectura: x86-64bit
  - Cachés del Procesador:
    - L1d: 32 KB
    - L1i: 32 KB
    - L2:  256 KB
    - L3:  3 MB
  - Memoria:
    - Memoria RAM (1): 8GB
    - Tipo: DDR4
    - Frecuencia: 1067 MHz 
    
 - Tarjeta Gráfica
    - Intel(R) HD Graphics 620
    - Resolucion: 1366x768 

 - Tarjeta de red wi-fi:
    - Descripcion: Qualcomm Atheros AR956x Wireless Network Adapter
    - Direccion MAC: 58:00:e3:3a:a2:a5
    - Velocidad de vinculo: 144/72 (Mbps)
    
  - Disco 1:
    - Marca Kingstone
    - Tpo SSD
    - Tamaño: 1 disco duro SSD 960 GB
    - Particiones: 1

# Desempeño MATMUL
![DESEMPEÑO MATMUL](https://user-images.githubusercontent.com/69157203/89699750-fa3bd100-d8f6-11ea-90eb-b08ded33ba88.png)

* Difieren bastante, analizando el primer gráfico, mi promedio de desempeño para matrices menores a 5 es de 0.1 s, mientras que el del profesor es de 0.1 ms. En el minimo alcanado por mi computador (cerca de las 12 a 15 iteraciones) mi minimo es cerca del doble que el computador del profesor. El máximo que alcanza mi computador en la matriz de 10.000x10.000 se demora 1 minuto, mientras que el del profesor 10 segundos. Por otro lado, en el gráfico 2, si bien la memoria que ocupa cada matriz es la misma, porcentaulmente con el total, el mio se nota mucho más exigido cerca de la matriz de 10.000x10.000 ya que esta muy cerca de usar toda su memoria de 8Gb, mientras que la del profesor, con más memoria, se ve que con holgura logra calcular la matriz.

* Estas diferencias se deben, en primer lugar a la capacidad que tiene cada procesador. Mi procesador es de uso diario, sin mayor exigencia que procesos sencillos, con menos hilos y nucleos que los del el profesor. Por otro lado, la memoria mia es casi la mitad que la del profesor. Estos factores limitan mi capacidad de procesamiento más que los que presenta el computador del profesor.

* El grafico de la memoria es lineal dado que al ser graficos logaritmicos y las matrices estar usando capacidad de procesamiento potenciales, se logra una relacion lineal entre los logaritmos de la memoria y del tamaño de la matriz. Por otro lado, la relacion entre tiempo de procesamiento no es lineal en log-log, por lo que significa que mientras más recursos use de memoria, menos capacidad de procesamiento le queda, esto se puede deber a la limitacion fisica de memoria se va llenando y va limitando la forma de de rocesamiento, esto señala que mientras más exigido este el procesador, más se va a demorar en procesarlo.

* Se uso Python v3.8

* Se uso NumPy v 1.18.5 incluido en Spyder (anaconda3).

* Durante el procesamiento usaron los cuatro nucleos lógicos, cuando uno se veia saturado, entraba otro. Imagen explicativa a continuacion. En ningun momento se usaron completamente los 4 nucleos.

![image](https://user-images.githubusercontent.com/69157203/89700215-7daaf180-d8fa-11ea-8468-e95765262303.png)

# Desempeño MIMATMUL

![DESEMPEÑO MIMATMUL](https://user-images.githubusercontent.com/69157203/89843741-978d4400-db47-11ea-8b45-5b9d49805ab0.png)

* Los graficos son bastante similares. difieren en el tiempo que se demoran en procesar la misma cantidad de información. Mi proceso para una matriz de 600x600 se demoro cerca de cinco minutos en cada corrida. De hacerlo para matrices más grandes hubiese estado mucho tiempo calculando. por otro lado,los tiempos de procesamiento minimos, fueron similares, al igual que el uso de memoria.

* Se pueden deber principalmente con el hardware, el procesador debe ser levemente mejor al mio y la memoria RAM, debe tener más capacidad. Esto genera que procese informacion más rapido y no se saturen tan rapido las memorias y cache.

* el Grafico de uso de memoria, no es lineal dado que van entrando al porcesamiento distintos elementos una vez que se ven sobrepasados en capacidad de procesamiento. Cuando van pasando informacion de un tipo a otro, se generan saltos, los cuales son coincidentes con la saturacion de la memoria que se esta usando para procesar, además a medida que van trabajando, se van incorporando más nucleos del procesador. Mientras más sobrepasado el computador, entra a memoria más lentas en el porcesamiento, lo que genera un aumento no lineal en log-log entre tiempo de procesamiento y tamaño de las matrices. No asi el grafico de memoria con tamaño de matices, los cuales son lineales en log-log.

* Version de Python: v3.8
* Numpy V 1.18.5

* Se ve que se usan los 2 nucleos y se ven los cuatro subprocesos en la imagen a continuacio.

![CPU](https://user-images.githubusercontent.com/69157203/89843744-9825da80-db47-11ea-8623-910fc5409f42.png)

# Desempeño INV

* Según los programas creados, las memorias utilizadas en mi  computador por los distintos tipos de datos son los siguientes:
  - Half: float16 - 4 bytes
  - Single: float32 - 4 bytes
  - Double: float64 - 8 bytes
  - Longdouble: float64 - 8 bytes
  
* Analizando la eficiencia de los algoritmos utilizando las funciones NumPy con los distintos tipos de datos, se tiene lo siguiente:
  - CASO 1 - NumPy: 
  
  ![RENDIMIENTO CASO 1](https://user-images.githubusercontent.com/69157203/90080032-8c691e00-dcd7-11ea-8694-4cac4f54e627.png)
  
  Se observa que el uso de memoria para los datos double, ocupan mayor memoria que en single. En cuanto al tiempo, se observa que el single tiene máyor variabilidad que lo que tiene double. Por otro lado, los tipos de dato half y longdouble no son soportados por numpy para invertir la matriz laplaceana.
  
  - CASO 2 - SciPy - False:
  
  ![RENDIMIENTO CASO 2](https://user-images.githubusercontent.com/69157203/90080278-3183f680-dcd8-11ea-8ac3-6f36dfba6c3c.png)

Se observa que la memoria utilizada por el longdouble es la mayor de todas, decreciendo para double, single y half respectivamente. En cuanto al tiempo, la mas estable en variabilidad de tiempo fue single, la que no presentó peaks inesperados.
  
  - CASO 3 - Scipy - True:
  
![RENDIMIENTO CASO 3](https://user-images.githubusercontent.com/69157203/90080615-11a10280-dcd9-11ea-9109-373b62e89df5.png)
  
  Se observa que la memoria utilizada por el longdouble es la mayor de todas, decreciendo para double, single y half respectivamente. En cuanto al tiempo, la mas estable en variabilidad de tiempo fue double, la que presentó menos peaks inesperados que el resto. Por otro lado, comparando los graficos con el caso 2, se tiene que hay mucha mayor variabilidad en la tendencia del recorrido del caso 3 en el uso del tiempo para los distintos tipos de dato, lo que señala que va moviendo datos de un lado a otro para intentar mejorar el rendimiento del algoritmo.
  
* Analizando los algoritmos para distintos tipos de datos.

  - HALF:
  
  ![Comparacion RENDIMIENTO half](https://user-images.githubusercontent.com/69157203/90080831-aa378280-dcd9-11ea-87e5-8851199cb25d.png)
  
  Se observa que los algoritmos son similares en el tiempo para datos de tipo half. El uso de memoria es el mismo dado el tipo de dato.
  
  - SINGLE
  
  ![Comparacion RENDIMIENTO single](https://user-images.githubusercontent.com/69157203/90080872-c4716080-dcd9-11ea-88f2-cd9230025b73.png)

  Se observa que presenta una mayor variabilidad en el tiempo para el CASO 3. El CASO 1 tambien presenta una variabilidad en el tiempo y mayor demora en matrices grandes en comparacion con los otros casos. Resulta el más estable en este caso el CASO 2. El uso de memoria es el mismo dado el tipo de dato.
  
  - DOUBLE
  
  ![Comparacion RENDIMIENTO double](https://user-images.githubusercontent.com/69157203/90080879-c9361480-dcd9-11ea-9f2a-051a9451eb27.png)

Los CASOS 1 y 2 son muy similares en su desempeño en el tiempo, mientras que el CASO 3 presenta gran variabilidad en algunos casos de matrices de tamaño medio. El uso de memoria es el mismo dado el tipo de dato.
  
  - LONGDOUBLE
  
  ![Comparacion RENDIMIENTO longdouble](https://user-images.githubusercontent.com/69157203/90080889-cd623200-dcd9-11ea-8c8b-ae06302b9799.png)
  
  El CASO 3 presenta una considerable demora en matrices de tamaño medio, pero se equipara en las de gran tamaño en el desempeño del CASO 2. El uso de memoria es el mismo dado el tipo de dato.
 
 
* Metodo de Inversion de NumPy y Scipy.
  - Yo considero que ambos utilizan el metodo LU con ajuste de Gauss-Jordan si no pueden por LU. La diferencia creo que está en las verificaciones que usa SciPy en la verificacion y en la optimización del algoritmo.
  
* Incidencia del Paralelismo y el Caché.
  - Considero que el paralelismo de los nucleos incide en dar potencia cuando estos estan optimizados para esa forma de proceso, pero no son tan eficientes cuando se debe operar con procesos que no son tan sofisticados. Ahi, el caché cobra importancia, donde empieza a procesar por paquetes de datos, procesos que requieren mucha memoria. EN conclusion, lo mejor es tener nucleos en paralelo, pero de no poder correr procesos en nucleos paralelos, el caché complementa esa falta de potencia y la calcula de forma paralela descongestionando el sistema. Se observa que los peaks pueden ser formas de optimizacion del algoritmo para que sean trabajados en paralelo, lo que traducido seria que el sistema trata de optimizar el proceso mandandolo al cache para que lo procese más rapido.
  
  # Rendimiento Ax=b (Entrega 6)

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

Comparando los resultados obtenidos con los entregados por el Ayudante/Profesor, es importante notar que el grafico entregado es inverso al obtenido por mi, lo que señala que dado que los poderes de procesamiento son mejores para el Ayudante/Profesor, seguramente optimicen mejor el uso de memoria y procesamiento, lo que hace que las funciones Scipy sea optima, mientras que en mi computador no haya tanto procesamiento, reusltan inversos, dado que enlentecen estas funciones mi procesamiento dado que requieren más recursos basales para poder estar funcionando en su optimo, logrando una saturacion de mi computador y un mal desempeño de estas funciones y siendo mejor el algoritmo de NumPy o de multiplicacion directa.

# Matrices dispersas y complejidad computacional (Entrega 7)

En esta entrega, se ve el comportamineto de Matrices llenas y complejas en distintos ambientes de armado y solucion del problema matematico en distintos tamaños de matrices. Se evaluara lña complejidad asintotica en casos de matrices laplaceanas de dimension N hasta 16.382.

* Observaciones
  1. al correr el programa, se observo que la memoria ram se vio saturada unicamente en el caso de matriz dispersa con inversion de matrices de N=16382. 
  
  ![Anotación 2020-08-21 163822](https://user-images.githubusercontent.com/69157203/90947939-c76dfe80-e407-11ea-8fdf-35cf080d65c3.png)
  2. Se observa que se saturo de igual manera el disco duro al 100% para el mismo caso de matriz y problema matematico.
  ![63822](https://user-images.githubusercontent.com/69157203/90947937-c5a43b00-e407-11ea-8453-a41913a72a60.png)
  
  3. El procesador no se vio sumamente exigido, pero si con harto trabajo para el mismo caso de matriz y problema matematico.
  ![Anotación 2020-08-21 094723](https://user-images.githubusercontent.com/69157203/90947938-c6d56800-e407-11ea-9adc-346a89d6b8c2.png)

* Resultado de rendimiento de MATMUL en LLENA y luego en DISPERSA

  ![DESEMPEÑO MATMUL_lleno](https://user-images.githubusercontent.com/69157203/90947979-377c8480-e408-11ea-8368-302a0d1b8121.png)

  ![DESEMPEÑO MATMUL_disperso](https://user-images.githubusercontent.com/69157203/90947980-3ba8a200-e408-11ea-9afa-63072667f522.png)

Se obvserva que los timepos de ensamblaje de las matrices llenas y dispersas se comportan similar, con una tendencia en N grandes a una scintota en N^2 en ambos casos. Se observa mayor variabilidad en los tiempos para la matriz llena que la dispersa. En tamaños de matriz pequeños, la matriz llena tiene un comportamiento constante en el ensamblaje mientras que la dispersa más bien asintyotico en N.

Para los tiempos de solucion, se ve claramente una tendencia constante para matrices cercanas a N=100 mientras que rtapidamente se comporta como O(N^3) para matrices mayores. Por otro lado la matriz dispersa es mas bien constante en la resolucion de este tipo de problemas.

* Resultado de rendimiento de Ax=b en LLENA y luego en DISPERSA
  
  ![DESEMPEÑO A_invb_lleno](https://user-images.githubusercontent.com/69157203/90947984-49f6be00-e408-11ea-91f8-c046faccdd18.png)
  
  ![DESEMPEÑO A_invb_disperso](https://user-images.githubusercontent.com/69157203/90947986-4c591800-e408-11ea-8420-719cb1e5f5f4.png)

Para este tipo de problemas, se observa que el ensamblaje de la matriz llena tiene un comportamiento O(N) para N menores a 200, mientras que rapidamente se comporta como O(N^2) para N mayores. por otro lado, la matriz dispersa en el ensamblaje, se comporta muy parecido, teniendo un comportamiento parecido a O(N) a contante para N menores a 200 y luego se vuelve asintotica a O(N^2). 

Por otro lado, el comportamiento de la solucoion tien un comportamiento para matrices llenas de forma asintotica en O(N^3), mientras que la matriz dispersa se comporta como conatnte para valores menores que 200 y luego toma un comportamiento de O(N).
    
* Resultado de rendimiento de inv(A) en LLENA y luego en DISPERSA

  ![DESEMPEÑO invA_lleno](https://user-images.githubusercontent.com/69157203/90947991-5d098e00-e408-11ea-8c05-7c5af4d182f6.png)
  ![DESEMPEÑO invA_disperso](https://user-images.githubusercontent.com/69157203/90947993-60047e80-e408-11ea-9bc5-62eca4d52010.png)
  
  
 Para este tipo de problemas, se observa que el ensamblaje de la matriz llena tiene un comportamiento O(N) para N menores a 200, mientras que rapidamente se comporta como O(N^2) para N mayores. por otro lado, la matriz dispersa en el ensamblaje, se comporta muy parecido, teniendo un comportamiento parecido a O(N) a contante para N menores a 2000 y luego se vuelve asintotica a O(N^2). 

Por otro lado, el comportamiento de la solucoion tien un comportamiento para matrices llenas de forma asintotica en O(N^3) para N menores a 2000, mientras que la matriz dispersa se comporta como O(N^2) para valores menores que 10000 y luego toma un comportamiento de O(N^4).
  


