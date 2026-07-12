#titulo
#input do usuário (o campo que escrevemos )
#a cada mensagem que o usuário enviar 
        #mostrar a mensagem que o usuário enviou
        #pegar a pergunta e enviar para uma IA responder 

#Framework Streamlit - apenas com python criar o front e back
# Utilizar a IA - Google Gemini

import streamlit as st
from google import genai
from google.genai import types

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.write('# Chat Vitoria') # os textos seguem um formato chamado marckdow 

if not 'lista_mensagens' in st.session_state:
    st.session_state['lista_mensagens'] = []


texto_usuario = st.chat_input('Digite sua mensagem')

for mensagem in st.session_state['lista_mensagens']:
    role = mensagem['role']
    content = message_content = mensagem['content']
    st.chat_message(role).write(content)
    # para cada mesagem dentro da lista de mensagens
    # pega quem mandou a mensagem 'role' e o que falou 'content'
    # e imprime na tela 

if texto_usuario:
    st.chat_message('user').write(texto_usuario)#dicionario 
    mensagem__usuario = {'role': 'user', 'content': texto_usuario}
    st.session_state['lista_mensagens'].append(mensagem__usuario)

    # ia respondeu usando o Gemini
    resposta_ia = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=[
            types.Content(
                role='model' if msg['role'] == 'assistant' else 'user',
                parts=[types.Part.from_text(text=msg['content'])]
            )
            for msg in st.session_state['lista_mensagens']
        ]
    )
    # chama a api do gemini para gerar uma resposta
    # define o modelo que vamos usar como o 'gemini-2.5-flash'
    # passa o histórico completo de mensagens dentro de 'contents'
    # faz um loop para rodar cada mensagem da sua 'lista_mensagens'
    # se quem mandou foi o 'assistant' muda para 'model', se não deixa 'user'
    # transforma o texto do 'content' no formato de texto que o google exige

    # Pega o texto da resposta da IA
    texto_resposta_ia = resposta_ia.text 

    st.chat_message('assistant').write(texto_resposta_ia)
    mensagem_ia = {'role': 'assistant', 'content': texto_resposta_ia}
    st.session_state['lista_mensagens'].append(mensagem_ia)