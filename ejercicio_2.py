#Escribir un programa que le pregunte al usuario una cantidad a invertir, 
#el interés porcentual anual y el número de años, y muestre por pantalla el capital obtenido en la 
#inversión redondeado a dos decimales.

inv=int(input("ingrese el monto de dinero a invertir: "))
intanual=float(input("ingrese la tasa interes porcentual anual: "))
years=int(input("ingrese la cantidad de años que desea invertir: "))


capital_final=inv*((intanual/100)+1)*years
capital_final=round(capital_final,2)
capital_final=str(capital_final)
print("el capital obtenido en la inversion es: "+capital_final)
