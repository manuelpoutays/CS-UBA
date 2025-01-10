import math
#pruebas
def prueba ():
    if False:
        print("1")
    elif True:
        print("2")
    elif True:
        print("3")
#estas las hizo el profe
def es_multiplo_de(n:int,m:int)->bool: 
    res:bool = (n%m)==0 #mod n m = 0
    return res
def es_nombre_largo(nombre:str)->bool:
    res : bool = 3<=len(nombre) and len(nombre)<=8
    return res

def devolver_el_doble_si_es_par(n):
    if es_multiplo_de(n,2):
        res : int = 2*n
    else: res: int = n
    return res
    
def imprimir_pares():
    i : int = 10 
    while i <= 40:
        print (i)
        i=i+2

def imprimir_pares2():
    i : int = 10 
    while i <= 40:
        if es_multiplo_de(i,2):
            print (i)
        i=i+2

def imprimir_pares_for():
    for i in range (10,41,2):
        print(i)


def factorial(n:int) ->int:#ejemplo del profe
    res: int = 1
    for i in range (1,n+1):
        res = res * i
    return res

def factorial_w(n:int) -> int: #otro ejemplo del profe pero cnn while en lugar de for
    res:int = 1 
    i:int = n-1
    while i>0:
        res=res*i
        i=i-1
    return res

def es_multiplo_de(n:int,m:int)->bool:
    res:bool = (n%m)==0 #mod n m = 0
    return res
def es_nombre_largo(nombre:str)->bool:
    res : bool = 3<=len(nombre) and len(nombre)<=8
    return res

def devolver_el_doble_si_es_par(n):
    if es_multiplo_de(n,2):
        res : int = 2*n
    else: res: int = n
    return res
    
def imprimir_pares():
    i : int = 10 
    while i <= 40:
        print (i)
        i=i+2

def imprimir_pares2():
    i : int = 10 
    while i <= 40:
        if es_multiplo_de(i,2):
            print (i)
        i=i+2

def imprimir_pares_for():
    for i in range (10,41,2):
        print(i)

#A partir de acá hice yo

#Ejercicio1
def imprimir_hola_mundo():
    print("Hola Mundo!")

def salto_de_linea (): 
    print ("Hola \nhola 2")

def raiz_de_2()->float:
    res:float = (round(math.sqrt(2),4))
    return res

#tendria que indicar el tipo de cada funcion

def perimetro () ->float:
    res:float = 2*math.pi
    return res

#Ejercicio 2

def imprimir_saludo(nombre:str): #otras formas de concatenar strings en https://j2logo.com/como-concatenar-y-formatear-strings/
    print("Hola " + nombre)

def raiz_cuadrada_de(numero): #uso de libreria
    res = math.sqrt(numero)
    return res

def fahrenheit_a_celsius(temp_far:float)->float:
    res=(((temp_far-32)*5)/9)
    return res

def imprimir_dos_veces(estribillo:str)->str: #Multiplicacion de str
    res = estribillo*2
    return res

def es_multiplo_de_mia(n:int,m:int)->bool: #Uso de crear una variable bool con una condicion booleana
    res:bool = n%m ==0
    return res

def es_par(numero:int)->bool: 
    res:bool = es_multiplo_de(numero,2)
    return res

def cantidad_de_pizzas(comensales:int,min_cant_de_porciones:int): #math.ceil redondea al entero cercano mas alto
    porcionesNecesarias:int=comensales*min_cant_de_porciones
    res:int = math.ceil(porcionesNecesarias/8) 
    return res

#Ejercicio 3
#Usos de operadores logicos
def alguno_es_o(numero1:float,numero2:float)->bool:
    res:bool=numero1==0 or numero2==0
    return res

def ambos_son_0(numero1:float,numero2:float)->bool:
    res:bool=numero1==0 and numero2==0
    return res

def es_nombre_largo2(nombre:str)->bool:
    res:bool = len(nombre)>=3 and len(nombre)<=8
    return res

def es_bisiesto(anio:int)->bool:
    res:bool= anio%400==0 or (anio%4==0 and not(anio%100==0))
    return res

#Ejercicio 4
def peso_pino(pino:float)->float:
    if pino<3:
        res:float=pino*300
        return res
    else:
        res:float=900+200*(pino-3)
        return res

def es_peso_util(peso:int)->bool:
    return peso>=400 and peso <= 1000


def sirve_pino(pino:float)->bool:
    return es_peso_util(peso_pino(pino))

