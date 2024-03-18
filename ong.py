def calcular_factorial(n):

    if n == 0:
        return 1
    else:
        return n * calcular_factorial(n - 1)

def calcular_productoria(lista):

    productoria = 1
    for num in lista:
        productoria *= num
    return productoria

def calcular(**kwargs):

    for key, value in kwargs.items():
        if key.startswith("fact_"):
            n = int(value)
            print(f"El factorial de {n} es {calcular_factorial(n)}")
        elif key.startswith("prod_"):
            lista = [int(x) for x in value]
            print(f"La productoria de {lista} es {calcular_productoria(lista)}")

# Ejemplo de uso
calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)