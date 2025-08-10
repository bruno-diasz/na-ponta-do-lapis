import streamlit as st
import time 
from views import View

class LoginUI:
    
    @staticmethod 
    def main():
        st.subheader("Login:")
        st.divider()
        try:
            with st.form("login"):
                email = st.text_input("Email:", placeholder="Digite seu email")
                senha = st.text_input("Senha:", type='password', placeholder="Digite sua senha")
                if st.form_submit_button("Entrar",type="primary"): 
                    st.session_state.usr = View.usuario_autenticar(email,senha)
                    st.rerun()
        except Exception as erro:
            st.error(f"{erro}")
            time.sleep(4)
            st.rerun()