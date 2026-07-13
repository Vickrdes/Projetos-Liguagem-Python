# Chatbot Conversacional com Inteligência Artificial 🤖💬

Este projeto foi desenvolvido com o objetivo de construir um Chatbot conversacional interativo utilizando a API oficial do Gemini e uma interface web simples e amigável.

## 🚀 Como Funciona?
O projeto utiliza o **Streamlit** para renderizar uma aplicação web onde o usuário pode interagir diretamente com o modelo de IA. O script se conecta à API do Gemini, envia as mensagens digitadas pelo usuário no chat e exibe as respostas geradas pela IA em tempo real.

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Python**: Linguagem base do projeto.
* **Streamlit (`import streamlit as st`)**: Biblioteca utilizada para construir toda a interface gráfica do chat de forma rápida e responsiva.
* **Google GenAI (`from google import genai`)**: O SDK oficial do Google para conectar e interagir com os modelos do Gemini.
* **Google GenAI Types (`from google.genai import types`)**: Utilizado para configurar os parâmetros de tipos e segurança das requisições enviadas à API.

## 🔑 Configuração da API
Para que o chatbot funcione, é necessário configurar a sua chave de API do Google Generative AI. 
O ideal é salvar sua chave dentro de um arquivo seguro local (como o `secrets.toml` do Streamlit) para proteger suas credenciais.

## 📦 Pré-requisitos
Para instalar as dependências necessárias para rodar este projeto, execute o comando abaixo no seu terminal:

```bash
pip install streamlit google-genai
