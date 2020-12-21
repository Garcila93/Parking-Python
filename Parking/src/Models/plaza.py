class Plaza:
    def __init__(self,num_plaza,tipo,ocupada,reservada,coste_min,vehiculo):
        self.__num_plaza=num_plaza
        self.__tipo=tipo
        self.__ocupada=ocupada
        self.__reservada=reservada
        self.__coste_min=coste_min
        self.__vehiculo=vehiculo
        
    @property
    def num_plaza(self):
        return self.__num_plaza
    
    @num_plaza.setter
    def num_plaza(self, num_plaza):
        self.__num_plaza=num_plaza

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo=tipo

    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self, ocupada):
        self.__ocupada=ocupada

    @property
    def reservada(self):
        return self.__reservada

    @reservada.setter
    def reservada(self, reservada):
        self.__reservada=reservada

    @property
    def costeMin(self):
        return self.__coste_min

    @costeMin.setter
    def costeMin(self, costeMin):
        self.__coste_min=costeMin

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo=vehiculo
