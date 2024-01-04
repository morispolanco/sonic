import streamlit as st
import requests

def obtener_respuesta_pregunta(pregunta, botsonic_token):
    api_endpoint = 'https://api.botsonic.ai/v1/botsonic/generate'

    headers = {
        'User-Agent': 'python-requests/2.28.1',
        'accept': 'application/json',
        'Authorization': f'Bearer {botsonic_token}',
    }

    json_data = {
        'question': pregunta,
        'chat_history': [],
    }

    response = requests.post(api_endpoint, headers=headers, json=json_data)

    if response.status_code == 200:
        return response.json()[0]['data']['answer'], response.json()[0]['data']['sources']
    else:
        return f'Error al realizar la solicitud: {response.status_code}\nRespuesta completa: {response.text}', None

def main():
    st.title("Aplicación de Streamlit - Preguntas sobre leyes de Guatemala")

    pregunta_usuario = st.text_input("Ingrese su pregunta:")

    # Reemplaza '<Your Botsonic token>' con tu token real de Botsonic
    botsonic_token = '9e9f56f9-5004-4e78-a875-2a28b320c8e9'

    if st.button("Obtener respuesta"):
        respuesta, fuentes = obtener_respuesta_pregunta(pregunta_usuario, botsonic_token)
        st.write("Respuesta:", respuesta)

        if fuentes:
            st.write("Fuentes:")
            for fuente in fuentes:
                st.write(f"URL: {fuente['url']}")
                st.write(f"Contenido: {fuente['content']}")
                st.write("---")

if __name__ == "__main__":
    main()
