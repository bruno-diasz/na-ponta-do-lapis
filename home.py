import streamlit as st
from views import View, Perfil
from templates.manter_usuarios_ui import ManterUsuarioUI 
from templates.manter_metodos_pagamentos_ui import ManterMetodosPagamentoUI
from templates.manter_despesas_ui import ManterDespesasUI
from templates.manter_categoria_ui import ManterCategoriaUI
from templates.manter_familia_ui import ManterFamiliaUI
from templates.relatorio_ui import RelatorioUI
from templates.login_ui import LoginUI

class HomeUI:

    @staticmethod
    def menu_visitante():
        if 'op' not in st.session_state:
            st.session_state.op = 0
       
        with st.sidebar:
            st.title(':red[Bem-Vindo, Visitante!] :smile:',)
            st.write('---')

            if st.button('**:material/login: Entrar**',use_container_width=True): st.session_state.op = 1
            if st.button('**:material/person_add: Cadastrar-se**',use_container_width=True): st.session_state.op = 2


        if st.session_state.op == 1:
            LoginUI.main()
        elif st.session_state.op == 2:
            ManterUsuarioUI.inserir()
        
           

    @staticmethod
    def menu_membro():
        if 'op' not in st.session_state:
            st.session_state.op = 0
        with st.sidebar:
            st.title(':red[Área do Membro]')
            st.subheader(f"E aí, :red[{st.session_state.usr.nome.split()[0]}]! Bem-vindo(a) de volta! ")
            st.write('---')

            if st.button('**:material/receipt: Minhas Despesas**',use_container_width=True): st.session_state.op = 1
            if st.button('**:material/group: Grupo Familiar**',use_container_width=True): st.session_state.op = 2
            if st.button('**:material/report: Relatório de Despesas**',use_container_width=True): st.session_state.op = 3
            st.divider()
            if st.button('**:material/logout: Sair da Conta**',use_container_width=True): st.session_state.op = 6

        if st.session_state.op == 1:
            ManterDespesasUI.main()
        elif st.session_state.op == 2:
            ManterFamiliaUI.main()
        elif st.session_state.op == 3:
            RelatorioUI.main()
        elif st.session_state.op == 6:
            HomeUI.logout()


    @staticmethod
    def menu_admin():
        if 'op' not in st.session_state:
            st.session_state.op = 0
        with st.sidebar:
            st.title(':red[Área do Admin]')
            st.subheader(f"E aí, :red[{st.session_state.usr.nome.split()[0]}]! Bem-vindo(a) de volta! ")
            st.write('---')

            if st.button('**:material/receipt: Minhas Despesas**',use_container_width=True): st.session_state.op = 1
            if st.button('**:material/category: Categorias**',use_container_width=True): st.session_state.op = 2
            if st.button('**:material/payment: Metodos de Pagamento**',use_container_width=True): st.session_state.op = 3
            if st.button('**:material/group: Grupo Familiar**',use_container_width=True): st.session_state.op = 4
            if st.button('**:material/report: Relatório de Despesas**',use_container_width=True): st.session_state.op = 5
            st.divider()
            if st.button('**:material/logout: Sair da Conta**',use_container_width=True): st.session_state.op = 6

        if st.session_state.op == 1:
            ManterDespesasUI.main()
        elif st.session_state.op == 2:
            ManterCategoriaUI.main()
        elif st.session_state.op == 3:
            ManterMetodosPagamentoUI.main()
        elif st.session_state.op == 4:
            ManterFamiliaUI.main()
        elif st.session_state.op == 5:
            RelatorioUI.main()
        elif st.session_state.op == 6:
            HomeUI.logout()

    @staticmethod
    def sidebar():
        if "usr" not in st.session_state:
            HomeUI.menu_visitante()
        elif st.session_state.usr.perfil.value == Perfil.ADMIN.value:
            HomeUI.menu_admin()
        elif st.session_state.usr.perfil.value == Perfil.MEMBRO.value:
            HomeUI.menu_membro()
     

    @staticmethod
    def logout():
        st.session_state.clear()
        st.rerun()
        
    @staticmethod
    def main():
        HomeUI.sidebar()
       
       
          
        
        

HomeUI.main()
        
    