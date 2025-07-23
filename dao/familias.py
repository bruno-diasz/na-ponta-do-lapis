from models.familia import Familia
from dao.crud import CRUD
import json

class Familias(CRUD):
    objetos = []  

    @classmethod
    def abrir(cls):
        try:
            with open("data/familias.json", mode="r") as arquivo:
                familias_json = json.load(arquivo)
                for obj in familias_json:
                    x = Familia(obj['id'],obj['nome'])
                    cls.objetos.append(x)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        lista_familias = []
        for obj in cls.objetos:
            lista_familias.append(obj.to_dict())
        with open ("data/familias.json", mode="w") as arquivo:
            json.dump(lista_familias, arquivo, indent =4)
