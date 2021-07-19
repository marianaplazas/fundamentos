#!/usr/bin/python3
'''
Este es un codigo explicativo para saber si dado un conjunto de elementos 
A en la forma de una lista y una relación R en la forma lista de tuplas,
se puede determinar si R es equivalente
La forma en que se recibe el input es por consola los elementos separados 
ṕor espacios y luego la relación R en pares separados por espacios
A = w x y z
R = xy wy zz
'''

def is_equivalent(A,R):
    listaA = A[:]
    listaR = R[:]
    reflexividad = is_reflexive(listaA,listaR)
    listaA = A[:]
    listaR = R[:]
    transitividad = is_transitive(listaR)
    listaA = A[:]
    listaR = R[:]
    simetria = is_symmetrical(listaR)
    if (reflexividad and simetria and transitividad):
        print("Esta relación es de equivalencia.")
    else:
        print("Esta relación no es de equivalencia porque:")
        if (reflexividad) == False:
            print("no es reflexiva.")
        if (simetria) == False:
            print("no es simétrica.")
        if (transitividad) == False:
            print("no es transitiva.")
        
            
def is_reflexive(elements,relation):
    for i in relation:
        if i.count(i[0]) == 2:
            elements.remove(i[0])
    if len(elements) > 0:
        return(False)
    else:
        return(True)

    
def is_symmetrical(relation):
    index = []
    for i in relation:
        if i.count(i[0]) == 2:
            index.append(relation.index(i))
    for i in sorted(index, reverse=True):
        del relation[i]

    if len(relation) == 0:
        return(True)  
        
    for i in relation:
        j = i
        j.reverse()
        relation.pop(relation.index(i))
        if relation.count(j) == 0:
            return(False)
        else:
            relation.pop(relation.index(j))
        return(True)

    
def is_transitive(relation):

    for i in relation:
        mayor = i[0]
        medio = i[1]
        secondpairs = filter(lambda x : x[0] == medio, relation)
        secondpairs = list(secondpairs)
        for pair in secondpairs:
            thisPair = []
            thisPair.insert(0, mayor)
            thisPair.insert(1, pair[1])
            if not(thisPair in relation):
                return False
    return True


print("")
print("Hola, soy tu asistente personal!")
print("Compruebo si una relación es de equivalencia.")
print("")
print("Por favor, ingresar los elementos con el formato: x y z")
A = input("Escribe los elementos del conjunto A: ")
print("")
print("Por favor, ingresar las parejas con el formato: xx yy zz")
Pairs = input("Escribe las parejas ordenadas de la relación R: ")
print("")
print("")

A = A.split(" ")
Pairs = Pairs.split(" ")
R = []

for i in Pairs:
    R.append(list(i))

is_equivalent(A,R)
print("")
print("Gracias, adiós!")
print("")
