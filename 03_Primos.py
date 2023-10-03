
# * Escribe un programa que se encargue de comprobar si un número es o no primo.
# * Hecho esto, imprime los números primos entre 1 y 100.

# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Iterar a través de los números del 1 al 100
for num in range(1, 101):
    if es_primo(num):
        print(num, end=" ")  # Imprime los números primos en la misma línea
