"""
Ferramentas de apoio para o Fomentô Agent.
"""

from typing import List, Dict, Any
import datetime

def consultar_criterios_edital(tipo_edital: str, area_tematica: str) -> dict:
    """
    Consulta os critérios de um edital com base no seu tipo e área temática.

    Args:
        tipo_edital (str): O tipo do edital (ex: 'socioambiental', 'inovacao', 'pesquisa', 'empreendedorismo').
        area_tematica (str): A área temática específica do edital.

    Returns:
        dict: Um dicionário contendo o status da operação, mensagem e a lista de critérios exigidos pelo edital.
    """
    # Banco de dados simulado
    banco_de_dados = {
        "socioambiental": {
            "restauracao_ecologica": [
                {"criterio": "aderencia_ao_objetivo", "peso": 30, "obrigatorio": True},
                {"criterio": "capacidade_tecnica", "peso": 20, "obrigatorio": True},
                {"criterio": "impacto_comunitario", "peso": 50, "obrigatorio": False}
            ]
        }
    }
    
    if tipo_edital in banco_de_dados and area_tematica in banco_de_dados[tipo_edital]:
        return {
            "status": "sucesso",
            "mensagem": "Critérios encontrados com sucesso.",
            "criterios": banco_de_dados[tipo_edital][area_tematica]
        }
    else:
        return {
            "status": "erro",
            "mensagem": "Critérios não encontrados para os parâmetros informados.",
            "criterios": []
        }

def calcular_nota_aderencia(criterios_avaliados: list) -> float:
    """
    Calcula a nota de aderência da proposta com base nos critérios avaliados.

    Args:
        criterios_avaliados (list): Lista de critérios avaliados indicando a 'nota' (0-100) e o 'peso' (0-100).

    Returns:
        float: A nota de aderência final, variando de 0.0 a 100.0, arredondada para duas casas decimais.
    """
    nota_ponderada_total = 0.0
    
    for criterio in criterios_avaliados:
        nota = criterio.get('nota', 0)
        peso = criterio.get('peso', 0)
        nota_ponderada_total += (nota * peso)
        
    nota_final = nota_ponderada_total / 100
    
    return round(nota_final, 2)

def registrar_log_execucao(etapa: str, status: str, resultado: str) -> dict:
    """
    Registra um log de execução das etapas do Fomentô Agent.

    Args:
        etapa (str): Nome da etapa sendo executada (ex: 'Ingestão de Dados').
        status (str): O status da execução (ex: 'sucesso', 'falha').
        resultado (str): Detalhes do resultado da execução da etapa.
        
    Returns:
        dict: Dicionário contendo os dados do log gerado e uma mensagem de sucesso.
    """
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    log_dict = {
        "timestamp": timestamp,
        "etapa": etapa,
        "status": status,
        "resultado": resultado
    }
    
    print(f"[LOG] {log_dict}")
    
    return {
        "status": "sucesso",
        "mensagem": "Log registrado com sucesso.",
        "log": log_dict
    }

if __name__ == '__main__':
    print("--- Iniciando testes das ferramentas Fomentô ---")
    
    # Teste 1: consultar_criterios_edital
    print("\n[Teste 1] consultar_criterios_edital")
    resultado_consulta = consultar_criterios_edital("socioambiental", "restauracao_ecologica")
    print(f"Resultado Consulta: {resultado_consulta}")
    
    # Teste 2: calcular_nota_aderencia
    print("\n[Teste 2] calcular_nota_aderencia")
    # Simulando avaliação: aderencia (100 * 30), capacidade (80 * 20), impacto (90 * 50)
    criterios_mock = [
        {"nota": 100, "peso": 30},
        {"nota": 80, "peso": 20},
        {"nota": 90, "peso": 50}
    ]
    nota_final = calcular_nota_aderencia(criterios_mock)
    print(f"Nota Final Calculada: {nota_final}")
    
    # Teste 3: registrar_log_execucao
    print("\n[Teste 3] registrar_log_execucao")
    resultado_log = registrar_log_execucao("Teste de Ferramentas", "sucesso", f"Nota calculada foi {nota_final}")
    print(f"Retorno do Log: {resultado_log}")
    
    print("\n--- Testes concluídos ---")
