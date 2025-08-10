from views import View
import streamlit as st
import pandas as pd


class RelatorioUI:
    @staticmethod
    def main():
        st.title("Relatório de Despesas")
        st.divider()

        st.subheader("Gastos por Categoria", divider='blue',)
        RelatorioUI.gastos_por_categoria()

        st.subheader("Gastos por Mês", divider='green')
        RelatorioUI.gastos_por_mes()
        st.divider()


    @staticmethod
    def gerar_relatorio():
       
        despesas = View.despesa_listar_por_usuario(st.session_state.usr.id)
        dic_despesas = [despesas.to_dict() for despesas in despesas]
        df_despesas = pd.DataFrame(dic_despesas)
        df_despesas['data'] = pd.to_datetime(df_despesas['data'])
        df_despesas['mes'] = df_despesas['data'].dt.to_period('M').astype(str)

        return df_despesas

    @staticmethod
    def gastos_por_categoria():
        df = RelatorioUI.gerar_relatorio()
        gastos_categoria = df.groupby('categoria_id')['valor'].sum()

        categorias = View.categoria_listar()
        dic_categoria = {categoria.id: categoria.nome for categoria in categorias}
        df_categoria = pd.DataFrame(dic_categoria.items(), columns=['id', 'nome'])
        gastos_categoria = pd.merge(gastos_categoria, df_categoria, left_on='categoria_id', right_on='id')
        gastos_categoria = gastos_categoria.set_index('nome')['valor']


        st.bar_chart(gastos_categoria, use_container_width=True, color=["#0b65ec"],height=500, x_label='Categorias', y_label='Gastos (R$)' )

    @staticmethod
    def gastos_por_mes():
        df = RelatorioUI.gerar_relatorio()
        gastos_mes = df.groupby('mes')['valor'].sum()
        st.line_chart(gastos_mes, use_container_width=True, color="#0ed862", height=500, x_label='Meses', y_label='Gastos (R$)')