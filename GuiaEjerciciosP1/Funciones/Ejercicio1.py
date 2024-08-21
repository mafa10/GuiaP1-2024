"""
Desarrollar una funcion que reciba 3 números positivos y devuelva el mayor estricto de los 3 (sino, devolver -1). Sin "and" ni "not" 
"""
def mayor_estricto(a,b,c):
    """
    pre: recibe 3 números
    pos: devuelve el mayor de los 3
    """
    indice = -1
    if a > b:
        if a > c:
            indice = a
    if b > a:
        if b > c:
            indice = b
    if c > a:
        if c > b:
            indice = c

    return indice 


#Programa Principal

print("Programa para calcular el número mayor estricto de entre 3 números")
print()
num1 = int(input("Ingrese un número positivo:"))
num2 = int(input("Ingrese un número positivo:"))
num3 = int(input("Ingrese un número positivo:"))
while num1 < 1:
    print("El número ingresado no es válido")
    num1 = int(input("Ingrese un número positivo:"))

while num2 < 1: #cuento al 0(cero) como número positivo
    print("El número ingresado no es válido")
    num2 = int(input("Ingrese un número positivo:"))

while num3 < 1: #cuento al 0(cero) como número positivo
    print("El número ingresado no es válido")
    num3 = int(input("Ingrese un número positivo:"))

mayor = mayor_estricto(num1,num2,num3)

print()
if mayor != -1:
    print("El número mayor estricto entre los 3 es:", mayor)
else:
    print("No se ha encontrado el número mayor")
    print(mayor)