### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionarios

my_other_set = {"César", "Salas", 20}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Enrique")
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("Salas") # Un set no admite repetidos
print(my_other_set)

print("Salas" in my_other_set)
print("Salazar" in my_other_set)

my_other_set.remove("César")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) # NameError: name 'my_other_set' is not defined

my_set = {"Salas", "César", 20}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Java", "MYSQL", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_set))