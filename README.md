# Aplicativo para Visualização de Ações

Este é um aplicativo web interativo que permite visualizar gráficos de preços de ações usando o **Y Finance**.

Você pode buscar ticker de ações de x empresa no google ou pode utilizar este link para teste https://www.dadosdemercado.com.br/acoes

Lembrando que é necessário ser em MAIÚSCULA e caso seja brasileira, deve conter .SA ao final. 

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
