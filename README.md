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
