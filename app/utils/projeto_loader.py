# import json
# import os

# def carregar_projetos():
#     """Carrega projetos do JSON"""
#     with open('projetos_data.json', 'r', encoding='utf-8') as f:
#         return json.load(f)

# def get_screenshots(projeto_id):
#     """Carrega screenshots do projeto"""
#     pasta = f"static/screenshots/{projeto_id}/"
#     if not os.path.exists(pasta):
#         return []
    
#     imgs = []
#     for arquivo in os.listdir(pasta):
#         if arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
#             imgs.append(os.path.join(pasta, arquivo))
#     return imgs[:2]  # Máximo 2 imagens
import json
import os
from pathlib import Path

# Obter caminho absoluto do diretório atual
BASE_DIR = Path(__file__).resolve().parent.parent  # aponta para app/

def carregar_projetos():
    """Carrega projetos do JSON"""
    json_path = BASE_DIR / 'projetos_data.json'
    
    # Verificação extra para debug
    if not json_path.exists():
        raise FileNotFoundError(f"Arquivo JSON não encontrado em: {json_path}")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_screenshots(projeto_id):
    """Carrega screenshots do projeto"""
    pasta = BASE_DIR / "static" / "screenshots" / projeto_id
    
    if not pasta.exists():
        return []
    
    imgs = []
    for arquivo in os.listdir(pasta):
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            imgs.append(str(pasta / arquivo))  # Caminho completo
    
    return imgs[:2]  # Máximo 2 imagens


# Mapeamentos diretos
MARCOS_PROJETOS = {
    "✔️ Projeto de Análise de Dados Veiculares (Setor Automotivo)": "dados_veiculares",
    "✔️ Hackathon Ada - Diversidade e Performance Corporativa": "hackathon_ada", 
    "✔️ Projeto de IA Médica - Detecção de Melanoma": "melanoma_representatividade",
    "✔️ Automação de Dashboards e Qualidade de Dados": "automacao_mapas_calor",
    "✔️ Estágio na CVM - LLMOps e Banco Vetorial": "cvm_vetorial_testes"
}

HISTORICO_PROJETOS = {
    "Análise de Dados Veiculares": "dados_veiculares",
    "EDA Estratégia Olist": "eda_olist", 
    "IA Médica - Melanoma": "melanoma_representatividade",
    "Hackathon Ada Hack": "hackathon_ada",
    "Automação Looker Studio": "automacao_mapas_calor",
    "Automação Limpeza Dados": "remocao_sufixos",
    "Dashboard Farmacêutica": "dashboard_farmaceutica",
    #"Estágio CVM": "cvm_vetorial_testes",
    "Banco Vetorial CVM": "cvm_vetorial_testes",
    "Automação Verificação": "cvm_verificacao_comunicados"
}