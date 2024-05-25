# Para trabajar con conexiones cliente-servidor usaremos la libreria socket
# En este ejemplo vamos a usar hilos (threads) para aceptar la conexion de multiples clientes

# Importamos la libreria socket
import socket
# Importamos la libreria threading para crear hilos
import threading

# Creamos una funcion para manejar los hilos
# solicitamos como parametros la conexion y la direccion del cliente
def HiloCliente(conexion, direccion):
    # Enviamos un mensaje de bienvenida al cliente
    conexion.send(str.encode("Bienvenido al servidor de MindTask!"))

    while True:
        # Recibimos datos del cliente
        recibido = conexion.recv(1024)

        # Imprimimos la dirección del cliente y el mensaje recibido
        print(direccion, "=", recibido.decode('utf-8'))

        # Preparamos la respuesta del servidor
        respuesta = "MindTask: Mensaje recibido: " + recibido.decode('utf-8')

        # Si no se recibe ningún dato, salimos del bucle
        if not recibido:
            break

        # Enviamos la respuesta al cliente
        conexion.send(str.encode(respuesta))

    # Cerramos la conexión con el cliente
    conexion.close()

# Creamos el socket para el servidor.
SocketServidor = socket.socket()
# Obtenemos el nombre del host local y lo ponemos en la variable host
host = socket.gethostname()
# Establecemos el puerto donde escuchará nuestro servidor
puerto = 30000

# Usando bind configuramos el socket con el host y el puerto dado en los parametros dados 
SocketServidor.bind((host, puerto))

# Imprimimos un mensaje indicando que estamos listos para recibir conexiones
print("Esperando conexiones...")

# Ponemos el socket del servidor a la escucha
SocketServidor.listen()

while True:
    # Aceptamos una nueva conexión de un cliente
    cliente, direccion = SocketServidor.accept()

    # Imprimimos la dirección del nuevo cliente
    print("Nuevo cliente: " + direccion[0] + "." + str(direccion[1]))

    # Creamos un nuevo hilo para manejar la conexión con el cliente
    hilo = threading.Thread(target=HiloCliente, args=(cliente, direccion[0] + "." + str(direccion[1]),))

    # Iniciamos el hilo
    hilo.start()

# Cerramos el socket del servidor (nunca se alcanzará en este bucle infinito)
SocketServidor.close()
