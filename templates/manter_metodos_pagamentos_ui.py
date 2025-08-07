import streamlit as st
import pandas as pd
import time
from views import View

class ManterMetodosPagamentoUI:

    @staticmethod
    def main():
        st.subheader(":material/payment: Administração de Métodos de Pagamento")
        listar, inserir, editar, remover = st.tabs(['**:material/article: Lista de Métodos**', '**:material/add: Cadastrar Método**', '**:material/edit: Editar Método**', '**:material/remove: Remover Método**'])
        with listar:
            ManterMetodosPagamentoUI.listar()
        with inserir:
            ManterMetodosPagamentoUI.inserir()
        with editar:
            ManterMetodosPagamentoUI.atualizar()
        with remover:
            ManterMetodosPagamentoUI.excluir()

    @staticmethod
    def listar():
        st.subheader(":material/article: Listagem de Métodos de Pagamento:")
        colun1, colun2 = st.columns([2, 1])
        colun1.divider()
        metodos = View.metodo_pagamento_listar()
        if len(metodos) == 0:
            st.write("Nenhum método de pagamento cadastrado")
        else:
            dic = []
            for obj in metodos:
                dic.append(obj.to_dict())
            df = pd.DataFrame(dic, columns=['id', 'nome', 'tipo', 'saldo_total', 'saldo_atual'])
            st.dataframe(df, hide_index=True, column_config={"id": "ID", "nome": "Nome", "tipo": "Tipo", "saldo_total": "Saldo Total (R$)", "saldo_atual": "Saldo Atual (R$)"})

    @staticmethod
    def inserir():
        st.subheader(":material/add: Cadastro:")
        colun1, colun2 = st.columns([2, 1])
        colun1.divider()
       
        try:
            with st.container(border=True):
                colun1, colun2 = st.columns([2, 1])
                
                nome = colun1.text_input("Nome do Método: ", placeholder='Digite o Nome do Método aqui')
                tipo = colun1.selectbox("Tipo de Método: ", ['Cartão de Crédito', 'Cartão de Débito', 'Pix', 'Boleto', 'Transferência'])
                saldo_total = colun1.number_input("Saldo Total (R$): ", min_value=0.0, step=0.01, format="%.2f")

                st.write('---')
                if st.button("Cadastrar", type='primary'):
                    View.metodo_pagamento_inserir(nome, tipo, saldo_total, st.session_state.usr.familia_id)
                    st.success("Cadastro realizado com sucesso.", icon=':material/check: ')
                    time.sleep(4)
                    st.rerun()
        except Exception as erro:
            st.error(f"Erro ao cadastrar o método de pagamento: {erro}")

    @staticmethod
    def atualizar():
        st.subheader(":material/edit: Edição:")
        colun1, colun2 = st.columns([2, 1])
        colun1.divider()

        metodos = View.metodo_pagamento_listar()
        metodo = st.selectbox("Selecione um Método para Edição:", metodos, format_func=lambda metodo: f'{metodo.id}. {metodo.nome}')
        if metodo:
            with st.container(border=True):
                colun1, colun2 = st.columns([2, 1])
                novo_nome = colun1.text_input("Novo Nome:", value=metodo.nome)
                match metodo.tipo.value:
                    case 'credito':
                        tipo = 0
                    case 'debito':
                        tipo = 1
                    case 'pix':
                        tipo = 2
                    case 'boleto':
                        tipo = 3
                    case 'transferencia':
                        tipo = 4
                    case _:
                        tipo = -1
                novo_tipo = colun1.selectbox("Novo Tipo:", ['Cartão de Crédito', 'Cartão de Débito', 'Pix', 'Boleto', 'Transferência'], index=tipo)
                novo_saldo_total = colun1.number_input("Novo Saldo Total (R$):", value=metodo.saldo_total, min_value=0.0, step=0.01, format="%.2f")
                st.divider()
                if st.button("Atualizar", type="primary"):
                    View.metodo_pagamento_atualizar(metodo.id, novo_nome, novo_tipo, novo_saldo_total, st.session_state.usr.familia_id)
                    st.success("Método de pagamento atualizado com sucesso.")
                    time.sleep(4)
                    st.rerun()

    @staticmethod
    def excluir():
        st.subheader(":material/remove: Exclusão:")
        colun1, colun2 = st.columns([2, 1])
        colun1.divider()

        metodos = View.metodo_pagamento_listar()
        metodo = st.selectbox("Selecione um Método para Exclusão:", metodos, format_func=lambda metodo: f'{metodo.id}. {metodo.nome}')
        st.divider()
        if metodo:
            if st.button("Excluir", type="primary"):
                View.metodo_pagamento_excluir(metodo.id)
                st.success("Método de pagamento excluído com sucesso.")
                time.sleep(4)
                st.rerun()
