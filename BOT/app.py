from PIL import Image, ImageDraw

def crear_mapa_sismo():
    # Crear una nueva imagen con un tamaño específico (por ejemplo, 500x500 píxeles)
    imagen = Image.new('RGB', (500, 500), color='white')

    # Obtener un objeto ImageDraw para dibujar en la imagen
    dibujo = ImageDraw.Draw(imagen)

    # Dibujar un punto en las coordenadas de longitud y latitud del sismo
    latitud = 12.3456  # Reemplaza con la latitud real del sismo
    longitud = -78.9101  # Reemplaza con la longitud real del sismo
    punto = (int(longitud), int(latitud))  # Convertir las coordenadas a enteros
    dibujo.point(punto, fill='red')

    # Guardar la imagen como "mapa_sismo.png"
    imagen.save('str/mapa_sismo.png')

# Llamar a la función para crear el mapa del sismo
crear_mapa_sismo()