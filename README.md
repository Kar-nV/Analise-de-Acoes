# Aplicativo de Visualização de Ações 💹

Este é um aplicativo web interativo que permite visualizar gráficos de preços de ações usando o **Y Finance**. O usuário pode escolher entre ações nacionais ou globais e especificar um período de tempo para obter dados detalhados sobre preços de fechamento, abertura, volume diário, entre outros.

## Funcionalidades

- Visualização de gráficos de preços de ações (fechamento, abertura, volume, e média móvel).
- Escolha entre ações **Nacionais (B3)** ou **Globais**.
- Suporte para visualização de ações de qualquer período selecionado pelo usuário.
- Interface amigável usando **Streamlit** para exibir gráficos interativos.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Streamlit**: Framework usado para criar a interface web interativa.
- **yfinance**: Biblioteca para acessar dados do Yahoo Finance.
- **forex-python**: Biblioteca para conversão de moedas.
- **pandas**: Utilizada para manipulação de dados financeiros.

## Como Executar o Projeto

### Pré-requisitos

Antes de começar, você precisará ter o Python instalado na sua máquina. Além disso, as seguintes bibliotecas precisam ser instaladas:

```bash
pip install yfinance streamlit forex-python pandas
```

## Executando o Projeto

Para iniciar o aplicativo, execute o seguinte comando no terminal dentro da pasta do projeto:

```bash
streamlit run app.py
```

## Como Usar

- No menu lateral, selecione o mercado desejado: ações brasileiras (Nacional) ou ações internacionais (Global).

 - Insira o ticker da ação desejada.
  
- Escolha a data de início e data de término do período que deseja visualizar.

- Clique no botão Visualizar Gráficos para gerar os gráficos de preços e estatísticas.
