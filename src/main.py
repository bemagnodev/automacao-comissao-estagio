import pandas as pd

from boa_scraper import extract_academic_data_from_BOA
from elegibility_validator import validate_eligibility


def main(boa_path: str):
    academic_data = extract_academic_data_from_BOA(boa_path)

    academic_data = {
        "periodos_integralizados": 16,
        "prazo_maximo": 14,
        "carga_horaria_obtida": 120,
        "creditos_obtidos": 40.0,
        "cr_acumulado": 5.5,
        "carga_horaria_extensao": 120,
    }

    # Scrape companies data from the provided PDF
    companies_df = pd.read_excel("data/affiliated_companies.xlsx")

    company_name = "2PLAN STUDIO ARQUITETURA LTDA"
    validate_eligibility(academic_data, companies_df, company_name, boa_path)


if __name__ == "__main__":
    boa_path = "data/boa - giovanna.pdf"
    main(boa_path)
