from datetime import datetime

class Ticket():
    def __init__(self,matricula,plaza,coste,pin,fec_ent=datetime.now(),fec_sal=datetime.now()):
        self.__fec_ent=fec_ent
        self.__fec_sal=fec_sal
        self.__matricula=matricula
        self.__plaza=plaza
        self.__coste=coste
        self.__pin=pin
        
    @property
    def fec_ent(self):
        return self.__fec_ent
    
    @fec_ent.setter
    def fec_ent(self, fec_ent):
        self.__fec_ent=fec_ent
        
    @property
    def fec_sal(self):
        return self.__fec_sal
    
    @fec_sal.setter
    def fec_sal(self, fec_sal):
        self.__fec_sal=fec_sal
        
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula=matricula
    
    @property
    def plaza(self):
        return self.__plaza
    
    @plaza.setter
    def plaza(self, plaza):
        self.__plaza=plaza

    @property
    def coste(self):
        return self.__coste

    @coste.setter
    def coste(self, coste):
        self.__coste=coste
        
    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin=pin
