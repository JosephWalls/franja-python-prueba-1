#Una panadería vende barras de pan a 3.49€ cada una. 
#El pan que no es el día tiene un descuento del 60%. 
#Escribe un programa que comience leyendo el número de barras vendidas 
#que no son del día. Después tu programa debe mostrar el precio habitual de una barra de pan, 
#el descuento que se le hace por no ser fresca y el coste final total

precio_pan=3.49
descuento=60/100

pan_vendido=int(input("ingrese cantidad de barras de pan vendidas que no son del dia: "))
cargo=pan_vendido*precio_pan
cargo=str(cargo)
precio_panstr=str(precio_pan)
print("El precio habitual de una barra de pan es: "+precio_panstr)
descuentostr=str(descuento)
print("el descuento aplicado para pan que no es del dia es: "+descuentostr)
precio_total=(precio_pan*descuento)*pan_vendido
precio_total=str(precio_total)
pan=str(pan_vendido)
print("el valor habitual por "+pan+" barra de pan seria "+cargo)
print("el valor por "+pan+" barras de pan que no son del dia es: "+precio_total)
