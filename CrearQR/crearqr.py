#Es necesario las librerias de qrcode para funcionar: python -m pip install qrcode pillow en cmd de vscode.
import qrcode

# El enlace web que quieres convertir
data = "Añadir el link o ruta para transformar." 

# Creamos el código QR
img = qrcode.make(data)

# Guardamos la imagen en tu computadora
img.save("Telefonoqr.png")

# Mostramos la imagen en pantalla
img.show()

print("Se ha realizado con éxito.")
