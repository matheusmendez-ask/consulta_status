import streamlit as st
import requests
import json

# Configurar o título, ícone e layout da página
st.set_page_config(
    page_title="Consulta de Status de Pedido",
    page_icon=":package:",  # Ícone personalizado
    layout="wide"
)

# Personalizar o estilo dos elementos
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background: #f5f5f5;  # Cor de fundo da página
        }}
        .sidebar .sidebar-content {{
            background: #3498db;  # Cor de fundo da barra lateral
            color: #3498db;  # Cor do texto na barra lateral
        }}
        .main .block-container {{
            background: #3498db;  # Cor de fundo dos blocos principais
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Titulo
st.title('Consulta de Status')

# Solicitar o numeroOrigem do usuário
numeroOrigem = st.text_input('Digite o Número do Pedido Conforme o Tiny:')

if st.button('Consultar'):
    if numeroOrigem:
        url = "https://{{bcmed}}.eship.com.br/?api={{api_key}}&funcao=webServiceCapturaStatus"
        url = url.replace('{{bcmed}}', 'bcmed').replace('{{api_key}}', '34484c4a60156541868ef8f57d19ab2d')

        params = {
            "api": "34484c4a60156541868ef8f57d19ab2d",
            "funcao": "webServiceCapturaStatus"
        }

        payload = {
            "request": f'{{"auth": {{"apikey": "34484c4a60156541868ef8f57d19ab2d"}}, "parameters": {{"numeroOrigem": "{numeroOrigem}", "codigoArmazem": ""}}}}'
        }

        response = requests.post(url, params=params, data=payload)
        r_pag_text = response.text
        json_response = json.loads(r_pag_text)
        condicional = json_response['erros']

        if isinstance(condicional, list) and 'erro' in condicional[0]:
            status = json_response['erros'][0]['erro']['mensagem']
        else:
            status = json_response['corpo']['status']['dados']

        # Exibir a resposta
        st.subheader('Resposta:')
        st.text(status)
    else:
        st.warning('Por favor, insira um Número.')

st.write('Desenvolvido com Streamlit')
