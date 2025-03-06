# Funciones para las operaciones
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "No se puede dividir por cero"
    else:
        return x / y

# Función principal de la calculadora
def calculadora():
    # Mostrar las opciones
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    # Solicitar la opción
    operacion = input("Ingrese el número de la operación (1/2/3/4): ")

    # Solicitar los números al usuario
    while True:
        try:
             num1 = float(input("Ingrese el primer número: "))
             break
        except ValueError:
             print("Por favor, ingrese un número válido.")
    
    while True:
        try:
            num2 = float(input("Ingrese el segundo número: "))
            break
        except ValueError:
             print("Por favor, ingrese un número válido.")
# Usar match para seleccionar la operación
    match operacion:
        case '1':
            print(f"Resultado: {sumar(num1, num2)}")
        case '2':
            print(f"Resultado: {restar(num1, num2)}")
        case '3':
            print(f"Resultado: {multiplicar(num1, num2)}")
        case '4':
            print(f"Resultado: {dividir(num1, num2)}")
        case _:
            print("Opción no válida.")

# Llamar a la función de la calculadora
calculadora()