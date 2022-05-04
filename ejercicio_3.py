#Escribir un programa que haga transformaciones de pesos a dólares. 
#Debe preguntarle al usuario si desea transformar de 
#pesos mexicanos a dólares, de pesos chilenos a dólares, o desde pesos argentinos a dólares. 
#Mostrar por pantalla la cantidad de monedas a convertir, la moneda que se convirtió y el monto en dólares

#precios pasados a dolar

clp_usd=855
mxn_usd=20
ars_usd=115

tipomoneda=input("Seleccione la moneda que quiere convertir CLP, MXN, ARS: ")
cantidad=int(input("Ingrese la cantidad que quiere pasar a dolares: "))

if tipomoneda=="CLP":

    change=cantidad/clp_usd
    change=round(change,2)
    change=str(change)
    print("El monto en CLP a convertir es: "+str(cantidad))
    print("El monto correspondiente en dolares de la moneda CLP es: "+change)

elif tipomoneda=="MXN":

    change=cantidad/mxn_usd
    change=round(change,2)
    change=(str(change))

    print("El monto en CLP a convertir es: "+str(cantidad))
    print("El monto correspondiente en dolares de la moneda MXN es: "+change)

elif tipomoneda=="ARS":

    change=cantidad/ars_usd
    change=round(change,2)
    change=str(change)

    print("El monto en CLP a convertir es: "+str(cantidad))
    print("El monto correspondiente en dolares de la moneda ARS es: "+change)

else:
    print("Ingrese un codigo de moneda correcto")
