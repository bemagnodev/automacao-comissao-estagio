import json
import re
from typing import Set, Dict, Any

import pdfplumber


def extract_academic_data_from_boa(pdf_path: str) -> dict:
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


def extract_required_courses(page_text: str) -> Set[str]:
    codes_to_exclude = {"ICPZ55", "ICPX06"}
    
    # Pattern to find required courses from periods 1-4.
    required_pattern = r"^((?:ICP|MAE|MAD|ICPX|ICPZ)\w+)\s+.*?\s+(?:\d+\.\d|NCC)\s+\d+\s+([1-4])"
    
    required_set = set()
    
    matches = re.findall(required_pattern, page_text, re.MULTILINE)
    for match in matches:
        course_code = match[0].upper()
        if course_code not in codes_to_exclude:
            required_set.add(course_code)
            
    return required_set


def extract_approved_courses(page_text: str) -> Set[str]:
    """
    Extracts all approved course codes from the text.

    :param page_text: The full text extracted from the first page of the BOA PDF.
    :return: A set of course codes for all approved courses.
    """
    codes_to_exclude = {"ICPZ55", "ICPX06"}

    # Pattern to find approved courses (lines ending with a grade).
    approved_pattern = r"^((?:ICP|MAE|MAD|ICPX|ICPZ)\w+)\s+.*?\s+\d+\.\d\s+\d+\s+([\d\.]{1,4})$"
    
    approved_set = set()
    
    matches = re.findall(approved_pattern, page_text, re.MULTILINE)
    for match in matches:
        course_code = match[0].upper()
        if course_code not in codes_to_exclude:
            approved_set.add(course_code)
            
    return approved_set


def check_course_completion_status(required_courses: Set[str], approved_courses: Set[str]) -> Dict[str, Any]:
    """
    Compares the set of required courses with the set of approved courses.

    :param required_courses: A set of required course codes.
    :param approved_courses: A set of approved course codes.
    :return: A dictionary containing the list of pending courses and a boolean indicating success.
    """
    pending_courses_set = required_courses - approved_courses
    
    has_completed_all = not pending_courses_set  # True if the pending set is empty
    
    return {
        "materias_pendentes": sorted(list(pending_courses_set)),
        "cumpriu_todas_materias": has_completed_all
    }


def analyze_course_completion(file_path: str) -> Dict[str, Any]:
    """
    Orchestrates the full process of extracting and comparing course data from a BOA PDF.

    :param file_path: The path to the BOA PDF file.
    :return: A dictionary with the complete analysis.
    """
    try:
        with pdfplumber.open(file_path) as pdf:
            page_1_text = pdf.pages[0].extract_text()

            # Step 1: Extract required courses
            required = extract_required_courses(page_1_text)
            
            # Step 2: Extract approved courses
            approved = extract_approved_courses(page_1_text)

            # TODO: implement extraction for other pages
            
            # Step 3: Compare and get the status
            completion_status = check_course_completion_status(required, approved)

            # Combine all information into a final report
            final_report = {
                "materias_necessarias_periodo4": sorted(list(required)),
                "materias_aprovadas": sorted(list(approved)),
                "status": completion_status
            }

            return final_report

    except Exception as e:
        return {"error": f"An error occurred while processing the PDF: {e}"}


if __name__ == "__main__":
    # file_path = r"data/boa - giovanna.pdf"
    file_path = r"data/boa.pdf"

    # academic_data = extract_academic_data_from_boa(file_path)
    # print(academic_data)
    
    full_analysis = analyze_course_completion(file_path)

    print("\n--- Course Completion Analysis ---")
    print(json.dumps(full_analysis, indent=2, ensure_ascii=False))
