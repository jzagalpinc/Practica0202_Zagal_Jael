# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delantera de la arroba @) pero con dominio ceu.es.

# Pido el correo electrónico al usuario
correo = input("Ingrese su correo electronico por favor:\n")

# Verificar si el correo contiene @
if '@' in correo:
    # Separo el nombre de usuario (antes del @)
    nombre = correo.split('@')[0]
    # Nuevo correo con el dominio ceu.es
    nuevo_correo = nombre + '@ceu.es'
    print("Su correo con el nuevo dominio es:", nuevo_correo)
else:
    print("Error: El correo debe contener @")