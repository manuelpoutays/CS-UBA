import random
"""         ---Ejercicios que hizo el profe---     """
def sumaTotal(s:[int])-> int:
    total:int = 0
    longitud:int =len(s)
    indice_actual:int = 0
    while indice_actual < longitud:
        total += s[indice_actual]
        indice_actual += 1
    return total
#es < a la longitud, y no <=, porque la longitud empieza a contar en 0
#+= es equivalente a poner total = indice_actual + ..
# explico debugging, mirar las diapos

#el profe lo hizo asi, es mas legible
def pertenece2(s:[int],e:int)->bool:
    indice:int = 0
    longitud:int = len(s)
    while indice < longitud:
        if e==s[indice]:
            res:bool = True
            return pertenece
        indice +=1
    return False
#otro mas del porfe
def pertenece3(s:[int],e:int)->bool:
    
    longitud:int = len(s)
    for i in range(0, longitud):
        if e == s[i]:
            return True
    return False
#este es del profe pero no funciono
def pertenece_generico(s:[],e) ->bool:
    for elem in s:
        print(elem)
        if elem == e:
            return True
    return False

#Ejercicio 5.1 del profe
def pertenece_a_cada_uno (s:[[int]],e:int) ->bool:
    res:[bool] = []
    for i in range(0,len(s)):
        res.append(pertenece_generico(s[i],e)) #el pertenece generico que copie no funciono #el append te agrega al final de la lista un elemento
    return res 
#hay otra forma de hacerlo; pero es interesante la lista de bool o la lista de listas; igual la lista de listas no se si esta bien, despues lo tengo que pensar

""""        ---Ejercicio 1---                 """

#Ejercicio 1.1
#este lo hice yo, se podrian agregar un par de print para entender mejor los ciclcos
def pertenece(s:[int],e:int)->bool:
    indice:int = 0
    longitud:int = len(s)
    while indice < longitud:
        if e==s[indice]:
            return True
        indice +=1
    return False

def perteneceFor(s:[int],e:int)->bool:
    for i in range (len(s)):
        if e==s[i]:
            return True
    return False

#Ejercicio 1.2
def divideATodos(s:[int],e:int) ->bool: 
    for i in range (0,len(s)):
        if not (s[i]%e == 0):
            return False
    return True

def divideATodosWhile(s:[int],e:int)->bool:
    indice=0
    while indice<len(s):
        if s[indice]%e != 0:
            return False
        indice += 1
    return True


#Ejercicicio 1.3
def sumaTotal(s:[int]) ->int:
    res = 0
    for i in range (0,len(s)):
        res += s[i]
    return res

def sumaTotalWhile(s:[float]) -> float:
    res = 0
    contador = 0
    while contador < len(s):
        res+= s[contador]
        contador+=1
    return res

#Ejercicio 1.4
def ordenados(s:[int]) ->bool:
    for i in range (0,len(s)-1):
        if s[i]>=s[i+1]:
            return False
    return True

def ordenadosWhile(s:[int])->bool:
    indice = 0
    while indice < len(s)-1:
        if s[indice] >= s[indice+1]:
            return False
        indice += 1 
    return True

#Ejercicio 1.5
def longitudDePalabras(s:[str]) ->bool:
    for i in range (0,len(s)):
        if len(s[i]) > 7:
            return True
    return False

#Ejercicio 1.6
def palindromo(palabra:str)->bool:
    indice=0
    for i in range (len(palabra)-1,-1,-1):
        if palabra[i] != palabra[indice]:
            return False
        indice +=1
    return True

#Ejercicio 1.7    
#este se hace con el codigo ascii
def fortaleza(contraseña:str) ->str :
    if tieneMayuscula(contraseña)==True and tieneMinuscula(contraseña) == True and tieneDigitoNumerico (contraseña) == True and len(contraseña)>= 8:
        return "VERDE"
    elif len(contraseña) < 5:
        return "ROJA"
    else:
        return "AMARILLA"

