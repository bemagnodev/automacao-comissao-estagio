# Projeto de Automação da Comissão de Estágio - IC/UFRJ
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

---

### Visão Geral
Ferramenta de automação em **Python** para otimizar a verificação de documentos da Comissão de Estágio do Instituto de Computação (IC) da UFRJ. O objetivo é reduzir o trabalho manual e agilizar a pré-análise e aprovação de alunos, como parte do projeto de extensão **InovaProcess**.

*Este repositório é um fork do [projeto original](https://github.com/Inova-Process/automacao-comissao-estagio), onde sou um contribuidor ativo.*

### O Problema
O processo atual de aprovação de estágios é manual, lento e propenso a gargalos. Os principais desafios são:
* **Prazos Rígidos:** Submissão de documentação com prazos rigorosos para os alunos.
* **Verificação Manual:** A comissão analisa cada documento manualmente, um processo demorado.
* **Falta de Transparência:** O aluno não possui um sistema claro para acompanhar o status da sua solicitação.

### A Solução (MVP)
A primeira versão (MVP) da ferramenta é um script de automação que realiza uma pré-análise dos documentos do aluno, retornando um resultado de **APROVADO** ou **REPROVADO** com base nas seguintes regras de negócio:
* Verificar se o Coeficiente de Rendimento (CRA) é ≥ 6.0.
* Validar a integralização de todos os créditos obrigatórios até o 4º período.
* Analisar se o aluno está dentro do prazo máximo de 14 semestres para conclusão do curso.
* Validar o cumprimento do mínimo de 160 horas de atividades de extensão.

### Tecnologias Utilizadas
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)  ![PDFPlumber](https://img.shields.io/badge/PDFPlumber-4A5568?style=for-the-badge)

### Meu Papel e Contribuições
Como um dos desenvolvedores do projeto, minhas responsabilidades atuais incluem:
* O desenvolvimento do script principal de automação em **Python**.
* A implementação das regras de negócio para extração e validação de dados do Histórico Escolar da UFRJ.
* Pesquisa e escolha das bibliotecas mais eficientes para manipulação de arquivos PDF.

### Como Executar
*Instruções de instalação e execução do projeto serão adicionadas em breve.*

### Contribuidores
* [Bernardo Magno](https://github.com/bemagnodev)
* [Felipe Rivetti](https://github.com/feliperivetti)
