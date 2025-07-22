import pdfplumber
import pandas as pd

# Caminho para o seu arquivo PDF
caminho_arquivo = r"C:\Users\fport\Downloads\Convenios-para-Estagios.pdf"

# Lista para armazenar os DataFrames de cada tabela encontrada
lista_dfs = []

# Abre o arquivo PDF
with pdfplumber.open(caminho_arquivo) as pdf:
    # Itera sobre cada página do PDF
    for pagina in pdf.pages:
        # Extrai todas as tabelas da página atual
        # O método extract_tables() retorna uma lista de tabelas
        tabelas_pagina = pagina.extract_tables()
        
        # Itera sobre cada tabela encontrada na página
        for tabela in tabelas_pagina:
            # Verifica se a tabela não está vazia para evitar erros
            if tabela:
                # Converte a tabela (que é uma lista de listas) em um DataFrame do Pandas
                # Assume que a primeira linha da tabela é o cabeçalho
                df_tabela = pd.DataFrame(tabela[1:], columns=tabela[0])
                
                # Adiciona o DataFrame da tabela atual à nossa lista de DataFrames
                lista_dfs.append(df_tabela)

# Verifica se alguma tabela foi encontrada antes de tentar concatenar
if lista_dfs:
    # Concatena todos os DataFrames da lista em um único DataFrame final
    df_final = pd.concat(lista_dfs, ignore_index=True)
    df_final.to_excel("tabelas_extraidas.xlsx", index=False)  # Salva o DataFrame final em um arquivo Excel
    
    # Imprime o DataFrame final com os dados de todas as páginas
    print("Tabelas extraídas com sucesso!")
    print(df_final)
else:
    print("Nenhuma tabela foi encontrada no arquivo PDF.")