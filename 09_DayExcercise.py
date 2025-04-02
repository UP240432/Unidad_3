##DAY_9##

# Solicitar la edad del usuario
age = int(input('Enter your age: '))
if age >= 18:
    print(f'You are old enough to drive')
else:
    print(f'You need {18 - age} years to drive')

# Comparar edades
yourAge = int(input("Enter your age: "))
myAge = 24

if myAge > yourAge:
    print(f"I'm {myAge - yourAge} older than you")
elif myAge < yourAge:
    print(f"You're {yourAge - myAge} older than me")
else:
    print(f'We are of the same age')

# Comparar dos números
n1 = int(input(f"Enter number 1: "))
n2 = int(input(f"Enter number 2: "))

if n1 > n2:
    print(f"{n1} is greater than {n2}")
elif n1 < n2:
    print(f"{n2} is greater than {n1}")
else:
    print(f'The numbers are equal')

# Calcular la calificación basada en la puntuación
score = int(input("Enter your score: "))

if score < 50:
    print(f"Your grade is F")
elif score <= 59:
    print(f"Your grade is D")
elif score <= 69:
    print(f"Your grade is C")
elif score <= 89:
    print(f"Your grade is B")
elif score <= 100:
    print(f"Your grade is A")
else:
    print(f"Score not valid")

# Determinar la estación del año según el mes
month = input("Enter the current month: ").upper()

if month in ["SEPTEMBER", "OCTOBER", "NOVEMBER"]:
    print(f"The current season is Autumn")
elif month in ["DECEMBER", "JANUARY", "FEBRUARY"]:
    print(f"The current season is Winter")
elif month in ["MARCH", "APRIL", "MAY"]:
    print(f"The current season is Spring")
elif month in ["JUNE", "JULY", "AUGUST"]:
    print(f"The current season is Summer")
else:
    print(f"Invalid Data")

# Manejo de frutas
fruits = ['banana', 'orange', 'mango', 'lemon']
newFruit = input("Enter a fruit: ").lower()

if newFruit in fruits:
    print(f"The {newFruit} is already in the list.")
else:
    print(f"Adding the {newFruit}...")
    fruits.append(newFruit)
print(fruits)

# Información de una persona
person = {
    'first_name': 'Patricia',
    'last_name': 'Esparza',
    'age': 22,
    'country': 'Mexico',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'Arduino', 'Python'],
    'address': {
        'street': 'Kozani',
        'zipcode': '20298'
    }
}

# Verificar habilidades
if 'skills' in person.keys():
    mid = int(len(person['skills']) / 2)
    print(person['skills'][mid])
    if "Python" in person['skills']:
        print(f"Python is a skill in the dictionary")
    else:
        print(f"Python is not a skill in the dictionary")
else:
    print(f"'skills' is not in the person")

# Determinar el tipo de desarrollador
fronDev = ['JavaScript', 'React']
backDev = ['Node', 'Python', 'MongoDB']
fullStack = ['React', 'Node', 'MongoDB']

if person['skills'] == fronDev:
    print(f"She's a front-end developer")
elif person['skills'] == backDev:
    print(f"She's a back-end developer")
elif person['skills'] == fullStack:
    print(f"She's a fullstack developer")
else:
    print(f"Unknown title")

# Estado civil
status = "She's married" 
if person['is_married'] 
else "She's not married"
print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. {status}")