mensaje = "Hola Mundor"

print(mensaje) 

resultado = 9/2

print(resultado)

print(type(resultado))
men="""Esto es un mensaje
con tres saltos
de linea"""

print(men)

num1 = 4
num2 = 1

if (num1 > num2):
    print("el num1 es mayor que num2")

pii = 3.1222
print(pii)
print(type(pii))

num = int(input("Introduce el numero: "))
if(num <= 0):
    num = 0
else:
    num = num * num
print(num)
print("Lorem34")


for i in range (20):
    if i == 12:
        print(f"Solo {i} horas")
    else:
        print(f"Ni {i}")