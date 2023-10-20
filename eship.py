import streamlit as st
import requests
import json

st.title('Consulta de Status de Pedido')

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

        # Exibir a resposta
        st.subheader('Resposta:')
        st.json(json_response)
    else:
        st.warning('Por favor, insira um Número.')

st.write('Desenvolvido com Streamlit')
