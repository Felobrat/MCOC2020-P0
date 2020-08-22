# Matrices dispersas y complejidad computacional

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
  