"""No use min y max, la forma de usarlo que paso un companero por el grupo es
    def peso_pino(altura: int) -> int:
        altura_cm: int = altura * 100
        peso_hasta_300 = min(900, altura_cm * 3)
        peso_mayor_300 = (altura_cm - 300) * 2
        peso_estimado = peso_hasta_300 + max(0, peso_mayor_300)
        return peso_estimado
    Muy creativo
"""
#Ejericio 5
#uso de if
def devolver_el_doble_si_es_par(numero):
    if numero%2==0:
        return numero*2
    else:
        return numero
    
"""se puede tambien escribir el if con una condicion ternaria, con la siguiente estructura
    valor = valor_si_es_verdadero if condicion else valor_si_es_falso
    ejemplo en la funcion de abajo
"""
def devolver_el_doble_si_es_par_hecho_por_un_companiero(numero: int) -> int: 
    return numero * 2 if numero % 2 == 0 else numero
"""otro ejemplo 
    calificacion = "Aprobado" if puntuacion >= 60 else "Reprobado"
    print(calificacion)
"""
def devolver_valor_si_es_par_sino_el_que_sigue(numero):
    return numero if numero%2 == 0 else numero+1

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:float)->float:
    if numero%9 == 0:
        return numero*3
    elif numero%3 == 0:
        return numero*2
    else:
        return numero

def lindo_nombre(nombre:str):
    if len(nombre)>=5:
        print("Tu nombre tiene muchas letras!")
    else:
        print("Tu nombre tiene menos de 5 caracteres")

def elRango(numero):
    if numero<5:
        print("Menor a 5")
    elif numero >= 10 and numero <= 20:
        print("Entre 10 y 20")
    elif numero>20:
        print("Mayor a 20")

def vacacionesONo(genero:str,edad:int):
    if edad<18 or (edad>=60 and genero.lower()=="f") or (edad>=65 and genero.lower()=="m"):
        print("Anda de vacaciones")
    else:
        print("Anda a trabajar")

"""usando una variable:str y lower lo pasa a minusculas. Por ejemplo nombre.lower()
   pasa la variable nombre a minusculas. Esta muy bueno para trabajar con string 
"""
#Ejercicio 6
def numeros1Al10():
    numero:int = 1
    while numero<=10:
        print(numero)
        numero+=1
def numerosParesEntre10y40():
    contador:int = 10
    while contador<=40:
        print(contador)
        contador+=2
def eco():
    contador:int = 1
    while(contador<=10):
        print("eco")
        contador += 1
def cuentaRegresiva(numero:int):
    while numero>=1:
        print(numero)
        numero -= 1
    print("Despegue")

def viajeAlPasado(AnioPartida:int,AnioLlegada:int):
    while AnioPartida > AnioLlegada:
        AnioPartida -= 1
        print(f"Viajo un anio al pasado, estamos en el anio: {AnioPartida}" )

def viajeAlPasadoAristoteles(AnioPartida:int):
    anioAristoteles = -384
    while AnioPartida >= anioAristoteles +20:
        AnioPartida -= 20
        print(f"Viajo 20 anios al pasado, estamos en el anio: {AnioPartida}" )

#Ejercicio 7
def numeros1Al10For():
    for i in range (1,11):
        print(i)
def numerosParesEntre10y40For():
    for i in range (10,41,2):
        print(i)
def ecoFor():
    for i in range (1,11):
        print("Eco")

def cuentaRegresivaFor(entrada): #Para que el for vaya para atras, hay que indicarle el punto de paso -1
    for i in range (entrada,0,-1):
        print(i)
    print("Despegar")

def viajeAlPasadoFor(AnioPartida:int,AnioLlegada:int):
    for i in range (AnioPartida,AnioLlegada-1,-1):
        print(f"Viajo un anio al pasado, estamos en el anio: {i}" )

def viajeAlPasadoAristoteles(AnioPartida:int):
    anioAristoteles = -384
    for i in range (AnioPartida-20,anioAristoteles,-20):
        print(f"Viajo 20 anios al pasado, estamos en el anio: {i}")

#Ejercicio 9

g: int = 1
def rt(x: int,) -> int:
    return x + g
def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g
"""Al definir una variable global, al modificar la variable se modifica en toda la funcion.
    En este caso cada vez que aplico la funcion g aumenta en 1
    En rt no se modifica la variable g, cada vez que aplico la funcion mantiene el mismo valor
"""