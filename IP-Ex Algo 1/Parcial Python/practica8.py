from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
"""Ejercicios hechos por mí"""
"""Manejo de archivos"""
#1.1
def contar_lineas(nombre_archivo:str)->int:
    archivo = open(nombre_archivo,"r")
    lineas = archivo.readlines()
    cantidad_de_lineas=len(lineas)
    archivo.close()
    print(lineas)
    print(cantidad_de_lineas)
    return cantidad_de_lineas
#1.2
def existe_palabra(palabra:str,nombre_archivo:str)->bool:
    archivo = open(nombre_archivo,"r")
    lineas = archivo.readlines()
    if archivo in lineas:
        resultado = True
    else:
        resultado = False
    archivo.close()
    return resultado

#1.3   
def cantidad_de_apariciones(nombre_archivo:str,palabra:str)->int: #read y split
    archivo = open(nombre_archivo,"r")
    lineas=archivo.read() #anotar para que sirve el read y el split
    palabras=lineas.split()    
    contadorPalabras=0
    for palab in palabras:
        if palab == palabra:
            contadorPalabras+=1
    archivo.close()
    return contadorPalabras

"""Ejercicio 2 """
def clonar_sin_comentarios(nombre_archivo:str):
    archivo=open(nombre_archivo,"r")
    lineas=archivo.readlines()
    archivo_sin_comentarios=open("sin_comentarios","w")
    for linea in lineas:
        nueva_linea=linea.strip()
        if not nueva_linea[0]=="#":
            archivo_sin_comentarios.write(linea)
    archivo.close()
    archivo_sin_comentarios.close()

"""Ejercicio 3"""
def orden_reverso(nombre_archivo:str):
    archivo = open(nombre_archivo,"r")
    lineas = archivo.readlines()
    archivo_reverso=open("reverso.txt","w")
    for i in range (len(lineas)-1,-1,-1):
        archivo_reverso.write(lineas[i])
    archivo_reverso.close()
    archivo.close() 

"""Ejercicio 4"""
def agregar_frase_al_final(nombre_archivo:str,frase:str):
    archivo=open(nombre_archivo,"a")
    archivo.write(frase)
    archivo.close()

"""Ejercicio 5"""
def agregar_frase_al_principio(nombre_archivo:str,frase:str):
    archivo=open(nombre_archivo,"r")
    lineas=archivo.readlines()
    archivo=open(nombre_archivo,"w")
    frase_a_agregar=frase
    archivo.write(frase_a_agregar+"\n")
    for linea in lineas:    
        archivo.write(linea)
    archivo.close()

"""Ejercicio 6""" #Uso del char, de listas y de concatenacion de str

"""leer archivo en binario
    archivo=open(nombre_archivo,"rb")
    contenido_en_binario:str = archivo.read()"""
def lista_palabras_legibles(nombre_archivo:str)->list[str]:
    lista_palabras:list[str]=obtener_palabras_de_un_archivo_binario(nombre_archivo)
    palabras_legibles:list[str] = []
    for palabra in lista_palabras:
        if es_palabra_con_caracteres_legibles(palabra)==True and len(palabra)>=5:
            palabras_legibles.append(palabra)
    return palabras_legibles

def obtener_palabras_de_un_archivo_binario(nombre_archivo:str)->list[str]:
    archivo=open(nombre_archivo,"rb")
    texto_en_binario=archivo.read()
    texto_traducido = ""
    lista_palabras=[]
    for caracter in texto_en_binario:
        texto_traducido +=chr(caracter)
    lista_palabras=texto_traducido.split()
    archivo.close()
    return lista_palabras

def es_palabra_con_caracteres_legibles(palabra:str)->bool: 
    for caracter in palabra:
        if caracter_legible(caracter)==False:
            return False
    return True

def caracter_legible(caracter:str)->bool:
    legible=False
    if caracter==" " or caracter =="_":
        legible=True
    elif "Z">=caracter>="A":
        legible=True
    elif "z">=caracter>="a":
        legible=True
    return legible

"""Ejercicio 7"""
def promedioEstudiante(lu:str)->float: 
    archivo=open("textosPractica8/notas.txt","r") #le pongo directamente el nombre del archivo pq asi es la especifiacion del ejercicio
    elementos:list=(archivo.read()).split(",") #por la especificacion del ejercicio asumo que tiene la forma:lu, materia, fecha, nota, lu ,materia, fecha...
    notasDelEstudiante=[]
    sumaDeNotasDelEstudiante=0
    for elemento in range (len(elementos)):
        if elementos[elemento]==lu:
            notasDelEstudiante.append(float(elementos[elemento+3]))
            sumaDeNotasDelEstudiante+=(float(elementos[elemento+3]))
    archivo.close()
    return sumaDeNotasDelEstudiante/len(notasDelEstudiante)

"""PILAS"""
miPila= Pila() #Pila de ejemplo para probar los ejercicios
miPila.put(1)
miPila.put(2)
miPila.put(3)

"""Ejercicio 8"""
def generar_nros_al_azar(n:int,desde:int,hasta:int)->Pila:
    p=Pila()
    for contador in range (n):
        p.put(random.randint(desde,hasta))
    return p
