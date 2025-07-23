from datetime import datetime

class Despesa:
    def __init__(self, id:int, descricao:str, valor:float, usuario_id:int, metodo_id:int, categoria_id:int):
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.usuario_id = usuario_id
        self.metodo_id = metodo_id
        self.categoria_id = categoria_id
        self.__data = datetime.now()
        
    #==== Getters e Setters =====

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
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self,descricao):
        if descricao.strip() == "":
            raise ValueError("O campo de descricao não pode estar vazio")
        self.__descricao = descricao.strip().title()

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self,valor):
        if not isinstance(valor, (int,float)):
            raise TypeError("O valor da despesa deve ser um número")
        if valor <= 0:
            raise ValueError("O valor do despesa deve ser maior do que 0")
        self.__valor = valor

    @property
    def usuario_id(self):
        return self.__usuario_id
    @usuario_id.setter
    def usuario_id(self, usuario_id):
        if usuario_id < 0 :
            raise ValueError("O usuario_id deve ser um numero positivo")
        if not isinstance(usuario_id, int):
            raise TypeError("O usuario_id deve ser um número inteiro")
        self.__usuario_id = usuario_id
    
    @property
    def metodo_id(self):
        return self.__metodo_id
    @metodo_id.setter
    def metodo_id(self, metodo_id):
        if metodo_id < 0 :
            raise ValueError("O metodo_id deve ser um numero positivo")
        if not isinstance(metodo_id, int):
            raise TypeError("O metodo_id deve ser um número inteiro")
        self.__metodo_id = metodo_id

    @property
    def categoria_id(self):
        return self.__categoria_id
    @categoria_id.setter
    def categoria_id(self, categoria_id):
        if categoria_id < 0 :
            raise ValueError("O categoria_id deve ser um numero positivo")
        if not isinstance(categoria_id, int):
            raise TypeError("O categoria_id deve ser um número inteiro")
        self.__categoria_id = categoria_id
    
    #======= Métodos  ======
    def __repr__(self):
        return (f"Despesa(id='{self.id}', "
                f"descricao='{self.descricao}', "
                f"valor='{self.valor}', "
                f"usuario_id='{self.usuario_id}', "
                f"metodo_id='{self.metodo_id}', "
                f"categoria_id='{self.categoria_id}', "
                f"data='{self.__data}")
    
    def to_dict(self):
        return {
            "id":self.id,
            "descricao":self.descricao,
            "valor":self.valor,
            "usuario_id":self.usuario_id,
            "metodo_id":self.metodo_id,
            "categoria_id":self.categoria_id,
            "data":self.__data
        }
        
