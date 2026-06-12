# Product Requirements Document (PRD): Fomentô Agent

## Missão do Agente
A missão do Fomentô Agent é atuar como um assistente inteligente especializado em analisar editais de fomento e avaliar o grau de aderência de propostas de projetos, garantindo agilidade, precisão e mitigação de riscos na submissão de projetos.

## O Problema
A análise de editais de fomento (como bolsas, subvenções, financiamentos para pesquisa, inovação, projetos socioambientais e empreendedorismo) é um processo altamente complexo, extenso e demorado. Envolve a leitura de documentos longos, interpretação de regras específicas, critérios de elegibilidade restritos e prazos inflexíveis, muitas vezes resultando em desclassificação por erros operacionais ou falta de alinhamento estratégico.

## A Solução
O Fomentô Agent propõe uma solução baseada em inteligência artificial para automatizar a triagem e análise de editais e propostas. Ele extrai os requisitos dos editais e cruza com os dados da proposta do usuário, identificando pontos fortes, fracos, documentos faltantes e riscos, otimizando o tempo da equipe e aumentando a taxa de sucesso nas aprovações.

## Workflow Principal (8 Etapas)
1. **Ingestão de Dados:** Recebimento do edital e da proposta (documentos ou dados estruturados).
2. **Extração de Requisitos do Edital:** Identificação de critérios de elegibilidade, documentação exigida e regras de pontuação.
3. **Análise da Proposta:** Leitura e estruturação das informações contidas na proposta do usuário.
4. **Cruzamento de Dados (Matching):** Comparação entre os requisitos do edital e as informações da proposta.
5. **Avaliação de Aderência:** Cálculo da nota de aderência com base nos critérios atendidos e pendentes.
6. **Identificação de Gaps e Riscos:** Levantamento de documentos faltantes e potenciais riscos de desclassificação.
7. **Geração de Recomendações:** Sugestões práticas para melhoria da proposta e adequação ao edital.
8. **Relatório Final (Output):** Entrega de um parecer estruturado contendo o status, nota, e detalhamento da análise.

## Validação (Checklist Humano)
Para garantir a qualidade e segurança da submissão, uma revisão humana é necessária. O checklist inclui:
- [ ] Revisar documentos faltantes apontados pelo agente.
- [ ] Validar a interpretação dos riscos identificados.
- [ ] Confirmar se o parecer final faz sentido dado o contexto estratégico.
- [ ] Decisão final sobre a submissão (Aprovar, Ajustar, Descartar).
