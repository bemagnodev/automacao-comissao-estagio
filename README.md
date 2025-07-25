# Projeto de Automação da Comissão de Estágio - IC/UFRJ

## 1. Visão Geral do Projeto

Este projeto visa o desenvolvimento de uma ferramenta para automatizar e otimizar o processo de verificação de documentos para a Comissão de Estágio do Instituto de Computação (IC) da UFRJ. O objetivo principal é reduzir a carga de trabalho manual da comissão e aumentar a eficiência da análise, oferecendo uma verificação preliminar automática dos critérios de elegibilidade dos alunos. A iniciativa faz parte do projeto InovaProcess, especificamente da Frente 2: Engenharia e Automação de Soluções.

## 2. O Processo Atual e Seus Desafios

O fluxo atual de solicitação e aprovação de estágios é um processo manual que, embora estruturado, apresenta diversos gargalos e pontos de atrito para alunos e para a comissão.

### Principais Desafios:
* **Dependência de Terceiros:** O processo depende da agilidade da empresa contratante para assinar o Plano de Atividades e o Termo de Compromisso, impactando a capacidade do aluno de cumprir os prazos.
* **Prazos Rígidos:** A submissão da documentação possui prazos rigorosos (15 dias de antecedência para o primeiro estágio e 30 dias para renovação). Solicitações fora do prazo ou com documentação incompleta são automaticamente indeferidas.
* **Processo Manual de Verificação:** A comissão analisa manualmente cada documento para validar a elegibilidade do aluno, um processo propenso a atrasos e erros.
* **Verificação de Convênios:** É um pré-requisito que a empresa tenha um convênio ativo com a UFRJ. Atualmente, a consulta é feita através de um arquivo PDF disponibilizado online, cuja frequência de atualização não é clara, o que pode gerar inconsistências.
* **Falta de Transparência:** Após a submissão, não há um sistema claro para que o aluno acompanhe o andamento da sua solicitação.

## 3. A Solução: Produto Mínimo Viável (MVP)

A primeira versão da ferramenta (MVP) consistirá em um script de automação focado na validação para a **primeira solicitação de estágio**. O script realizará a leitura e interpretação dos documentos acadêmicos do aluno e, ao final, retornará um resultado simplificado de **APROVADO** ou **REPROVADO** na pré-análise.

### Funcionalidades do MVP:
O script irá extrair e validar as seguintes regras de negócio:
* **Coeficiente de Rendimento (CRA):** Verificar se o CRA do aluno é igual ou superior a 6,0.
* **Integralização de Créditos:** Validar se o aluno já integralizou todos os créditos das disciplinas até o 4º período, inclusive.
* **Prazo de Integralização do Curso:** Analisar o período de ingresso do aluno e validar se ele não ultrapassou o período máximo de 14 semestres para a conclusão do curso.
* **Horas de Extensão:** Validar se o aluno já cumpriu o mínimo de 160 horas de atividades de extensão.

## 4. Documentos Processados

Para a análise, o aluno deve encaminhar um conjunto de documentos à comissão, que servirão de entrada para a ferramenta. O MVP focará na leitura e extração de dados principalmente do **Boletim/Histórico Escolar**.

* Boletim acadêmico atualizado.
* Boletim de Orientação Acadêmica (BOA) do período vigente.
* Plano de Atividades do Estagiário.
* Termo de Compromisso.
* Cópia da apólice de seguro de acidentes pessoais.

## 5. Pilha Tecnológica (Tech Stack)

* **Linguagem de Programação:** **Python**
    * **Justificativa:** A escolha se baseia em seu robusto ecossistema de bibliotecas para manipulação de PDFs e análise de dados (como `pdfplumber`, `PyPDF2`, `pandas`), sua capacidade de prototipagem ágil, a ampla documentação e suporte da comunidade e seu potencial de escalabilidade para futuras funcionalidades com Inteligência Artificial e Machine Learning.

## 6. Riscos e Pontos de Atenção

* **Alteração no Layout dos Documentos Acadêmicos:** Uma mudança no layout do Histórico Escolar pela UFRJ pode quebrar o script de análise, gerando erros ou leituras incorretas.
    * **Mitigação:** O código será bem documentado para facilitar ajustes.
* **Desatualização do PDF de Convênios:** A ferramenta pode aprovar ou reprovar uma empresa com base em uma lista desatualizada, causando transtornos.
    * **Mitigação:** A comissão será informada de que a checagem é baseada na última versão conhecida do PDF, recomendando uma dupla checagem manual até que uma solução definitiva seja implementada.

## 7. Escopo Futuro (Pós-MVP)

Após a validação do MVP, o projeto poderá evoluir para incluir:
* **Criação de uma Interface Web Simples:** Um portal para que um membro da comissão possa fazer o upload dos documentos, em vez de executar o script localmente.
* **Notificação Automática por E-mail:** Integrar um serviço de envio de e-mails para comunicar o resultado da pré-análise.
* **Automação do Processo de Renovação:** Expandir a ferramenta para lidar com as regras específicas da renovação de estágio, como a validação do relatório de atividades, avaliações e a regra de não reprovação com nota inferior a 4,0.
