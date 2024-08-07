### Strings ###

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String \ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)

my_new_scape_string = "\\t Este es un String \\n escapado"
print(my_new_scape_string)

# \n: New line / Nueva linea
# \t: Tab means (8 lineas) / Sangria de 8 lineas
# \\: Back slash / Representa un backslash literal
# \': Single quote  (') / Representa una comilla simple
# \": Double quote (") / Representa una comilla doble

print('-' * 30)

# Formateo

# %s - String (or any object with string representation, like numbers)
# %d - Integers
# %f - Floating point Numbers
# "%.number of digitsf" - Floating point numbers with fixed precision 

name, surmane, age = "Cesar", "Salas", 20

print("Mi nombre es %s %s y mi edad es %d" %(name, surmane, age)) 
# or
my_data = "Mi nombre es %s %s y mi edad es %d" %(name, surmane, age)
# or .format
my_data = "Mi nombre es {} {} y mi edad es {}" .format(name, surmane, age)
# or
my_data = f"Mi nombre es {name} {surmane} y mi edad es {age}"
print(my_data)
# Todas las líneas imprime Mi nombre es Cesar Salas y mi edad es 20

print('-' * 30)

# Strings  and numbers

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

print('-' * 30)

# Interpolación de Datos

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

print('-' * 30)

# Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print(language[1])
print(language[5])

print('-' * 30)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

print('-' * 30)

# División con saltos

new_language = "ynonPth"
language_slice = new_language[0:6:2]
print(language_slice)

print('-' * 30)

# Reverse

reverse_language = language[:: -1]
print(reverse_language)
print("-" * 30)

# Funciones

print(new_language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.find("t"))
print(language.upper().isupper())
print(language.lower().isupper())
print(language.replace("y", "i"))
print(language.startswith("Py"))
