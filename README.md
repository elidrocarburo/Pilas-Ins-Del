# Pilas-Ins-Del
Ejercicio acerca de agregar y eliminar elementos de una pila
<p>El siguiente código es acerca de agregar y eliminar elementos de una pila de manera gráfica, para saber el comportamiento de la misma pila al estar eliminando ciertos elementos del mismo.</p>
<p>Lo primero que haremos es importar la librería "mathplotlib.pyplot" para poder graficar nuestra pila.</p>
<p>Después cree mi clase de pilas, seguido por los métodos "graficar_pila", "agregar_elemento" y "eliminar_elemento", estas 3 actuando en nuestro vector de "pila".</p>
<ul>
  <li>graficar_pila: método que hace uso de la librería previamente importada, donde "alturas" permite que todos los elementos de la pila tengan el mismo tamaño, "plt.figure" da las dimensiones de la figura, en este caso, una figura 4x4, "plt.bar" se basa en la variable alturas para hacer la figura de una barra de color azul, "plt.xlabel" es el nombre que tendrá el eje X y "plt.ylabel" el nombre que tendrá el eje Y, "plt.title" es el nombre de nuestra gráfica, "plt.xticks" configura los nombres de nuestra figura y "plt.show" nos muestra la gráfica ya terminada en forma de un programa.</li>
  <li>agregar_elemento: método que permite que agreguemos los elementos a la pila, en este caso, al querer agregar letras haremos un input de tipo string y con Pila.append estaremos llenando la pila con los elementos que estamos pidiendo al usuario, donde tenemos un límite para agregar elementos. Al final haremos llamada al método de "graficar_pila" para que nos muestre cómo quedó al final la pula.</li>
  <li>eliminar_elemento: se encarga de eliminar los elementos que queramos de la pila, lo contrario al anterior método, sólo que con la diferencia que si un elemento que queramos eliminar no está en la pila, nos mandará un mensaje de error.</li>
<p>Al final, colocaremos nuestra pila y haremos la llamada a los métodos "agregar_elemento" y "eliminar_elemento" de la clase Pilas, donde todo va a estar llenándose en nuestro vector de "pila".</p>
</ul>
