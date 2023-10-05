class Procedure:
    def __init__(self,procedure,date,pract,charge,Id):
        self.__procedure=procedure
        self.__date=date
        self.__pract=pract
        self.__charge=charge
        self.__Id=Id
    def get_procedure(self):
        return self.__procedure
    def get_date(self):
        return self.__date
    def get_pract(self):
        return self.__pract
    def get_charge(self):
        return self.__charge
    def get_Id(self):
        return self.__Id