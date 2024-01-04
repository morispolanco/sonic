import streamlit as st
import requests

def obtener_respuesta_pregunta(pregunta, api_token):
    url = "https://api.botsonic.ai/v1/botsonic/generate"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }
    payload = {"input": pregunta}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("output", "No se pudo obtener una respuesta.")
    else:
        return f"Error al realizar la solicitud: {response.status_code}"

def main():
    st.title("Aplicación de Streamlit - Preguntas sobre leyes de Guatemala")

    pregunta_usuario = st.text_input("Ingrese su pregunta:")

    if st.button("Obtener respuesta"):
        api_token = "9e9f56f9-5004-4e78-a875-2a28b320c8e9"
        respuesta = obtener_respuesta_pregunta(pregunta_usuario, api_token)
        st.write("Respuesta:", respuesta)

if __name__ == "__main__":
    main()