"""Ejercicio 9"""
def cantidad_elementos(p:Pila)->int:
    print(f"{p.queue} PILA INICIAL")
    elementos_de_p:list=[]
    while not(p.empty()):
        elemento=p.get()
        elementos_de_p.append(elemento)
    for indice in  range(len(elementos_de_p)-1,-1,-1):
        p.put(elementos_de_p[indice])
    print(f"{p.queue} PILA FINAL")
    print(f"{len(elementos_de_p)} CANTIDAD DE ELEMENTOS DE LA PILA")
    return len(elementos_de_p)

"""Ejercicio 10"""
def maximo_de_una_lista(lista:list[int])->int:
    MaximoElemento=lista[0]
    for indice in  range(len(lista)):
        if lista[indice]>MaximoElemento:
            MaximoElemento=lista[indice]
    return MaximoElemento

def elementos_de_una_pila_a_lista(p:Pila)->list: #pasa los elementos a una lista sin modificar la pila
    elementos_de_p:list=[]
    while not(p.empty()):
        elemento=p.get()
        elementos_de_p.append(elemento)
    for indice in  range(len(elementos_de_p)-1,-1,-1):
        p.put(elementos_de_p[indice])
    return elementos_de_p

def buscar_el_maximo(p:Pila)->int:
    lista_de_elementos_de_p=elementos_de_una_pila_a_lista(p)
    maximo=maximo_de_una_lista(lista_de_elementos_de_p)
    return maximo

"""Ejercicio 11""" #Pilas con str
def str_a_pila(s:str)->Pila:
    p=Pila()
    for caracter in s:
        p.put(caracter)
    return p

def esta_bien_balanceada(s:str)->bool:
    parentesisAbiertos=0
    parentesisCerrados=0
    pilaDeLaOperacion=str_a_pila(s)
    while not pilaDeLaOperacion.empty():
        if parentesisAbiertos>parentesisCerrados:
            return False
        elemento=pilaDeLaOperacion.get()
        if elemento=="(":
            parentesisAbiertos+=1
        if elemento==")":
            parentesisCerrados+=1
    return parentesisAbiertos==parentesisCerrados

"""Ejercicio 12"""
def notacion_polaca(expresion:str)->float:
    lista_operaciones:list=expresion.split()
    operando=Pila()
    for token in lista_operaciones:
        if "9">=token>="0":
            operando.put(float(token))
        if "/"==token:
            elemento2=operando.get()
            elemento1=operando.get()
            resultado=elemento1/elemento2
            operando.put(resultado)
        if "*"==token:
            elemento2=operando.get()
            elemento1=operando.get()
            resultado=elemento1*elemento2
            operando.put(resultado)
        if "+"==token:
            elemento2=operando.get()
            elemento1=operando.get()
            resultado=elemento1+elemento2
            operando.put(resultado)
        if "-"==token:
            elemento2=operando.get()
            elemento1=operando.get()
            resultado=elemento1-elemento2
            operando.put(resultado)
    print(operando.queue)
    elemento_final=operando.get()
    print(elemento_final)

"""COLAS"""
colaEjemplo= Cola()
colaEjemplo.put(1)
colaEjemplo.put(2)
colaEjemplo.put(3)
"""Ejercicio 13"""
def generar_nros_al_azar_colas(n:int,desde:int,hasta:int)->Cola:
    c=Cola()
    for i in range (n):
        c.put(random.randint(desde,hasta))
    return c

"""Ejercicio 14"""
def pasar_elementos_de_cola_a_lista(c:Cola)->list: #no modidica a la cola
    elementos_de_la_lista:list=[]
    while not(c.empty()):
        elementos_de_la_lista.append(c.get())
    for elementos in elementos_de_la_lista:
        c.put(elementos)
    return elementos_de_la_lista

def cantidad_elementos_cola(c:Cola)->int:
    lista_elementos_cola=pasar_elementos_de_cola_a_lista(c)
    return len(lista_elementos_cola)

"""Ejercicio 15"""
def buscar_el_maximo_cola(c:Cola)->int:
    lista_elementos_de_la_cola=pasar_elementos_de_cola_a_lista(c)
    elementoMaximo=lista_elementos_de_la_cola[0]
    for elemento in lista_elementos_de_la_cola:
        if elemento>elementoMaximo:
            elementoMaximo=elemento
    return elementoMaximo

"""Ejercicio 16"""
def armar_secuencia_de_bingo()->Cola[int]:
    lista_de_numeros=list(range(100))
    random.shuffle(lista_de_numeros)
    bolillero=Cola()
    for numero in lista_de_numeros:
        bolillero.put(numero)
    return bolillero

def jugar_carton_bingo(carton:list[int],bolillero:Cola[int])->int:
    bolillasNecesarias=0
    bolillasAcertadas=0
    while bolillasAcertadas<len(carton):
        elemento=bolillero.get()
        bolillasNecesarias+=1
        if elemento in carton:
            bolillasAcertadas += 1
    print(bolillasNecesarias)
    return bolillasNecesarias

#bolillero_bingo=armar_secuencia_de_bingo()
#jugar_carton_bingo([1,2,3,4],bolillero_bingo)

