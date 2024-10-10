import matplotlib.pyplot as plt

class Pilas:
    def graficar_pila(pila):
        alturas = [1] * len(pila)
        plt.figure(figsize=(4, 4))
        plt.bar(range(len(pila)), alturas, color='blue')
        plt.xlabel('Posición en la pila')
        plt.ylabel('Valor')
        plt.title('Estado de la pila')
        plt.xticks(range(len(pila)), pila)
        plt.show()

    def agregar_elemento(Pila):
        for i in range (9):
            elemento = str(input("Ingrese un elemento: "))
            Pila.append(elemento)
            print(f'Pila después de agregar "{elemento}": {Pila}')
            Pilas.graficar_pila(Pila)

    def eliminar_elemento(Pila):
        for i in range(4):
            elemento = input("¿Qué elemento desea eliminar?: ")
            if elemento in Pila:
                Pila.remove(elemento)
                print(f'Pila después de eliminar "{elemento}": {Pila}')
                Pilas.graficar_pila(Pila)
            else:
                print(f'El elemento "{elemento}" no está en la pila.')

pila = []
Pilas.agregar_elemento(pila)
Pilas.eliminar_elemento(pila)