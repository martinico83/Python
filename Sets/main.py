# LOS SETS NO PUEDEN MODIFICARSE, NO TIENEN ORDEN Y NO ADMITEN LISTAS NI DICCIONARIOS Y SI REPITO ELEMENTOS PYTHON LOS IGNORA
#mi_set = set([1,2,3,4,5])
mi_set = set([1,2,3,4,5,(5,4,1)]) # con tuples

#mi_set = set({1,2,3,4,5})
#mi_set = set((1,2,3,4,5))
print(type(mi_set))
print(mi_set)
print(len(mi_set))

print(10 in mi_set)


otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

s1 = {1,2,3}
s2 = {3,4,5,10}
s3 = s1.union(s2)

s3.add(20)
s3.add(5) # AGREGE UN ELEMENTO REPETIDO POR LO TANTO PYTHON LO IGNORA
s3.remove(10)
s3.pop() # ELIMINA UN NUMERO DEL SET ALEATOREAMENTE
s3.clear() # LIMPIA EL SET
print(s3)