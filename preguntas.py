"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("data.csv", "r") as file:
        df = file.readlines()
    df = [line.replace("\t", ";") for line in df]
    df = [line.split(";") for line in df]
    x=0
    for i in range(0,len(df)):
        x+=int(df[i][1])
    return x


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open("data.csv", "r") as file:
        df = file.readlines()
    df = [line.replace("\t", ";") for line in df]
    df = [line.split(";") for line in df]
    y=[]
    a=[]
    for j in range(0,len(df)):
        y.append(df[j][0])
    for i in y:
        a.append((i,y.count(i)))
    a=list(set(a))
    a.sort()
    return a


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open("data.csv", "r") as file:
        df = file.readlines()
    df = [line.replace("\t", ";") for line in df]
    df = [line.split(";") for line in df]
    a=[]
    for j in range(0,len(df)):
        a.append(df[j][0:2])
    dicc={}
    for key,value in a:
        if key in dicc:
            dicc[key]+=int(value)
        else:
            dicc[key]=int(value)
    respuesta=[(key,dicc[key]) for key in dicc]
    respuesta.sort()
    return respuesta


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv", "r") as file:
        df = file.readlines()
    df = [line.replace("\t", ";") for line in df]
    df = [line.split(";") for line in df]
    a=[]
    for j in range(0,len(df)):
        a.append(df[j][2])
    lista=[]
    for line in a:
        lista.append(line.split("-")[1])
    tempo={}
    for key in lista:
        if key in tempo:
            tempo[key]+=1
        else:
            tempo[key]=1
    respuesta=[(key,tempo[key]) for key in tempo]
    respuesta.sort()
    return  respuesta


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv", "r") as file:
        df = file.readlines()
    df = [line.replace("\t", ";") for line in df]
    df = [line.split(";") for line in df]
    a=[]
    for j in range(0,len(df)):
        a.append(df[j][0:2])
    minn=dict()
    for key,value in a:
        if key in minn:
            minn[key].append(value)
        else:
            minn[key] = [value]
    answ=[]
    for p in minn:
        answ.append( (p,int(max(minn[p])),int(min(minn[p]))))
    answ=sorted(answ)
    return answ


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv", "r") as file:
        df = file.readlines()
    df = [line.replace("\t", ";") for line in df]
    df = [line.replace("\n", "") for line in df]
    df = [line.split(";") for line in df]
    a=[]
    for j in range(0,len(df)):
        a.append(df[j][4])
    a=[p.split(",") for p in a]
    df2=[]
    for p in a:
        for j in p:
            df2.append(j.split(":"))
    dicc2={}
    for key,value in df2:
        if key in dicc2:
            dicc2[key].append(int(value))
        else:
            dicc2[key] = [int(value)]
    resp=[]
    for p in dicc2:
        resp.append( (p,int(min(dicc2[p])),int(max(dicc2[p]))))
    resp=sorted(resp)
    return resp


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv", "r") as file:
        df = file.readlines()
    df = [line.replace("\t", ";") for line in df]
    df = [line.replace("\n", "") for line in df]
    df = [line.split(";") for line in df]
    a=[]
    for j in range(0,len(df)):
        a.append([int(df[j][1]),df[j][0]])
    dicc2={}
    for key,value in a:
        if key in dicc2:
            dicc2[key].append(value)
        else:
            dicc2[key] = [value]
    respuesta=[(key,dicc2[key]) for key in dicc2]
    respuesta.sort()
    return respuesta


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv", "r") as file:
        df = file.readlines()
    df = [line.replace("\t", ";") for line in df]
    df = [line.replace("\n", "") for line in df]
    df = [line.split(";") for line in df]
    a=[]
    for j in range(0,len(df)):
        a.append([int(df[j][1]),df[j][0]])
    dicc2={}
    for key,value in a:
        if key in dicc2:
            dicc2[key].append(value)
        else:
            dicc2[key] = [value]
    respuesta=[(key,sorted(list(set(dicc2[key])))) for key in dicc2]
    respuesta.sort()
    return respuesta


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open("data.csv", "r") as file:
        df = file.readlines()
    df = [line.replace("\t", ";") for line in df]
    df = [line.replace("\n", "") for line in df]
    df = [line.split(";") for line in df]
    a=[]
    for j in range(0,len(df)):
        a.append(df[j][4])
    a=[p.split(",") for p in a]
    df2=[]
    for p in a:
        for j in p:
            df2.append(j.split(":")[0])
    df2.sort()
    tempo={}
    for key in df2:
        if key in tempo:
            tempo[key]+=1
        else:
            tempo[key]=1
    return tempo


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("data.csv", "r") as file:
        df = file.readlines()
    df = [line.replace("\t", ";") for line in df]
    df = [line.replace("\n", "") for line in df]
    df = [line.split(";") for line in df]
    a=[]
    for j in range(0,len(df)):
        a.append(df[j][4])
    a=[p.split(",") for p in a]
    b=[]
    for j in range(0,len(df)):
        b.append(df[j][3])
    b=[p.split(",") for p in b]
    df3=[]
    for x in range(0,len(a)):
        df3.append((df[x][0],len(b[x]),len(a[x])))
    return df3


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open("data.csv", "r") as file:
        df = file.readlines()
    df = [line.replace("\t", ";") for line in df]
    df = [line.replace("\n", "") for line in df]
    df = [line.split(";") for line in df]
    a=[]
    for j in range(0,len(df)):
        a.append([df[j][1],df[j][3].split(",")])
    df2=[]
    for j in a:
        for i in j[1]:
            df2.append([i,j[0]])
    df2.sort()
    dicc={}
    for key,value in df2:
        if key in dicc:
            dicc[key]+=int(value)
        else:
            dicc[key]=int(value)
    return dicc


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("data.csv", "r") as file:
        df = file.readlines()
    df = [line.replace("\t", ";") for line in df]
    df = [line.replace("\n", "") for line in df]
    df = [line.split(";") for line in df]
    a=[]
    b=[]
    for j in range(0,len(df)):
        a.append(df[j][4].split(","))
        for i in range(0,len(a[j])):
            b.append([df[j][0],a[j][i].split(":")[1]])
    b.sort()
    dicc={}
    for key,value in b:
        if key in dicc:
            dicc[key]+=int(value)
        else:
            dicc[key]=int(value)
    return dicc
