from abc import ABC, abstractmethod

class CRUD(ABC):

    objetos = []

    @classmethod
    def inserir(cls, obj:object):
        cls.abrir()
       
        for elemento in cls.objetos:
            if elemento.id >= obj.id:
                 obj.id = elemento.id + 1

        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list[object]:
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id:int):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x is not None: 
            cls.objetos.remove(x)
            cls.objetos.insert(obj.id,obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x is not None: 
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    @abstractmethod
    def salvar(cls):
        pass

    @classmethod
    @abstractmethod
    def abrir(cls):
        pass
