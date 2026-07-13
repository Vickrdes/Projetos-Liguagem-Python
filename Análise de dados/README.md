# Análise de Dados: Identificação de Causas de Cancelamento de Clientes (Churn) 📊📉

Este projeto foi desenvolvido durante a **Aula 2** com o objetivo de analisar uma base de dados de clientes para calcular a taxa de cancelamento atual e diagnosticar as principais causas que levam os clientes a deixarem o serviço.

## 🚀 Como Funciona?
O projeto foi construído em um Jupyter Notebook (`.ipynb`). O fluxo da análise consistiu em:
1. **Tratamento dos Dados:** Limpeza de dados nulos e ajustes na base.
2. **Cálculo de Churn:** Identificação do percentual geral de clientes que cancelaram o serviço.
3. **Análise de Causa Raiz:** Utilização de gráficos para cruzar as informações dos clientes com o cancelamento e entender os motivos.
4. **Simulação de Impacto:** Criação de condições no código para recalcular qual seria o novo percentual de cancelamento caso os principais gargalos identificados fossem corrigidos.

## 🔍 Insights Diagnósticos Encontrados
A análise dos gráficos revelou os principais fatores que elevam drasticamente o cancelamento:
* **Tipo de Contrato:** Clientes com contrato do tipo mensal possuem alta taxa de cancelamento.
  * *Ação sugerida:* Incentivar a migração para o contrato anual (ex: oferecendo descontos).
* **Ligações ao Call Center:** O cancelamento dispara entre clientes que ligam mais de 4 vezes para o suporte.
  * *Ação sugerida:* Criar um plano de ação ("alerta vermelho") para resolver o problema do cliente de forma prioritária quando ele atingir 3 ligações.
* **Dias de Atraso:** Clientes com mais de 20 dias de atraso no pagamento apresentam alta recorrência de cancelamento.
  * *Ação sugerida:* Implementar um aviso ou processo de negociação ("alerta vermelho") assim que o atraso atingir 15 dias.

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Python**: Linguagem base utilizada no ambiente Jupyter.
* **Pandas**: Para manipulação, limpeza e análise estatística da base de dados.
* **Plotly**: Forneceu os gráficos interativos fundamentais para cruzar as variáveis e diagnosticar os motivos de cancelamento.

## 📦 Pré-requisitos
Para rodar este notebook, você precisará instalar as seguintes bibliotecas no seu ambiente Python:

```
