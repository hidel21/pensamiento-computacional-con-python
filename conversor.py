def conversor(tipo_moneda, valor_dolar):
    pesos = input("Cuantos "+ tipo_moneda +" tienes?: ")
    pesos= float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" +dolares+ " dolares")


menu= """
Bienvenido al conversor de monedas 👨🏼‍💻💰

Opciones:
1- Pesos Chilenos
2- Pesos Colombianos
3- Bolivares

Elige una opcion: """

opcion= input(menu)

if opcion =='1':
    conversor("Pesos Chilenos", 907.06)
elif opcion == '2':
    conversor("Pesos Colombianos", 4317.18)
elif opcion == '3':
    conversor("Bolivares", 5.81)
else:
    print('ingrese una opción correcta porfavor')


#Hola estoy haciendo pruebas de git 

