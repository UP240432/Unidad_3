edad = 22
altura = 1.65  # Cambié la altura a un valor diferente
num_comp = 5 + 3j  # Cambié el número complejo
print("Edad:", edad)
print("Altura:", altura)
print("Número complejo:", num_comp)

base = float(input("Introduce la base del triángulo: "))
altura_triangulo = float(input("Introduce la altura del triángulo: "))
area = 0.5 * base * altura_triangulo
print("El área del triángulo es:", area)

import math  
largo = float(input("Introduce el largo del rectángulo: "))
ancho = float(input("Introduce el ancho del rectángulo: "))

area_rectangulo = largo * ancho
perimetro_rectangulo = 2 * (largo + ancho)

print("Área del rectángulo:", area_rectangulo)
print("Perímetro del rectángulo:", perimetro_rectangulo)

radio = float(input("Introduce el radio del círculo: "))

pi = 3.14
area_circulo = pi * radio * radio
circunferencia = 2 * pi * radio

print("Área del círculo:", area_circulo)
print("Circunferencia del círculo:", circunferencia)

pendiente = 3  # Cambié la pendiente
interseccion_x = 3 / 3  
interseccion_y = -3  

print("Pendiente de y = 3x - 3:", pendiente)
print("Intersección con eje X:", interseccion_x)
print("Intersección con eje Y:", interseccion_y)

x1, y1 = 1, 1  # Cambié los puntos
x2, y2 = 5, 7

pendiente_2 = (y2 - y1) / (x2 - x1)
distancia_euclidiana = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Pendiente entre (1,1) y (5,7):", pendiente_2)
print("Distancia euclidiana:", distancia_euclidiana)

print("¿Las pendientes son iguales?", pendiente == pendiente_2)

for x in range(-5, 5):  # Cambié el rango
    y = x**2 + 4*x + 4
    if y == 0:
        print(f"y es 0 cuando x es {x}")

longitud_piton = len("patrón")  # Cambié la palabra
longitud_dragon = len("dragón")

print("¿'patrón' es más largo que 'dragón'?", longitud_piton > longitud_dragon) 

print("'on' está en 'patrón' y 'dragón'?", "on" in "patrón" and "on" in "dragón")

oracion = "Espero que este curso no esté lleno de ejemplos."
print("'ejemplos' está en la oración?", "ejemplos" in oracion)

print("¿'encendido' no está en 'dragón' ni en 'patrón'?", "encendido" not in "dragón" and "encendido" not in "patrón")

longitud_python = len("python")
longitud_float = float(longitud_python)
longitud_string = str(longitud_float)

print("Longitud de 'python' como float:", longitud_float)
print("Longitud de 'python' como string:", longitud_string)

numero = int(input("Introduce un número para verificar si es par: "))
print("¿El número es par?", numero % 2 == 0)

print("¿7 // 3 es igual a int(2.7)?", 7 // 3 == int(2.7))

print("¿El tipo de '10' es igual al tipo de 10?", type("10") == type(10))

try:
    print("¿int('9.8') es igual a 10?", int("9.8") == 10)  
except ValueError:
    print("No se puede convertir '9.8' a entero.")

horas = float(input("Introduce las horas trabajadas: "))
tarifa = float(input("Introduce la tarifa por hora: "))

pago = horas * tarifa

print("El pago total es:", pago)

años = int(input("Introduce el número de años: "))
segundos_por_año = 365 * 24 * 60 * 60
segundos_vividos = años * segundos_por_año

print("Has vivido aproximadamente", segundos_vividos, "segundos.")

años_maximos = 100
segundos_maximos = an