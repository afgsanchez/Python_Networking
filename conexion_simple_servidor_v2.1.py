# Para trabajar con conexiones cliente-servidor usaremos la libreria socket
# En este ejemplo añadimos una logica en el cliente para que dependiendo de la 
# informacion que introduzca el usuario, el aplicativo cerrará la conexión y 
# cerrará tanto el cliente como el servidor. La informacion que debe introducir para que 
# esto ocurra es el valor 0

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

# Creamos una variable "fin" y la seteamos en False.
# Cuando recibamos el valor 0 desde el cliente, "fin" cambiará
# a True y cerrará la aplicación.
fin = False

# Cuando un cliente se conecta c crea un nuevo objeto
# socket para la conexión con el cliente.
# addr es la dirección IP y el puerto del cliente

# s.accept() significa que el objeto socket s está 
# aceptando una conexión entrante y creando un nuevo 
# objeto socket para manejar esta conexión específica.
c, addr = s.accept()

# Imprimimos la dirección del cliente que se ha conectado
print('Conexión recibida de', addr)

# Creamos el bucle infinito while que se ejecutará mientras que
# en la información recibida no reciba el valor 0.
# Cuando lo reciba, cerrará la conexión y el programa.
while not fin:

    # Guardamos en la variable info los datos recibidos y los decodificamos.
    info = c.recv(1024).decode('utf-8')

    # Imprimimos los datos guardados en la variable info.
    print("Informacion recibida: ", info)

    # Verificamos si en los datos de la variable info está el valor 0
    if info == "0":
        # Si esta el valor 0 seteamos la variable fin a True, lo que
        # terminará el bucle while y el servidor se cerrará.
        fin = True

# Cerramos el objeto socket c
c.close()

# Cerramos el socket s que esta escuchando a la espera de conexiones.
s.close()

# Informamos que se esta cerrando el programa.
print("Cerrando programa...")

