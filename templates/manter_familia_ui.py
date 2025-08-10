import time
from views import View, Perfil
import streamlit as st
import pandas as pd


class ManterFamiliaUI:

    @staticmethod
    def main():
       # st.write(st.session_state)
       # col1, col2, col3 = st.columns([1, 5, 1])
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
        m_familia, despesas, definir_orcamento = st.tabs(["Minha Família", "Despesas", "Definir Orçamento"])
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
                    with col1.expander(f"{membro.nome} -- ID {membro.id}"):
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
            colun1, colun2 = st.columns([2, 1])
            colun1.divider()

            despesas = View.despesa_listar_por_familia(st.session_state.usr.familia_id)
            if len(despesas) == 0:
                st.write("Nenhuma despesa cadastrada")
            else:
                dic = []
                for obj in despesas:
                    dic.append(obj.to_dict())
                df = pd.DataFrame(dic, columns=['id', 'descricao', 'valor', 'metodo_id', 'categoria_id', 'data', 'usuario_id'])
                df_formatado = df.style.format({"valor": "R$ {:.2f}"})
                st.dataframe(df_formatado, hide_index=True, column_config={"id": "ID", "descricao": "Descrição", "valor": "Valor (R$)", "usuario_id":"Usuario","metodo_id": "Método de Pagamento", "categoria_id": "Categoria", "data": "Data"})
                
                dic1 = []
                usuarios = View.familia_listar_usuarios(st.session_state.usr.familia_id)
                for obj in usuarios:
                    dic1.append(obj.to_dict())
                df_usuarios = pd.DataFrame(dic1, columns=['id', 'nome', 'email', 'senha', 'perfil', 'familia_id'])
                df_final =pd.merge(df, df_usuarios, left_on='usuario_id', right_on='id')
                st.dataframe(df_final)
     
            
                               

                   

