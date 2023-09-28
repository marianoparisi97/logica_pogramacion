#
# * Escribe una función que reciba dos palabras (String) y retorne
# * verdadero o falso (Bool) según sean o no anagramas.
# * - Un Anagrama consiste en formar una palabra reordenando TODAS
# *   las letras de otra palabra inicial.
# * - NO hace falta comprobar que ambas palabras existan.
# * - Dos palabras exactamente iguales no son anagrama.
#

Palabra_uno = input("Ingrese la primer Palabra: ")
palabra_dos = input("Ingrese la segunda Palabra: ")

def anagrama(palabra_uno, palabra_dos):
    #Verificar que las 2 entradas sean str.
    if isinstance(palabra_uno, str) and isinstance(palabra_dos, str):
        #Elimina los espacios en blanco delante y detras de la cadena de texto.
        palabra_uno = palabra_uno.strip()
        palabra_dos = palabra_dos.strip()
    
    if palabra_uno and palabra_dos: #Verifica que sean cadenas no vacias de texto
        if sorted(palabra_uno) == sorted(palabra_dos): #Ordena las palabraas alfabeticamente y las compara
            return True #Si son anagramas devuelve Trues
    return False #si no son anagramas devuelve False


resultado = anagrama(Palabra_uno, palabra_dos)
print(resultado)
