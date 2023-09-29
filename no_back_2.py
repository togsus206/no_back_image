import sys
import readline
from rembg import remove
from PIL import Image

def input_with_correction(prompt):
    try:
        readline.set_startup_hook(lambda: readline.insert_text(""))
        user_input = input(prompt)
        return user_input
    finally:
        readline.set_startup_hook()

if __name__ == "__main__":
        try:
            image_source = input_with_correction("Path de la imagen a convertir o salir: ")

            if image_source.lower() == "salir":
                sys.exit(1)

            output_source = "sin_fondo.png"

            input_image = Image.open(image_source)
            output_image = remove(input_image)
            output_image.save(output_source)
            print("Imagen convertida y guardada como sin_fondo.png")
            

        except Exception as e:
            print("Hubo un problema con la imagen:", str(e))

