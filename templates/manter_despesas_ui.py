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
            df = pd.DataFrame(dic, columns=['id', 'descricao', 'valor', 'metodo_id', 'categoria_id', 'data'])
            st.dataframe(df, hide_index=True, column_config={"id": "ID", "descricao": "Descrição", "valor": "Valor (R$)", "metodo_id": "Método de Pagamento", "categoria_id": "Categoria", "data": "Data"})

    @staticmethod
    def inserir():
        st.subheader(":material/add: Cadastro:")
        colun1, colun2 = st.columns([2, 1])
        colun1.divider()

        try:
            with st.container(border=True):
                colun1, colun2 = st.columns([2, 1])
                m = View.metodo_pagamento_listar()
                c = View.categoria_listar()

                descricao = colun1.text_input("Descrição: ", placeholder='Digite a Descrição da Despesa aqui')
                valor = colun1.number_input("Valor (R$): ", min_value=0.0, step=0.01, format="%.2f")
                metodo_pagamento = colun1.selectbox("Método de Pagamento: ", m, format_func=lambda metodo: metodo.nome)
                categoria = colun1.selectbox("Categoria: ", c, format_func=lambda categoria: categoria.nome)

                st.write('---')
                if st.button("Cadastrar", type='primary'):
                    View.despesa_inserir(descricao, valor, categoria.id, st.session_state.usr.id, metodo_pagamento.id)
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
        metodo = View.metodo_pagamento_listar()
        categoria = View.categoria_listar()
        despesa = st.selectbox("Selecione uma Despesa para Edição:", despesas, format_func=lambda despesa: f'{despesa.id}. {despesa.descricao}')
        if despesa:
            with st.container(border=True):
                colun1, colun2 = st.columns([2, 1])
                nova_descricao = colun1.text_input("Nova Descrição:", value=despesa.descricao)
                novo_valor = colun1.number_input("Novo Valor (R$):", value=despesa.valor, min_value=0.0, step=0.01, format="%.2f")
                novo_metodo_pagamento = colun1.selectbox("Novo Método de Pagamento:", metodo, index=[m.id for m in metodo].index(despesa.metodo_id), format_func=lambda metodo: metodo.nome)
                nova_categoria = colun1.selectbox("Nova Categoria:", categoria, index=[c.id for c in categoria].index(despesa.categoria_id), format_func=lambda categoria: categoria.nome)

                st.write('---')
                if st.button("Atualizar", type='primary'):
                    View.despesa_atualizar(despesa.id, nova_descricao, novo_valor, nova_categoria.id, despesa.usuario_id, novo_metodo_pagamento.id)
                    st.success("Edição realizada com sucesso.", icon=':material/check: ')
                    time.sleep(4)
                    st.rerun()

    @staticmethod
    def excluir():
        st.subheader(":material/remove: Exclusão:")
        colun1, colun2 = st.columns([2, 1])
        colun1.divider()

        despesas = View.despesa_listar()
        despesa = st.selectbox("Selecione uma Despesa para Exclusão:", despesas, format_func=lambda despesa: f'{despesa.id}. {despesa.descricao}')
        if despesa:
          
                colun1, colun2 = st.columns([2, 1])
                colun1.divider()
                if st.button("Excluir", type='primary'):
                    View.despesa_excluir(despesa.id)
                    st.success("Despesa excluída com sucesso.")
                    time.sleep(4)
                    st.rerun()
        else:
            st.write("Nenhuma despesa selecionada para exclusão.")