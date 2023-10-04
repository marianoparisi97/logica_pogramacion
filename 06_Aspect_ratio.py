"""
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
 *   mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
"""

# # # -------------------------------------------------- # # #

import requests
from PIL import Image
from io import BytesIO

url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

try: # Manejo de errores
    
    #Realiza un GET para solicitar la imagen
    response = requests.get(url)

    #Verificacion si la solicitud fue exitosa mediante codigos HTML
    if response.status_code == 200:
        # Abre la imagen desde los datos binarios descargados utilizando BytesIO
        img = Image.open(BytesIO(response.content))
        # Obtiene las dimensiones de la imagen
        width, height = img.size
        #Muestra el tamaño de la imagen
        print(f"El ancho es {width} y el alto es {height} Pixeles")

        #Calcula el MCD de alto y ancho
        def mcd(a,b):
            if a%b != 0:
                return mcd(b,a%b)
            else:
                return b
        mcd_result = mcd(width, height)
        #print(mcd_result) Imprime el multiplo comun divisor del ancho y alto de la imagen.
        print(f"La relación de aspecto es: {int(width/mcd_result)}:{int(height/mcd_result)}")
    else:
        print("No se pudo descargar la imagen.")


except Exception as e:
    print(f"Ocurrio un error: {str(e)}")


