# Para trabajar con conexiones cliente-servidor usaremos la libreria socket
# Este es un ejemplo se un cliente básico

#Importamos la libreria socket
import socket

# Creamos un objeto socket de tipo TCP/IP
s = socket.socket()

# Especificamos a que direccion y puerto nos vamos a conectar.
# En este ejemplo usamos nuestro servidor local que hemos creado de ejemplo.
# Como ip le especificamos que obtenga el hostname de la maquina local
# que es donde esta nuestro servidor. Si fuera un servidor externo le especificariamos
# la ip de ese servidor.
ip = socket.gethostname()
puerto = 12345

# Le decimos a nuestro socket que se conecte a la direccion
# configurada en las variables ip y puerto
s.connect((ip, puerto))

# Al conectarse, nuestro servidor manda un mensaje a este cliente.
# Guarda lo que recibe en un objeto socket con la funcion recv
# en bloques de 1024 bytes (s.recv(1024))
# Lo imprimimos en pantalla.
print(f"Información recibida: {s.recv(1024)}")
print(f"Información recibida: {s.recv(1024)}")

# Cerramos la conexión del socket.
s.close()