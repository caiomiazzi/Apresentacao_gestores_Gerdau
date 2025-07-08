import streamlit as st
import pandas as pd
import base64
import os
from utils.projeto_loader import MARCOS_PROJETOS, HISTORICO_PROJETOS
from utils.projeto_display import exibir_projeto, exibir_projeto_inline  


# Configuração da página
st.set_page_config(
    page_title="Caio Miazzi | Stellantis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =============================================================
# SOLUÇÃO ROBUSTA PARA A IMAGEM
# =============================================================

# Obter diretório do script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Construir caminho absoluto para a imagem
LOGO_PATH = os.path.join(SCRIPT_DIR, "static", "stellantis_logo_2.png")

# Verificação e fallback
if not os.path.exists(LOGO_PATH):
    # Tentar caminho alternativo (um nível acima)
    ALT_PATH = os.path.join(SCRIPT_DIR, "..", "static", "stellantis_logo_2.png")
    if os.path.exists(ALT_PATH):
        LOGO_PATH = ALT_PATH
    else:
        st.error(f"ERRO CRÍTICO: Logo não encontrada em:\n{LOGO_PATH}\nNem em:\n{ALT_PATH}")
        st.info("Conteúdo do diretório atual: " + str(os.listdir(SCRIPT_DIR)))
        if os.path.exists(os.path.join(SCRIPT_DIR, "static")):
            st.info("Conteúdo de static/:" + str(os.listdir(os.path.join(SCRIPT_DIR, "static"))))
        st.stop()

# Converter imagem para base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    
try:
    logo_base64 = image_to_base64(LOGO_PATH)
    IMAGE_HTML = f"data:image/png;base64,{logo_base64}"
except Exception as e:
    st.error(f"Erro ao converter imagem: {str(e)}")
    IMAGE_HTML = ""

# =============================================================

# Cores da Stellantis
STELLANTIS_BLUE = "#002B5C"
STELLANTIS_LIGHT_BLUE = "#0066CC"
STELLANTIS_SILVER = "#C0C0C0"

# CSS customizado - Tema Stellantis com responsividade
st.markdown(f"""
<style>
    .main-header {{
        background: linear-gradient(135deg, {STELLANTIS_BLUE} 0%, {STELLANTIS_LIGHT_BLUE} 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
    }}
    
    .hero-content {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.5rem;
    }}
    
    .hero-title {{
        font-size: clamp(1.8rem, 4vw, 2.5rem);
        font-weight: 700;
        margin-bottom: 0.5rem;
    }}
    
    .hero-info {{
        font-size: clamp(0.9rem, 2.5vw, 1.1rem);
        opacity: 0.9;
        margin-bottom: 0.5rem;
    }}
    
    .stellantis-logo {{
        max-width: 150px;
        height: auto;
        margin-top: 1rem;
    }}
    
    .section-title {{
        color: {STELLANTIS_BLUE};
        font-size: clamp(1.2rem, 3vw, 1.5rem);
        font-weight: 600;
        margin: 1.5rem 0 1rem 0;
        border-bottom: 2px solid {STELLANTIS_BLUE};
        padding-bottom: 0.5rem;
    }}
    
    .journey-item {{
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid {STELLANTIS_BLUE};
    }}
    
    .milestone-item {{
        background: white;
        padding: 0.8rem;
        border-radius: 8px;
        margin: 0.3rem 0;
        border-left: 3px solid {STELLANTIS_LIGHT_BLUE};
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }}
    
    .value-item {{
        background: #e8f4fd;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid {STELLANTIS_BLUE};
    }}
    
    .quote-section {{
        background: linear-gradient(to right, #f8f9fa, #e9ecef);
        padding: 1.5rem;
        border-radius: 10px;
        font-style: italic;
        text-align: center;
        margin: 1.5rem 0;
        border: 1px solid {STELLANTIS_SILVER};
    }}
    
    .tech-tags {{
        text-align: center;
        padding: 1rem;
        background: {STELLANTIS_BLUE};
        color: white;
        border-radius: 10px;
        font-size: clamp(0.9rem, 2.5vw, 1.1rem);
        font-weight: 600;
    }}
    
    .contact-links {{
        text-align: center;
        margin: 1rem 0;
    }}
    
    .contact-links a {{
        color: white;
        text-decoration: none;
        margin: 0 1rem;
        font-weight: 500;
    }}
    
    .contact-links a:hover {{
        text-decoration: underline;
    }}
    
    /* Layout sem rolagem - ajuste à tela */
    .main .block-container {{
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 100%;
    }}
    
    /* Ajuste de altura para não precisar scroll */
    .main-header {{
        min-height: 20vh;
    }}
    
    .journey-item {{
        padding: 0.8rem;
        margin: 0.3rem 0;
    }}
    
    .milestone-item {{
        padding: 0.6rem;
        margin: 0.2rem 0;
        font-size: 0.9rem;
    }}
    
    .section-title {{
        margin: 1rem 0 0.5rem 0;
        font-size: clamp(1.1rem, 2.5vw, 1.4rem);
    }}
    
    /* Responsividade para colunas */
    @media (max-width: 768px) {{
        .stColumns > div {{
            margin-bottom: 0.5rem;
        }}
        
        .main-header {{
            min-height: 15vh;
        }}
    }}
    
    /* Ajuste específico para viewport */
    @media (max-height: 800px) {{
        .journey-item, .milestone-item {{
            padding: 0.5rem;
            margin: 0.2rem 0;
        }}
        
        .section-title {{
            margin: 0.8rem 0 0.3rem 0;
        }}
    }}
    /* NOVOS ESTILOS PARA OS LOGOS */
    .top-logo {{
        text-align: center;
        margin-bottom: 1rem;
        padding: 10px;
    }}
    
    .bottom-logo {{
        text-align: center;
        margin-top: 2rem;
        padding: 15px;
    }}
    
    .logo-img {{
        width: 120px;
        height: auto;
        opacity: 0.9;
    }}
</style>
""", unsafe_allow_html=True)

# Inicializar estado do botão histórico
if 'show_history' not in st.session_state:
    st.session_state.show_history = False

# =============================================================
# LOGO NO TOPO (acima do cabeçalho principal)
# =============================================================
st.markdown(f"""
<div class="top-logo">
    <img src="{IMAGE_HTML}" alt="Stellantis Logo" class="logo-img">
</div>
""", unsafe_allow_html=True)

# Cabeçalho principal SEM LOGOS
st.markdown(f"""
<div class="main-header">
    <div class="hero-content">
        <div style="text-align: center;">
            <h1 class="hero-title">Caio Miazzi</h1>
            <p class="hero-info">32 anos | São Paulo - SP</p>
            <p class="hero-info">Cientista de Dados em Formação (Bacharel, UNIVESP) | Estagiário em Ciência de Dados na CVM</p>
            <div class="contact-links">
                <a href="https://www.linkedin.com/in/caiomiazzi" target="_blank">LinkedIn</a> | 
                <a href="https://github.com/caiomiazzi" target="_blank">GitHub</a>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Seção Minha Jornada
st.markdown('<h2 class="section-title">Minha Jornada Fora da Curva 🚀</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.1rem; color: #666; margin-bottom: 1rem;"><strong>Transição de carreira impulsionada pela curiosidade, prática e propósito.</strong></p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="journey-item">
        <h4>📚 2013 - 2018: Professor de Geografia</h4>
        <p>Comunicação, didática e visão socioambiental</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="journey-item">
        <h4>💼 2018 - 2022: Vendas e Gestão</h4>
        <p>Relacionamento, indicadores e liderança</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="journey-item">
        <h4>💻 2023 - Atual: Dados e Tecnologia</h4>
        <p>Projetos práticos, automação e IA</p>
    </div>
    """, unsafe_allow_html=True)

# Principais Marcos
st.markdown('<h2 class="section-title">Principais Marcos da Jornada em Dados</h2>', unsafe_allow_html=True)

for marco_texto, projeto_id in MARCOS_PROJETOS.items():
    key_toggle = f"toggle_{projeto_id}"

    if key_toggle not in st.session_state:
        st.session_state[key_toggle] = False

    col1, col2 = st.columns([5, 1])
    with col1:
        st.markdown(f'<div class="milestone-item">{marco_texto}</div>', unsafe_allow_html=True)
    with col2:
        label = "🔍 Ver" if not st.session_state[key_toggle] else "🔽 Ocultar"
        if st.button(label, key=f"btn_{projeto_id}"):
            st.session_state[key_toggle] = not st.session_state[key_toggle]

    if st.session_state[key_toggle]:
        with st.container():
            exibir_projeto_inline(projeto_id)
            st.markdown("---")  # separador visual

# st.markdown('<h2 class="section-title">Principais Marcos da Jornada em Dados</h2>', unsafe_allow_html=True)

# for marco_texto, projeto_id in MARCOS_PROJETOS.items():
#     col1, col2 = st.columns([5, 1])
#     with col1:
#         st.markdown(f'<div class="milestone-item">{marco_texto}</div>', unsafe_allow_html=True)
#     with col2:
#         # Alteração aqui: usar marco_texto na chave para garantir unicidade
#         if st.button("🔍 Ver", key=f"marco_{marco_texto}"):
#             exibir_projeto(projeto_id)
    
# Botão toggle para histórico completo
st.markdown("---")
button_text = "📋 OCULTAR HISTÓRICO COMPLETO" if st.session_state.show_history else "📋 VER HISTÓRICO COMPLETO DETALHADO"

if st.button(button_text, use_container_width=True):
    st.session_state.show_history = not st.session_state.show_history

# Mostrar/ocultar histórico baseado no estado
if st.session_state.show_history:
    st.markdown("### 📊 Histórico Completo de Projetos e Experiências")
    
    # Dados completos para a tabela
    dados_completos = [
        ["2013-2018", "Professor de Geografia", "Desenvolvimento de comunicação e didática", "Didática, Oratória, Liderança"],
        ["2018-2021", "Vendas e Atendimento", "Relacionamento com clientes, foco em resultados", "Negociação, Persuasão, CRM"],
        ["2021-2022", "Gerente de Restaurante", "Gestão de equipe e indicadores operacionais", "Gestão de Pessoas, KPIs"],
        ["2023", "Curso SQL - Udemy", "Primeira formação formal em Dados", "SQL, Banco de Dados"],
        ["2023-2024", "Bootcamp Ada Tech & iFood", "Formação intensiva em Data Science", "Python, SQL, Power BI, EDA"],
        ["2024", "Análise de Dados Veiculares", "Precificação e desvalorização no setor automotivo", "Python, Selenium, Web Scraping"],
        ["2024", "EDA Estratégia Olist", "Segmentação e insights estratégicos", "SQL, Pandas, Análise de Negócio"],
        ["2024", "IA Médica - Melanoma", "CNN com foco em representatividade", "CNN, Transfer Learning, Ética IA"],
        ["2024", "Hackathon Ada Hack", "Índice de diversidade corporativa", "Python, Power BI, Estatística"],
        ["2024", "Automação Looker Studio", "Automatização de visualizações", "Python, Automação de Processos"],
        ["2024", "Automação Limpeza Dados", "Pipeline de qualidade de dados", "Python, ETL, Data Quality"],
        ["2024", "Dashboard Farmacêutica", "BI estratégico personalizado", "Power BI, UX Design"],
        ["2024", "Bootcamp ML Atlântico", "Modelos preditivos e otimização", "Machine Learning, Python"],
        ["2024", "Estágio A² BI", "Pipelines e insights estratégicos", "Python, BI, Análise Exploratória"],
        ["2025", "Estágio CVM", "Dados críticos e LLMOps", "Python, SQL, LLM, Automação"],
        ["2025", "Banco Vetorial CVM", "IA generativa e testes unitários", "Vector Database, RAG, Testes"],
        ["2025", "Automação Verificação", "NLP para comunicados oficiais", "NLP, Chunking, Similaridade"]
    ]
    # Adicionar coluna "Ações" no DataFrame
    dados_completos_com_acoes = []
    for linha in dados_completos:
        experiencia = linha[1]
        projeto_id = HISTORICO_PROJETOS.get(experiencia)
        nova_linha = linha + [projeto_id if projeto_id else ""]
        dados_completos_com_acoes.append(nova_linha)

    df_historico = pd.DataFrame(dados_completos_com_acoes, columns=[
        "Período", "Experiência", "Descrição", "Tecnologias", "ID Projeto"
    ])

    # Exibir tabela
    st.dataframe(df_historico, use_container_width=True, hide_index=True)

    # Adicionar botões após a tabela
    for experiencia, projeto_id in HISTORICO_PROJETOS.items():
        if st.button(f"Ver {experiencia}", key=f"hist_{projeto_id}"):
            exibir_projeto(projeto_id)
    # df_historico = pd.DataFrame(dados_completos, columns=[
    #     "Período", "Experiência", "Descrição", "Tecnologias"
    # ])
    
    # st.dataframe(df_historico, use_container_width=True, hide_index=True)

# Chamada para ação final
st.markdown("""
<div class="tech-tags">
    <strong>Pronto para contribuir com a transformação digital da Stellantis</strong><br>
    Dados • Inovação • Sustentabilidade • Futuro
</div>
""", unsafe_allow_html=True)

# =============================================================
# LOGO NO FINAL (após a chamada para ação)
# =============================================================
st.markdown(f"""
<div class="bottom-logo">
    <img src="{IMAGE_HTML}" alt="Stellantis Logo" class="logo-img">
</div>
""", unsafe_allow_html=True)






#==============================================================================================
# temporario
# Adicione temporariamente no final do main.py:
exibir_projeto("dados_veiculares")
exibir_projeto("hackathon_ada")

# TESTE DE CAMINHOS (remova depois de verificar)
st.markdown("---")
st.subheader("Debug de Caminhos")

try:
    from utils.projeto_loader import carregar_projetos, get_screenshots, BASE_DIR
    
    st.success(f"BASE_DIR: {BASE_DIR}")
    st.success(f"Caminho JSON: {BASE_DIR / 'projetos_data.json'}")
    
    projetos = carregar_projetos()
    st.success(f"Projetos carregados: {len(projetos)}")
    
    # Teste com um projeto conhecido
    projeto_teste = "dados_veiculares"
    screenshots = get_screenshots(projeto_teste)
    st.success(f"Screenshots para {projeto_teste}: {screenshots}")
    
except Exception as e:
    st.error(f"Erro no teste: {str(e)}")
