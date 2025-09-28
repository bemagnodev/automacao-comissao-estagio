import streamlit as st
import pandas as pd

def select_company(companies_df: pd.DataFrame) -> str:
    # 2. Componente de Seleção (Selectbox)
    st.header("2. Selecione a Empresa Conveniada")

    # Lista das empresas conveniadas
    empresas_conveniadas = companies_df["INSTITUIÇÃO"].tolist()

    # O widget selectbox retorna o nome que foi selecionado
    selected_company = st.selectbox(
        "Escolha uma empresa abaixo:",
        options=empresas_conveniadas,
        index=None,
        placeholder="Selecione uma das empresas conveniadas à UFRJ",
        help="O nome selecionado será associado ao documento enviado."
    )

    st.write("#### Não encontrou a empresa?")

    # 2. Crie o checkbox para ativar a entrada manual
    ativar_entrada_manual = st.checkbox("Digitar o nome de outra empresa")

    # 3. Variável para armazenar o nome final da empresa
    nome_empresa_final = ""

    # 4. Lógica condicional baseada no checkbox
    if ativar_entrada_manual:
        # Se o checkbox estiver MARCADO, mostre o campo de texto
        nome_digitado = st.text_input(
            "Digite o nome da nova empresa:",
            placeholder="Nome da empresa que não está na lista"
        )
        # O nome final será o que o usuário digitar
        nome_empresa_final = nome_digitado.strip()
    else:
        # Se o checkbox estiver DESMARCADO, o nome final é o do selectbox
        nome_empresa_final = selected_company

    return nome_empresa_final