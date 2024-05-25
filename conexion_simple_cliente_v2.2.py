# Para trabajar con conexiones cliente-servidor usaremos la libreria socket

# Este ejemplo es un servidor simple, solo para probar que el servidor v2.2
# puede aceptar multiples conexiones.
# Ejecutaremos este cliente varias veces para ver como el servidor acepta las conexiones.

import socket

# Preparamos el SocketCliente
SocketCliente = socket.socket()
# Obtenemos el nombre del host local y lo ponemos en la variable host
host = socket.gethostname()
# Establecemos el puerto donde nos conectaremos al servidor
puerto = 30000

# Le decimos al socket que conecte al host y puerto indicados en la configuracion al Socket
SocketCliente.connect((host, puerto))

# Capturamos la respuesta del servidor a donde nos conectamos en la variable respuesta
respuesta = SocketCliente.recv(1024)

# Imprimimos la respuesta
# print("Respuesta recibida: ", respuesta.decode('utf-8'))
print(f"Respuesta recibida: {respuesta.decode('utf-8')}")

# Creamos un bucle que enviará al servidor lo que vayamos escribiendo en el cliente.
# Capturamos la entrada del usuario en una variable con un input
while True:
    # Solicitamos al usuario que ingrese un mensaje
    Input = input("Mensaje: ")
    # Codificamos el mensaje a formato utf-8
    Input = Input.encode('utf-8')
    # Enviamos el mensaje al servidor
    SocketCliente.send(Input)

    # Recibimos la respuesta del servidor
    respuesta = SocketCliente.recv(1024)
    # Imprimimos la respuesta del servidor
    print(respuesta.decode('utf-8'))

# Cerramos el socket del cliente (nunca se alcanzará en este bucle infinito)
SocketCliente.close()

