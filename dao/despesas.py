from models.despesa import Despesa
from datetime import datetime
from dao.crud import CRUD

import json

class Despesas(CRUD):
    objetos = []  

    @classmethod
    def abrir(cls):
        try:
            with open("data/despesas.json", mode="r") as arquivo:
                despesas_json = json.load(arquivo)
                for obj in despesas_json:
                    x = Despesa(obj['id'],
                                obj['descricao'],
                                obj['valor'],
                                obj['usuario_id'],
                                obj['metodo_id'],
                                obj['categoria_id'])
                    x.data = datetime.strptime(obj["data"],"%d/%m/%Y %H:%M:%S") 
                    cls.objetos.append(x)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        lista_despesas = []
        for obj in cls.objetos:
            lista_despesas.append(obj.to_dict())
        with open ("data/despesas.json", mode="w") as arquivo:
            json.dump(lista_despesas, arquivo, indent =4)
