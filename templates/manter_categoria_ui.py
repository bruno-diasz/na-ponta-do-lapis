from views import View
import streamlit as st
import pandas as pd
import time 

class ManterCategoriaUI:
    @staticmethod
    def main():
        st.subheader(":material/category: Administração de Categorias")
        listar, inserir, editar, remover = st.tabs(['**:material/article: Lista de Categorias**', '**:material/add: Cadastrar Categoria**', '**:material/edit: Editar Categoria**', '**:material/remove: Remover Categoria**'])
        with listar:
            ManterCategoriaUI.listar()
        with inserir:
            ManterCategoriaUI.inserir()
        with editar:
            ManterCategoriaUI.atualizar()
        with remover:
            ManterCategoriaUI.excluir()

    @staticmethod
    def listar():
        st.subheader(":material/article: Listagem de Categorias:")
        colun1, colun2 = st.columns([2, 1])
        colun1.divider()

        categorias = View.categoria_listar()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            dic = []
            for obj in categorias:
                dic.append(obj.to_dict())
            df = pd.DataFrame(dic, columns=['id', 'nome'])
            st.dataframe(df, hide_index=True, column_config={"id": "ID", "nome": "Nome"})
    @staticmethod
    def inserir():
        st.subheader(":material/add: Cadastro:")
        colun1, colun2 = st.columns([2, 1])
        colun1.divider()

        try:
            with st.container(border=True):
                colun1, colun2 = st.columns([2, 1])

                nome = colun1.text_input("Nome: ", placeholder='Digite o Nome da Categoria aqui')

                st.write('---')
                if st.button("Cadastrar", type='primary'):
                    View.categoria_inserir(nome)
                    st.success("Cadastro realizado com sucesso.", icon=':material/check: ')
                    time.sleep(4)
                    st.rerun()
        except Exception as erro:
            st.error(f"Erro ao cadastrar a categoria: {erro}")

    @staticmethod
    def atualizar():
        st.subheader(":material/edit: Edição:")
        colun1, colun2 = st.columns([2, 1])
        colun1.divider()

        try:
            c = View.categoria_listar()
            categoria = st.selectbox("Selecione uma Categoria:", c, format_func=lambda categoria: categoria.nome)
            with st.container(border=True):
                colun1, colun2 = st.columns([2, 1])

                nome = colun1.text_input("Novo Nome: ", placeholder='Digite o Nome da Categoria aqui', value=categoria.nome)

                st.write('---')
                if st.button("Atualizar", type='primary'):
                    View.categoria_atualizar(categoria.id, nome)
                    st.success("Atualização realizada com sucesso.", icon=':material/check: ')
                    time.sleep(4)
                    st.rerun()
        except Exception as erro:
            st.error(f"Erro ao atualizar a categoria: {erro}")

    @staticmethod
    def excluir():
        st.subheader(":material/remove: Exclusão:")
        colun1, colun2 = st.columns([2, 1])
        colun1.divider()

        try:
            colun1, colun2 = st.columns([2, 1])
            c = View.categoria_listar()
            categoria = st.selectbox("Selecione uma Categoria para Exclusão:", c, format_func=lambda categoria: categoria.nome)
            st.write('---')

            if st.button("Excluir", type='primary'):
                View.categoria_excluir(categoria.id)
                st.success("Exclusão realizada com sucesso.", icon=':material/check: ')
                time.sleep(4)
                st.rerun()

        except Exception as erro:
            st.error(f"Erro ao excluir a categoria: {erro}")
        except ValueError as ve:
            st.error(f"Erro: {ve}")
       

    