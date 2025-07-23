from models.metodo_pagamento import MetodoDePagamento,Tipo
from dao.crud import CRUD

import json

class MetodosDePagamento(CRUD):
    objetos = []  

    @classmethod
    def abrir(cls):
        try:
            with open("data/metodos_de_pagamento.json", mode="r") as arquivo:
                metodos_json = json.load(arquivo)
                for obj in metodos_json:
                    x = MetodoDePagamento(obj['id'],
                                obj['nome'],
                                Tipo(obj['tipo']),
                                obj['saldo_total'],
                                obj['familia_id'])
                    cls.objetos.append(x)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        lista_metodos = []
        for obj in cls.objetos:
            lista_metodos.append(obj.to_dict())
        with open ("data/metodos_de_pagamento.json", mode="w") as arquivo:
            json.dump(lista_metodos, arquivo, indent =4)
