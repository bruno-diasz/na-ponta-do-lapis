from models.usuario import Usuario,Perfil
from dao.crud import CRUD

import json

class Usuarios(CRUD):
    objetos = []  

    @classmethod
    def abrir(cls):
        try:
            cls.objetos.clear()
            with open("data/usuarios.json", mode="r") as arquivo:
                usuarios_json = json.load(arquivo)
                for obj in usuarios_json:
                    x = Usuario(obj['id'],
                                obj['nome'],
                                obj['email'],
                                obj['senha'],
                                Perfil(obj['perfil']),
                                obj['familia_id'])
                    cls.objetos.append(x)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        lista_usuarios = []
        for obj in cls.objetos:
            lista_usuarios.append(obj.to_dict())
        with open ("data/usuarios.json", mode="w") as arquivo:
            json.dump(lista_usuarios, arquivo, indent =4)
