def piramide_invertida(filas):
    for i in range(filas, 0, -1):
        print('*' * i)
        #llamar a la función con el número de filas deseado
filas=int(input("Ingrese una piramide invertida: "))
piramide_invertida(filas)