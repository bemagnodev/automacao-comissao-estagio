import numpy as np
import pandas as pd

from boa_scraper import analyze_course_completion


def validate_company_affiliation(companies_df: pd.DataFrame, company_name: str) -> bool:
    # Maybe we should validate the company`s CNPJ instead of the name?
    institutions = companies_df['INSTITUIÇÃO'].values

    index = np.searchsorted(institutions, company_name)

    if not(index < len(institutions) and institutions[index] == company_name):
        return False
    return True


def validate_eligibility(academic_data: dict, companies_df: pd.DataFrame, company_name: str, boa_path: str) -> bool:
    
    academic_requirements = {
        "minimum_cr": 6.0,
        "max_periods": academic_data["prazo_maximo"],
        "minimum_ext_hours": 160.0,
        "minimum_credits": 87
    }

    is_valid = True

    # Validations according to business rules
    if not(academic_data["cr_acumulado"] >= academic_requirements["minimum_cr"]):
        print(f"CRA ({academic_data["cr_acumulado"]}) está abaixo do mínimo exigido {academic_requirements["minimum_cr"]}.")
        is_valid = False

    if not(academic_data["periodos_integralizados"] <= academic_data["prazo_maximo"]):
        print(f"Prazo máximo de integralização do curso ({academic_data["prazo_maximo"]} períodos) foi ultrapassado.")
        is_valid = False
    
    if not(academic_data["carga_horaria_extensao"] >= academic_requirements["minimum_ext_hours"]):
        print(f"Faltam {academic_requirements["minimum_ext_hours"] - academic_data["carga_horaria_extensao"]} horas de extensão. Mínimo exigido: {academic_requirements["minimum_ext_hours"]} horas.")
        is_valid = False
    
    if not validate_company_affiliation(companies_df, company_name):
        print(f"A empresa {company_name} não é afiliada à UFRJ.")
        is_valid = False
    

    # Check the required courses
    if not(academic_data["creditos_obtidos"] >= academic_requirements["minimum_credits"]):
        is_valid = False
        return is_valid


    report = analyze_course_completion(boa_path)

    if not(report["status"]["cumpriu_todas_materias"]):
        print(f"Não cumpriu todas as matérias obrigatórias. Faltam {len(report['status']['materias_pendentes'])} matérias.")
        is_valid = False 



    if is_valid:
        print("Todas as condições para a validação do estágio foram atendidas. O estudante está apto a realizar o estágio.")

    return is_valid


if __name__ == "__main__":
    # academic_data = extract_academic_data_from_BOA("data/boa.pdf")

    academic_data = {
        "periodos_integralizados": 16,
        "prazo_maximo": 14,
        "carga_horaria_obtida": 120,
        "creditos_obtidos": 40.0,
        "cr_acumulado": 5.5,
        "carga_horaria_extensao": 120,
    }

    # print(academic_data)
    
    # Scrape companies data from the provided PDF
    companies_df = pd.read_excel("data/affiliated_companies.xlsx")

    empresa_teste = "2PLAN STUDIO ARQUITETURA LTDA"
    validate_eligibility(academic_data, companies_df, empresa_teste)
