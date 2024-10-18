 # Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extensión donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
 
# Se solicita el número de teléfono al usuario
telefono = input("Introduce un número de teléfono con formato +34-XXXXXXXXX-XX:\n")

# Validación: que el prefijo sea +34
if not telefono.startswith('+34-'):
    print("Error: El número debe empezar con +34-")
else:
    # Divido la cadena usando el guión como separador
    partes = telefono.split('-')
    
    # Extraigo solo el número principal (sin prefijo ni extensión)
    numero_principal = partes[1]
    
    # Resultado
    print("El número de teléfono sin prefijo ni extensión es:", numero_principal)