import streamlit as st


def report_card(academic_data, validations_dict):
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
            
        st.write("")

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