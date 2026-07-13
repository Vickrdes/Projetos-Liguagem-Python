# Automação de Cadastro de Produtos 🤖🛒

Este projeto foi desenvolvido durante a **Aula 1** com o objetivo de automatizar o processo repetitivo de cadastro de produtos em um sistema web, eliminando o trabalho manual de copiar e colar.

## 🚀 Como Funciona?
O script lê as informações de um arquivo de banco de dados local (`.csv`) e, utilizando ferramentas de automação de interface, simula as ações humanas de clicar, digitar e navegar pelo navegador para preencher o formulário do site automaticamente.

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Python**: Linguagem base do projeto.
* **PyAutoGUI**: Para o controle automático do mouse e do teclado (cliques e preenchimento de campos).
* **Time**: Para gerenciar os intervalos de espera (`sleep`) enquanto a página web carrega.
* **Pandas**: Para ler e estruturar os dados do arquivo `produtos.csv`.

## 📦 Pré-requisitos
Antes de rodar o script, é necessário instalar as dependências. Você pode fazer isso executando o comando abaixo no terminal:

```bash
