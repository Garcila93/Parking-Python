class Parking():

    def __init__(self,lista_turismos,lista_motos,lista_minus,lista_clientes):
        self.__lista_turismos=lista_turismos
        self.__lista_motos=lista_motos
        self.__lista_minus=lista_minus
        self.__lista_clientes=lista_clientes

    @property
    def listaTurismo(self):
        return self.__lista_turismos

    @listaTurismo.setter
    def listaTurismo(self, listaTurismos):
        self.__lista_turismos=listaTurismos

    @property
    def listaMotos(self):
        return self.__lista_motos

    @listaMotos.setter
    def listaMotos(self, listaMotos):
        self.__lista_motos=listaMotos

    @property
    def listaMinus(self):
        return self.__lista_minus

    @listaMinus.setter
    def listaMinus(self, listaMinus):
        self.__lista_minus=listaMinus

    @property
    def listaClientes(self):
        return self.__lista_clientes

    @listaClientes.setter
    def listaClientes(self, listaClientes):
        self.__lista_clientes=listaClientes
