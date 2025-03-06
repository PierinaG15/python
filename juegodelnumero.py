import random

# Elige un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

print("¡Bienvenido al juego de Adivina el Número!")
print("Estoy pensando en un número entre 1 y 10. ¿Puedes adivinar cuál es?")

intentos = 0
adivinado = False

while not adivinado:
    try:
        # Pedir al jugador que introduzca un número
        respuesta = int(input("Introduce tu número (entre 1 y 10): "))
        intentos += 1

        # Verificar si la respuesta está dentro del rango
        if respuesta < 1 or respuesta > 10:
            print("Por favor, introduce un número dentro del rango de 1 a 10.")
            continue

        # Comparar la respuesta con el número secreto
        if respuesta < numero_secreto:
            print("¡Demasiado bajo! Intenta con un número mayor.")
        elif respuesta > numero_secreto:
            print("¡Demasiado alto! Prueba con un número menor.")
        else:
            print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
            adivinado = True
    except ValueError:
        print("Por favor, introduce un número válido.")
