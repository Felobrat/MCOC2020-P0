# MCOC2020-P0

# Mi Computador
* Año 2015
* Marca: ASUS
* Modelo: X556UAK
* Sistema Operativo: Windows 10 Home
* Procesador: Intel(R) Core(TM) i5-7200U CPU @2.50Hz 2.71Hz 
* Velocodad Maxima: 3.10Hz
* Tarjeta Grafica: Gráficos HD Intel® 620
* Resolucion: 1366x768
* Caché: 3MB
* Arquitectura: 64bit
* Nucleos: 2
* Hilos: 4
* Memoria RAM: 8GB (2) DDR4 
* Almacenamiento: 1 disco duro SSD 960 GB

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
