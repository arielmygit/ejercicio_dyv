arreglo = [-6, -2, -3, 0, 9, -1]
n = len(arreglo)

def producto_cruzado_maximo(arreglo, inicio, medio, fin):
    producto_izquierda = arreglo[medio]
    producto = 1
    # O(n)
    for i in range(medio, inicio - 1, -1):
        producto *= arreglo[i]
        producto_izquierda = max(producto_izquierda, producto)
    #O(2)
    producto_derecha = arreglo[medio + 1]
    producto = 1
    # O(n)
    for i in range(medio + 1, fin + 1):
        producto *= arreglo[i]
        producto_derecha = max(producto_derecha, producto)

    
    return producto_izquierda * producto_derecha

def producto_maximo(arreglo, inicio, fin):
    # O(1)
    if inicio == fin:
        return arreglo[inicio]
    
    # O(log n)
    medio = (inicio + fin) // 2

    # O(log n)
    maximo_izquierda = producto_maximo(arreglo, inicio, medio)
    
    # O(log n)
    maximo_derecha = producto_maximo(arreglo, medio + 1, fin)
    
    # O(n)
    maximo_cruzado = producto_cruzado_maximo(arreglo, inicio, medio, fin)
    
    
    return max(maximo_izquierda, maximo_derecha, maximo_cruzado)

#O(2)
resultado = producto_maximo(arreglo, 0, n - 1)
print("El producto máximo en el arreglo es: "+str(resultado))


