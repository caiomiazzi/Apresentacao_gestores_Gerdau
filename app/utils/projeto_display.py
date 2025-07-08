import streamlit as st
import base64
from .projeto_loader import carregar_projetos, get_screenshots

def img_to_base64(img_path):
    """Converte imagem para base64 usando caminho absoluto (não usado no novo modelo)"""
    try:
        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e:
        st.error(f"Erro ao carregar imagem: {e}")
        return None

def exibir_projeto(projeto_id):
    """Exibe projeto com st.expander (mantido se ainda quiser usar em outras partes)"""
    try:
        projetos = carregar_projetos()
        if projeto_id not in projetos:
            st.error(f"Projeto {projeto_id} não encontrado!")
            return

        projeto = projetos[projeto_id]

        with st.expander(f"🔍 {projeto['titulo']}", expanded=False):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"**📅 {projeto['periodo']}**")
                st.markdown(projeto['descricao'])

                links = []
                if projeto.get('github'):
                    links.append(f"[GitHub]({projeto['github']})")
                if projeto.get('demo'):
                    links.append(f"[Demo]({projeto['demo']})")

                if links:
                    st.markdown("🔗 " + " | ".join(links))

            with col2:
                screenshots = get_screenshots(projeto_id)
                for img_path in screenshots:
                    st.image(img_path, width=150)

    except Exception as e:
        st.error(f"Erro ao exibir projeto: {str(e)}")

def exibir_projeto_inline(projeto_id):
    """Exibe projeto em formato inline com slider e imagem ampliada"""
    try:
        projetos = carregar_projetos()
        if projeto_id not in projetos:
            st.error(f"Projeto {projeto_id} não encontrado!")
            return

        projeto = projetos[projeto_id]
        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(f"### {projeto['titulo']}")
            st.markdown(f"**📅 {projeto['periodo']}**")
            st.markdown(projeto['descricao'])

            links = []
            if projeto.get('github'):
                links.append(f"[GitHub]({projeto['github']})")
            if projeto.get('demo'):
                links.append(f"[Demo]({projeto['demo']})")
            if links:
                st.markdown("🔗 " + " | ".join(links))

        with col2:
            screenshots = get_screenshots(projeto_id)

            if screenshots:
                if len(screenshots) == 1:
                    st.image(screenshots[0], use_container_width=True)
                else:
                    idx = st.slider(
                        label="Visualizar imagens",
                        min_value=0,
                        max_value=len(screenshots) - 1,
                        step=1,
                        key=f"slider_{projeto_id}",
                        label_visibility="collapsed"
                    )
                    st.image(screenshots[idx], use_container_width=True)
            else:
                st.info("Nenhuma imagem disponível para este projeto.")

    except Exception as e:
        st.error(f"Erro ao exibir projeto: {str(e)}")


def botao_projeto(projeto_id, key):
    """Renderiza botão do projeto (caso ainda queira usar em outros contextos)"""
    if st.button("🔍 Ver", key=key):
        exibir_projeto(projeto_id)





# import streamlit as st
# import base64
# from .projeto_loader import carregar_projetos, get_screenshots

# def img_to_base64(img_path):
#     """Converte imagem para base64 usando caminho absoluto"""
#     try:
#         with open(img_path, "rb") as f:
#             return base64.b64encode(f.read()).decode()
#     except Exception as e:
#         st.error(f"Erro ao carregar imagem: {e}")
#         return None

# def exibir_projeto(projeto_id):
#     """Exibe projeto em expandable"""
#     try:
#         projetos = carregar_projetos()
#         if projeto_id not in projetos:
#             st.error(f"Projeto {projeto_id} não encontrado!")
#             return
    
#         projeto = projetos[projeto_id]
    
#         with st.expander(f"🔍 {projeto['titulo']}", expanded=False):
#             col1, col2 = st.columns([3, 1])
            
#             with col1:
#                 st.markdown(f"**📅 {projeto['periodo']}**")
#                 st.markdown(projeto['descricao'])
                
#                 # Links
#                 links = []
#                 if projeto.get('github'):
#                     links.append(f"[GitHub]({projeto['github']})")
#                 if projeto.get('demo'):
#                     links.append(f"[Demo]({projeto['demo']})")
                
#                 if links:
#                     st.markdown("🔗 " + " | ".join(links))
            
#             with col2:
#                 # Screenshots com caminhos corrigidos
#                 screenshots = get_screenshots(projeto_id)
#                 for img_path in screenshots:
#                     # Usar caminho absoluto para a imagem
#                     img_b64 = img_to_base64(img_path)
#                     if img_b64:
#                         st.markdown(
#                             f'<img src="data:image/png;base64,{img_b64}" width="150">', 
#                             unsafe_allow_html=True
#                     )
#     except Exception as e:
#         st.error(f"Erro ao exibir projeto: {str(e)}")

# def botao_projeto(projeto_id, key):
#     """Renderiza botão do projeto"""
#     if st.button("🔍 Ver", key=key):
#         exibir_projeto(projeto_id)

# def exibir_projeto_inline(projeto_id):
#     """Exibe projeto em formato inline (sem expander)"""
#     try:
#         projetos = carregar_projetos()
#         if projeto_id not in projetos:
#             st.error(f"Projeto {projeto_id} não encontrado!")
#             return

#         projeto = projetos[projeto_id]
#         col1, col2 = st.columns([3, 1])
        
#         with col1:
#             st.markdown(f"**📅 {projeto['periodo']}**")
#             st.markdown(projeto['descricao'])

#             links = []
#             if projeto.get('github'):
#                 links.append(f"[GitHub]({projeto['github']})")
#             if projeto.get('demo'):
#                 links.append(f"[Demo]({projeto['demo']})")
#             if links:
#                 st.markdown("🔗 " + " | ".join(links))

#         with col2:
#             screenshots = get_screenshots(projeto_id)
#             for img_path in screenshots:
#                 st.image(img_path, width=150)
#     except Exception as e:
#         st.error(f"Erro ao exibir projeto: {str(e)}")
