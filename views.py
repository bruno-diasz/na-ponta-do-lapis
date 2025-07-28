from dao.categorias import Categorias, Categoria
from dao.despesas import Despesas, Despesa
from dao.familias import Familias, Familia
from dao.metodos_de_pagamento import MetodosDePagamento, MetodoDePagamento
from dao.usuarios import Usuarios, Usuario, Perfil

class View:
    @staticmethod
    def usuario_inserir(nome:str, email:str, senha:str, perfil:str):
        if perfil == 'membro': p = Perfil.MEMBRO 
        if perfil == 'admin': p = Perfil.ADMIN
        u = Usuario(0,nome,email,senha, p, 0)
        Usuarios.inserir(u)

    @staticmethod
    def usuario_listar():
        return Usuarios.listar()
    
    @staticmethod
    def usuario_atualizar(id:str, nome:str, email:str, senha:str, perfil:str):
        u = Usuarios.listar_id(id)
        if u is None:
            raise ValueError("id do usuario não encontrado")
        u_editado = Usuario(0,nome,email,senha, p, 0)
        