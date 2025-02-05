# Projeto de Análise de Dados Industriais

Este projeto tem como objetivo realizar a análise de dados de produção industrial para otimizar processos e identificar melhorias. Utilizando dados sintéticos de produção, vamos calcular KPIs (Indicadores-chave de Performance) para avaliar a eficiência da produção, como Lead Time, Tempo de Setup, Eficiência de Produção, e outros.

## Estrutura do Projeto

- **data/**: Contém os dados utilizados para análise (ex: arquivos CSV).
- **notebooks/**: Contém notebooks Jupyter com análises e visualizações.
- **scripts/**: Contém scripts Python para processamento e cálculos.
- **docs/**: Contém documentos de planejamento e relatórios.
- **README.md**: Descrição geral do projeto.

## Objetivo

O objetivo deste projeto é utilizar Python para realizar a análise de dados industriais, focando na eficiência de produção e otimização de processos.

## KPIs Calculados

- Lead Time (Tempo de Ciclo)
- Tempo de Setup
- Eficiência de Produção
- Utilização da Máquina
- Custo de Produção

## Tecnologias Utilizadas

- **Python**: Para processamento e análise de dados.
- **Pandas**: Para manipulação e análise de dados.
- **Matplotlib/Seaborn**: Para visualizações gráficas.

## Como Executar

1. Clone o repositório:
2. Instale as dependências:
3. Execute os scripts ou notebooks para análise.

## Geração de Dados Sintéticos

Para simular um ambiente de produção, criamos dados sintéticos que representam o processo de fabricação de produtos. Abaixo estão as informações sobre como os dados são gerados e o que cada variável representa:

- **ID_Produto**: Um identificador único para cada produto produzido.
- **Data_Producao**: A data de produção de cada produto, gerada aleatoriamente entre 1º de janeiro e 30 dias à frente.
- **Tempo_Producao**: O tempo de produção, variando entre 30 a 240 minutos, representando o tempo que leva para produzir um item.
- **Tempo_Setup**: O tempo de configuração da máquina, variando entre 10 a 60 minutos, necessário antes de iniciar a produção.
- **Quantidade_Produzida**: A quantidade de unidades produzidas, variando entre 10 e 100 unidades.

A geração dos dados é feita por um script Python, que utiliza a biblioteca **Pandas** para criar um DataFrame e salvar os dados em um arquivo **CSV** na pasta `data/`.

Exemplo de execução do código:

```bash
python scripts/gerar_dados.py
