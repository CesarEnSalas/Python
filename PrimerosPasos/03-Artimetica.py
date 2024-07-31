# Aritmetica con numeros
print(5 + 15)
print(5 - 15)
print(5 * 15)
print(15 / 5)
print(5**3)
print(10 % 3)
print(100 // 20)
print('-' * 30)

# Operadores Aritmeticos
"""
Solamente se puede utilizar el signo +, 
dado que este simbolo junta las cadenas
"""
print("Hola" + "Python" + "¿Qué tal?")


"""
Para juntar cadenas con elementos 
de diferente tipo es necesario reconbertirlos 
en el tipo con el que se van a juntar
"""
print("Hola " + str(5))

"""
Repetir un texto cierta cantidad de veces
"""
print("Hola " * 5)
print("Hola " * (2**3))
print('-' * 30)

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print('-' * 30)

### Operadores Comparativos Con Strings ###

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")
print("Hola" == "Bola")
print("Hola" >= "Zola")  # Ordenación Alfabetica
print('-' * 30)

### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 == 4 or "Hola" <= "Python")
print(3 >= 4 and "Hola" <= "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4)) # El not sirve para negar la comparación booleana