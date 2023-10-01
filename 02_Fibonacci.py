# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en
#   la que el siguiente siempre es la suma de los dos anteriores.
#   0, 1, 1, 2, 3, 5, 8, 13...


""" /// ESTE CODIGO ITERA 50 VECES LA SUCESION DE FIBONACCI Y NO HASTA EL NUMERO 50

num1, num2 = 0, 1

fibonacci = 0

while fibonacci < 50:

    suma_fibo = num1 + num2
    print(suma_fibo)

    num1, num2 = num2, suma_fibo #Actualiza las primeras variables con el valor actual de Fibonacci

    fibonacci += 1

"""
### CODIGO DONDE ITERA HASTA EL NUMERO 50 O EL VALOR QUE SE PONGA EN EL WHILE

num1, num2 = 0, 1

while num1 <= 50:
    # Imprime el numero actual (end=" ") Hace que este todo en una misma linea
    print(num1, end=" ")
    
    # Calcular el siguiente número de Fibonacci
    siguiente_numero = num1 + num2
    
    # Actualizar los números anteriores
    num1, num2 = num2, siguiente_numero
