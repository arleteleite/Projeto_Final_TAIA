import json
import sys
import os

# Adiciona a pasta tools ao sys.path para importar o módulo
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools'))
import tools_fomento

def avaliar_minha_proposta_3():
    print("=== INICIANDO AVALIAÇÃO DE minha_proposta_3.txt ===")
    
    # 1. Ler o conteúdo de minha_proposta_3.txt
    caminho_proposta = "minha_proposta_3.txt"
    if not os.path.exists(caminho_proposta):
        print(f"Erro: Arquivo {caminho_proposta} não encontrado.")
        sys.exit(1)
        
    with open(caminho_proposta, "r", encoding="utf-8") as f:
        conteudo_proposta = f.read()
    
    print(f"1. Leitura de {caminho_proposta} realizada com sucesso.")
    print("--- Conteúdo da Proposta ---")
    print(conteudo_proposta)
    print("----------------------------\n")
    
    # 2. Consultar regras (Tool Call para consultar_criterios_edital)
    print("2. [Tool Call] consultar_criterios_edital(tipo='socioambiental', area='restauracao_ecologica')")
    res_criterios = tools_fomento.consultar_criterios_edital("socioambiental", "restauracao_ecologica")
    print(f"Resultado da Consulta: {res_criterios}\n")
    
    if res_criterios["status"] != "sucesso":
        print("Erro ao consultar critérios.")
        sys.exit(1)
        
    criterios = res_criterios["criterios"]
    
    # 3. Avaliação rigorosa (notas do Agente baseadas no texto)
    # Aderência ao Objetivo: 95 (excelente restauração de 50ha de nascentes e matas ciliares no Cerrado)
    # Capacidade Técnica: 100 (equipe excelente: 2 doutores, 1 biólogo sênior, >15 anos de exp)
    # Impacto Comunitário: 10 (baixíssimo: apenas 4 famílias beneficiadas, caráter apenas de ajuda de custo/tráfego)
    criterios_avaliados = [
        {"criterio": "aderencia_ao_objetivo", "nota": 95, "peso": 30},
        {"criterio": "capacidade_tecnica", "nota": 100, "peso": 20},
        {"criterio": "impacto_comunitario", "nota": 10, "peso": 50}
    ]
    
    print("3. Avaliação Rigorosa:")
    for ca in criterios_avaliados:
        print(f"   - Critério: {ca['criterio']} | Nota: {ca['nota']} | Peso: {ca['peso']}")
    print("")
    
    # 4. Calcular a nota (Tool Call para calcular_nota_aderencia)
    print("4. [Tool Call] calcular_nota_aderencia")
    nota_final = tools_fomento.calcular_nota_aderencia(criterios_avaliados)
    print(f"Nota final ponderada calculada: {nota_final}\n")
    
    # 5. Registrar log (Tool Call para registrar_log_execucao)
    print("5. [Tool Call] registrar_log_execucao")
    tools_fomento.registrar_log_execucao(
        etapa="Análise de Proposta (minha_proposta_3.txt)",
        status="analise_concluida",
        resultado=f"Análise finalizada com nota final: {nota_final}"
    )
    print("")
    
    # 6. Gerar saída JSON final (schema_saida.json)
    # Detalhar no parecer_final o contraste entre equipe excelente e baixíssimo impacto social, justificando a nota final de 53.5
    saida = {
        "status": "pendente",
        "nota_aderencia": nota_final,
        "criterios_atendidos": [
            "aderencia_ao_objetivo",
            "capacidade_tecnica"
        ],
        "criterios_pendentes": [
            "impacto_comunitario"
        ],
        "documentos_faltantes": [],
        "riscos_identificados": [
            "Baixíssimo Impacto Comunitário: A proposta beneficia diretamente apenas 4 famílias locais e restringe-se a uma ajuda de custo temporária para passagem de maquinário. Não há iniciativas de educação ambiental ou viveiros comunitários.",
            "Desalinhamento com a diretriz socioambiental: O peso de impacto comunitário no edital é de 50%, e a falta de engajamento social coloca o projeto em desvantagem crítica."
        ],
        "recomendacoes": [
            "Reformular a seção de impacto comunitário da proposta para engajar de forma contínua as famílias locais.",
            "Propor a criação de viveiros comunitários ou programas de capacitação e educação ambiental.",
            "Aumentar o número de beneficiários diretos do projeto."
        ],
        "parecer_final": (
            "A proposta 'Recuperação Ecológica do Vale Verde' demonstra excelente aderência ao objetivo de restauração "
            "de nascentes e matas ciliares no bioma Cerrado (Nota 95). Além disso, a capacidade técnica da equipe é indiscutível "
            "e exemplar, contando com doutores e biólogo sênior com vasta experiência (Nota 100). No entanto, o edital é de natureza "
            "socioambiental e atribui peso de 50% ao Impacto Comunitário. Neste quesito, a proposta é extremamente fraca e limitada "
            "(Nota 10), atendendo apenas 4 famílias em caráter emergencial para tráfego de máquinas, sem engajamento social real. "
            "Essa disparidade entre uma equipe excelente e um baixíssimo impacto social gerou uma nota final de 53.5, deixando o status "
            "da proposta como 'pendente' até que passe por revisão humana complementar para avaliar a viabilidade de readequação social."
        ),
        "necessita_revisao_humana": True
    }
    
    json_string = json.dumps(saida, indent=2, ensure_ascii=False)
    
    with open("resultado_avaliacao.json", "w", encoding="utf-8") as f:
        f.write(json_string)
        
    print("6. Arquivo 'resultado_avaliacao.json' gerado de acordo com schema_saida.json.")
    print("\n--- JSON FINAL GERADO ---")
    print(json_string)
    print("====================================================")

if __name__ == '__main__':
    avaliar_minha_proposta_3()
