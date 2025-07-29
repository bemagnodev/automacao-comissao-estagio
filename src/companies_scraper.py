import pandas as pd
import pdfplumber


def scrape_companies_from_pdf(pdf_path: str, output_excel_path: str = "extracted_tables.xlsx") -> pd.DataFrame:
    dataframes = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                if table:
                    df = pd.DataFrame(table[1:], columns=table[0])
                    dataframes.append(df)

    if dataframes:
        final_df = pd.concat(dataframes, ignore_index=True)
        final_df.to_excel(output_excel_path, index=False)
        print("Tables successfully extracted!")
        print(final_df)
        return final_df
    else:
        print("No tables found in the PDF.")
        return pd.DataFrame()

if __name__ == "__main__":
    pdf_path = r"data/convenios-estagio.pdf"
    output_excel_path = "data/affiliated_companies.xlsx"
    scrape_companies_from_pdf(pdf_path, output_excel_path)
