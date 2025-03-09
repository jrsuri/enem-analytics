# Análise dos Microdados do ENEM 2022

## Objetivo do projeto
Este repositório é voltado para a análise dos microdados do **ENEM 2022**. O projeto inclui organização de dados, análise exploratória, modelagem de machine learning e considerações para deploy.

## Estrutura do repositório

- **`/data/`** – Conjunto de dados (amostras e arquivos de referência) e arquivos de saída
- **`/models/`** – Modelos treinados
- **`/notebooks/`** – Notebooks de análise e modelagem
- **`/scripts/`** – Scripts de download dos dados e inferência
- **`dataset_description.md`** – Descrição do dataset
- **`LICENSE`** – Licença do repositório
- **`README.md`** – Explicação do repositório e orientações gerais
- **`requirements.txt`** – Lista de dependências do projeto

## Como reproduzir o projeto

1. **Clone este repositório**
   ```bash
   git clone https://github.com/jrsuri/enem-analytics.git
   cd enem-analytics

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt

3. **Execute o script para baixar os microdados**
   ```bash
   python scripts/download_microdados_2022.py
   
4. **Execute os notebooks na ordem em que aparecem**

## Caso queira apenas fazer previsões
1. **Execute o script a seguir**
   ```bash
   python scripts/inferencia.py

## Sobre os microdados do ENEM 2022
Os microdados do ENEM são disponibilizados pelo INEP e contêm informações detalhadas sobre os participantes, suas respostas e resultados nas provas. Neste projeto, utilizamos esses dados para análise estatística e modelagem preditiva.

## Requisitos
- Python 3.10+
- Bibliotecas listadas em `requirements.txt`

## Licença
Este repositório segue a licença MIT.
