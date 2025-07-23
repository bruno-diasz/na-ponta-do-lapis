from enum import Enum

class Perfil(Enum):
    ADMIN = "admin"
    MEMBRO = 'membro'

class Usuario:
    def __init__(self,id:int, nome:str, email:str, senha:str, perfil:Perfil, familia_id:int):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfil = perfil
        self.familia_id = familia_id

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

    @property
    def email(self) -> str:
        return self.__email
    @email.setter
    def email(self, valor):
        if not isinstance(valor, str):
             raise TypeError("O email de ser uma string")
        if "@" not in valor:
            raise ValueError("Formato de email inválido!")
        self.__email = valor.strip().lower()

    @property
    def senha(self) -> str:
        return self.__senha
    @senha.setter 
    def senha(self, senha:str):
        if not isinstance(senha, str):
            raise TypeError("O senha de ser uma string")
        self.__senha = senha.strip()

    @property
    def perfil(self):
        return self.__perfil
    @perfil.setter
    def perfil(self,perfil):
        if not isinstance(perfil, Perfil):
            raise TypeError("O perfil deve ser uma instância do ENUM Perfil")
        self.__perfil = perfil

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
    
    #========== Metódos =================

    def __repr__(self):
        return (f"Usuario(id='{self.id}', "
                f"nome='{self.nome}', "
                f"email='{self.email}', "
                f"senha='{self.senha}', "
                f"perfil='{self.perfil}', "
                f"familia_id='{self.familia_id}')")
    
    def to_dict(self):
        return{
            "id":self.id,
            "nome":self.nome,
            "email":self.email,
            "senha":self.senha,
            "perfil":self.perfil,
            "familia_id":self.familia_id
        }



#u = Usuario(0,'bruno','teste@','1234','ADMIN',0)
#print(u)