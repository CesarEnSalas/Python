### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"César", "Apellido":"Salas", "Edad":20, 1:"Python"}

my_dict = {"Nombre":"César", 
           "Apellido":"Salas", 
           "Edad":20, 
           "Lenguajes": {"Python", "Java", "JavaScript"},
           1:1.85
          }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle Cesar"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("César" in my_dict)
print("Nombre"in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "César")
print((my_new_dict))

print(my_new_dict.values())
print(dict.fromkeys(list(my_new_dict.values())))
print(tuple(my_new_dict))
print(set(my_new_dict))