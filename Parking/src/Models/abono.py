class Abono():
    def __init__(self,Cliente,fec_ini,fec_fin,meses,precio,pin,plaza):
        self.__Cliente=Cliente
        self.__fec_ini=fec_ini
        self.__fec_fin=fec_fin
        self.__meses=meses
        self.__precio=precio
        self.__pin=pin
        self.__plaza=plaza

    @property
    def Cliente(self):
        return self.__Cliente

    @Cliente.setter
    def Cliente(self, Cliente):
        self.__Cliente=Cliente

    @property
    def fec_ini(self):
        return self.__fec_ini

    @fec_ini.setter
    def fec_inc(self, fec_ini):
        self.__fec_ini=fec_ini
    @property
    def fec_fin(self):
        return self.__fec_fin

    @fec_fin.setter
    def fec_fin(self, fec_fin):
        self.__fec_fin=fec_fin

    @property
    def meses(self):
        return  self.__meses

    @meses.setter
    def meses(self, meses):
        self.__meses=meses

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio=precio

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza=plaza
        
