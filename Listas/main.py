mi_lista = ['a','b','c']
otra_lista = [12,5.6,"hola"]
tamanio = len(otra_lista)
print(otra_lista[0])
print(otra_lista[0:2])
print(mi_lista+otra_lista)
lista2 = mi_lista + otra_lista
print(lista2)
lista2 [2] = "Bolu"  #esto se puede hacer y con los strings no
print(lista2)
lista2.append("Martin")
print(lista2)
resultado = lista2.pop(4)
print(resultado)

lista3 = ['f','e','a','i']
lista3.sort()
print(lista3)
lista3.reverse()
print(lista3)
nueva_lista = lista3.sort()
print(nueva_lista)
print(type(nueva_lista))


