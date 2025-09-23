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


def validate_eligibility(academic_data: dict, companies_df: pd.DataFrame, boa_path: str) -> dict:
    
    academic_requirements = {
        "minimum_cr": 6.0,
        "max_periods": academic_data["prazo_maximo"],
        "minimum_ext_hours": 160.0,
        "minimum_credits": 87
    }

    validations_dict = {
        "valid_cr": True,
        "valid_periods": True,
        "valid_ext_hours": True,
        "valid_company": True,
        "valid_credits": True,
        "valid_courses": True,
        "valid_student": True
    }

    # Validations according to business rules
    if not(academic_data["cr_acumulado"] >= academic_requirements["minimum_cr"]):
        validations_dict["valid_cr"] = False
        validations_dict["valid_student"] = False

    if not(academic_data["periodos_integralizados"] <= academic_data["prazo_maximo"]):
        validations_dict["valid_periods"] = False
        validations_dict["valid_student"] = False
    
    if not(academic_data["carga_horaria_extensao"] >= academic_requirements["minimum_ext_hours"]):
        validations_dict["valid_ext_hours"] = False
        validations_dict["valid_student"] = False
    
    # if not validate_company_affiliation(companies_df, company_name):
    #     validations_dict["valid_company"] = False
    #     validations_dict["valid_student"] = False
    

    # Check the required courses
    if not(academic_data["creditos_obtidos"] >= academic_requirements["minimum_credits"]):
        validations_dict["valid_credits"] = False
        validations_dict["valid_courses"] = False
        validations_dict["valid_student"] = False
        return validations_dict

    report = analyze_course_completion(boa_path)

    if not(report["status"]["cumpriu_todas_materias"]):
        validations_dict["valid_courses"] = False
        validations_dict["valid_student"] = False 

    return validations_dict


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
