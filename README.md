# ALGORITMOS_2_Pablo_Jimenez_Girardeau

# Ejercicio 3: Cálculo del Factorial

## Precondición
- El valor de **n** debe ser un número entero no negativo.

## Poscondición
- El resultado será el factorial de **n**, que es el producto de todos los enteros positivos menores o iguales a **n**.
- La función devolverá 1 si **n** es 0, ya que **0! = 1** por definición.

## Datos de entrada
- Un número entero **n**.

## Datos de salida
- El factorial del número entero **n**.

## Hipótesis
- Se asume que **n** es un número entero no negativo.

## Efecto
- La función factorial calculará recursivamente el factorial del número **n**.
- El programa principal llamará a la función factorial con un número de prueba y mostrará el resultado.

## Pseudocódigo
```python
def factorial(n):
    """
    La función recibe un parámetro **n** que representa el número del cual se calculará el factorial.
    - Si **n** es 0, retorna 1 ya que por definición **0! = 1**.
    - Si **n** es mayor que 0, retorna **n** multiplicado por el factorial de **n-1**.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ejercicio 4: Ejercicio Ordenacion
# Bubble Sort

## Objetivo
El objetivo de este ejercicio es entender y explicar el funcionamiento del método de ordenación Bubble Sort (Ordenamiento Burbuja) y demostrar su aplicación en un contexto teórico.

## Explicación del Método Bubble Sort

Bubble Sort es un algoritmo de ordenación simple que repite pasos a través de una lista, comparando elementos adyacentes y cambiándolos si están en el orden incorrecto. Este proceso se repite hasta que la lista esté ordenada.

### Funcionamiento
1. **Comparación e Intercambio:** Comienza en el primer elemento de la lista y compara el elemento actual con el siguiente. Si el elemento actual es mayor que el siguiente, se intercambian.
2. **Iteraciones:** Recorre la lista varias veces. En cada pasada, el elemento más grande "burbujea" hacia el final de la lista.
3. **Pasada Completa:** Se repite el proceso de comparación e intercambio para cada elemento de la lista en cada pasada, excluyendo los últimos elementos ya ordenados.

### Ventajas
- **Simplicidad:** Es fácil de entender y de implementar.
- **Memoria:** No requiere memoria adicional significativa (es un algoritmo en sitio).

### Desventajas
- **Ineficiencia:** Es menos eficiente en términos de tiempo de ejecución comparado con otros algoritmos de ordenación, especialmente para listas grandes (complejidad temporal O(n^2)).

### Cuándo Usar Bubble Sort
- Cuando se trabaja con listas pequeñas.
- Cuando la simplicidad del código es más importante que la eficiencia.
- Cuando se necesita un algoritmo de ordenación estable (mantiene el orden relativo de elementos iguales).

## Ejemplo Conceptual

Vamos a aplicar el método Bubble Sort a la siguiente lista de números: `[34, 7, 23, 32, 5]`.

### Lista Inicial
`[34, 7, 23, 32, 5]`

### Pasada 1
1. Comparar 34 y 7, como 34 > 7, intercambiamos:
   `[7, 34, 23, 32, 5]`
2. Comparar 34 y 23, como 34 > 23, intercambiamos:
   `[7, 23, 34, 32, 5]`
3. Comparar 34 y 32, como 34 > 32, intercambiamos:
   `[7, 23, 32, 34, 5]`
4. Comparar 34 y 5, como 34 > 5, intercambiamos:
   `[7, 23, 32, 5, 34]`

### Pasada 2
1. Comparar 7 y 23, no se necesita intercambio:
   `[7, 23, 32, 5, 34]`
2. Comparar 23 y 32, no se necesita intercambio:
   `[7, 23, 32, 5, 34]`
3. Comparar 32 y 5, como 32 > 5, intercambiamos:
   `[7, 23, 5, 32, 34]`

### Pasada 3
1. Comparar 7 y 23, no se necesita intercambio:
   `[7, 23, 5, 32, 34]`
2. Comparar 23 y 5, como 23 > 5, intercambiamos:
   `[7, 5, 23, 32, 34]`

### Pasada 4
1. Comparar 7 y 5, como 7 > 5, intercambiamos:
   `[5, 7, 23, 32, 34]`

### Lista Ordenada
`[5, 7, 23, 32, 34]`

Después de estas pasadas, la lista está completamente ordenada. Bubble Sort asegura que los elementos grandes se "burbujen" hacia el final de la lista con cada iteración, y el proceso se repite hasta que no se necesiten más intercambios.
