from enum import Enum

class Tipo(Enum):
    DEBITO = 'debito'
    CREDITO = 'credito'

class MetodoDePagamento:
    def __init__(self, id:int, nome:str, tipo, saldo_total:float, familia_id:int):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.saldo_total = saldo_total
        self.familia_id = familia_id
        self.__saldo_atual = saldo_total


    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        if id < 0 :
            raise ValueError("O id deve ser um numero positivo")
        if not isinstance(id, int):
            raise TypeError("O id deve ser um número inteiro")
        self.__id = id

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        if nome.strip() == "":
            raise ValueError("O campo de nome não pode estar vazio")
        self.__nome = nome.strip().title()

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo:Tipo):
        if not isinstance(tipo, Tipo):
            raise TypeError("O tipo deve ser uma instancia do Enum Tipo")
        self.__tipo = tipo

    @property
    def saldo_total(self):
        return self.__saldo_total
    @saldo_total.setter
    def saldo_total(self,saldo_total):
        if not isinstance(saldo_total, (int,float)):
            raise TypeError("O saldo total deve ser um número")
        if saldo_total <= 0:
            raise ValueError("O valor do saldo total deve ser maior do que 0")
        self.__saldo_total = saldo_total

    @property
    def saldo_atual(self):
        return self.__saldo_atual
    @saldo_atual.setter
    def saldo_atual(self,saldo_atual):
        if not isinstance(saldo_atual, (int,float)):
            raise TypeError("O saldo atual deve ser um número")
        if saldo_atual < 0:
            raise ValueError("O valor do saldo atual deve ser positivo")
        self.__saldo_atual = saldo_atual
    
    @property
    def familia_id(self):
        return self.__familia_id
    @familia_id.setter
    def familia_id(self, familia_id):
        if familia_id < 0 :
            raise ValueError("O id deve ser um numero positivo")
        if not isinstance(familia_id, int):
            raise TypeError("O id deve ser um número inteiro")
        self.__familia_id = familia_id

    #==== Métodos =====
    def __repr__(self):
        return (f"MetodoDePagamento(id='{self.id}', "
                f"nome='{self.nome}', "
                f"tipo='{self.tipo}', "
                f"saldo_total='{self.saldo_total}', "
                f"familia_id='{self.familia_id}', "
                f"saldo_atual='{self.saldo_atual}')")
    
    def to_dict(self):
        return{
            "id":self.id,
            "nome":self.nome,
            "tipo":self.tipo,
            "saldo_total":self.saldo_total,
            "familia_id":self.familia_id,
            "saldo_atual":self.saldo_atual
        }
    

    