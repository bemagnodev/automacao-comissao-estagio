import streamlit as st
# from ..boa_scraper import validate_boa
import pdfplumber


def validate_boa(uploaded_file) -> bool:
    # Garante que o "cursor" de leitura do arquivo está no início
    uploaded_file.seek(0)
    with pdfplumber.open(uploaded_file) as pdf:
        first_page_text = pdf.pages[0].extract_text()
        
        if "BOLETIM DE ORIENTAÇÃO ACADÊMICA" in first_page_text:
            return True
        return False



def file_upload():
    st.header("1. Faça o upload do seu BOA em PDF")
    uploaded_file = st.file_uploader(
        "Escolha o arquivo PDF",
        type="pdf",
        help="Apenas arquivos no formato .pdf são aceitos."
    )

    if uploaded_file:
        if validate_boa(uploaded_file):
            st.success(f"Arquivo {uploaded_file.name} foi validado e carregado com sucesso!")
            return uploaded_file
        else:
            st.error("O arquivo carregado não é um BOA válido. Por favor, verifique o arquivo e tente novamente.")
