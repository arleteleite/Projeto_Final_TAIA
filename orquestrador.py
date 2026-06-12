import json
import sys
import os

# Adiciona a pasta tools ao sys.path para importar o módulo
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools'))
import tools_fomento

def executar_workflow():
    print("=== INÍCIO DO WORKFLOW FOMENTÔ AGENT ===")
    
    # Etapa 1
    print("\n1. [Simulação] Recebendo proposta: 'Reflorestamento Sustentável do Cerrado'")
    tipo_edital = "socioambiental"
    area_tematica = "restauracao_ecologica"
    print(f"   - Tipo de Edital: {tipo_edital}")
    print(f"   - Área Temática: {area_tematica}")

    # Etapa 2
    print("\n2. [Tool Call] consultar_criterios_edital")
    resultado_criterios = tools_fomento.consultar_criterios_edital(tipo_edital, area_tematica)
    criterios = resultado_criterios["criterios"]
    print("   - Regras recuperadas do edital:")
    for c in criterios:
        print(f"     * {c['criterio']} (Peso: {c['peso']}, Obrigatório: {c['obrigatorio']})")

    # Etapa 3
    print("\n3. [Simulação] Avaliador atribuindo notas")
    # Escalonando as notas 9, 8, 9 para 90, 80, 90 para adequação ao padrão 0-100 do cálculo
    criterios_avaliados = [
        {"criterio": "aderencia_ao_objetivo", "nota": 90, "peso": 30},
        {"criterio": "capacidade_tecnica", "nota": 80, "peso": 20},
        {"criterio": "impacto_comunitario", "nota": 90, "peso": 50}
    ]
    print("   - Notas atribuídas (escala 0-100):")
    for ca in criterios_avaliados:
        print(f"     * {ca['criterio']}: {ca['nota']}")

    # Etapa 4
    print("\n4. [Tool Call] calcular_nota_aderencia")
    nota_final = tools_fomento.calcular_nota_aderencia(criterios_avaliados)
    print(f"   - Nota final ponderada calculada: {nota_final}")

    # Etapa 5
    print("\n5. [Tool Call] registrar_log_execucao")
    resultado_log = tools_fomento.registrar_log_execucao("Avaliação da Proposta", "analise_concluida", f"Proposta avaliada com nota {nota_final}")
    print("   - Log registrado!")

    # Etapa 6
    print("\n6. [Processamento] Empacotando resultado final em JSON (Contrato: schema_saida.json)")
    saida_json = {
        "status": "aprovado_para_revisao",
        "nota_aderencia": nota_final,
        "criterios_atendidos": [
            "aderencia_ao_objetivo (Nota 90)", 
            "capacidade_tecnica (Nota 80)", 
            "impacto_comunitario (Nota 90)"
        ],
        "criterios_pendentes": [],
        "documentos_faltantes": [
            "Certidão Negativa de Débitos Ambientais"
        ],
        "riscos_identificados": [
            "Cronograma de plantio das mudas está muito concentrado em poucos meses"
        ],
        "recomendacoes": [
            "Apresentar plano de contingência caso ocorram atrasos na entrega das mudas"
        ],
        "parecer_final": "A proposta 'Reflorestamento Sustentável do Cerrado' atende muito bem aos critérios do edital, apresentando forte impacto comunitário e boa aderência aos objetivos. O projeto obteve uma excelente nota, porém exige complementação documental e mitigação de pequenos riscos operacionais identificados. Recomenda-se avançar com o projeto.",
        "necessita_revisao_humana": True
    }

    json_string = json.dumps(saida_json, indent=2, ensure_ascii=False)
    
    # Salvando em arquivo para demonstrar que o arquivo foi gerado
    with open("resultado_avaliacao.json", "w", encoding="utf-8") as f:
        f.write(json_string)
        
    print("   - Arquivo 'resultado_avaliacao.json' gerado e salvo.")
    
    print("\n=== JSON FINAL GERADO ===")
    print(json_string)

if __name__ == '__main__':
    executar_workflow()
