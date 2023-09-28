#Ejercicio: Calculadora de Factorial

#Escribe un programa en Python que calcule el factorial de un número entero no negativo ingresado por el usuario. El factorial de un número entero positivo "n" se calcula multiplicando todos los enteros desde 1 hasta "n". Por ejemplo, el factorial de 5 (denotado como 5!) es igual a 5 x 4 x 3 x 2 x 1 = 120.
#Pasos a seguir:
    #Solicita al usuario que ingrese un número entero no negativo.
    #Verifica si el número ingresado es válido (no negativo).
    #Si el número es válido, calcula su factorial.
    #Imprime el resultado.
    #Si el número no es válido, muestra un mensaje de error y solicita nuevamente al usuario que ingrese un número válido.

resultado = 1

while True:
    numero = (input("Ingrese un numero entero mayor a 0:"))
    if numero.isdigit(): #Verifica que la respuesta contenga solo numeros.
        numero = int(numero) #Convierte el str de la respuesta en un entero
        if numero >= 0:
            break #Sale del bucle si el numero es valido
    
    print("Entrada no valida. Ingrese un numero entero mayor a 0:")

for i in range(1, numero +1):
    resultado *= i

print(f"el factorial del {numero} es {resultado}")