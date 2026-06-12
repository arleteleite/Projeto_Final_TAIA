import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'tools'))
import tools_fomento

def avaliar_minha_proposta():
    # 2. Consultar regras
    res_criterios = tools_fomento.consultar_criterios_edital("socioambiental", "restauracao_ecologica")
    
    # 3. Avaliação (simulando as notas do LLM baseadas no texto lido)
    criterios_avaliados = [
        {"criterio": "aderencia_ao_objetivo", "nota": 95, "peso": 30},
        {"criterio": "capacidade_tecnica", "nota": 90, "peso": 20},
        {"criterio": "impacto_comunitario", "nota": 100, "peso": 50}
    ]
    
    # 4. Calcular a nota
    nota_final = tools_fomento.calcular_nota_aderencia(criterios_avaliados)
    
    # 5. Registrar log
    tools_fomento.registrar_log_execucao(
        etapa="Análise de Proposta (minha_proposta.txt)",
        status="analise_concluida",
        resultado=f"Análise finalizada. Nota: {nota_final}"
    )
    
    # 6. Gerar saída JSON final
    saida = {
        "status": "aprovado_para_revisao",
        "nota_aderencia": nota_final,
        "criterios_atendidos": [
            "aderencia_ao_objetivo",
            "capacidade_tecnica",
            "impacto_comunitario"
        ],
        "criterios_pendentes": [],
        "documentos_faltantes": [
            "Certidão Negativa de Débitos Ambientais"
        ],
        "riscos_identificados": [
            "Cronograma logístico de alto risco: plantio de 10.000 mudas concentrado em apenas 2 meses (novembro e dezembro)."
        ],
        "recomendacoes": [
            "Anexar a Certidão Negativa assim que for emitida.",
            "Estender a janela de plantio ou apresentar um plano de mitigação para contingências climáticas."
        ],
        "parecer_final": (
            "A proposta 'Reflorestamento Sustentável do Cerrado' atende excelentemente aos objetivos do edital. "
            "A capacidade técnica da equipe (engenheiros e biólogo experientes) é muito sólida (Nota 90), e a aderência "
            "ao objetivo de restauração de nascentes é alta (Nota 95). Destaca-se de maneira excepcional o impacto comunitário "
            "(Nota 100), pois 20 famílias serão integradas gerando renda alternativa. No entanto, há falta de uma certidão "
            "obrigatória e o cronograma de plantio é agressivo, concentrando muito risco em dois meses. O projeto é forte e "
            "merece aprovação para revisão humana para avaliar o risco do cronograma."
        ),
        "necessita_revisao_humana": True
    }
    
    json_string = json.dumps(saida, indent=2, ensure_ascii=False)
    
    print("\n--- JSON GERADO COM SUCESSO ---")
    print(json_string)

if __name__ == '__main__':
    avaliar_minha_proposta()
