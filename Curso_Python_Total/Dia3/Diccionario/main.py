#miDiccionario = {'Perro':'Mamifero de 4 patas','Gusano':'Invertebrado del mundo de los insectos'}

#print(type(miDiccionario))

#print(miDiccionario)

#resultado=miDiccionario['Gusano']

#print(resultado)

#clienteGanador={'Nombre': 'Rodolfo','DNI': 30334271, 'Edad': 52}

#resultado2=clienteGanador['DNI']
#print(resultado2)

clienteVip={'Nombre': 'jose', 'Altura':1.70, 'Compras': [12.33,17.55,65.20,12,20], 'Colectivero': {'linea 22': 180, 'Kilometras': 200}}

print(clienteVip['Compras'][1])

print(clienteVip['Nombre'].upper())
print(clienteVip.keys())
print(clienteVip.values())
print(clienteVip.items())