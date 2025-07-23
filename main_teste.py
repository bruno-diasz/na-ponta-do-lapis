from dao.usuarios import Usuarios
from dao.despesas import Despesas
from dao.categorias import Categorias
from dao.familias import Familias
from dao.metodos_de_pagamento import MetodosDePagamento
from models.familia import Familia
from models.metodo_pagamento import MetodoDePagamento,Tipo
from models.categoria import Categoria
from models.despesa import Despesa
from models.usuario import Usuario,Perfil



#a = Usuario(0,'Bruno','bruno@',"1234",Perfil.MEMBRO,1)
#Usuarios.inserir(a)
#obj1 = Usuarios.listar()
#print(obj1)

# b = Despesa(0,"teste",4.4,0,0,0)
# Despesas.inserir(b)
# obj2 = Despesas.listar()
# print(ob2j)

# c = Categoria(0,"macarrão")
# Categorias.inserir(c)
# obj3 = Categorias.listar()
# print(obj3)

# d = Familia(0,"simpsons")
# Familias.inserir(d)
# obj4 = Familias.listar()
# print(obj4)

# e = MetodoDePagamento(0,'nubanko',Tipo.CREDITO,5.3,0)
# MetodosDePagamento.inserir(e)
# obj5 =MetodosDePagamento.listar()
# print(obj5)