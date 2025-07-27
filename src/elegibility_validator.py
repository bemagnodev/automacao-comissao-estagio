from BOA_scraper import extract_academic_data_from_BOA

import numpy as np
import pandas as pd

def validate_company_affiliation(companies_df: pd.DataFrame, company_name: str) -> bool:
    # Maybe we should validate the company`s CNPJ instead of the name?
    institutions = companies_df['INSTITUIÇÃO'].values

    index = np.searchsorted(institutions, company_name)

    if not(index < len(institutions) and institutions[index] == company_name):
        return False
    return True


def validate_eligibility(academic_data: dict, companies_df: pd.DataFrame, company_name: str) -> bool:
    is_valid = True

    # Validations according to business rules
    if not(academic_data["cr_acumulado"] >= 6.0):
        print("Invalid: CR acumulado is below 6.0.")
        is_valid = False

    if not(academic_data["periodos_integralizados"] <= academic_data["prazo_maximo"]):
        print("Invalid: Periodos integralizados exceeds prazo maximo.")
        is_valid = False
    
    if not(academic_data["carga_horaria_extensao"] >= 160.0):
        print("Invalid: Carga horaria de extensao is below 160 hours.")
        is_valid = False
    
    # TODO: Uncomment and implement the logic for materias_obrigatorias
    # if not(academic_data["creditos"] >= 100000):
    #     print("Invalid: Creditos obtained is below 100000.")
    #     is_valid = False

    if not validate_company_affiliation(companies_df, company_name):
        print(f"Invalid: Company {company_name} is not affiliated with UFRJ.")
        is_valid = False

    if is_valid:
        print("All validations passed. The student is eligible.")

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

    print(academic_data)
    
    # Scrape companies data from the provided PDF
    companies_df = pd.read_excel("data/affiliated_companies.xlsx")

    empresa_teste = "2PLAN STUDIO ARQUITETURA LTDA"
    validate_eligibility(academic_data, companies_df, empresa_teste)
