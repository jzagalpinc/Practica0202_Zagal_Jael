# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

# Fecha al usuario
fecha = input("Por favor introduce tu fecha de nacimiento (dd/mm/aaaa):\n")

# DIvido la fecha en día, mes y año usando la / como separador
dia, mes, ano = fecha.split('/')

# Resultado
print("Día:", dia)
print("Mes:", mes)
print("Año:", ano)