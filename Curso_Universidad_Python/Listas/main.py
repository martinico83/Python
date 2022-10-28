nombres = ['Maria', 'Edit', 'Lucas', 'Emilia']

# print(nombres)

# print(nombres[2])

# for nombre in nombres:
#     print(nombre)

print(nombres[1:3]) #desde el indice 1 sin incluir el indice 3
print(nombres[:3]) #desde el inicio sin incluir el indice 3
print(nombres[0:])#desde el indice indicado hasta el

print(len(nombres))
nombres.append('Ricardo')
print(nombres)
nombres.insert(1,'Micaela')
print(nombres)
nombres.remove('Emilia')
print(nombres)
#remover el ultimo valor agregado
nombres.pop()
print(nombres)
del nombres[2]
print(nombres)
nombres.clear()
print(nombres)
del nombres
print(nombres)




