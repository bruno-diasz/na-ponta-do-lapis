class Categoria:
    def __init__(self, id:int, nome:str):
        self.id = id
        self.nome = nome

    #=========== Getters e Setters ============
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

    #====== Metódos ======

    def __repr__(self):
        return f"Categoria(id='{self.id}, nome='{self.nome}')"
    
    def to_dict(self):
        return {"id":self.id, "nome":self.nome}