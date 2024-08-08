### Listas ###

## Un Array y una lista en Python son los mismo

my_list = list()
my_other_list = []

print(len(my_list)) ## Se crean las listas pero estan vacias dado que no tienen ningun valor
print("-" * 30)


my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list)) ## A diferencia de esta, dado que ya tienen valores y posee una longitud diferente
print("-" * 30)

my_other_list = [20, 1.85, "César", "Salas"]
print(type(my_other_list)) ## Las listas pueden tener diferentes datos dato que se toma como una clase tipo list
print("-" * 30)

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list[len(my_other_list) - 1])
print(my_other_list.count("César"))
print(my_list.count(30))
# print(my_other_list[4]) IndexError 
# print(my_other_list[-5]) IndexError
print("-"* 30)

## Desempaquetado de Elementos

age, height, name, surmane = my_other_list
print(age)

print(my_list + my_other_list)
print("-" * 30)

## Agregar y Eliminar elementos a la lista

my_other_list.append("Enrique")
print(my_other_list) ## Agrega el final de la lista

my_other_list.insert(1, "Azul")
print(my_other_list) ## Agrega en una posición de la lista

my_other_list.remove("Azul")
print(my_other_list) ## Elimina el elemento con el nombre Azul

my_other_list.remove(20)
print(my_other_list)

my_other_list.pop 
print(my_other_list) ## Elimnina el ultimo elemento de la lista

my_other_list.reverse()
print(my_other_list) ## Invierte el orden de la lista

my_other_list.sort()
print(my_other_list) ## El sort funciona para ordenar una lista mediante criterios, en caso de estar solo ordena de menor a menor 

del my_other_list[2]
print(my_other_list) ## Elimina de la lista el elemento en la posición 2

my_other_list.clear()
print(my_other_list) ## Vacia la lista por completo