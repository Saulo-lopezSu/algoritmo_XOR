#mensaje = input("Ingrese su mensaje: ")
#binario = ""

# Recorremos cada carácter del mensaje
#for letra in mensaje:
    # Obtenemos el valor ASCII del carácter
 #   ascii_code = ord(letra)
    
    # Convertimos el valor ASCII a su representación binaria y lo agregamos al resultado final
  #  binario += bin(ascii_code)[2:].zfill(8) + " "

# Eliminamos el último espacio que se agregó de más
#binario = binario[:-1]

#print("El mensaje en binario es:", binario)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-------version_2------------
#mensaje = input("Ingrese su mensaje: ")
#clave = input("Ingrese una clave: ")
#binario_mensaje = ""
#binario_clave = ""

# Convertimos la clave a su representación binaria y la agregamos al resultado final
#binario_clave += "".join(format(ord(letra), '08b') for letra in clave) + " "

# Recorremos cada carácter del mensaje
#for letra in mensaje:
    # Obtenemos el valor ASCII del carácter
 #   ascii_code = ord(letra)
    
    # Convertimos el valor ASCII a su representación binaria y lo agregamos al resultado final
  #  binario_mensaje += bin(ascii_code)[2:].zfill(8) + " "

# Eliminamos el último espacio que se agregó de más en el mensaje
#binario_mensaje = binario_mensaje[:-1]

#print("El mensaje en binario es:", binario_mensaje)
#print("La clave en binario es:", binario_clave)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-------version_3------------------------------------
#mensaje = input("Ingrese su mensaje: ")
#clave = input("Ingrese una clave: ")
#binario_mensaje = ""
#binario_clave = ""

# Convertimos la clave a su representación binaria y la agregamos al resultado final
#binario_clave += " ".join(format(ord(letra), '08b') for letra in clave)

# Recorremos cada carácter del mensaje
#for letra in mensaje:
    # Obtenemos el valor ASCII del carácter
 #   ascii_code = ord(letra)
    
    # Convertimos el valor ASCII a su representación binaria y lo agregamos al resultado final
  #  binario_mensaje += bin(ascii_code)[2:].zfill(8) + " "

#print("Mensaje en binario: ", binario_mensaje)

# Eliminamos el último espacio en blanco agregado al final del mensaje en binario
#binario_mensaje = binario_mensaje.rstrip()

# Eliminamos los espacios en blanco de la clave
#binario_clave = binario_clave.replace(" ", "")

#print("Clave en binario: ", binario_clave)

# Inicializamos la variable donde almacenaremos el resultado de la operación XOR
#resultado_xor = ""

# Recorremos los bloques de 8 dígitos binarios del mensaje y realizamos la operación XOR con la clave
#for i in range(0, len(binario_mensaje), 9):
 #   bloque_mensaje = binario_mensaje[i:i+8]
  #  bloque_xor = ""
    
   # for j in range(len(bloque_mensaje)):
        # Realizamos la operación XOR bit a bit entre los dígitos binarios del bloque de mensaje y los de la clave
    #    bit_xor = int(bloque_mensaje[j]) ^ int(binario_clave[j])
     #   bloque_xor += str(bit_xor)
    
    # Agregamos el resultado de la operación XOR al resultado final
    #resultado_xor += bloque_xor + " "

#print("Resultado de la operación XOR: ", resultado_xor)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#------Versión_4------------------------------------------
mensaje = input("Ingrese su mensaje: ")
clave = input("Ingrese una clave: ")
binario_mensaje = ""
binario_clave = ""

# Convertimos la clave a su representación binaria y la agregamos al resultado final
binario_clave += " ".join(format(ord(letra), '08b') for letra in clave)

# Recorremos cada carácter del mensaje
for letra in mensaje:
    # Obtenemos el valor ASCII del carácter
    ascii_code = ord(letra)
    
    # Convertimos el valor ASCII a su representación binaria y lo agregamos al resultado final
    binario_mensaje += bin(ascii_code)[2:].zfill(8) + " "

print("Mensaje en binario: ", binario_mensaje)

# Eliminamos el último espacio en blanco agregado al final del mensaje en binario
binario_mensaje = binario_mensaje.rstrip()

# Eliminamos los espacios en blanco de la clave
binario_clave = binario_clave.replace(" ", "")

print("Clave en binario: ", binario_clave)

# Inicializamos la variable donde almacenaremos el resultado de la operación XOR
resultado_xor = ""

# Recorremos los bloques de 8 dígitos binarios del mensaje y realizamos la operación XOR con la clave
for i in range(0, len(binario_mensaje), 9):
    bloque_mensaje = binario_mensaje[i:i+8]
    bloque_xor = ""
    
    for j in range(len(bloque_mensaje)):
        # Realizamos la operación XOR bit a bit entre los dígitos binarios del bloque de mensaje y los de la clave
        bit_xor = int(bloque_mensaje[j]) ^ int(binario_clave[j])
        bloque_xor += str(bit_xor)
    
    # Agregamos el resultado de la operación XOR al resultado final
    resultado_xor += bloque_xor + " "

print("Resultado de la operación XOR: ", resultado_xor)

# Dividimos el resultado de la operación XOR en bloques de 8 bits y convertimos cada bloque a su correspondiente caracter ASCII
resultado_final = ""

for i in range(0, len(resultado_xor), 9):
    bloque_xor = resultado_xor[i:i+8]
    resultado_final += chr(int(bloque_xor, 2))

print("Resultado final en ASCII: ", resultado_final)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
