import pdfplumber
import re


def extract_academic_data_from_BOA(pdf_path: str) -> dict:
    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() or ""

    # 2. Define os padrões de busca para cada campo de interesse
    # A chave do dicionário será a chave no nosso resultado final.
    # O valor é o texto exato que procuramos no documento.
    patterns = {
        "periodos_integralizados": r"Períodos Integralizados \(RES 10/2004 - CEG\):",
        "prazo_maximo": r"Prazo máximo de integralização:",
        "carga_horaria_obtida": r"Carga horária obtida acumulada:",
        "creditos_obtidos": r"Créditos obtidos acumulados:",
        "cr_acumulado": r"CR acumulado:",
        "carga_horaria_extensao": r"Carga horária acumulada extensão:"
    }

    extracted_data = {}

    # 3. Itera sobre cada padrão para encontrar o valor correspondente
    for key, label in patterns.items():
        # Constrói a expressão regular:
        # - texto_label: O texto que estamos procurando.
        # - \s*: Procura por zero ou mais espaços, quebras de linha ou tabs.
        # - ([\d.]+): Captura um grupo de um ou mais dígitos (\d) ou pontos (.).
        #   Este grupo é o nosso valor!
        regex = rf"{label}\s*([\d.]+)"

        # Procura pelo padrão no texto completo
        match = re.search(regex, full_text)

        if match:
            extracted_data[key] = float(match.group(1))
        else:
            extracted_data[key] = "Not found"

    return extracted_data


if __name__ == "__main__":
    file_path = r"C:\Users\fport\Downloads\boa - giovanna.pdf"

    academic_data = extract_academic_data_from_BOA(file_path)
    print(academic_data)
