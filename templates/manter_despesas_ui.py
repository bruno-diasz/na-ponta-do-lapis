from views import View
import streamlit as st
import pandas as pd
import time 

class ManterDespesasUI:
    
    @staticmethod
    def main():
        st.subheader(":material/receipt: Administração de Despesas")
        listar, inserir, editar, remover = st.tabs(['**:material/article: Lista de Despesas**', '**:material/add: Cadastrar Despesa**', '**:material/edit: Editar Despesa**', '**:material/remove: Remover Despesa**'])
        with listar:
            ManterDespesasUI.listar()
        with inserir:
            ManterDespesasUI.inserir()
        with editar:
            ManterDespesasUI.atualizar()
        with remover:
            ManterDespesasUI.excluir()

    @staticmethod
    def listar():
        st.subheader(":material/article: Listagem de Despesas:")
        colun1, colun2 = st.columns([2, 1])
        colun1.divider()

        despesas = View.despesa_listar()
        if len(despesas) == 0:
            st.write("Nenhuma despesa cadastrada")
        else:
            dic = []
            for obj in despesas:
                dic.append(obj.to_dict())
            df = pd.DataFrame(dic, columns=['id', 'nome', 'valor', 'usuario', 'metodo_pagamento', 'categoria'])
            st.dataframe(df, hide_index=True, column_config={"id": "ID", "nome": "Nome", "valor": "Valor (R$)", "usuario": "Usuário", "metodo_pagamento": "Método de Pagamento", "categoria": "Categoria"})

    @staticmethod
    def inserir():
        st.subheader(":material/add: Cadastro:")
        colun1, colun2 = st.columns([2, 1])
        colun1.divider()

        try:
            with st.container(border=True):
                colun1, colun2 = st.columns([2, 1])

                nome = colun1.text_input("Nome da Despesa: ", placeholder='Digite o Nome da Despesa aqui')
                valor = colun1.number_input("Valor (R$): ", min_value=0.0, step=0.01, format="%.2f")
                usuario = colun1.text_input("Usuário: ", placeholder='Digite o Nome do Usuário aqui')
                metodo_pagamento = colun1.selectbox("Método de Pagamento: ", ['Cartão de Crédito', 'Cartão de Débito', 'Pix', 'Boleto', 'Transferência'])
                categoria = colun1.text_input("Categoria: ", placeholder='Digite a Categoria aqui')

                st.write('---')
                if st.button("Cadastrar", type='primary'):
                    View.despesa_inserir(nome, valor, usuario, metodo_pagamento, categoria)
                    st.success("Cadastro realizado com sucesso.", icon=':material/check: ')
                    time.sleep(4)
                    st.rerun()
        except Exception as erro:
            st.error(f"Erro ao cadastrar a despesa: {erro}")
    @staticmethod
    def atualizar():
        st.subheader(":material/edit: Edição:")
        colun1, colun2 = st.columns([2, 1])
        colun1.divider()

        despesas = View.despesa_listar()
        despesa = st.selectbox("Selecione uma Despesa para Edição:", despesas, format_func=lambda despesa: f'{despesa.id}. {despesa.nome}')
        if despesa:
            with st.container(border=True):
                colun1, colun2 = st.columns([2, 1])
                novo_nome = colun1.text_input("Novo Nome:", value=despesa.nome)
                novo_valor = colun1.number_input("Novo Valor (R$):", value=despesa.valor, min_value=0.0, step=0.01, format="%.2f")
                novo_usuario = colun1.text_input("Novo Usuário:", value=despesa.usuario)
                novo_metodo_pagamento = colun1.selectbox("Novo Método de Pagamento:", ['Cartão de Crédito', 'Cartão de Débito', 'Pix', 'Boleto', 'Transferência'], index=['Cartão de Crédito', 'Cartão de Débito', 'Pix', 'Boleto', 'Transferência'].index(despesa.metodo_pagamento))
                nova_categoria = colun1.text_input("Nova Categoria:", value=despesa.categoria)

                st.write('---')
                if st.button("Atualizar", type='primary'):
                    View.despesa_atualizar(despesa.id, novo_nome, novo_valor, novo_usuario, novo_metodo_pagamento, nova_categoria)
                    st.success("Edição realizada com sucesso.", icon=':material/check: ')
                    time.sleep(4)
                    st.rerun() 
    @staticmethod
    def excluir():
        st.subheader(":material/remove: Exclusão:")
        colun1, colun2 = st.columns([2, 1])
        colun1.divider()

        despesas = View.despesa_listar()
        despesa = st.selectbox("Selecione uma Despesa para Exclusão:", despesas, format_func=lambda despesa: f'{despesa.id}. {despesa.nome}')
        if despesa:
            with st.container(border=True):
                colun1, colun2 = st.columns([2, 1])
                if st.button("Excluir", type='primary'):
                    View.despesa_excluir(despesa.id)
                    st.success("Despesa excluída com sucesso.")
                    time.sleep(4)
                    st.rerun()
        else:
            st.write("Nenhuma despesa selecionada para exclusão.")