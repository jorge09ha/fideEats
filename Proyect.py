##########################################################################################

LINE = "---------------------------------------"

cuentaTOTAL = []
itensTOTAL = []
totalpedido = 0

##########################################################################################
#COLORES

class Fore:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    GREY = '\033[90m'
    RESET = '\033[0m'

##########################################################################################
#Combertidor de txt a listas.

import re

codigos = []
productos = []
PecioComidas = []
MenuComidas = []

with open(r"menu.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        x = re.search('(?<=#)\d+',line) #Busca cualquier numero precedido por #
        if x: #Si encuentra coincidencia la imprime
            codigos.append(int(x.group(0)))

        x = re.search('(?<=c)\d+',line) #Busca cualquier numero precedido por c
        if x: #Si encuentra coincidencia la imprime
            PecioComidas.append(int(x.group(0)))

        x = re.search('(?<=-)\w+',line) #Busca cualquier numero precedido por c
        if x: #Si encuentra coincidencia la imprime
            productos.append(str(x.group(0)))

##########################################################################################
#Menu de selecion de pedidos.

def f_pedido():
    print(LINE,Fore.YELLOW+"NUEVO PEDIDO"+Fore.RESET,LINE,sep='\n')
    print ("1. Restaurante", "2. A domicilio", "3. Regresar",LINE, sep='\n')
    nPedido=input("Ingrese algún número de la lista: ")
    print(LINE)
    if nPedido == '1':
        f_restaurante()
    elif nPedido == '2':
        f_domicilio()
    elif nPedido == '3':
        return opcion
    else:
        print (Fore.RED+'Error. Opcion no valida, solo se permiten numeros dentro de la lista'+Fore.RESET,sep='\n')
        print (Fore.RED+'Intente nuevamente.'+Fore.RESET,sep='\n')
        return f_pedido()

##########################################################################################
#Menu de ingreso de dastos pedidos en restaurante.

def f_restaurante():
    print(Fore.YELLOW+"PEDIDO EN RESTAURANTE"+Fore.RESET,LINE,sep='\n')
    print(Fore.GREEN+"Hora De realizar el pedido, El menu se desplegara a continuación"+Fore.RESET,sep='\n')
    f_selecMENU()
    e = 0
    while e < 1:
        for i in range (len(itensTOTAL)):
            print(Fore.YELLOW+"Item #"+str(i+1)+" "+str(itensTOTAL[+i])+" "+str(cuentaTOTAL[+i])+Fore.RESET)

        print(LINE,Fore.YELLOW+"Quiere agregar algo mas?"+Fore.RESET,LINE,sep='\n')
        print("1."+Fore.GREEN+"SI"+Fore.RESET,"2."+Fore.RED+"NO"+Fore.RESET,sep='\n')
        agregarMAS = f_numEntero()
        if agregarMAS == 1:
            f_selecMENU()
        elif agregarMAS == 2:
            print(LINE,Fore.GREEN+"Perfecto, su orden  de platos ha sido tomada con exito."+Fore.RESET,sep='\n')
            f_facturaRES()
            e = e + 1
        else:
            print (LINE,Fore.RED+'Error. Opcion no valida, solo se permiten numeros dentro de la lista'+Fore.RESET,sep='\n')
            print (Fore.RED+'Intente nuevamente.'+Fore.RESET,LINE,sep='\n')

##########################################################################################
#Menu de ingreso de dastos pedidos a domicilio.

def f_domicilio():
    d = 0
    n = 0
    x = 0
    e = 0

    print(Fore.YELLOW+"PEDIDO A DOMICILIO"+Fore.RESET,LINE,sep='\n')
    while d < 1:
        direcc=str(input("Por favor ingrese la direccion de su domicilio: "))
        print(LINE,Fore.YELLOW+'"'+str(direcc)+'"'+Fore.RESET+" es la direccion correcta de su domicilio?",LINE,sep='\n')
        print("1."+Fore.GREEN+"SI"+Fore.RESET,"2."+Fore.RED+"NO"+Fore.RESET,sep='\n')
        confirDIREC = f_numEntero()
        if confirDIREC == 1:
            d = d + 1
            print(LINE,"Perfecto, la direccion es "+Fore.GREEN+str(direcc)+Fore.RESET,LINE,sep='\n')
        elif confirDIREC == 2:
            print(LINE,Fore.YELLOW+"Cual es la direccion?"+Fore.RESET,LINE,sep='\n')
        else:
            print (LINE,Fore.RED+'Error. Opcion no valida, solo se permiten numeros dentro de la lista'+Fore.RESET,sep='\n')
            print (Fore.RED+'Intente nuevamente.'+Fore.RESET,LINE,sep='\n')

    while x < 1:
        print ("Segun la direccion: "+Fore.YELLOW+str(direcc)+Fore.RESET+", cual es el valor del envio:"," ",sep='\n')
        envio=f_numEntero()

        print(LINE,Fore.YELLOW+'" ₡'+str(envio)+'"'+Fore.RESET+" es el monto correcto de envio?",LINE,sep='\n')
        print("1."+Fore.GREEN+"SI"+Fore.RESET,"2."+Fore.RED+"NO"+Fore.RESET,sep='\n')
        confirDIREC = f_numEntero()
        if confirDIREC == 1:
            x = x + 1
            print(LINE,"Perfecto, el monto de envio es: "+Fore.GREEN+"₡"+str(envio)+Fore.RESET,LINE,sep='\n')
        elif confirDIREC == 2:
            print(LINE,Fore.YELLOW+"Cual es el monto de envio?"+Fore.RESET,LINE,sep='\n')
        else:
            print (LINE,Fore.RED+'Error. Opcion no valida, solo se permiten numeros dentro de la lista'+Fore.RESET,sep='\n')
            print (Fore.RED+'Intente nuevamente.'+Fore.RESET,LINE,sep='\n')

    while n < 1:
        numTEL=str(input("Por favor ingrese el numero de telefono: "))
        print(LINE,Fore.YELLOW+'"'+str(numTEL)+'"'+Fore.RESET+" es el numero de telefono correcto?",LINE,sep='\n')
        print("1."+Fore.GREEN+"SI"+Fore.RESET,"2."+Fore.RED+"NO"+Fore.RESET,sep='\n')
        confirTEL = f_numEntero()
        if confirTEL == 1:
            n = n + 1
            print(LINE,"Perfecto, El numero es: "+Fore.GREEN+str(numTEL)+Fore.RESET,LINE,sep='\n')
        elif confirTEL == 2:
            print(LINE,Fore.YELLOW+"Cual es el numero?"+Fore.RESET,LINE,sep='\n')
        else:
            print (LINE,Fore.RED+'Error. Opcion no valida, solo se permiten numeros dentro de la lista'+Fore.RESET,sep='\n')
            print (Fore.RED+'Intente nuevamente.'+Fore.RESET,LINE,sep='\n')

    f_selecMENU()

    while e < 1:
        for i in range (len(itensTOTAL)):
            print(Fore.YELLOW+"Item #"+str(i+1)+" "+str(itensTOTAL[+i])+" "+str(cuentaTOTAL[+i])+Fore.RESET)

        print(LINE,Fore.YELLOW+"Quiere agregar algo mas?"+Fore.RESET,LINE,sep='\n')
        print("1."+Fore.GREEN+"SI"+Fore.RESET,"2."+Fore.RED+"NO"+Fore.RESET,sep='\n')
        agregarMAS = f_numEntero()
        if agregarMAS == 1:
            f_selecMENU()
        elif agregarMAS == 2:
            print(LINE,Fore.GREEN+"Perfecto, su orden  de platos ha sido tomada con exito."+Fore.RESET,sep='\n')
            f_facturaDOMI(direcc,envio,numTEL)
            print (LINE,Fore.GREEN+"El Pedido sera enviado a: "+Fore.YELLOW+str(direcc)+Fore.RESET,sep='\n')
            print (Fore.GREEN+"El numero de telefono es: "+Fore.YELLOW+str(numTEL)+Fore.RESET,sep='\n')
            e = e + 1
        else:
            print (LINE,Fore.RED+'Error. Opcion no valida, solo se permiten numeros dentro de la lista'+Fore.RESET,sep='\n')
            print (Fore.RED+'Intente nuevamente.'+Fore.RESET,LINE,sep='\n')

##########################################################################################
#Seleccion de platos del menu.

def f_selecMENU():

    menuTXT = open('menu.txt')
    menu = menuTXT.read()
    print(Fore.YELLOW)
    print ("{:<6} {:<25} {:<15}".format('ITEM', 'PRODUCTO', 'PRECIO'),LINE,sep='\n')
    print(menu)
    print(Fore.RESET)
    menuTXT.close()

    print(Fore.GREEN+"Por favor ingrese el # de ITEM"+Fore.RESET,LINE,sep='\n')
    pedido  = f_numEntero()

    print(LINE,"El ITEM: "+Fore.YELLOW+str(pedido)+Fore.RESET+" es el correcto?",LINE,sep='\n')
    print("1."+Fore.GREEN+"SI"+Fore.RESET,"2."+Fore.RED+"NO"+Fore.RESET,sep='\n')
    confirPEDIDO = f_numEntero()

    #print ("Total a pagar $:",cuentaTOTAL)

    if confirPEDIDO == 1:
        j=0
        while j < 1:
            print(LINE,"Perfecto, se agrega el ITEM "+Fore.GREEN+str(pedido)+Fore.RESET+" al pedido.","",sep='\n')
            if pedido==1:
                cuentaTOTAL.append(PecioComidas[0])
                itensTOTAL.append(productos[0])
                j = j + 1
            elif pedido==2:
                cuentaTOTAL.append(PecioComidas[1])
                itensTOTAL.append(productos[1])
                j = j + 1
            elif pedido==3:
                cuentaTOTAL.append(PecioComidas[2])
                itensTOTAL.append(productos[2])
                j = j + 1
            elif pedido==4:
                cuentaTOTAL.append(PecioComidas[3])
                itensTOTAL.append(productos[3])
                j = j + 1
            elif pedido==5:
                cuentaTOTAL.append(PecioComidas[4])
                itensTOTAL.append(productos[4])
                j = j + 1
            elif pedido==6:
                cuentaTOTAL.append(PecioComidas[5])
                itensTOTAL.append(productos[5])
                j = j + 1
            elif pedido==7:
                cuentaTOTAL.append(PecioComidas[6])
                itensTOTAL.append(productos[6])
                j = j + 1
            elif pedido==8:
                cuentaTOTAL.append(PecioComidas[7])
                itensTOTAL.append(productos[7])
                j = j + 1
            elif pedido==9:
                cuentaTOTAL.append(PecioComidas[8])
                itensTOTAL.append(productos[8])
                j = j + 1
            elif pedido==10:
                cuentaTOTAL.append(PecioComidas[9])
                itensTOTAL.append(productos[9])
                j = j + 1
            else:
                print (LINE,Fore.RED+'Error. Opcion no valida, solo se permiten numeros dentro de la lista'+Fore.RESET,sep='\n')
                print (Fore.RED+'Intente nuevamente.'+Fore.RESET,LINE,sep='\n')

    elif confirPEDIDO == 2:
        print(LINE,Fore.YELLOW+"Cual es el # de ITEM?"+Fore.RESET,LINE,sep='\n')
        file = open('menu.txt')
        menu = file.read()
        print(Fore.YELLOW)
        print ("{:<6} {:<25} {:<15}".format('ITEM', 'PRODUCTO', 'PRECIO'),LINE,sep='\n')
        print(menu)
        print(Fore.RESET)
    else:
        print (LINE,Fore.RED+'Error. Opcion no valida, solo se permiten numeros dentro de la lista'+Fore.RESET,sep='\n')
        print (Fore.RED+'Intente nuevamente.'+Fore.RESET,LINE,sep='\n')

##########################################################################################
#Login para acceso a los datos financieros.

def f_loging():
    import getpass
    count = 0
    print(LINE,Fore.YELLOW+'Ingresar el usuario y contraseña correcto para continuar.'+Fore.RESET,LINE,sep='\n')

    while count<3:
        username=input('Username: ')
        password = getpass.getpass('Password: ')
        if  username=='admin' and password=='admin01' :
            print(LINE,Fore.GREEN+'ACCESO CORRECTO'+Fore.RESET,sep='\n')
            count=4
            f_finanzas()
        else:
            print(LINE,Fore.RED+'Access denegado.'+Fore.RESET,sep='\n')
            count+=1
    return opcion

##########################################################################################
#Menu de datos financieros.

def f_finanzas():
    print(LINE,Fore.MAGENTA+"ESTADOS FINANCIEROS"+Fore.RESET,LINE,sep='\n')

    print ("1. Estado Financieros", "2. Consultar Facturas", "3. Regresar",LINE, sep='\n')
    menuFINAN=input("Ingrese algún número de la lista: ")
    print(LINE)
    if menuFINAN == '1':
        f_EstadosF()
    elif menuFINAN == '2':
        f_facturas()
    elif menuFINAN == '3':
        return opcion
    else:
        print (Fore.RED+'Error. Opcion no valida, solo se permiten numeros dentro de la lista'+Fore.RESET,sep='\n')
        print (Fore.RED+'Intente nuevamente.'+Fore.RESET,sep='\n')
        f_finanzas()

##########################################################################################
#Ventas totales.
def f_EstadosF():

    gananciasTXT = open("Finanzas/Ganancias.txt","r")
    ganancias = gananciasTXT.read()
    gananciasTXT.close()

    haciendaTXT = open("Finanzas/Hacienda.txt","r")
    hacienda = haciendaTXT.read()
    haciendaTXT.close()

    print(Fore.MAGENTA)
    print("Las ganancias son de: ₡",ganancias)
    print("Monto destinado para Hacienda : ₡",hacienda)
    print(Fore.RESET)

    f_finanzas()
##########################################################################################
#Consultar Facturas.
def f_facturas():
    print(LINE,Fore.MAGENTA+"VER FACTURAS"+Fore.RESET,LINE,sep='\n')

    facturaR = open("Finanzas/NumeroFactura.txt","r")
    nunFACTURA = facturaR.read()
    nunFACTURA = int(nunFACTURA)-1
    facturaR.close()

    print("La cantidad de facturas es de: ", nunFACTURA)
    print("")
    facturas = int(input("Ingrese el numero de factura a consultar: "))

    estado = True
    while estado:
        estado = False
        if facturas <= nunFACTURA and facturas > 0:
            archivo = open("Facturas/factura"+str(facturas)+".txt")
            mostrar_factura = archivo.read()
            print(Fore.YELLOW)
            print(mostrar_factura)
            print(Fore.RESET)
            archivo.close()
            f_finanzas()
        else:
            print(LINE+Fore.RED,"Factura no existe."+Fore.RESET,sep='\n')
            f_finanzas()

##########################################################################################
#Facturacion.

#Facturacion Restaurante.
def f_facturaRES():
    print("Hora de hacer la factura del pedido en restaurante")

    facturaR = open("Finanzas/NumeroFactura.txt","r")
    nunFACTURA = facturaR.read()
    newFACTURA = int(nunFACTURA)+1
    facturaR.close()

    facturaW = open("Finanzas/NumeroFactura.txt","w")
    facturaW.write(str(newFACTURA))
    facturaW.close()

    total=0
    iva=.13
    t_iva=0
    total_final=0
    item=0

    print(LINE,Fore.MAGENTA+'FACTURA #'+str(nunFACTURA),LINE,sep='\n')


    facturaTXT = open("Facturas/factura"+str(nunFACTURA)+".txt", "w")
    facturaTXT.write(LINE+"\n"+'FACTURA #'+nunFACTURA+"\n"+LINE+"\n")

    for i in range (len(cuentaTOTAL)):
        item=item+1
        print("Item #"+str(i+1)+" "+str(itensTOTAL[+i])+" "+str(cuentaTOTAL[+i]))
        facturaTXT.write("Item #"+str(i+1)+" "+str(itensTOTAL[+i])+" "+str(cuentaTOTAL[+i])+"\n")
        total=(cuentaTOTAL[+i])+total
    print(LINE,"Total: ₡ " + str(total),LINE,sep='\n')
    t_iva=iva*total
    print("IVA: ₡ " + str(t_iva),LINE,sep='\n')
    total_final=total+t_iva
    print("Total a pagar: ₡ " + str(total_final)+Fore.RESET,sep='\n')

    facturaTXT.write(LINE+"\n"+"Total: "+str(total)+"\n"+LINE+"\n")
    facturaTXT.write("IVA: "+str(t_iva)+"\n"+LINE+"\n")
    facturaTXT.write("Total a pagar: "+str(total_final)+"\n"+LINE+"\n")
    facturaTXT.close()

    gananciasR = open("Finanzas/Ganancias.txt","r")
    ganancias = gananciasR.read()
    new_ganancias = int(ganancias)+total
    gananciasR.close()
    gananciasW = open("Finanzas/Ganancias.txt","w")
    gananciasW.write(str(new_ganancias))
    gananciasW.close()

    haciendaR = open("Finanzas/Hacienda.txt","r")
    hacienda = haciendaR.read()
    new_hacienda = float(hacienda)+t_iva
    haciendaR.close()
    haciendaW = open("Finanzas/Hacienda.txt","w")
    haciendaW.write(str(new_hacienda))
    haciendaW.close()

    cuentaTOTAL.clear()
    itensTOTAL.clear()

#Facturacion Domicilio.
def f_facturaDOMI(direcc,envio,numTEL):
    print("Hora de hacer la factura del pedido a domicilio")

    facturaR = open("Finanzas/NumeroFactura.txt","r")
    nunFACTURA = facturaR.read()
    newFACTURA = int(nunFACTURA)+1
    facturaR.close()

    facturaW = open("Finanzas/NumeroFactura.txt","w")
    facturaW.write(str(newFACTURA))
    facturaW.close()

    total=0
    iva=.13
    t_iva=0
    total_final=0
    item=0

    print(LINE,Fore.MAGENTA+'FACTURA #'+str(nunFACTURA),LINE,sep='\n')

    facturaTXT = open("Facturas/factura"+str(nunFACTURA)+".txt", "w")
    facturaTXT.write(LINE+"\n"+'FACTURA #'+nunFACTURA+"\n"+LINE+"\n")

    for i in range (len(cuentaTOTAL)):
        item=item+1
        print("Item #"+str(i+1)+" "+str(itensTOTAL[+i])+" "+str(cuentaTOTAL[+i]))
        facturaTXT.write("Item #"+str(i+1)+" "+str(itensTOTAL[+i])+" "+str(cuentaTOTAL[+i])+"\n")
        total=(cuentaTOTAL[+i])+total
    print(LINE,"Total: ₡ " + str(total),LINE,sep='\n')
    total=total+envio
    t_iva=iva*total
    print("Envio: ₡ " + str(envio),LINE,sep='\n')
    print("IVA: ₡ " + str(t_iva),LINE,sep='\n')
    total_final=total+t_iva

    print("Total a pagar: ₡ " + str(total_final)+Fore.RESET,sep='\n')

    facturaTXT.write(LINE+"\n"+"Total: "+str(total)+"\n"+LINE+"\n")
    facturaTXT.write("IVA: "+str(t_iva)+"\n"+LINE+"\n")
    facturaTXT.write("Envio: "+str(envio)+"\n"+LINE+"\n")
    facturaTXT.write("Total a pagar: "+str(total_final)+"\n"+LINE+"\n")
    facturaTXT.write("Direccion: "+direcc+"\n")
    facturaTXT.write("Telefono: "+numTEL+"\n"+LINE+"\n")
    facturaTXT.close()

    gananciasR = open("Finanzas/Ganancias.txt","r")
    ganancias = gananciasR.read()
    new_ganancias = int(ganancias)+total
    gananciasR.close()
    gananciasW = open("Finanzas/Ganancias.txt","w")
    gananciasW.write(str(new_ganancias))
    gananciasW.close()

    haciendaR = open("Finanzas/Hacienda.txt","r")
    hacienda = haciendaR.read()
    new_hacienda = float(hacienda)+t_iva
    haciendaR.close()
    haciendaW = open("Finanzas/Hacienda.txt","w")
    haciendaW.write(str(new_hacienda))
    haciendaW.close()

    cuentaTOTAL.clear()
    itensTOTAL.clear()
##########################################################################################
#Ingreso de SOLO numeros enteros.

def f_numEntero():

    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opcion: "))
            correcto=True
        except ValueError:
            print(LINE,Fore.RED+'Error. introducir numeros valido'+Fore.RESET,LINE,sep='\n')
    return num

##########################################################################################
#Opcines menu principal.

def f_opcion():

    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input('Ingrese algún número de la lista: '))
            correcto=True
        except ValueError:
            print (LINE,Fore.RED+'Error. Opcion no valida, solo se permiten numeros enteros'+Fore.RESET,sep='\n')
            print (Fore.RED+'Intente nuevamente.'+Fore.RESET,sep='\n')
            print(LINE,Fore.CYAN+"MENU PRINCIPAL"+Fore.RESET,LINE,sep='\n')
            print ("1. Nuevo Pedido","2. Estados Financieros","3. Salir",LINE,sep='\n')
    return num

##########################################################################################
#Menu principal

salir = False
opcion = 0
print(LINE)
print("""
  _ ___  _   _     _     ___ __ 
 |_  |  | \ |_ |  |_  /\  | (_  
 |  _|_ |_/ |_ |_ |_ /--\ | __) 
                                
""")

print(LINE,Fore.GREEN+"Bienvenido al Restaurante Fideleats"+Fore.RESET,sep='\n')
while not salir:

    print(LINE,Fore.CYAN+"MENU PRINCIPAL"+Fore.RESET,LINE,sep='\n')
    print ("1. Nuevo Pedido","2. Estados Financieros","3. Salir",LINE,sep='\n')

    opcion = f_opcion()

    if opcion == 1:
        f_pedido()
    elif opcion == 2:
        f_loging()
    elif opcion == 3:
        salir = True
        #print (f_menu)
    else:
        print (LINE,Fore.RED+'Error. Opcion no valida, solo se permiten numeros enteros'+Fore.RESET,sep='\n')
        print (Fore.RED+'Intente nuevamente.'+Fore.RESET,sep='\n')

print (LINE,Fore.GREEN+"Gracias por usar nuestro programa"+Fore.RESET,LINE,sep='\n')