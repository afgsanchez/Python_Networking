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
# Luego lo imprimimos en pantalla.
datos_recibidos = s.recv(1204)

# Decodificamos los bytes recibidos a una cadena de texto usando UTF-8
datos_recibidos = datos_recibidos.decode('utf-8')

# Dividimos los datos recibidos en mensajes individuales usando el delimitador "\n"
mensajes = datos_recibidos.split("\n")

# Imprimimos cada mensaje recibido
for datos in mensajes:
    print(f"Información recibida: {datos}")

# Preparamos un mensaje de despedida para enviar al servidor
info = "Ya me desconecto, un placer."
# Codificamos el mensaje a bytes usando UTF-8
bytes_info = info.encode('utf-8')

# Imprimimos el mensaje que será enviado
print("Informacion enviada: ", info)

# Enviamos los bytes del mensaje codificado al servidor
s.send(bytes_info)

# Recibimos la respuesta del servidor, la decodificamos y la imprimimos
print("informacion recibida" , s.recv(1024).decode('utf-8'))


# Cerramos la conexión del socket.
s.close()