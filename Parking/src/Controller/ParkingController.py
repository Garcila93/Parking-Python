import random as r

class ParkingController:

    def __init__(self,Vehiculo,Parking,Plaza,Ticket):
        self.__Parking=Parking
        self.__Vehiculo=Vehiculo
        self.__Plaza=Plaza
        self.__Ticket=Ticket

    @property
    def Parking(self):
        return self.__Parking
    @Parking.setter
    def Parking(self, Parking):
        self.__Parking=Parking
    @property
    def Vehiculo(self):
        return self.__Vehiculo
    @Vehiculo.setter
    def Vehiculo(self, Vehiculo):
        self.__Vehiculo= Vehiculo
    @property
    def Plaza(self):
        return self.__Plaza

    @Plaza.setter
    def Plaza(self, Plaza):
        self.__Plaza=Plaza

    @property
    def Ticket(self):
        return self.__Ticket

    @Ticket.setter
    def Ticket(self, Ticket):
        self.__Ticket=Ticket

    def asignarPlaza(self,Vehiculo,Plaza,Parking):
        print("Buscando plaza")
        if Vehiculo.tipo=="Turismo":

            numpla=r.randint(0,len(Parking.listaTurismo))
            if numpla==None:
                plaza=Plaza(numpla,"Turismo",True,False,0.12,Vehiculo)
                Parking.listaTurismo.append(plaza)
                return print("Plaza de turismo encontrada")
            else: ParkingController.asignarPlaza()

        elif Vehiculo.tipo=="Moto":
            numpla=r.randint(0,len(Parking.listaMotos))
            if numpla==None:
                plaza=Plaza(numpla,"Moto",True,False,0.08,Vehiculo)
                Parking.listaMotos.append(plaza)
                return print("Plaza de Motocicleta encontrada")
            else: ParkingController.asignarPlaza()

        else:
            numpla=r.randint(0,len(Parking.listaMinus))
            if numpla==None:
                plaza=Plaza(numpla,"Minusvalido",True,False,0.10,Vehiculo)
                Parking.listaMinus.append(plaza)
                return print("Plaza para vehiculos de movilidad reducida encontrada")
            else: ParkingController.asignarPlaza()

    def generarTicket(self,Ticket):
        print("********** Generando Ticket **********\n")
        print(f'Matricula del vehiculo ${Ticket.matricula}\n'
              f'Estacionado el día ${Ticket.fec_ent.strftime("%A %d %B %Y %I:%M")}\n'
              f'Su pin ${Ticket.pin}\n'
              f'Gracias por usar nuestros servicios')
    
    def retirarVehiculo(self,Plaza,Ticket,matricula=None,pin=None,num_pl=None):
        if matricula==Plaza.vehiculo.matricula and num_pl==Plaza.num_plaza and pin==Ticket.pin:
            ParkingController.generarTicket()
            Plaza.vehiculo=None
            return Plaza.vehiculo
        else:
            print("Vehiculo no encontrado")


    def crearAbonado(self,Abono,Cliente):
        Abono.Cliente=Cliente

    def asignarPlazaAbonado(self,Vehiculo,Plaza,Parking):

            numpla=r.randint(0,len(Parking.listaTurismo))
            if numpla==None:
                plaza=Plaza(numpla,Vehiculo.tipo,True,True,0,Vehiculo)
                Parking.listaTurismo.append(plaza)
                return print("Plaza asiganada a cliente")
            else: ParkingController.asignarPlazaAbonado()

   # def retirarVehiculoAbonado(self):







