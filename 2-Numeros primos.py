#numero = int(input("Dígame un numero: "))
#print("El num es ",numero)

numero= int(input("¿De qué número quiere saber los divisores? "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1
    print("divisor:", n)

if contador > 0 :
  print("El número no es primo" )
else:
  print("El nÚmero es primo")