import streamlit as st

st.set_page_config(page_title="Portfólio Caio Miazzi | Stellantis", layout="centered")

# Cabeçalho visual
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color:#002B5C;">Caio Miazzi</h1>
        <h3>Cientista de Dados em Formação | Estagiário na CVM</h3>
        <p>Conectando Dados, Tecnologia e Sustentabilidade</p>
    </div>
    """, unsafe_allow_html=True
)

# Logo Stellantis centralizado
st.image("D:\\T.I\\Stellantis\\stellantis_logo.png", width=150)

# Slide da apresentação
st.markdown("---")
st.subheader("Resumo da Apresentação (Slide)")

slide_path = "D:\\T.I\\Stellantis\\Painel_Stellantis_Apresentacao.pdf"  # Ou PDF
st.image(slide_path, use_container_width=True)

# Espaço interativo - Linha do Tempo
st.markdown("---")
st.subheader("Linha do Tempo Interativa de Projetos e Formação")

with st.expander("Clique para visualizar minha trajetória completa"):
    st.markdown(
        """
        ### Linha do Tempo de Projetos e Formação

        🗺️ **2013-2018:** Professor de Geografia - Comunicação e Sustentabilidade  
        🤝 **2018-2022:** Vendas e Gestão - Relacionamento e Indicadores  
        🛠️ **2023:** Curso SQL para Análise de Dados  
        🚀 **2023-2024:** Bootcamp Ada & iFood - Formação prática em dados  
        🚗 **2024:** Projetos práticos: Análise Veicular | IA Médica | Hackathon Ada Hack  
        ⚙️ **2024:** Automação de Processos | Dashboards | Limpeza de Dados  
        🤖 **2024:** Bootcamp Machine Learning Atlântico Avanti  
        🔎 **2024:** Estágio A² Business Intelligence  
        🏛️ **2025:** Estágio CVM - Dados críticos, LLMOps, Banco Vetorial, Automação Analítica  
        """
    )

    st.success("Acesse meu [LinkedIn](https://www.linkedin.com/in/caiomiazzi) ou [GitHub](https://github.com/caiomiazzi) para detalhes dos projetos.")

# Rodapé
st.markdown("---")
st.info("Este portfólio foi criado como material complementar para o Painel Gerdau.")
