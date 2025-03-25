cadena1 = '30' + ' ' + 'Días' + ' ' + 'De' + ' ' + 'Java'
print(cadena1)  

cadena2 = 'Programación' + ' ' + 'Para' + ' ' + 'Todos'
print(cadena2)  

company = "Programación Para Todos"
print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize()) 
print(company.title()) 
print(company.swapcase()) 

print(company.split()[1:])

print(company.find('Programación')) 

print(company.replace('Programación', 'JavaScript'))

company = company.replace('Programación', 'JavaScript')
print(company)

print(company.split())

cadena = 'Twitter, LinkedIn, Amazon, Facebook, Microsoft, Apple, IBM'
print(cadena.split(', '))

print(company[0])

print(len(company) - 1)

print(company[10])


acronimo1 = ''.join([word[0] for word in 'JavaScript Para Todos'.split()])
print(acronimo1) 

acronimo2 = ''.join([word[0] for word in 'Programación Para Todos'.split()])
print(acronimo2) 

posicion_P = company.find('P')
if posicion_P != -1:
    print(f"La posición de 'P' es: {posicion_P}")
else:
    print("No se encontró la letra 'P' en la cadena.")

posicion_T = company.find('T')
if posicion_T != -1:
    print(f"La posición de 'T' es: {posicion_T}")
else:
    print("No se encontró la letra 'T' en la cadena.")

print(company.rfind('o'))

oracion = 'No se puede terminar una oración con aunque aunque aunque aunque es una conjunción'
print(oracion.find('aunque'))

print(oracion.rindex('aunque'))

inicio = oracion.find('aunque')
fin = oracion.rfind('aunque') + len('aunque')
print(oracion[inicio:fin])

print(company.startswith('Programación'))

print(company.endswith('Todos'))

print(' Programación Para Todos '.strip())

print('30DíasDeJava'.isidentifier()) 
print('cincuenta_días_de_java'.isidentifier())  

bibliotecas = ['Flask', 'Django', 'FastAPI', 'Tornado', 'Pyramid']
print('#'.join(bibliotecas))

print("I am enjoying this journey.\nI just wonder what is next.")

print("\njuan\t25\tspain\tmadrid")

radius = 15
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} square meters.")

print(f"10 + 5 = {10 + 5}")
print(f"10 - 5 = {10 - 5}")
print(f"10 * 5 = {10 * 5}")
print(f"10 / 5 = {10 / 5:.2f}")
print(f"10 % 5 = {10 % 5}")
print(f"10 // 5 = {10 // 5}")
print(f"10 ** 5 = {10 ** 5}")