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
