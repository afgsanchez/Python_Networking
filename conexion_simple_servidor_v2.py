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
    # Para ello tenemos que codificar el envío en una secuencia de bytes

    # Define una cadena de texto mensaje que contiene varios mensajes separados por saltos de línea (\n).
    mensaje = "Gracias por conectar. \nEsto es un texto de prueba. \nA ver que pasa."
    # Convertimos la cadena mensaje en una secuencia de bytes utilizando la codificación UTF-8.
    mensaje_bytes = mensaje.encode('utf8')
    # Enviamos los bytes codificados a través del socket c.
    c.send(mensaje_bytes)

    # Esta línea recibe hasta 1024 bytes de datos desde el socket c, los imprime en la consola
    # y decodifica los bytes a una cadena antes de imprimirlos.
    print("Informacion recibida: ", c.recv(1024).decode('utf-8'))
    # Definimos una cadena de texto info con el mensaje "El gusto es mío.".
    info = "El gusto es mío."
    # Convertimos la cadena info en una secuencia de bytes utilizando la codificación UTF-8.
    bytes_info = info.encode('utf-8')

    # Imprime en la consola la información que será enviada.
    print("Informacion enviada: ", info)
    # Enviamos los bytes codificados a través del socket c.
    c.send(bytes_info)

    #Cierra la conexión del socket c.
    c.close()
