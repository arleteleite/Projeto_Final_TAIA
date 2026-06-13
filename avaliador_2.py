import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'tools'))
import tools_fomento

def avaliar_minha_proposta_2():
    # 2. Consultar regras
    res_criterios = tools_fomento.consultar_criterios_edital("socioambiental", "restauracao_ecologica")
    
    # 3. Avaliação rigorosa (notas do Agente)
    criterios_avaliados = [
        {"criterio": "aderencia_ao_objetivo", "nota": 95, "peso": 30},
        {"criterio": "capacidade_tecnica", "nota": 30, "peso": 20},
        {"criterio": "impacto_comunitario", "nota": 100, "peso": 50}
    ]
    
    # 4. Calcular a nota
    nota_final = tools_fomento.calcular_nota_aderencia(criterios_avaliados)
    
    # 5. Registrar log
    tools_fomento.registrar_log_execucao(
        etapa="Análise de Proposta (minha_proposta_2.txt)",
        status="analise_concluida",
        resultado=f"Análise finalizada. Nota final: {nota_final}"
    )
    
    # 6. Gerar saída JSON final
    saida = {
        "status": "pendente",
        "nota_aderencia": nota_final,
        "criterios_atendidos": [
            "aderencia_ao_objetivo",
            "impacto_comunitario"
        ],
        "criterios_pendentes": [
            "capacidade_tecnica"
        ],
        "documentos_faltantes": [],
        "riscos_identificados": [
            "Capacidade Técnica Crítica: A equipe executora é composta exclusivamente por recém-formados sem experiência prática comprovada em restauração ecológica, representando alto risco para a execução de 50 hectares."
        ],
        "recomendacoes": [
            "Condicionar a aprovação à inclusão de um responsável técnico sênior ou contratação de consultoria especializada para orientar a execução do projeto."
        ],
        "parecer_final": (
            "A proposta tem excelente aderência aos objetivos do edital (Nota 95) e o impacto comunitário é máximo (Nota 100), com cronograma realista e documentação completa. Entretanto, a Capacidade Técnica da equipe foi severamente penalizada (Nota 30) e considerada pendente. O projeto é de grande magnitude (50 hectares e 10.000 mudas) e será o primeiro executado por esta equipe de recém-formados, que admite não ter experiência prática. Apesar da nota final alta devido aos pesos (84.5), o risco operacional é extremo. Status alterado para 'pendente' aguardando avaliação humana sobre o risco da equipe."
        ),
        "necessita_revisao_humana": True
    }
    
    json_string = json.dumps(saida, indent=2, ensure_ascii=False)
    
    with open("resultado_avaliacao.json", "w", encoding="utf-8") as f:
        f.write(json_string)
        
    print("\n--- JSON GERADO COM SUCESSO ---")
    print(json_string)

if __name__ == '__main__':
    avaliar_minha_proposta_2()
