#Una panadería vende barras de pan a 3.49€ cada una. 
#El pan que no es el día tiene un descuento del 60%. 
#Escribe un programa que comience leyendo el número de barras vendidas 
#que no son del día. Después tu programa debe mostrar el precio habitual de una barra de pan, 
#el descuento que se le hace por no ser fresca y el coste final total

precio_pan=3.49
dscto=0.6

pan_vendido=int(input("ingrese cuantas barras de pan que no son del dia se han vendido: "))
cargo=pan_vendido*precio_pan
cargo=str(cargo)
precio_panstr=str(precio_pan)
print("El precio habitual de una barra de pan es: "+precio_panstr)
dsctostr=str(dscto)
print("el descuento aplicado para pan que no es del dia es: "+dsctostr)
precio_final=(precio_pan*dscto)*pan_vendido
precio_final=str(precio_final)
pan=str(pan_vendido)
print("el valor habitual por "+pan+" barra de pan seria "+cargo)
print("el valor por "+pan+" barras de pan que no son del dia es: "+precio_final)
