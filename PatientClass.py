class Patient:
    def __init__(self, Id, name, phone, vet_stat,address):
        self.__id=Id
        self.__name=name
        self.__phone=phone
        self.__vet_stat=vet_stat
        self.__address=address
    def get_id (self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_vet_stat(self):
        return self.__vet_stat
    def get_address (self):
        return self.__address
