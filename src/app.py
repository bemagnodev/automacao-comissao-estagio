import pandas as pd
import streamlit as st

from boa_scraper import extract_academic_data_from_boa
from elegibility_validator import validate_eligibility

from components.description_card import description_card
from components.file_upload import file_upload
from components.report_card import report_card
# from components.select_company import select_company


def main():
    companies_df = pd.read_excel("data/affiliated_companies.xlsx")

    # --- Configuração da Página ---
    st.set_page_config(
        page_title="Upload de BOA e Seleção",
        page_icon="📄",
        layout="centered"
    )

    # --- Componentes da Interface ---
    st.title("Automação da Comissão de Estágio")

    description_card()

    st.markdown("---")

    uploaded_file = file_upload()

    # company_name = select_company(companies_df)

    st.markdown("---")

    # --- Lógica e Exibição dos Resultados ---
    if st.button("Processar Dados"):
        # Verifica se um arquivo foi carregado
        if uploaded_file is not None:            
            with st.spinner('Processando os dados... Por favor, aguarde.'):
                academic_data = extract_academic_data_from_boa(uploaded_file)
                # academic_data = {
                #                     "periodos_integralizados": 16,
                #                     "prazo_maximo": 14,
                #                     "carga_horaria_obtida": 120,
                #                     "creditos_obtidos": 120.0,
                #                     "cr_acumulado": 5.5,
                #                     "carga_horaria_extensao": 120,
                #                 }
                
                validations_dict = validate_eligibility(academic_data, companies_df, uploaded_file)
                # st.write(validations_dict)
                report_card(academic_data, validations_dict)
                if validations_dict["valid_student"]:
                    st.success("Todas as condições para a validação do estágio foram atendidas. O estudante está apto a realizar o estágio.")

        elif uploaded_file is None:
            st.error("Erro: Por favor, faça o upload de um arquivo PDF válido antes de processar.")
        else:
            st.warning("Algo deu errado. Verifique se todas as opções foram preenchidas.")


if __name__ == "__main__":
    main()
