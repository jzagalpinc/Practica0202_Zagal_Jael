# Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

# Pido los datos al usuario
nombre = input("Por favor introduce el nombre del producto:\n")
precio = float(input("Por favor introduce el precio unitario:\n"))
unidades = int(input("Por favor introduce el número de unidades:\n"))

# Calcular el coste total
coste_total = precio * unidades

# Formateo la salida usando format
# {:6.2f} -> 6 dígitos enteros, 2 decimales, número flotante
# {:3d} -> 3 dígitos, número entero
# {:8.2f} -> 8 dígitos enteros, 2 decimales, número flotante
salida = f"{nombre}: {precio:6.2f}€/unidad, {unidades:3d} unidades, Total: {coste_total:8.2f}€"

# Resultado
print(salida)