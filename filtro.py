
import sys

def filtrar_productos(precios, umbral, operacion="mayor"):

    productos_filtrados = {}

    for producto, precio in precios.items():
        if operacion == "mayor" and precio > umbral:
            productos_filtrados[producto] = precio
        elif operacion == "menor" and precio < umbral:
            productos_filtrados[producto] = precio

    return productos_filtrados


precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}


if len(sys.argv) == 2:
    umbral = int(sys.argv[1])
    productos_filtrados = filtrar_productos(precios, umbral)
    if productos_filtrados:
        print(f"Los productos mayores al umbral son: {', '.join(productos_filtrados.keys())}")
    else:
        print("No hay productos que cumplan la condición especificada.")
elif len(sys.argv) == 3:
    umbral = int(sys.argv[1])
    operacion = sys.argv[2]
    productos_filtrados = filtrar_productos(precios, umbral, operacion)
    if productos_filtrados:
        print(f"Los productos {operacion} al umbral son: {', '.join(productos_filtrados.keys())}")
    else:
        print("No hay productos que cumplan la condición especificada.")
else:
    print("Lo sentimos, no es una operación válida")