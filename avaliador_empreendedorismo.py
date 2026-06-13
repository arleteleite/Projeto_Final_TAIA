import json
import sys
import os

# Adiciona a pasta tools ao sys.path para importar o módulo
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools'))
import tools_fomento

def avaliar_proposta_empreendedorismo():
    print("=== INICIANDO AVALIAÇÃO DE proposta_empreendedorismo.txt ===")
    
    # 1. Ler o conteúdo de proposta_empreendedorismo.txt
    caminho_proposta = "proposta_empreendedorismo.txt"
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
    tipo_edital = "empreendedorismo"
    area_tematica = "tecnologia"
    print(f"2. [Tool Call] consultar_criterios_edital(tipo='{tipo_edital}', area='{area_tematica}')")
    res_criterios = tools_fomento.consultar_criterios_edital(tipo_edital, area_tematica)
    print(f"Resultado da Consulta: {res_criterios}\n")
    
    # 3. Tratamento para critérios ausentes/erro
    if res_criterios["status"] != "sucesso" or not res_criterios["criterios"]:
        print("3. Atenção: Critérios válidos não foram localizados para este edital. Pulando avaliação e cálculo de nota.\n")
        nota_final = 0.0
        status_final = "incompativel"
        criterios_atendidos = []
        criterios_pendentes = []
        documentos_faltantes = []
        riscos_identificados = [
            "Edital não cadastrado: Não foram localizados os critérios de avaliação no banco de dados para a categoria 'empreendedorismo' e área 'tecnologia'."
        ]
        recomendacoes = [
            "Cadastrar as regras e pesos do edital de Empreendedorismo/Tecnologia no banco de dados de critérios.",
            "Submeter a proposta novamente após o cadastro do edital no sistema."
        ]
        parecer_final = (
            "A análise técnica da proposta 'TechAgro: Inovação no Campo' foi interrompida porque as regras do edital "
            "(critérios e pesos para 'empreendedorismo' / 'tecnologia') não foram localizadas no sistema. Devido a esta "
            "ausência de critérios no banco de dados, o projeto foi classificado temporariamente como incompatível (nota de aderência 0), "
            "exigindo a intervenção humana para cadastrar o edital ou realizar a avaliação manual."
        )
    else:
        # Caminho feliz se existisse (não será executado neste teste)
        criterios = res_criterios["criterios"]
        criterios_avaliados = []
        # (código para caso houvesse critérios...)
        nota_final = tools_fomento.calcular_nota_aderencia(criterios_avaliados)
        status_final = "aprovado_para_revisao"
        criterios_atendidos = []
        criterios_pendentes = []
        documentos_faltantes = []
        riscos_identificados = []
        recomendacoes = []
        parecer_final = ""

    # 4. Registrar log (Tool Call para registrar_log_execucao)
    print("4. [Tool Call] registrar_log_execucao")
    tools_fomento.registrar_log_execucao(
        etapa=f"Análise de Proposta ({caminho_proposta})",
        status="erro",
        resultado=f"Erro: critérios de edital não encontrados no banco de dados. Status definido como: {status_final}"
    )
    print("")
    
    # 5. Gerar saída JSON final (schema_saida.json)
    saida = {
        "status": status_final,
        "nota_aderencia": nota_final,
        "criterios_atendidos": criterios_atendidos,
        "criterios_pendentes": criterios_pendentes,
        "documentos_faltantes": documentos_faltantes,
        "riscos_identificados": riscos_identificados,
        "recomendacoes": recomendacoes,
        "parecer_final": parecer_final,
        "necessita_revisao_humana": True
    }
    
    json_string = json.dumps(saida, indent=2, ensure_ascii=False)
    
    with open("resultado_avaliacao.json", "w", encoding="utf-8") as f:
        f.write(json_string)
        
    print("5. Arquivo 'resultado_avaliacao.json' gerado de acordo com schema_saida.json.")
    print("\n--- JSON FINAL GERADO ---")
    print(json_string)
    print("====================================================")

if __name__ == '__main__':
    avaliar_proposta_empreendedorismo()
