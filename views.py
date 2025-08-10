from dao.categorias import Categorias, Categoria
from dao.despesas import Despesas, Despesa
from dao.familias import Familias, Familia
from dao.metodos_de_pagamento import MetodosDePagamento, MetodoDePagamento, Tipo
from dao.usuarios import Usuarios, Usuario, Perfil
from datetime import date

class View:

    #=== Operações de usuario ===
    @staticmethod
    def usuario_inserir(nome:str, email:str, senha:str, perfil:str, familia_id:int = None):
        if perfil == 'membro': p = Perfil.MEMBRO 
        if perfil == 'admin': p = Perfil.ADMIN

        u = Usuario(0,nome,email,senha, p, familia_id)
        Usuarios.inserir(u)

    @staticmethod
    def usuario_listar():
        return Usuarios.listar()
    
    @staticmethod
    def usuario_atualizar(id:str, nome:str, email:str, senha:str, perfil:str):
        u = Usuarios.listar_id(id)

        if u is None:
            raise ValueError("id do usuario não encontrado")
        if perfil == 'membro': p = Perfil.MEMBRO 
        if perfil == 'admin': p = Perfil.ADMIN

        u_editado = Usuario(id,nome,email,senha, p, u.familia_id)
        Usuarios.atualizar(u_editado)

    @staticmethod
    def usuario_excluir(id):
        u = Usuarios.listar_id(id)
        if u is None:
            raise ValueError("id do usuario não encontrado")
        Usuarios.excluir(u)

    @staticmethod
    def usuario_listar_id(id):
        u = Usuarios.listar_id(id)
        if u is None:
            raise ValueError("id do usuario não encontrado")
        return u
    
    @staticmethod
    def usuario_autenticar(email:str, senha:str):
        for usuario in Usuarios.listar():
            if usuario.email == email and usuario.senha == senha:
                return usuario

        raise ValueError("Credenciais inválidas!")
    
    #=== Operações de despesas ===
    @staticmethod
    def despesa_inserir(descricao:str, valor:float, categoria_id:int, usuario_id:int, metodo_pagamento_id:int, data:date):
        c = Categorias.listar_id(categoria_id)
        if c is None:
            raise ValueError("id da categoria não encontrado")
        u = Usuarios.listar_id(usuario_id)
        if u is None:
            raise ValueError("id do usuario não encontrado")
        m = MetodosDePagamento.listar_id(metodo_pagamento_id)
        if m is None:
            raise ValueError("id do metodo de pagamento não encontrado")

        d = Despesa(0, descricao, round(valor, 2), usuario_id, metodo_pagamento_id, categoria_id, data)
        Despesas.inserir(d)
    
    @staticmethod
    def despesa_listar():
        return Despesas.listar()
    
    @staticmethod
    def despesa_listar_por_usuario(usuario_id:int):
        depesas = [despesa for despesa in Despesas.listar() if despesa.usuario_id == usuario_id]
        return depesas
    
    @staticmethod
    def despesa_listar_por_familia(familia_id:int):
        if familia_id is None:
            raise ValueError("O id da família não pode ser None")
        familia = [usuario for usuario in Usuarios.listar() if usuario.familia_id == familia_id]
        despesas = []
        for d in Despesas.listar():
            for u in familia:
                if d.usuario_id == u.id:
                    despesas.append(d)
        return despesas

    @staticmethod
    def despesa_atualizar(id:str, nome:str, valor:float, categoria_id:int, usuario_id:int, metodo_pagamento_id:int, data:date):
        d = Despesas.listar_id(id)
        if d is None:
            raise ValueError("id da despesa não encontrado")

        c = Categorias.listar_id(categoria_id)
        if c is None:
            raise ValueError("id da categoria não encontrado")
        u = Usuarios.listar_id(usuario_id)
        if u is None:
            raise ValueError("id do usuario não encontrado")
        m = MetodosDePagamento.listar_id(metodo_pagamento_id)
        if m is None:
            raise ValueError("id do metodo de pagamento não encontrado")

        d_editada = Despesa(id, nome, round(valor, 2), usuario_id, metodo_pagamento_id, categoria_id, data)
        Despesas.atualizar(d_editada)

    @staticmethod
    def despesa_excluir(id):
        d = Despesas.listar_id(id)
        if d is None:
            raise ValueError("id da despesa não encontrado")
        Despesas.excluir(d)

    @staticmethod
    def despesa_listar_id(id):
        d = Despesas.listar_id(id)
        if d is None:
            raise ValueError("id da despesa não encontrado")
        return d
    
    #=== Operações de categorias ===
    @staticmethod
    def categoria_inserir(nome:str):
        c = Categoria(0, nome)
        Categorias.inserir(c)

    @staticmethod
    def categoria_listar():
        return Categorias.listar()

    @staticmethod
    def categoria_atualizar(id:str, nome:str):
        c = Categorias.listar_id(id)
        if c is None:
            raise ValueError("id da categoria não encontrado")
        c_editada = Categoria(id, nome)
        Categorias.atualizar(c_editada)

    @staticmethod
    def categoria_excluir(id):
        c = Categorias.listar_id(id)
        if c is None:
            raise ValueError("id da categoria não encontrado")
        Categorias.excluir(c)

    @staticmethod
    def categoria_listar_id(id):
        c = Categorias.listar_id(id)
        if c is None:
            raise ValueError("id da categoria não encontrado")
        return c

    #=== Operações de métodos de pagamento ===
    @staticmethod
    def metodo_pagamento_inserir(nome:str, tipo:str, saldo_total:float,familia_id:int):
        if tipo == 'Cartão de Débito': tipo = Tipo.DEBITO
        elif tipo == 'Cartão de Crédito': tipo = Tipo.CREDITO
        elif tipo == 'Pix': tipo = Tipo.PIX
        elif tipo == 'Boleto': tipo = Tipo.BOLETO
        elif tipo == 'Transferência': tipo = Tipo.TRANSFERENCIA

        m = MetodoDePagamento(0, nome,tipo,saldo_total,familia_id)
        MetodosDePagamento.inserir(m)

    @staticmethod
    def metodo_pagamento_listar():
        return MetodosDePagamento.listar()

    @staticmethod
    def metodo_pagamento_atualizar(id:str, nome:str, tipo:str, saldo_total:float, familia_id:int):
        m = MetodosDePagamento.listar_id(id)
        if m is None:
            raise ValueError("id do metodo de pagamento não encontrado")
        
        if tipo == 'Cartão de Débito': tipo = Tipo.DEBITO
        elif tipo == 'Cartão de Crédito': tipo = Tipo.CREDITO
        elif tipo == 'Pix': tipo = Tipo.PIX
        elif tipo == 'Boleto': tipo = Tipo.BOLETO
        elif tipo == 'Transferência': tipo = Tipo.TRANSFERENCIA
        
        m_editado = MetodoDePagamento(id, nome, tipo, saldo_total, familia_id)
        MetodosDePagamento.atualizar(m_editado)

    @staticmethod
    def metodo_pagamento_excluir(id):
        m = MetodosDePagamento.listar_id(id)
        if m is None:
            raise ValueError("id do metodo de pagamento não encontrado")
        MetodosDePagamento.excluir(m)

    @staticmethod
    def metodo_pagamento_listar_id(id):
        m = MetodosDePagamento.listar_id(id)
        if m is None:
            raise ValueError("id do metodo de pagamento não encontrado")
        return m
    
    #=== Operações de familias ===

    @staticmethod
    def familia_inserir(nome:str, usuario_id:int):
        if nome.strip() == "":
            raise ValueError("nome da familia não pode ser vazio")
        u = Usuarios.listar_id(usuario_id)
        if u is None:
            raise ValueError("id do usuario não encontrado")
        
        f = Familia(0, nome)
        Familias.inserir(f)
        View.familia_adicionar_usuario(f.id, usuario_id)
        u.perfil = Perfil.ADMIN
        Usuarios.atualizar(u)

        return f

    @staticmethod
    def familia_listar():
        return Familias.listar()

    @staticmethod
    def familia_atualizar(id:str, nome:str):
        f = Familias.listar_id(id)
        if f is None:
            raise ValueError("id da familia não encontrado")
        f_editada = Familia(id, nome)
        Familias.atualizar(f_editada)

    @staticmethod
    def familia_excluir(id):
        f = Familias.listar_id(id)
        if f is None:
            raise ValueError("id da familia não encontrado")
        Familias.excluir(f)

    @staticmethod
    def familia_listar_id(id):
        f = Familias.listar_id(id)
        if f is None:
            raise ValueError("id da familia não encontrado")
        return f
    
    @staticmethod
    def familia_adicionar_usuario(familia_id:int, usuario_id:int):
        f = Familias.listar_id(familia_id)
        if f is None:
            raise ValueError("id da familia não encontrado")
        u = Usuarios.listar_id(usuario_id)
        if u is None:
            raise ValueError("id do usuario não encontrado")
        u.familia_id = familia_id
        u.perfil = Perfil.MEMBRO
        Usuarios.atualizar(u)
    
    @staticmethod
    def familia_remover_usuario(usuario_id:int):
        u = Usuarios.listar_id(usuario_id)
        if u is None:
            raise ValueError("id do usuario não encontrado")
        if u.familia_id is None:
            raise ValueError("O usuario não pertence a nenhuma familia")
        u.familia_id = None
        u.perfil = Perfil.ADMIN
        Usuarios.atualizar(u)
    
    @staticmethod
    def familia_listar_usuarios(familia_id:int):
        familia = View.familia_listar_id(familia_id)
        familia_membros = [u for u in View.usuario_listar() if u.familia_id == familia.id]
        return familia_membros


