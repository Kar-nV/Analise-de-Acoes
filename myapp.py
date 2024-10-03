import yfinance as yf
import streamlit as st
import pandas as pd
from forex_python.converter import CurrencyRates
from datetime import datetime

# Configurações da página
st.set_page_config(
    page_title="Aplicativo de Ações",
    page_icon="💹",
    layout="wide",
)

# Função para obter a moeda com base no mercado
def obter_moeda(opcao_mercado):
    return "BRL" if opcao_mercado == "Nacional" else "USD"

# Função para exibir os gráficos e valores
def exibir_graficos(ticker_df, ticker_symbol, moeda_pais):
    st.subheader(f"Gráfico de Fechamento para {ticker_symbol} ({moeda_pais})")
    st.markdown("Este gráfico mostra a variação do preço de fechamento da ação ao longo do tempo.")
    
    st.line_chart(round(ticker_df['Close'], 2), use_container_width=True)
    
    # Valores máximos e mínimos como ponto flutuante
    max_value = float(ticker_df['Close'].max())
    min_value = float(ticker_df['Close'].min())
    
    st.text(f"Valor Máximo: {max_value:.2f} | Valor Mínimo: {min_value:.2f}")

    # Exibindo outros gráficos
    st.subheader(f"Outros Elementos do Gráfico para {ticker_symbol} ({moeda_pais})")

    # Função auxiliar para mostrar gráficos com rótulos e contexto
    def show_chart_with_context(chart_data, label):
        st.subheader(f"{label}")
        st.line_chart(round(chart_data, 2), use_container_width=True)

        max_value = float(chart_data.max())
        min_value = float(chart_data.min())

        st.markdown(f"**Valor Máximo:** {max_value:.2f} | **Valor Mínimo:** {min_value:.2f}")

    show_chart_with_context(ticker_df['Open'], "Preço de Abertura")
    show_chart_with_context(ticker_df['Close'].rolling(window=20).mean(), "Média Móvel")
    show_chart_with_context(ticker_df['Volume'], "Volume Diário")

# Função principal para carregar e processar os dados do ticker
def carregar_dados(ticker_symbol, start_date, end_date):
    ticker_data = yf.Ticker(ticker_symbol)
    ticker_df = ticker_data.history(period='1d', start=start_date, end=end_date)

    if ticker_df.empty:
        raise ValueError(f"Não foram encontrados dados para o ticker {ticker_symbol} no período especificado.")
    
    return ticker_df

# Exibição do título principal e descrição
st.title("Gráfico de Ações")
st.write("""
    Insira o Ticker e a data desejada para obter informações detalhadas sobre uma ação no período selecionado.
""")

# Opção para escolher entre ações da B3 ou ações globais
opcao_mercado = st.sidebar.radio("Escolha o mercado:", ("Nacional", "Global"))

# Campo para inserir o símbolo da ação
exemplo_simbolo = "PETR4.SA" if opcao_mercado == "Nacional" else "AAPL"
ticker_symbol = st.sidebar.text_input(f"Insira o Ticker da ação (Utilize .SA ao final caso seja uma ação nacional. Ex.: {exemplo_simbolo}):", exemplo_simbolo)

# Obtendo a data atual
data_atual = datetime.today().strftime('%Y-%m-%d')

# Campos para inserir o período de tempo
start_date = st.sidebar.text_input("Data de início (YYYY-MM-DD):", "2010-05-31")
end_date = st.sidebar.text_input("Data de término (YYYY-MM-DD):", data_atual)

# Botão para atualizar os dados e exibir gráficos
if st.sidebar.button("Visualizar Gráficos"):
    try:
        # Adicionando mensagem de carregamento
        with st.spinner('Aguarde... Carregando dados'):
            if not ticker_symbol:
                raise ValueError("Por favor, insira um ticker.")
            
            # Carregar os dados da ação
            ticker_df = carregar_dados(ticker_symbol, start_date, end_date)

            # Obter moeda com base no mercado
            moeda_pais = obter_moeda(opcao_mercado)

            # Exibir gráficos e valores
            exibir_graficos(ticker_df, ticker_symbol, moeda_pais)

    except ValueError as e:
        st.error(f"Erro: {e}")
    except Exception as e:
        st.error(f"Ocorreu um erro inesperado: {e}")
