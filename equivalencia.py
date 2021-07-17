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
A = input("Give me the next element to your A: ")
Pairs = input("Give me the pairs of your R: ")

A = A.split(" ")
Pairs = Pairs.split(" ")
R = []

for i in Pairs:
    R.append(list(i))

#def is_equivalent(elements,relation):
'''
def is_reflexive(elements,relation):
    for i in elements:
        for j in relation:
            print(j.count(i))
'''
def is_symmetrical(relation):
    for i in relation:
        if i.count(i[0]) == 2:
            relation.pop(relation.index(i))  
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
    '''
    (3,2),(1,1),(2,1)

    (3,2),(2,1),(3,1)
    (1,1)()
    (2,1)(1,1)(2,1)
    '''
    for i in relation:
        #micro armado
        mayor = i[0]
        medio = i[1]
        #traeme todos los que empiezan con el medio
        secondpairs = filter(lambda x : x[0] == medio, relation)
        print(list(secondpairs))

is_transitive(R)
#print(is_symmetrical(A,R))