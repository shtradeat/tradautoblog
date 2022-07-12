menu = """
Bienvenido al conversor Internacional de monedas 

Opcion 1: Pesos Colombianos
Opción 2: Pesos Argentinos
Opción 3: Pesos Mexicanos

Elige una opción
"""

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Cuántos pesos Colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 4530
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")
elif opcion == 2:
    pesos = input("Cuántos pesos Argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 129
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")
elif opcion == 3:
    pesos = input("Cuántos pesos Mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 21
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")
else: 
    print("Escribe una opción correcta")

