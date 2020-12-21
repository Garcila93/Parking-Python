from src.Models.abono import Abono
from src.Models.cliente import Cliente
from src.Models.factura import Factura
from src.Models.parking import Parking
from src.Models.plaza import Plaza
from src.Models.ticket import Ticket
from src.Models.vehiculo import Vehiculo
from src.Controller.ParkingController import ParkingController
import pickle
import numpy as np
import datetime as dt

plazasParking=int(input("Inserte el número de plazas que tendra el parking\n"))
p=Parking()
pc=ParkingController()
p.listaTurismo=np.full(round(plazasParking*0.7),None)
p.listaMinus=np.full(round(plazasParking*0.15),None)
p.listaMotos=np.full(round(plazasParking*0.15),None)
adminpass=1234
v1=Vehiculo("3958-CXT","Turismo")
v2=Vehiculo("1234-BCD","Moto")
v3=Vehiculo("9876-FGH","Minus")
pl1=Plaza(1,"Turismo",None,None)
t1=Ticket()
op=1

while op!="0":
    print("Bienvenido a nuestro parking\n"
          "Pulse [1] para acceder al parking sin abono\n"
          "Pulse [2] para acceder al parking con abono\n"
          "Pulse [3] para acceder en modo Administrador")
    op=input()
    if op=="1":
        op1=-1
        while op1!="0":
            print("Pulse [1] para guardar su vehiculo\n"
                  "Pulse [2] para retirar su vehiculo\n"
                  "Pulse [0] para volver atras")
            op1=input()
            if op1=="1":
                tipo=input("¿Qué tipo de vehiculo va a depositar?(Turismo, Moto, Minus)")
                matricula=input("A continuacion introduzca la matricula")
                if tipo.lower()=="turismo":
                    nuevoVehiculo=Vehiculo(matricula,tipo)
                    pc.asignarPlaza(nuevoVehiculo,Plaza,p)
                    pc.generarTicket(t1)
                elif tipo.lower()=="moto":
                    nuevoVehiculo=Vehiculo(matricula,tipo)
                    pc.asignarPlaza(nuevoVehiculo,Plaza,p)
                    pc.generarTicket(t1)
                else :
                    nuevoVehiculo=Vehiculo(matricula,tipo)
                    pc.asignarPlaza(nuevoVehiculo,Plaza,p)
                    pc.generarTicket(t1)

            if op1=="2":
                matricula=input("Introduzca la matricula del vehiculo que desea retirar")
                numpl=input("Introduzca el numero de plaza que se le asigno a su vehiculo")
                pin=input("Introduzca el pin que aparece en el ticket para retirar el vehiculo")
                pc.retirarVehiculo(Plaza,Ticket,matricula,pin,numpl)
    elif op=="2":
        op2=-1
        while op2!="0":
            print("Bienvenido a la zona de abonados")
            op2=input()
    elif op=="3":
        clave=input("Introduzca clave de Admin")
        if clave==adminpass:
            op3=-1
            while op3!="0":
                print("Bienvenido a la zona de Administración, ¿Qué desea realizar?\n"
                      "[1] Consultar estado del parking\n"
                      "[2] Comprobar Facturación\n"
                      "[3] Consultar Abonados\n"
                      "[4] Dar de Alta a un Abonado")
                op3=input()
                if op3=="1":
                    print()
                if op3=="2":
                    print()
                if op3=="3":
                    print()
                if op3=="4":
                    print("A continuacion inserte los datos necesarios para dar de alta a un nuevo abonado")
                    dni=input("Inserte DNI")
                    nombre=input("Inserte el nombre")
                    apellidos=input("Inserte los apellidos")
                    num_tarjeta=input("Inserte el número de la tarjeta donde se realizará el cobro")
                    email=input("Inserte el email")
                    tipo=input("Inserte el tipo de vehiculo que tiene el cliente")
                    matricula=input("Inserte la mátricula del vehiculo")
                    nuevoVehCliente=Vehiculo(matricula,tipo)
                    nuevoCLiente=Cliente(dni,nombre,apellidos,num_tarjeta,email,nuevoVehCliente)
                    fec_ini=dt.datetime.now()
                    meses=input("¿De cuanto tiempo sera el abono?, introduzca la fecha en numero de meses")
                    if meses==1:
                        precioAbono=25
                    elif meses==3:
                        precioAbono=70
                    elif meses==6:
                        precioAbono=130
                    elif meses==12:
                        precioAbono==200
                    fec_fin=fec_ini+fec_ini.timedelta(months=meses)
                    pin=input("Introducir pin deseado por el cliente")
                    plazaCliente=ParkingController.asignarPlazaAbonado()
                    nuevoAbono=Abono(nuevoCLiente,fec_ini,fec_fin,meses,precioAbono,pin,plazaCliente)
                    pc.Parking.listaClientes.append(nuevoAbono)
                    print("Nuevo Abonado registrado")
                else:
                    print("Opción no válida")
        else:
            print("Contraseña incorrecta!!")
    else:
        print("Opción no válida")
