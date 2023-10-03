"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""


def multiply_areas(tr_width, tr_height, sq_width, sq_height, rect_width, rect_height):

    tr_area = (tr_width * tr_height) / 2
    sq_area = sq_width * sq_height
    rect_area = rect_width * rect_height

    return tr_area, sq_area, rect_area

triangle_width = float(input("Ingrese la base del triangulo (en mm): "))
triangule_height = float(input("Ingrese la altura del triangulo (en mm): "))

square_width = float(input("Ingrese la base del cuadrado (en mm): "))
square_heigth = float(input("Ingrese la altura del cuadrado (en mm): "))

rectangle_width = float(input("Ingrese la base del rectangulo (en mm): "))
rectangle_height = float(input("Ingrese la altura del rectangulo (en mm): "))

tr_area, sq_area, rect_area = multiply_areas(triangle_width, triangule_height, square_width, square_heigth, rectangle_width, rectangle_height)

print("El area del triangulo es ", tr_area, "mm²")
print("El area del cuadrado es ", sq_area, "mm²")
print("El area del rectangulo es ", rect_area, "mm²")