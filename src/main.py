from elegibility_validator import validate_eligibility

import pandas as pd


def main():
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

    company_name = "2PLAN STUDIO ARQUITETURA LTDA"
    validate_eligibility(academic_data, companies_df, company_name)


if __name__ == "__main__":
    main()
