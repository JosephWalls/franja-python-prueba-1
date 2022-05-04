#Escribir un programa que le pregunte al usuario una cantidad a invertir, 
#el interés porcentual anual y el número de años, y muestre por pantalla el capital obtenido en la 
#inversión redondeado a dos decimales.

inv=int(input("ingrese su inversion inicial: "))
intanual=float(input("ingrese la tasa de interes porcentual anual: "))
years=int(input("ingrese el plazo en años de su inversion: "))

final_cap=inv*((intanual/100)+1)*years
final_cap=round(final_cap,2)
final_cap=str(final_cap)

print("el capital total estimado es: "+final_cap)