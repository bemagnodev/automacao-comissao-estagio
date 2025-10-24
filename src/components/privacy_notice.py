import streamlit as st


def render_privacy_notice():
    """Exibe o aviso de privacidade e segurança dos dados dentro de um expander."""
    
    with st.expander("🔒 Aviso de Privacidade e Segurança dos Dados"):
        st.info(
            """
            Seus dados estão seguros. O documento enviado (BOA) é utilizado **apenas em tempo de execução** para processar as informações. 
            
            Não armazenamos seu arquivo em nenhum banco de dados e ele é descartado assim que a análise é concluída.
            """
        )
