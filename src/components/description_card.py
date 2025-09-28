import streamlit as st

def description_card():
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
