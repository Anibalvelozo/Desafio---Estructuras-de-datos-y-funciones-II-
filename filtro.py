import sys

def filtrar_productos(precios, umbral, modo='mayor'):
    productos_filtrados = {}
    
    if modo == 'menor':
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio < umbral}
    elif modo == 'mayor':
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio > umbral}
    else:
        return "Lo sentimos, no es una operación válida"
    
    return productos_filtrados

def main():
    precios = {'Notebook': 700000,
               'Teclado': 25000,
               'Mouse': 12000,
               'Monitor': 250000,
               'Escritorio': 135000,
               'Tarjeta de Video': 1500000}

    if len(sys.argv) == 2:
        umbral = int(sys.argv[1])
        modo = 'mayor'
    elif len(sys.argv) == 3 and sys.argv[2] == 'menor':
        umbral = int(sys.argv[1])
        modo = 'menor'
    else:
        print("Por favor, ingrese un umbral y opcionalmente 'menor' para filtrar los productos menores al umbral.")
        return
    
    productos_filtrados = filtrar_productos(precios, umbral, modo)
    
    if isinstance(productos_filtrados, dict):
        if modo == 'mayor':
            print(f"Los productos mayores al umbral son: {', '.join(productos_filtrados.keys())}")
        else:
            print(f"Los productos menores al umbral son: {', '.join(productos_filtrados.keys())}")
    else:
        print(productos_filtrados)

main()