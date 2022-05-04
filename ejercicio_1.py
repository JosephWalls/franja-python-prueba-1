#Una panadería vende barras de pan a 3.49€ cada una. 
#El pan que no es el día tiene un descuento del 60%. 
#Escribe un programa que comience leyendo el número de barras vendidas 
#que no son del día. Después tu programa debe mostrar el precio habitual de una barra de pan, 
#el descuento que se le hace por no ser fresca y el coste final total

price=3.49
dscto=0.6

sellings=int(input("Ingrese cuantas barras de pan vendidas no son del día: "))
charge=sellings*price
charge=str(round(charge,2))
pricestr=str(price)
print("El precio habitual de una barra de pan es: "+pricestr)
dsctostr=str(dscto)
print("El descuento que se le hace por no ser fresco: "+dsctostr)
final_price=(price*dscto)*sellings
final_price=str(round(final_price,2))
bread=str(sellings)
print("El precio habitual seria: "+charge)
print("El coste final total es: "+final_price)
