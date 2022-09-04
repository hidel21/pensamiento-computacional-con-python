# import random 

# def generar_contrasena():
#     mayusculas = ['A', 'B', 'C', 'D', 'E', 'F',
#     'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#     'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
#     'V', 'X', 'Y', 'Z']
   
#     minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
#      'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
#      'p', 'q', 'r', 's', 't', 'u',
#      'v', 'x', 'y', 'z']

#     numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#     characters = ['*', '+', '-', '/', '@', '_', '?', '!', '[',
#      '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°',
#       '^', '&', '$', '#', '"']
    
#     caracteres = mayusculas + minusculas + numeros + characters

#     contrasena = []

#     for i in range(15):
#         caracter_random = random.choice(caracteres)
#         contrasena.append(caracter_random)

#         contrasena = "".join(contrasena)
#         return contrasena




# def run():
#     contraseña = generar_contrasena()
#     print('Tu nueva contrasena es:  ' + contraseña)



# if __name__ == '_main_':
#     run()


import random


def generador_id():
    #Generamos datos de entrada para el id aleatorio
    cedula = int(input("Dijita la cedula: "))
    apellido = input("Dijita la Apellido: ")
    nombre = input("Dijita el nombre: ")
    nacionalidad = input("Dijita tu nacionalidad: ")
    fecha_entrada = int(input("Dijista tu fecha entrada MM/DD/AA : "))
    numero_aleatorio = random.randint(1000,9999)

    # Convertimos las variables enteras a string
    cedula = str(cedula)
    fecha_entrada = str(fecha_entrada)
    numero_aleatorio = str(numero_aleatorio)

    #Reducimos los string a sus primero 4 caracteres
    nombre = nombre[:3]
    apellido = apellido[:3]
    nacionalidad = nacionalidad[:3]
    cedula = cedula[:3]    
    fecha_entrada = fecha_entrada[:3]
    

    #Convierto esos 4 caracteres en una lista
    lista_cedula = list(cedula)
    lista_nombre = list(nombre)
    lista_apellido = list(apellido)
    lista_nacionalidad = list(nacionalidad)
    lista_fecha_entrada = list(fecha_entrada)
    lista_numero_aleatorio = list(numero_aleatorio)

    #concatenacion de las listas
    combinacion = lista_nombre + lista_apellido + lista_nacionalidad + lista_cedula + lista_fecha_entrada + lista_numero_aleatorio
    # lista mutable que contendra nuestro id unico (coparen con un contador si quieren entender)
    id_unico = []

    # ciclo que se itera 15 veces escogiendo 1 caracter a la ves y agregandolo a id_unico
    for i in range(15):
        id_random = random.choice(combinacion)
        id_unico.append(id_random)
    #convertimos la lista en un string
    id_unico = "".join(id_unico)
    #regresamos el valor string a la funcion generador_id()
    return id_unico


def run():    
    id_unico = generador_id()
    print ("Tu id unico es: "+ id_unico+"")


if __name__ == "__main__":
    run()