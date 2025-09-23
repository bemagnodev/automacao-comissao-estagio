import pandas as pd
import streamlit as st

from elegibility_validator import validate_eligibility
from boa_scraper import extract_academic_data_from_boa, validate_boa


def generate_report_card(academic_data, validations_dict):
    """
    Gera um card de relatório de elegibilidade no Streamlit.

    Args:
        student_name (str): O nome do estudante.
        validations_dict (dict): Dicionário com os resultados booleanos das validações.
        academic_data (dict): Dicionário com os dados acadêmicos do estudante.
    """
    
    # --- Container Principal para o Card ---
    with st.container(border=True):
        st.subheader(f"Resultado para {academic_data.get('nome_aluno', 'Aluno Desconhecido')}")
        st.markdown("---")

        # --- Status Final (APTO/INAPTO) ---
        if validations_dict.get("valid_student", False):
            st.success(f"✅ PARABÉNS! O(A) aluno(a) está APTO(A).")
        else:
            st.error(f"❌ ATENÇÃO! O(A) aluno(a) está INAPTO(A).")
        
        st.write("") # Adiciona um espaço

        # --- Painel de Desempenho Rápido ---
        st.write("**Painel de Desempenho**")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="CR Acumulado", value=f'{academic_data.get("cr_acumulado", 0.0)}')
        with col2:
            st.metric(label="Períodos Cursados", value=f'{academic_data.get("periodos_integralizados", 0)}')
        with col3:
            st.metric(label="Horas de Extensão", value=f'{academic_data.get("carga_horaria_extensao", 0)}h')
            
        st.write("") # Adiciona um espaço

        # --- Expander para Detalhes dos Critérios ---
        with st.expander("Ver análise detalhada dos critérios"):
            
            # Mapeamento de chaves para nomes amigáveis e requisitos de exemplo

            academic_requirements = {
                                        "minimum_cr": 6.0,
                                        "max_periods": academic_data["prazo_maximo"],
                                        "minimum_ext_hours": 160.0,
                                        "minimum_credits": 87
                                    }

            criteria_map = {
                "valid_cr": {"name": "Coeficiente de Rendimento", "value": academic_data.get("cr_acumulado"), "required": academic_requirements["minimum_cr"]},
                "valid_periods": {"name": "Períodos Cursados", "value": academic_data.get("periodos_integralizados"), "required": f'<= {academic_requirements["max_periods"]}'},
                "valid_ext_hours": {"name": "Horas de Extensão", "value": academic_data.get("carga_horaria_extensao"), "required": f">= {academic_requirements['minimum_ext_hours']}"},
                # "valid_company": {"name": "Empresa Conveniada", "value": validations_dict.get("valid_company"), "required": "True"},
                "valid_courses": {"name": "Disciplinas Obrigatórias", "value": validations_dict.get("valid_courses"), "required": "True"},
            }

            for key, validation_status in validations_dict.items():
                if key in criteria_map:
                    details = criteria_map[key]
                    icon = "✅" if validation_status else "❌"
                    
                    st.markdown(
                        f"{icon} **{details['name']}:** (Seu: `{details['value']}` | Requisito: `{details['required']}`)"
                    )


