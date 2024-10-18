# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

# Pido precio al usuario
precio = input("Por favor ntroduce el precio en euros (con dos decimales):\n")

# Divido el precio en euros y céntimos usando el *punto como separador
euros, centimos = precio.split('.')

# Resultado
print(euros, "euros y", centimos, "céntimos")