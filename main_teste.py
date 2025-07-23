from dao.usuarios import Usuarios
from dao.despesas import Despesas
from models.despesa import Despesa
from models.usuario import Usuario,Perfil



#a = Usuario(0,'Bruno','bruno@',"1234",Perfil.MEMBRO,1)
#Usuarios.inserir(a)
#obj = Usuarios.listar()
#print(obj)

b = Despesa(0,"teste",4.4,0,0,0)
Despesas.inserir(b)
obj = Despesas.listar()
print(obj)