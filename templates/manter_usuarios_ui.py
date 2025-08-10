import streamlit as st
import pandas as pd
import time
from views import View


class ManterUsuarioUI:

    @staticmethod
    def main():
        st.subheader(":material/person: Administração de Usuários")
        listar, inserir, editar, remover = st.tabs(['**:material/article_person: Lista de Usuários**','**:material/person_add: Cadastrar Usuário**','**:material/person_edit: Editar Usuário**','**:material/person_remove: Remover Usuário**'])
        with listar:
            ManterUsuarioUI.listar()
        with inserir:
            ManterUsuarioUI.inserir()
        with editar:
            ManterUsuarioUI.atualizar()
        with remover:
            ManterUsuarioUI.excluir()

    @staticmethod
    def listar():
        st.subheader(":material/article_person: Listagem de Usuários:")
        colun1,colun2 = st.columns([2,1])
        colun1.divider()
        usuarios = View.usuario_listar()
        if len(usuarios) == 0:
            st.write("Nenhum usuario cadastrado")
        else:
            dic = []
            for obj in usuarios:
                dic.append(obj.to_dict())
            df = pd.DataFrame(dic, columns=['id', 'nome', 'email', 'fone', 'funcao'])
            st.dataframe(df, hide_index=True,column_config={"id": "ID", "nome": "Nome", "email": "E-mail", "fone": "Telefone", "funcao": "Função"})

    @staticmethod
    def inserir():
        st.subheader(":material/person_add: Cadastro:")
        colun1,colun2 = st.columns([2,1])
        colun1.divider()
        try:
            with st.container(border=True):
                col1,col2 = st.columns(2)
                nome = col1.text_input("Nome: ", placeholder='Digite seu Nome aqui')
                email = col2.text_input("E-mail: ", placeholder='Digite seu E-mail aqui')
                senha = col1.text_input("Senha: ", type='password', placeholder='Digite sua Senha aqui')
                senha2 = col2.text_input("Repita a Senha: ", type='password', placeholder='Repita sua Senha aqui')
                perfil = "admin"

                st.write('---')
                if st.button("Cadastrar", type='primary'):
                    View.usuario_inserir(nome, email, senha, perfil)
                    st.success("Cadastro realizado com sucesso.", icon=':material/check: ')
                    time.sleep(4)
                    st.rerun()
        except Exception as erro:
                st.error(f"{erro}",icon=":material/error:")
                time.sleep(4)
                st.rerun()

    @staticmethod
    def atualizar():
        st.subheader(":material/person_edit: Edição de Usuário:")
        colun1,colun2 = st.columns([2,1])
        colun1.divider()
        try:
            clientes= View.usuario_listar()
            cliente = st.selectbox('Selecione um Usuário para editar:',clientes, format_func=lambda cliente: f'{cliente.id}. {cliente.email}') 
            
            with st.container(border=True):
                col1,col2 = st.columns(2)
                nome = col1.text_input("Novo Nome: ", placeholder='Digite seu novo Nome aqui',value=cliente.nome )
                email = col2.text_input("Novo E-mail: ", placeholder='Digite seu novo E-mail aqui', value=cliente.email)
                senha = col1.text_input("Nova Senha: ", type='password', placeholder='Digite sua nova Senha aqui', value=cliente.senha)
                senha2 = col2.text_input("Nova Repita a Senha: ", type='password', placeholder='Digite novamente sua nova Senha aqui', value=cliente.senha)
                fone = col1.text_input("Novo Telefone: ", placeholder='Digite seu novo Telefone aqui', value=cliente.fone)
        
                if cliente.funcao == "cliente": cliente_func = 0
                elif cliente.funcao == "entregador": cliente_func = 1
                elif  cliente.funcao == "admin": cliente_func = 2
                if "usr" in st.session_state and st.session_state.usr.funcao == "admin":
                    funcao = col2.selectbox("Função: ", ["cliente", "entregador", "admin"], format_func= lambda funcao : funcao.capitalize(), key="editar_func", index= cliente_func)

                st.write('---')
                if st.button("Atualizar", type='primary'):
                    View.usuario_atualizar(cliente.id, nome, email, fone, senha, senha2, funcao)
                    st.success("Atualização realizado com sucesso.", icon=":material/check:")
                    time.sleep(4)
                    st.rerun()

        except Exception as erro:
            st.error(f"{erro}",icon=":material/error:")
            time.sleep(4)
            st.rerun()


    @staticmethod
    def excluir():
        st.subheader(":material/person_remove: Exclusão de Usuário:")
        colun1,colun2 = st.columns([2,1])
        colun1.divider()

        clientes= View.usuario_listar()
        cliente = st.selectbox('Selecione um Usuário para remover:',clientes, format_func=lambda cliente: f'{cliente.id}. {cliente.email}') 

        st.write('---')
        if st.button("Remover", type='primary'):
            View.usuario_excluir(cliente.id)
            st.success("Exclusão realizado com sucesso.",icon=":material/check:")
            time.sleep(4)
            st.rerun()