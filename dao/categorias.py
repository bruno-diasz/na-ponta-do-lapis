from models.categoria import Categoria
from dao.crud import CRUD
import json

class Categorias(CRUD):
    objetos = []  

    @classmethod
    def abrir(cls):
        try:
            with open("data/categorias.json", mode="r") as arquivo:
                categorias_json = json.load(arquivo)
                for obj in categorias_json:
                    x = Categoria(obj['id'],obj['nome'])
                    cls.objetos.append(x)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        lista_categorias = []
        for obj in cls.objetos:
            lista_categorias.append(obj.to_dict())
        with open ("data/categorias.json", mode="w") as arquivo:
            json.dump(lista_categorias, arquivo, indent =4)
