
#importar clase Alumno
from Alumno import Alumno
#importar clase faker
from faker import Faker
#crear instancia de faker
fake=Faker()
alumno=Alumno(fake.name(),fake.random_int(1,100))
#imprimir alumno    
#print(alumno)
#print(alumno.esMayorEdad())
# dgenerar lista de 100 alumnos y separar segunsean mayor o menor de edad


# Crear listas para almacenar alumnos mayores y menores de edad
mayores_edad = []
menores_edad = []

# Generar 100 alumnos aleatorios
for _ in range(100):
    nombre = fake.name()  # Generar un nombre aleatorio
    edad = fake.random_int(1, 100)  # Generar una edad aleatoria entre 1 y 100
    alumno = Alumno(nombre, edad)  # Crear una instancia de Alumno
    
    # Separar según la edad
    if alumno.esMayorEdad():
        mayores_edad.append(alumno)
    else:
        menores_edad.append(alumno)

# Imprimir la cantidad de alumnos mayores y menores de edad
print(f"Alumnos mayores de edad: {len(mayores_edad)}")
print(f"Alumnos menores de edad: {len(menores_edad)}")

# Opcional: Imprimir algunos de los alumnos para ver los resultados
print("\nAlumnos mayores de edad (primeros 5):")
for alumno in mayores_edad[:5]:
    print(alumno)

print("\nAlumnos menores de edad (primeros 5):")
for alumno in menores_edad[:5]:
    print(alumno)
    
    #contar nombres repetidos en un diccionario
    



