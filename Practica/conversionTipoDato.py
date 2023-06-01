# Foma Implicita
num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))

# Forma Explicita

num3 = 5.8

print(num3)
print(type(num3))

num4 = int(num3)

print(num4)
print(type(num4))

edad = input('Dime tu edad: ') # El contenido que ingresa el usuario por teclado se toma como string

print(type(edad))

edad = int(edad)

print(type(edad))

nueva_edad = 1 + edad

print('Tu nueva edad va a ser ' + nueva_edad) # Esto da un error porque no se puede concatenar string con int

