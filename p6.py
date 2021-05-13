#Imports

import math
from decimal import *


#Práctica 6 - RSA por bloques
#Datos iniciales (modificar)

alf = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ0123456789 ,.:!-¿?()"
msj = "wVBñú94wAU9gaÓc66:YCúVIwAlk)U9ULBMQ)-7caóNS8nvB08h 8úÍtÑJ)¿sYqLBÁ4duCsfkóx)aKE9(3:Hf(¿NmoGñ!DABBÑ6eÑrGUPábCñtdawqbíVWPbéecJÑM)LAc¿2ywRrñrth,896u6on?7b5J81v(LFTÉóN?sNB!ñr,:b877da4ñ4??8hdG "



#Susituir los \n por doble espacio
msj = msj.replace('\\r\\n', '  ')
msj = msj.replace('\\n', '  ')
msj = msj.replace('\\\\n', '  ') 

#Clave publica
n = 743330222539755158153
e = 80263681

#p y q para el descifrado (clave privada)
p = 27264083009
q = 27264083017


N = len(alf) #Simbolos del alfabeto
k = math.floor(math.log(n, N)) #Longitud del bloque
getcontext().prec = 50

#Funciones
def obtenerMensaje(c, N):
    msj_final =""

    cociente = 0
    resto = 0

    bucle = True

    while(bucle):

        cociente = math.floor(Decimal(c)/Decimal(N))
        resto = c%N
        lolxd = alf[resto]
        if(cociente < N):
            bucle = False
        else:
            msj_final = msj_final + alf[resto]
            c = cociente

    msj_final = msj_final + alf[resto] + alf[cociente]

    return msj_final[::-1]

def obtenerEntero(msg, k):
    num = 0
    for i in range(k):
        num = num + (alf.index( msg[i] ) * pow(N, k-(i+1)))
    return num


#Descifrado

#Bloques de longitud k+1
bloques = [msj[i:i+(k+1)] for i in range(0, len(msj), (k+1))]
msj_final = ""

#Calculo la clave privada
phi = (p-1) * (q-1) 
d = pow(e, -1, phi)

#Descifro cada bloque de longitud k+1
for i in range(len(bloques)):
    c = obtenerEntero(bloques[i], len(bloques[i])) #Entero a descifrar


    #Descifro con RSA simple la c
    m = pow(c, d, n) #Entero descifrado

    msj_final_bloque = obtenerMensaje(m, N)
    msj_final = msj_final + msj_final_bloque

#Resultados
print(*msj_final.split("  "), sep="\n")