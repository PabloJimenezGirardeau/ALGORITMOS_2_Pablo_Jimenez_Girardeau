# factorial.py

def factorial(n):
    """Calcula el factorial de un número dado.
    
    Parameters
    ----------
    n : int
        Número entero al que se le calculará el factorial.
        
    Returns
    -------
    int
        El factorial del número dado.
        
    Example
    -------
    factorial(5)
    120
    """
    # Caso base: 0! es 1
    if n == 0:
        return 1
    # Paso recursivo: n * (n-1)!
    else:
        return n * factorial(n - 1)

def main():
    print("=================================================================.")
    print("Caso de Prueba 1: Verificar el factorial de 5.")
    print("=================================================================.")
    print("El factorial de 5 es: ", factorial(5))

if __name__ == "__main__":
    main()
