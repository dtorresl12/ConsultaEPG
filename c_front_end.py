#lanzar con streamlit run c_front_end.py en el terminal

import b_backend
import streamlit as st
from streamlit_chat import message

st.set_page_config(page_title="Consulta EPG", page_icon="None", layout="centered", 
                   initial_sidebar_state="auto", menu_items=None)

#st.image("UNIVERSIDAD-CONTINENTAL-POSGRADO-LOGO-2.jpg")
st.title("App de Consulta - Continental EPG")
#st.markdown("<h1 style='text-align: center; '>App de Consulta - Continental EPG </a></h3>", unsafe_allow_html=True)
st.write("""Hola, pregúntame lo que quieras saber sobre el perfil de nuestros estudiantes
         """)

if 'preguntas' not in st.session_state:
    st.session_state.preguntas = []
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = []

def click():
    if st.session_state.user != '':
        pregunta = st.session_state.user
        respuesta = b_backend.consulta(pregunta)

        st.session_state.preguntas.append(pregunta)
        st.session_state.respuestas.append(respuesta)

        # Limpiar el input de usuario después de enviar la pregunta
        st.session_state.user = ''


with st.form('my-form'):
   query = st.text_input('¿En qué te puedo ayudar?', key='user', help='Pulsa Enviar para hacer la pregunta')
   submit_button = st.form_submit_button('Enviar',on_click=click)

if st.session_state.preguntas:
    for i in range(len(st.session_state.respuestas)-1, -1, -1):
        message(st.session_state.respuestas[i], key=str(i))

    # Opción para continuar la conversación
    continuar_conversacion = st.checkbox('Quieres hacer otra pregunta?')
    if not continuar_conversacion:
        st.session_state.preguntas = []
        st.session_state.respuestas = []

st.markdown("<h4 style='text-align: center; color: #D9D0D0; font-size: 14px '> Desarrollado por: Equipo de Inteligencia Comercial </a></h3>", 
            unsafe_allow_html=True)

# hide_menu_style = """
#                     <style>
#                     #MainMenu {visibility: hidden; }
#                     footer {visibility: hidden; }
#                     </style>
#                     """
# st.markdown(hide_menu_style, unsafe_allow_html=True)
