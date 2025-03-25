
#Day 6
# Excersise 1
# Declare a tuple with three values of your choice.

my_tuple = ('one', 'two', 'three')
print(my_tuple)

# Excersise 2
# Assign the first value to a variable name, the second value to a variable age and the third value to a variable address.

name, age, address = my_tuple
print(name)
print(age)
print(address)

# Excersise 3

# Declare a tuple with different data types: 'a', 1, 2.0

my_tuple = ('a', 1, 2.0)
print(my_tuple)

# Excersise 4
# Find the length of your tuple

print(len(my_tuple))

# Excersise 5
# Get the first item in the tuple

print(my_tuple[0])

# Excersise 6
# Get the second item in the tuple

print(my_tuple[1])

# Excersise 7
# Get the last item in the tuple

print(my_tuple[-1])

# Excersise 8
# Use slicing to get the first two items in the tuple

print(my_tuple[0:2])

# Excersise 9
# Use slicing to get the last two items in the tuple

print(my_tuple[1:])

# Excersise 10
# Use slicing to get the middle item in the tuple

print(my_tuple[1])

# Excersise 11
# Delete the first item in the tuple

my_tuple = my_tuple[1:]
print(my_tuple)

# Excersise 12
# Delete the last item in the tuple

my_tuple = my_tuple[:-1]
print(my_tuple)

# Excersise 13
# Delete the middle item in the tuple

my_tuple = my_tuple[0:1] + my_tuple[2:]
print(my_tuple)

# Excersise 14
# Delete the whole tuple

del my_tuple
print(my_tuple) # This will raise an error because the tuple has been deleted



perro = {}

perro['nombre'] = 'Toto'
perro['color'] = 'Negro'
perro['raza'] = 'Chihuahua'
perro['patas'] = 4
perro['edad'] = 1

print("Diccionario perro:", perro)

estudiante = {
    'nombre': 'Jesus',
    'apellido': 'Esparza',
    'género': 'Masculino',
    'edad': 23,
    'estado_civil': 'Soltero',
    'habilidades': ['Python', 'Aleman','Ingles'],
    'país': 'Mexico',
    'ciudad': 'Aguacalientes',
    'dirección': 'Kozani #111, Paseos del Sur'
}
longitud_estudiante = len(estudiante)
print("Longitud del diccionario estudiante:", longitud_estudiante)

tipo_habilidades = type(estudiante['habilidades'])
print("Tipo de dato de habilidades:", tipo_habilidades)

estudiante['habilidades'].append('Análisis de Datos')
estudiante['habilidades'].append('Machine Learning')
print("Habilidades actualizadas:", estudiante['habilidades'])

claves_estudiante = list(estudiante.keys())
print("Claves del diccionario estudiante:", claves_estudiante)

valores_estudiante = list(estudiante.values())
print("Valores del diccionario estudiante:", valores_estudiante)

tuplas_estudiante = list(estudiante.items())
print("Diccionario como lista de tuplas:", tuplas_estudiante)

estudiante.pop('estado_civil')
print("Diccionario estudiante después de eliminar estado civil:", estudiante)

del perro
print("Diccionario perro eliminado.")



# Level 1
# 1
age = int(input('Enter age: '))
if age >= 18:
    print("You are old enough to drive.")
else:
    print("You need to wait", 18 - age, "years.")

# 2
my_age = 22

if age == my_age:
    print("We are the same age")
elif age > my_age:
    print("You are", age - my_age, "years older than me")
else:
    print("I am", my_age - age, "years older than you")

# 3
a = int(input("Enter number: "))
b = int(input("Enter number: "))
if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is lesser than", b)
else:
    print("Both numbers are equal")

# Level 2
# 1
score = int(input("Enter score: "))

grades = {}
for i in range(90, 101):
    grades[i] = 'A'
for i in range(70, 90):
    grades[i] = 'B'
for i in range(60, 70):
    grades[i] = 'C'
for i in range(50, 60):
    grades[i] = 'D'
for i in range(0, 50):
    grades[i] = 'F'

print("Grade:", grades[score])

# 2
month = input('Enter month: ').title()
if month in ["September", "October", "November"]:
    print("Autumn")
if month in ["December", "January", "February"]:
    print("Winter")
if month in ["March", "April", "May"]:
    print("Spring")

else: print("Summer")

# 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter fruit: ')
print('That fruit already exists in the list' if fruit in fruits else fruits.append(fruit))
print(fruits)

# Level 3
person = {
    'first_name': 'Samuel',
    'last_name': 'Zermeño',
    'age': 21,
    'country': 'Mexico',
    'is_marred': False,
    'skills': ['Play Guitar', 'Create Videos', 'Run', 'sing', 'Python'],
    'address': {
        'street': 'Calle 21',
        'zipcode': '20298'
    }
}

if person['skills']:
    print(person['skills'][len(person['skills']) // 2])
    print("Python" in person['skills'])
    if ['Javascript', 'React'] == person['skills']:
        print('Front End Developer')
    elif ['Node', 'MongoDB', 'React'] == person['skills']:
        print('Full Stack Developer')
    else:
        print("Unknown Title")

if person['is_marred']:
    print(person['first_name'], person['last_name'], "lives in", person['country'], ". He is married")
else:
    print(person['first_name'], person['last_name'], "lives in", person['country'], ". He is not married")