def tieneMayuscula(a:str)-> bool:
    longitud:str = len(a)
    for i in range (0,longitud):
        if a[i] >= "A" and a[i] <= "Z":
            return True
    return False

def tieneMinuscula(a:str)-> bool:
    longitud:str = len(a)
    for i in range (0,longitud):
        if a[i] >= "a" and a[i] <= "z":
            return True
    return False

def tieneDigitoNumerico(a:str)-> bool:
    
    longitud:str = len(a)
    for i in range (0,longitud):
        if a[i] >= "0" and a[i] <= "9":
            return True
    return False

#Ejercicio 1.8
def movimientosCuentaBancaria(operaciones:[tuple])->tuple:
    saldo=0
    for i in range (len(operaciones)):
        if (operaciones[i])[0] == "I":
            saldo += (operaciones[i])[1]
        elif (operaciones[i])[0] == "R":
            saldo -= (operaciones[i])[1]
    return saldo

#Ejercicio 1.9
#Lo hizo un companiero, me parecio que no valia la pena gastar tanto tiempo pensandolo
def tresVocalesDistintas(palabra: str) -> bool:
    vocales = ["a","e","i","o","u"]
    for caracter in palabra:
        for vocal in vocales:
            if caracter == vocal:
                vocales.remove(vocal)
    return len(vocales) <= 2

""""Segunda parte"""
#Bastantes ejercicios de crear una lista vacia e ir agregando elemntos

#Ejercicio 2.1
def inout(lista:[int])->[int]:
    for i in range (0,len(lista),2):
        lista[i] = 0
    return lista

#Ejercicio 2.2
def tipoIn(lista:[int])->[int]:
    listaDevuelta = []
    for i in range (0,len(lista)):
        if i%2 == 0:
            listaDevuelta.append(0)
        else:
            listaDevuelta.append(lista[i])
    return listaDevuelta

#Ejercicio 2.3
def listaSinVocales(lista:[str])->[str]:
    nuevaLista = []
    for palabra in lista:
        nuevaLista.append(palabraSinVocales(palabra))
    return nuevaLista

def palabraSinVocales(palabra:str)->str:
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    palabraSinVocales = ""
    for letra in palabra:
         if not(letra in vocales):
            palabraSinVocales = palabraSinVocales + letra
    return palabraSinVocales

#Ejercicio 2.4
def reemplazaVocalesPalabra(palabra:str)->str:
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    palabraSinVocales = ""
    for letra in palabra:
        if not(letra in vocales):
            palabraSinVocales = palabraSinVocales + letra
        else:
            palabraSinVocales = palabraSinVocales + "_"
    return palabraSinVocales

def reemplazaVocales(lista:[str])->[str]:
    nuevaLista = []
    for palabra in lista:
        nuevaLista.append(reemplazaVocalesPalabra(palabra))
    return nuevaLista

#Ejercicio 2.5
def daVueltaStr(lista:[int])->[int]:
    nuevaLista = []
    for i in range (len(lista)-1,-1,-1):
        nuevaLista.append(lista[i])
    return nuevaLista

#Ejercicio 2.6
#la nueva lista tiene todos los elemntos de s, y no tiene elementos repetidos
def eliminarRepetidos(s:[str])->[str]:
    listaSinRepetidos = []
    for i in s:
        if not (i in listaSinRepetidos):
            listaSinRepetidos.append(i)
    return listaSinRepetidos

"""Ejercicio 3"""
#Listas para testear: [3,4,5,6] [5,6,7,8,1] [4,5,6,4,4]
#voy a hacer la variable sumaDeNotas: y la variable promedio y el return segun las condiciones
def aprobado(notas:list[int])->int:
    if hayNotaMenorA4(notas) or promedioNotas(notas) < 4:
        return 3
    if not(hayNotaMenorA4(notas)) and promedioNotas(notas) >= 7:
        return 1
    if not(hayNotaMenorA4(notas)) and (promedioNotas(notas) >= 4 and promedioNotas(notas) < 7):
        return 2

