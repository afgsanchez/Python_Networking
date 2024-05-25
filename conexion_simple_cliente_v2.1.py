# Para trabajar con conexiones cliente-servidor usaremos la libreria socket

# En este ejemplo añadimos una logica en el cliente para que dependiendo de la 
# informacion que introduzca el usuario, el aplicativo cerrará la conexión y 
# cerrará tanto el cliente como el servidor. La informacion que debe introducir para que 
# esto ocurra es el valor 0

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

# Creamos una variable "fin" y la seteamos en False.
# Cuando enviemos el valor 0 al servidor, "fin" cambiará
# a True y cerrará la aplicación.
fin = False

# Creamos el bucle infinito while que se ejecutará mientras que
# en la información enviada no sea el valor 0.
# Cuando envie el valor 0, cerrará la conexión y el programa.
while not fin:

    # Lo que vamos a mandar lo recibiremos e un input que el usuario nos pasará.
    # Lo guardaremos en una variable llamada info y lo codificaremos a utf-8 para poder mandarlo.
    # info = bytes(input("Introduce un entero, si pones 0 se cerrará el aplicativo: "), 'utf-8')
    info = input("Introduce un entero, si pones 0 se cerrará el aplicativo: ").encode('utf-8')

    # le decimos al socket s que mande el contenido de la variable info:
    s.send(info)

    # Verificamos si en los datos de la variable info está el valor 0
    # Recuerda que tenemos los datos codificados así que tenemos que
    # decodificar para poder leer la variable info
    if info.decode('utf-8') == "0":
    # Si esta el valor 0 seteamos la variable fin a True, lo que
    # terminará el bucle while y el servidor se cerrará.
        fin = True

    # Cerramos el socket s.
s.close()

# Informamos que se esta cerrando el programa.
print("Cerrando programa...")

