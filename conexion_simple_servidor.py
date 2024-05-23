# Para trabajar con conexiones cliente-servidor usaremos la libreria socket
# Este es un ejemplo se un servidor básico

#Importamos la libreria socket
import socket

# Creamos un objeto socket de tipo TCP/IP
s = socket.socket()

# Obtenemos el nombre del host local y lo ponemos en la variable nombre
nombre = socket.gethostname()
# Establecemos el puerto donde escuchará nuestro servidor
puerto = 12345

# Vinculamos el socket al nombre de host y al puerto especificado.
# Significa que el servidor está a la escucha en la ip de nuestra
# maquina (que es el servidor) en el puerto especificado.
s.bind((nombre, puerto))

# Imprimimos la informacion de nuestro servidor
print('Informacion del servidor: IP: (',nombre,') Puerto: (',puerto,')')

# Ponemos el socket en modo escucha, queda listo para aceptar
# conexiones entrantes.
s.listen()

# Iniciamos un bucle infinito (while) que permitirá al servidor aceptar 
# múltiples conexiones.
while True:

    # Cuando un cliente se conecta c crea un nuevo objeto
    # socket para la conexión con el cliente.
    # addr es la dirección IP y el puerto del cliente
    
    # s.accept() significa que el objeto socket s está 
    # aceptando una conexión entrante y creando un nuevo 
    # objeto socket para manejar esta conexión específica.
    c, addr = s.accept()

    # Imprimimos la dirección del cliente que se ha conectado
    print('Conexión recibida de', addr)

    # Envíamos un mensaje de agradecimiento al cliente. 
    # La b antes de la cadena indica que se envía 
    # como datos binarios.
    c.send(b'Gracias por conectar.')
    c.send(b'Mandame un mensaje.')

    # Cerramos la conexión con el cliente.
    c.close()