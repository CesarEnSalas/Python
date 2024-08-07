# Variables

first_name = 'Cesar'
last_name = "Enrique"

variable = "Hola Mundo"
print(variable)

numero = 42
my_int_to_str_variable = str(numero)
print(numero)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

print('-' * 30)

# Concatenación de variables en un print 
print(variable, first_name, last_name, numero, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

print('-' * 30)

# Longitud de la cadena (len)
print(len(variable))

print('-' * 30)

# Variables en una sola linea. ¿Cuidado con abusar de esta sintaxis?
name, surname, age = "Cesar Enrique", "Salas Pierre", 20

print("Me llamo:", name, surname, ".Mi edad es:", age)

"""
# Inputs
first_name = input("¿Como te llamas? ")
age = input("¿Cuantos años tienes? ")

print(first_name)
print(age)
"""

print('-' * 30)

# Forzamos el tipo
address: str = "Mi direccion"
address = 32
print(address)


