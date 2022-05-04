#Escribir un programa que haga transformaciones de pesos a dólares. 
#Debe preguntarle al usuario si desea transformar de 
#pesos mexicanos a dólares, de pesos chilenos a dólares, o desde pesos argentinos a dólares. 
#Mostrar por pantalla la cantidad de monedas a convertir, la moneda que se convirtió y el monto en dólares

#precios pasados a dolar
clp_dolar=855
ars_dolar=115
mxn_dolar=20

tipomoneda=input("seleccione la moneda que quiere convertir CLP, ARS, MXN: ")
cantidad=int(input("ingrese la cantidad que quiere pasar a dolar: "))
if tipomoneda=="clp":
    conver=cantidad/clp_dolar
    conver=round(conver,2)
    conver=str(conver)
    print("el monto correspondiente en dolares de la moneda CLP es: "+conver)
else:
    if tipomoneda=="ars":
        conver=cantidad/ars_dolar
        conver=round(conver,2)
        conver=str(conver)
        print("el monto en dolares de la moneda ARS es: "+conver)

    else:
        if tipomoneda=="mxn":
            conver=cantidad/mxn_dolar
            conver=round(conver,2)
            conver=(str(conver))
            print("el monto en dolares de la moneda MXN es: "+conver)