"""Ejercicio 17""" #Uso cola auxiliar
#Cola[(prioridad,nombre,especialidad)]
def n_pacientes_urgentes(c:Cola[(int,str,str)])->int:
    cola_pacientes:Cola[int,str,str]=c #Cola auxiliar
    print(cola_pacientes.queue)
    cantidad_de_pacientes_prioritarios=0
    while not cola_pacientes.empty():
        paciente=cola_pacientes.get()       
        if 3>=paciente[0]>=1:
            cantidad_de_pacientes_prioritarios+=1
    print(cantidad_de_pacientes_prioritarios)
    return cantidad_de_pacientes_prioritarios

#pacientes_ejemplo=Cola()
#pacientes_ejemplo.put([1,"nombre","radio"])
#n_pacientes_urgentes(pacientes_ejemplo)
"""Ejercicio 18"""
#falta este

"""DICCIONARIOS"""
"""Ejercicio 19"""
def agrupar_por_longitud(nombre_archivo:str)->dict:
    palabras_longitud={}
    archivo=open(nombre_archivo,"r")
    palabras=(archivo.read()).split()
    for palabra in palabras:
        if not(len(palabra) in palabras_longitud):
            palabras_longitud[len(palabra)]=1
        else:
            palabras_longitud[len(palabra)]+=1
    archivo.close()
    #print(palabras_longitud)
    return palabras_longitud
"""Ejercicio 20"""
def promedioEstudianteDiccionarios()->dict[str,float]: 
    archivo=open("textosPractica8/notas.txt","r") #le pongo directamente el nombre del archivo pq asi es la especifiacion del ejercicio
    lineas:list=(archivo.readlines()) #por la especificacion del ejercicio asumo que tiene la forma:lu, materia, fecha, nota /n lu, nota etc (en el primero lo hice distinto)
    diccionario_notas_estudiantes:dict[str,list[float]]={}
    for linea in lineas:
        elementos_linea=linea.split(",")
        if not(elementos_linea[0] in diccionario_notas_estudiantes): #elementos_linea[0] es cada LU
            diccionario_notas_estudiantes[elementos_linea[0]]=[elementos_linea[3]]
        else:
            diccionario_notas_estudiantes[elementos_linea[0]].append(elementos_linea[3])
    #print(diccionario_notas_estudiantes)
    alumnos=diccionario_notas_estudiantes.keys()
    diccionario_promedio_estudiantes:dict[str,list[float]]={}
    for alumno in alumnos:
        suma_notas_alumno=0
        for nota in diccionario_notas_estudiantes[alumno]:
                suma_notas_alumno+=float(nota)
                #print(suma_notas_alumno)
        diccionario_promedio_estudiantes[alumno]=suma_notas_alumno/len(diccionario_notas_estudiantes[alumno])
    archivo.close()
    print(diccionario_promedio_estudiantes)
    return(diccionario_notas_estudiantes)

"""Ejercicio 21"""
def la_palabra_mas_frecuente(nombre_archivo:str)->str:
    archivo=open(nombre_archivo,"r")
    palabras=(archivo.read()).split()
    diccionario_palabras:dict[str,int]={}
    for palabra in palabras:
        if not(palabra in diccionario_palabras):
            diccionario_palabras[palabra]=1
        else:
            diccionario_palabras[palabra]+=1
    palabra_que_mas_aparece=palabras[0]
    cantidad_de_apariciones=diccionario_palabras[palabras[0]]
    for palabra in palabras:
        if diccionario_palabras[palabra]>cantidad_de_apariciones:
            cantidad_de_apariciones=diccionario_palabras[palabra]
            palabra_que_mas_aparece=palabra
    archivo.close()
    print(palabra_que_mas_aparece)
    return palabra_que_mas_aparece
    
#la_palabra_mas_frecuente("textosPractica8/prueba2.txt")

"""Ejercicio 22"""
historiales:dict[str,(Pila,Pila)]={}
def visitar_sitio(historiales:dict[str,(Pila,Pila)],usuario:str,sitio:str):
        if not(usuario in historiales):
            historiales[usuario]=(Pila(),Pila())
            historiales[usuario][0].put(sitio)
        else:
            historiales[usuario][0].put(sitio)

def navegar_atras(historiales:dict[str,(Pila,Pila)],usuario:str): 
    ultimo_sitio_visitado=historiales[usuario][0].get()
    (historiales[usuario][1]).put(ultimo_sitio_visitado)
    print(ultimo_sitio_visitado)
    return ultimo_sitio_visitado

def navegar_adelante(historiales:dict[str,(Pila,Pila)],usuario:str):
    sitio_adelante=historiales[usuario][1].get()
    historiales[usuario][0].put(sitio_adelante)
    print(sitio_adelante)
    return sitio_adelante

visitar_sitio(historiales,"manu","google")
visitar_sitio(historiales,"manu","face")
visitar_sitio(historiales,"manu","insta")
navegar_atras(historiales,"manu")
navegar_atras(historiales,"manu")
navegar_adelante(historiales,"manu")
navegar_adelante(historiales,"manu")