import streamlit as st
from views import View, Perfil
from templates.manter_usuarios_ui import ManterUsuarioUI 
from templates.login_ui import LoginUI

class IndexUI:

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

            if st.button('**:material/receipt: Cadastrar despesas**',use_container_width=True): st.session_state.op = 1
            if st.button('**:material/receipt: Minhas despesas**',use_container_width=True): st.session_state.op = 2
            if st.button('**:material/receipt: Relatório de despesas**',use_container_width=True): st.session_state.op = 3
            st.divider()
            if st.button('**:material/logout: Sair da Conta**',use_container_width=True): st.session_state.op = 4

        if st.session_state.op == 1:
            pass
        elif st.session_state.op == 2:
            pass
        elif st.session_state.op == 3:
            pass
        elif st.session_state.op == 4:
            IndexUI.logout()


    @staticmethod
    def menu_admin():
        if 'op' not in st.session_state:
            st.session_state.op = 0
        with st.sidebar:
            st.title(':red[Painel Administrativo]')
            st.subheader(f"E aí, :red[{st.session_state.usr.nome.split()[0]}]! Bem-vindo(a) de volta! ")
            st.write('---')

            if st.button('**:material/person: Gerenciar Usuarios**',use_container_width=True): st.session_state.op = 1
            if st.button('**:material/package_2: Lorem**',use_container_width=True): st.session_state.op = 2
            if st.button('**:material/category: Ipsum**',use_container_width=True): st.session_state.op = 3
            if st.button('**:material/receipt: Lorem**',use_container_width=True): st.session_state.op = 4
            st.divider()
            if st.button('**:material/logout: Sair da Conta**',use_container_width=True): st.session_state.op = 5

        if st.session_state.op == 1:
            ManterUsuarioUI.main()
        elif st.session_state.op == 2:
            pass
        elif st.session_state.op == 3:
            pass
        elif st.session_state.op == 4:
            pass
        elif st.session_state.op == 5:
            IndexUI.logout()

    @staticmethod
    def sidebar():
        if "usr" not in st.session_state:
            IndexUI.menu_visitante()
        elif st.session_state.usr.perfil == Perfil.ADMIN:
            IndexUI.menu_admin()
        elif st.session_state.usr.perfil == Perfil.MEMBRO:
            IndexUI.menu_membro()
        else:
            st.write(type(st.session_state.usr.perfil), st.session_state.usr.perfil)

    @staticmethod
    def logout():
        del st.session_state.usr
        st.rerun()
        
    @staticmethod
    def main():
        IndexUI.sidebar()
       
       
          
        
        

IndexUI.main()
        
    