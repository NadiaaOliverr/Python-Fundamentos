
#Uma classe não é coesa quando ela tem mais responsabildiades do que deveria ter

#A legibilidade é um ponto muito relevante pois no dia a dia o programador gasta muito mais tempo lendo código do que escrevendo!
class Conta:
    def __init__(self, numero, titular, saldo, limite=10.0):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular 
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print(f"Saldo de R$ {self.__saldo} do titular {self.__titular}")
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        self.__saldo = valor
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    def get_saldo(self):
        return self.__saldo
    
    def get_limite(self):
        return self.__limite

    def get_titular(self):
        return self.__titular

    def set_limite(self, limite):
        self.__limite = limite
    
     