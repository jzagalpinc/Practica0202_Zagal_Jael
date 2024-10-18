# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

# Frase y la vocal al usuario
frase = input("Introduce una frase:\n")
vocal = input("Introduce una vocal:\n")

# Reemplazo la vocal por su versión en mayúscula
frase_modificada = frase.replace(vocal, vocal.upper())

# Resultado
print("Frase con la vocal en mayúscula:", frase_modificada)