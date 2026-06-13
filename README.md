# 🚀 Fomentô Agent

## Descrição do Projeto
O Fomentô Agent é um Workflow Agêntico desenvolvido como Projeto Final da disciplina de Tópicos Avançados em IA (TAIA). Ele automatiza o Procedimento Operacional Padrão (POP) de análise de aderência de propostas a editais de fomento.

## Estrutura do Repositório
- `prd_fomento_agent.md`: Documentação principal do contexto, problema e workflow.
- `workflow.yaml`: Mapeamento declarativo das etapas e dependências do processo.
- `contratos/`: Contém os JSON Schemas estritos para entrada e saída de dados.
- `tools/tools_fomento.py`: Scripts Python utilizados para Tool Calling (cálculo matemático, consulta a "banco de dados" e geração de logs).

## Como funciona (Tool Calling)
A Inteligência Artificial atua como um motor de raciocínio que orquestra ferramentas locais. Em vez de alucinar notas, o agente consulta os pesos reais do edital (`consultar_criterios_edital`), delega a matemática exata para o script Python (`calcular_nota_aderencia`) e registra o histórico da execução (`registrar_log_execucao`), retornando um parecer final auditável e validado para revisão humana.
