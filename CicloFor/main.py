# cadena = 'hola'
#
# for letra in cadena:
#     print(letra)
# else:
#     print('Fin del ciclo for')

# for letra in 'Holanda':
#     if letra == 'a':
#         print(f'La letra encontrada es: {letra}')
#         break
# else:
#     print('fin')

# for i in range(6):
#     if i % 2 == 0:
#         print(f'Numero: {i}')

for i in range(6):
    if i % 2 == 0:
        continue
    print(f'Numero: {i}')