# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

# Pido los productos al usuario
productos = input("Por favot introduce los productos separados por comas:\n")

# Divido la cadena en una lista usando la coma como separador
lista_productos = productos.split(',')

# Resultado, he tenido que utilizar un bucle
for producto in lista_productos:
    # strip() elimina espacios en blanco al inicio y final
    print(producto.strip())