def hayNotaMenorA4(notas:list[int])->bool:
    for i in notas:
        if i < 4:
            return True
    return False

def promedioNotas(notas:list[int])->int:
    sumaDeNotas:int = 0
    for i in notas:
        sumaDeNotas += i
    promedio:float = sumaDeNotas/len(notas)
    return promedio

"""Ejercicio 4 - Input """
#4.1 Lista de str
def listaEstudiantes()->list[str]:
    listaEstudiantes:list[str] = []
    estudiante:str = input("ingrese el nombre del estudiante o LISTO para terminar ")
    while not(estudiante=="LISTO"):
        listaEstudiantes.append(estudiante)
        estudiante = input("ingrese el nombre del estudiante o LISTO para terminar ")
    return listaEstudiantes 

#4.2 tupla
def historialMonederoElectronico() -> list[tuple]:
    historial:list[tuple] = []
    operacion = input("Ingrese C para cargar creditos, D para descontar creditos,o X para finalizar ")
    while not(operacion=="X"):
        if operacion == "C":
            monto=input("Ingrese el monto a cargar ")
            historial.append((operacion,monto))
            operacion = input("Ingrese C para cargar creditos, D para descontar creditos,o X para finalizar ")
        elif operacion=="D":
            monto=input("Ingrese el monto a descontar ")
            historial.append((operacion,monto))
            operacion = input("Ingrese C para cargar creditos, D para descontar creditos,o X para finalizar ")
        elif not(operacion=="C" or operacion=="D"):
            operacion = input("Operacion invalida. Ingrese C para cargar creditos, D para descontar creditos,o X para finalizar ")
    return historial

#4.3 randint
def sieteYMedio()->list[int]:
    listadoCartas:list[int] = [1,2,3,4,5,7,8,9,10,11,12]
    sumaDePuntos:float = 0
    numeroInicial:int = random.randint(1,12)
    while numeroInicial == 8 or numeroInicial == 9:
        numeroInicial = random.randint(0,12)
    historialDeCartas:list[int] = [numeroInicial]
    sumaDePuntos += sistemaDeSumaDePuntos(numeroInicial)
    decision = input(f"Tu carta es {numeroInicial}, escribi SEGUIR o PLANTARSE ")
    while decision=="SEGUIR":
        cartaParaAgregar = random.choice(listadoCartas)
        historialDeCartas.append(cartaParaAgregar)
        sumaDePuntos += sistemaDeSumaDePuntos(cartaParaAgregar)
        decision = input("Escribi SEGUIR o PLANTARSE ")
    if decision == "PLANTARSE":
        if sumaDePuntos > 7.5:
            print(f"La suma de puntos es {sumaDePuntos}, perdiste. Tu historial de cartas es {historialDeCartas}")
            return historialDeCartas
        if sumaDePuntos <= 7.5:
            print(f"La suma de puntos es {sumaDePuntos}.Tu historial de cartas es {historialDeCartas} ")
            return historialDeCartas

def sistemaDeSumaDePuntos(numero:int)->int: 
    #Si es figura suma 0.5, sino suma el valor de la carta
    if numero >= 10:
        return 0.5
    else:
        return numero

"""Ejercicio 5 - Lista de listas"""
#5.1
def perteneceACadaUno(s:list[list[int]],e:int)->bool:
    for i in s:
        if pertenece(i,e)==False:
            return False
    return True

#5.2
def esMatriz(s:list[list[int]])->bool:
    if len(s)==0 or len(s[0])==0:
        return False
    for i in range (len(s)):
        if len(s[i]) != len(s[0]):
            return False
    return True

#5.3 
def filasOrdenadas(m:list[list[int]])->bool:
    for i in range (len(m)):
        if ordenados(m[i])==False:
            return False
    return True

#5.4 