def main():
    companies_df = pd.read_excel("data/affiliated_companies.xlsx")

    # --- Configuração da Página ---
    st.set_page_config(
        page_title="Upload de BOA e Seleção",
        page_icon="📄",
        layout="centered"
    )

    # --- Título e Descrição ---
    st.title("Automação da Comissão de Estágio")
    with st.expander("ℹ️ Como funciona o sistema? (Clique para expandir)"):
        st.markdown("""
        Este sistema foi projetado para simplificar e acelerar a verificação de elegibilidade de estágios, seguindo um fluxo de trabalho claro e eficiente:
        
        - **1. Upload do BOA:** O processo começa com o upload do **Boletim de Orientação Acadêmica (BOA)**, o histórico escolar oficial do aluno. O sistema primeiro valida se o arquivo é um BOA autêntico.
        
        - **2. Seleção da Empresa:** Em seguida, o usuário seleciona a empresa conveniada onde o estágio será realizado. Caso a empresa não esteja na lista, é possível digitar o nome manualmente.
        
        - **3. Validação Automática:** Com um clique, o sistema lê o PDF, extrai todos os dados acadêmicos relevantes (CR, períodos integralizados, horas de extensão, matérias obrigatórias, empresas conveniadas) e os compara com as regras de elegibilidade do estágio.
        
        - **4. Relatório Instantâneo:** Imediatamente após a análise, um relatório visual é gerado, indicando se o aluno está **APTO** ou **INAPTO** e detalhando o resultado de cada critério individual.
        """)

    with st.expander("🎯 Próximos Passos e Evolução do Processo"):
        st.markdown("""
        Para tornar a automação ainda mais completa, os próximos passos envolvem a análise de documentos adicionais do processo de estágio:
        
        - **1. Leitura de Documentos do Estágio:** Implementar o upload e a leitura automatizada de três novos documentos:
            - **Plano de Atividades do Estagiário**
            - **Termo de Compromisso de Estágio (TCE)**
            - **Cópia da Apólice de Seguro de Acidentes Pessoais**
            
        - **2. Validações Cruzadas:** Utilizar os dados extraídos desses novos documentos para realizar verificações essenciais:
            - **Carga Horária Semanal:** Confirmar se o plano de atividades especifica **20 horas semanais**.
            - **Prazo de Início:** Verificar se a data de início do estágio no TCE respeita o prazo de **15 dias de antecedência** da data de submissão.
            - **Preenchimento Automático:** Extrair o nome da empresa diretamente do TCE para preencher o campo de seleção automaticamente.
        """)

    with st.expander("🚀 Ideias de Melhorias Futuras"):
        st.markdown("""
        Além dos próximos passos, planejamos outras funcionalidades para aprimorar a ferramenta a longo prazo:
        
        - **📄 Geração de Relatório em PDF:** Adicionar um botão para exportar o relatório de elegibilidade final para um arquivo PDF formatado, pronto para ser arquivado ou enviado.
        
        - **⚙️ Banco de Dados de Empresas:** Integrar com um banco de dados real para gerenciar as empresas conveniadas, permitindo adicionar e editar informações diretamente pelo sistema.
        
        - **📧 Notificações por E-mail:** Implementar o envio de um e-mail automático para a comissão de estágio ou para o aluno com o resultado da análise.
        """)

    st.markdown("---")

    # --- Componentes da Interface ---

    # 1. Componente de Upload de Arquivo (PDF)
    st.header("Faça o upload do seu BOA em PDF")
    uploaded_file = st.file_uploader(
        "Escolha o arquivo PDF",
        type="pdf",
        help="Apenas arquivos no formato .pdf são aceitos."
    )

    if uploaded_file:
        if validate_boa(uploaded_file):
            st.success(f"Arquivo {uploaded_file.name} foi validado e carregado com sucesso!")
        else:
            st.error("O arquivo carregado não é um BOA válido. Por favor, verifique o arquivo e tente novamente.")

    # # 2. Componente de Seleção (Selectbox)
    # st.header("2. Selecione a Empresa Conveniada")

    # # Lista das empresas conveniadas
    # empresas_conveniadas = companies_df["INSTITUIÇÃO"].tolist()

    # # O widget selectbox retorna o nome que foi selecionado
    # selected_company = st.selectbox(
    #     "Escolha uma empresa abaixo:",
    #     options=empresas_conveniadas,
    #     index=None,
    #     placeholder="Selecione uma das empresas conveniadas à UFRJ",
    #     help="O nome selecionado será associado ao documento enviado."
    # )

    # st.write("#### Não encontrou a empresa?")

    # # 2. Crie o checkbox para ativar a entrada manual
    # ativar_entrada_manual = st.checkbox("Digitar o nome de outra empresa")

    # # 3. Variável para armazenar o nome final da empresa
    # nome_empresa_final = ""

    # # 4. Lógica condicional baseada no checkbox
    # if ativar_entrada_manual:
    #     # Se o checkbox estiver MARCADO, mostre o campo de texto
    #     nome_digitado = st.text_input(
    #         "Digite o nome da nova empresa:",
    #         placeholder="Nome da empresa que não está na lista"
    #     )
    #     # O nome final será o que o usuário digitar
    #     nome_empresa_final = nome_digitado.strip()
    # else:
    #     # Se o checkbox estiver DESMARCADO, o nome final é o do selectbox
    #     nome_empresa_final = selected_company
    # st.markdown("---")

    nome_empresa_final = "2PLAN STUDIO ARQUITETURA LTDA"

    # --- Lógica e Exibição dos Resultados ---
    if st.button("Processar Dados"):
        # Verifica se um arquivo foi carregado E se um nome foi selecionado
        if uploaded_file is not None and nome_empresa_final:            
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
                
                validations_dict = validate_eligibility(academic_data, companies_df, nome_empresa_final, uploaded_file)
                # st.write(validations_dict)
                generate_report_card(academic_data, validations_dict)
                if validations_dict["valid_student"]:
                    st.success("Todas as condições para a validação do estágio foram atendidas. O estudante está apto a realizar o estágio.")

        elif uploaded_file is None:
            st.error("Erro: Por favor, faça o upload de um arquivo PDF antes de processar.")
        else:
            st.warning("Algo deu errado. Verifique se todas as opções foram preenchidas.")


if __name__ == "__main__":
    main()
