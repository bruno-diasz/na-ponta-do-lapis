import time
from views import View, Perfil
import streamlit as st
import pandas as pd


class ManterFamiliaUI:

    @staticmethod
    def main():
        if st.session_state.usr.familia_id is None:
           

            if 'op2' not in st.session_state:
                st.subheader(":material/group: Grupo Familiar")
                st.warning("Você não tem uma família cadastrada.")
                st.divider()
                if st.button("Criar Família", use_container_width=True):
                    st.session_state.op2 = 1
                    st.rerun()
                if st.button("Entrar na Família", use_container_width=True,):
                    st.session_state.op2 = 2
                    st.rerun()
            else:
                if st.session_state.op2 == 1: ManterFamiliaUI.criar()
                elif st.session_state.op2 == 2: ManterFamiliaUI.entrar()

        else:
            ManterFamiliaUI.exibir()
    
    @staticmethod
    def criar():
        try:
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.subheader("Criar Família")
                nome_familia = st.text_input("Nome da Família")
                if st.button("Criar", use_container_width=True):
                    print(nome_familia)
                    View.familia_inserir(nome_familia, st.session_state.usr.id)
                    st.success("Família criada com sucesso!")
                    time.sleep(4)
                    st.session_state.usr = View.usuario_listar_id(st.session_state.usr.id)
                    del st.session_state.op2
                    st.rerun()

                if st.button("Voltar", use_container_width=True):
                    del st.session_state.op2
                    st.rerun()
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
            time.sleep(4)
            st.rerun()

    @staticmethod
    def entrar():
        try:
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.subheader("Entrar na Família")
                familia_id = st.number_input("ID da Família", min_value=0, step=1)
                if st.button("Entrar", use_container_width=True):
                    View.familia_adicionar_usuario(familia_id, st.session_state.usr.id)
                    st.success("Você entrou na família com sucesso!")
                    time.sleep(4)
                    del st.session_state.op2
                    st.session_state.usr = View.usuario_listar_id(st.session_state.usr.id)
                    st.rerun()
                if st.button("Voltar", use_container_width=True):
                    del st.session_state.op2
                    st.rerun()
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
            time.sleep(4)
            st.rerun()

    @staticmethod
    def exibir():
        st.header("Grupo Familiar")
        m_familia, despesas, definir_orcamento, relatorio = st.tabs(["Minha Família", "Despesas", "Definir Orçamento", "Relatório"])
        with m_familia:
            familia = View.familia_listar_id(st.session_state.usr.familia_id)
            familia_membros = View.familia_listar_usuarios(st.session_state.usr.familia_id)
            st.subheader(f"Família - :red[{familia.nome}]")
            st.caption(f"**ID:** {familia.id}")
            st.divider()
            st.write("**Membros:**")
            with st.container(border=False):
                col1, col2 = st.columns([1.5, 1])
                for membro in familia_membros:
                    with col1.expander(f"{membro.nome} "):
                        colun1, colun2 = st.columns(2)
                        if membro.perfil.value == "admin":
                            if colun1.button("Remover Admin", key=f"remover_admin_{membro.id}"):
                                View.usuario_atualizar(membro.id, membro.nome, membro.email, membro.senha, "membro")
                                if membro.id == st.session_state.usr.id:
                                    st.session_state.usr = View.usuario_listar_id(membro.id)
                                time.sleep(4)
                                st.rerun()
                        else:
                            if colun1.button("Tornar Admin", key=f"tornar_admin_{membro.id}"):
                                View.usuario_atualizar(membro.id, membro.nome, membro.email, membro.senha, "admin")
                                if membro.id == st.session_state.usr.id:
                                    st.session_state.usr = View.usuario_listar_id(membro.id)
                                time.sleep(4)
                                st.rerun()
                        if colun2.button("Remover da Família", key=f"remover_familia_{membro.id}"):
                            View.familia_remover_usuario(membro.id)
                            if membro.id == st.session_state.usr.id:
                                st.session_state.usr = View.usuario_listar_id(membro.id)
                            time.sleep(4)
                            st.rerun()
        with despesas:
            st.subheader(":material/article: Listagem de Despesas da Familia:")
            if st.session_state.usr.perfil.value == 'membro':
                st.write("Você não tem permissão para visualizar esta seção.")
            else:
                colun1, colun2 = st.columns([2, 1])
                colun1.divider()
                despesas = View.despesa_listar_por_familia(st.session_state.usr.familia_id)
                if len(despesas) == 0:
                    st.write("Nenhuma despesa cadastrada")
                else:
                    dic_despesas = [ obj.to_dict() for obj in despesas]
                    dic_usuarios = [ obj.to_dict() for obj in View.familia_listar_usuarios(st.session_state.usr.familia_id)]
                    dic_categorias = [ obj.to_dict() for obj in View.categoria_listar()]
                    dic_metodos = [ obj.to_dict() for obj in View.metodo_pagamento_listar()]

                    df_despesas = pd.DataFrame(dic_despesas, columns=['id', 'descricao', 'valor', 'metodo_id', 'categoria_id', 'data', 'usuario_id'])
                    df_usuarios = pd.DataFrame(dic_usuarios, columns=['id', 'nome'])
                    df_categorias = pd.DataFrame(dic_categorias, columns=['id', 'nome'])
                    df_metodos = pd.DataFrame(dic_metodos, columns=['id', 'nome'])

                    df = pd.merge(df_despesas, df_usuarios, left_on='usuario_id', right_on='id', suffixes=('', '_usuario'))
                    df = pd.merge(df, df_metodos, left_on='metodo_id', right_on='id', suffixes=('', '_metodo'))
                    df = pd.merge(df, df_categorias, left_on='categoria_id', right_on='id', suffixes=('', '_categoria'))

                    df = df.drop(columns=['metodo_id', 'categoria_id', 'id_usuario', 'id_metodo', 'id_categoria', 'usuario_id'])

                    df_formatado = df.style.format({"valor": "R$ {:.2f}"})
                    st.dataframe(df_formatado, hide_index=True, column_config={"id": "ID", "descricao": "Descrição", "valor": "Valor (R$)", "nome":"Usuario","nome_metodo": "Método de Pagamento", "nome_categoria": "Categoria", "data": "Data"})

        with definir_orcamento:
            st.subheader(":material/money: Definir Orçamento Familiar")
            if st.session_state.usr.perfil.value == 'membro':
                st.write("Você não tem permissão para visualizar esta seção.")
        with relatorio:
            st.subheader(":material/report: Relatório de Despesas da Familia")
            if st.session_state.usr.perfil.value == 'membro':
                st.write("Você não tem permissão para visualizar esta seção.")
            else:
                st.divider()
            #---------
                dic_despesas = [ obj.to_dict() for obj in View.despesa_listar_por_familia(st.session_state.usr.familia_id)]
                dic_usuarios = [ obj.to_dict() for obj in View.familia_listar_usuarios(st.session_state.usr.familia_id)]

                df_despesas = pd.DataFrame(dic_despesas, columns=['id', 'valor', 'data', 'usuario_id'])
                df_usuarios = pd.DataFrame(dic_usuarios, columns=['id', 'nome'])

                df = pd.merge(df_despesas, df_usuarios, left_on='usuario_id', right_on='id', suffixes=('', '_usuario'))
                df['data'] = pd.to_datetime(df['data'])
                df['mes'] = df['data'].dt.to_period('M').astype(str)
                
                gastos_para_grafico = df.pivot_table(index='mes',
                                        columns='nome',
                                        values='valor',
                                        aggfunc='sum').fillna(0)
                
                gastos_para_grafico = gastos_para_grafico.sort_index()
                st.line_chart(gastos_para_grafico, use_container_width=True, height=500, x_label='Meses', y_label='Gastos (R$)')