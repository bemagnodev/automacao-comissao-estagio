import pandas as pd
import streamlit as st
from PIL import Image 
import os

# Funções de backend
from boa_scraper import extract_academic_data_from_boa
from elegibility_validator import validate_eligibility

# Componentes da interface
from components.sidebar import render_sidebar
from components.header import render_header
from components.file_upload import file_upload
from components.report_card import report_card
# from components.select_company import select_company


def main():
    # --- Configuração de caminhos ---
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    FAVICON_PATH = os.path.join(PROJECT_ROOT, "assets", "icon.png")
    LOGO_PATH = os.path.join(PROJECT_ROOT, "assets", "logo_ic.png")
    COMPANIES_PATH = os.path.join(PROJECT_ROOT, "data", "affiliated_companies.xlsx")
    
    companies_df = pd.read_excel(COMPANIES_PATH)

    # --- Configuração da Página ---  
    st.set_page_config(
        page_title="Validador de Estágios",
        page_icon=FAVICON_PATH,
        layout="centered"
    )

    # --- Sidebar ---
    render_sidebar()

    # --- Cabeçalho com Logo ---
    render_header(LOGO_PATH)

    # --- Componentes da Interface ---
    uploaded_file = file_upload()

    # --- Lógica e Exibição dos Resultados ---
    if st.button("Analisar Elegibilidade", type="primary", use_container_width=True):
        # Verifica se um arquivo foi carregado
        if uploaded_file is not None:            
            with st.spinner('Analisando documento... Por favor, aguarde.'):
                academic_data = extract_academic_data_from_boa(uploaded_file)
                # academic_data = {
                #                     "periodos_integralizados": 10,
                #                     "prazo_maximo": 12,
                #                     "carga_horaria_obtida": 200,
                #                     "creditos_obtidos": 120.0,
                #                     "cr_acumulado": 9.5,
                #                     "carga_horaria_extensao": 380,
                #                 }
                
                validations_dict = validate_eligibility(academic_data, companies_df, uploaded_file)
                # st.write(validations_dict)
                st.session_state['academic_data'] = academic_data
                st.session_state['validations_dict'] = validations_dict
        else:
                if 'validations_dict' in st.session_state:
                    del st.session_state['validations_dict']
                st.error("Erro: Por favor, faça o upload de um arquivo PDF válido antes de processar.")
    
    # --- EXIBIÇÃO DOS RESULTADOS ---
    if 'validations_dict' in st.session_state:
        st.divider()
        report_card(st.session_state['academic_data'], st.session_state['validations_dict'])
        if st.session_state['validations_dict'].get("valid_student", False):
            st.success("Todas as condições para a validação do estágio foram atendidas.")
            st.markdown("**Próximo Passo:** [Acessar o Formulário de Inscrição para o Estágio](https://docs.google.com/forms/d/e/1FAIpQLSeNnHzF-xM3wSCf2ALQrhWYzP-GNhKy4nDWbOwqBqZtx7fGBw/viewform)")


if __name__ == "__main__":
    main()
