n1 = int(input("Ingresa el primer numero:"))
n2 = int(input("Ingresa el segundo numero:"))

suma = 1
resta = 2
multiplicacion = 3
division = 4

print("Selecciona 1 para sumar")
print("Selecciona 2 para restar")
print("Selecciona 3 para multiplicar")
print("Selecciona 4 para dividir")
opcion = int(input("Selecciona una opcion:"))

if opcion == suma:
    print("Tu resultado es " + str(n1 + n2))
elif opcion == resta:
    print("Tu resultado es " + str(n1 - n2))
elif opcion == multiplicacion:
    print("Tu resultado es " + str(n1 * n2))
elif opcion == division:
    print("Tu resultado es " + str(n1 / n2))
else:
    print("Opcion incorrecta")