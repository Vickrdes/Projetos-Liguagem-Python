# Classificação de Score de Crédito com Machine Learning 🤖💳

Este projeto foi desenvolvido durante a **Aula 3** com o objetivo de construir um modelo de Machine Learning capaz de analisar o perfil e o histórico de clientes para classificar automaticamente o seu score de crédito em três categorias: **Ruim**, **Standard** ou **Bom**.

## 🚀 Como Funciona?
O projeto foi desenvolvido em um Jupyter Notebook (`.ipynb`) seguindo as etapas fundamentais de um projeto de ciência de dados:
1. **Tratamento de Dados:** Limpeza da base de dados fornecida.
2. **Engenharia de Recursos (Label Encoding):** Utilização do `LabelEncoder` da biblioteca Scikit-Learn para transformar colunas de texto (como profissão, tipo de residência, etc.) em números legíveis para os algoritmos de IA.
3. **Divisão da Base:** Separação dos dados em conjuntos de **treino** (para a IA aprender) e **teste** (para avaliar a eficiência).
4. **Treinamento e Comparação de Modelos:** Dois algoritmos de classificação foram testados e comparados para medir a acurácia (taxa de acerto):
   * **Random Forest / Árvore de Decisão:** Obteve uma acurácia aproximada de **82.04%**.
   * **KNN (K-Nearest Neighbors):** Obteve uma acurácia aproximada de **73.30%**.
5. **Previsão em Novos Dados:** Com o modelo campeão definido (Árvore de Decisão devido à maior acurácia), novos dados de clientes foram importados, o modelo previu o score de cada um e salvou o resultado adicionando uma nova coluna na base de dados.

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Python**: Linguagem base do projeto.
* **Pandas**: Para manipulação, filtragem e estruturação das tabelas de dados.
* **Scikit-Learn (sklearn)**: Utilizado para o pré-processamento de dados (`LabelEncoder`), divisão de treino/teste e para a construção e avaliação dos modelos de IA (`RandomForestClassifier` e `KNeighborsClassifier`).
* **Plotly**: Para geração de gráficos interativos durante a análise exploratória.

## 📦 Pré-requisitos
Para executar este projeto, você precisará instalar as seguintes dependências no terminal:

```
