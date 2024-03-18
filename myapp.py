import yfinance as yf
import streamlit as st
import pandas as pd
from forex_python.converter import CurrencyRates

# Configurando a página
st.set_page_config(
    page_title="Aplicativo de Ações",
    page_icon="💹",
    layout="wide",
)

# Função para obter a moeda com base no mercado
def obter_moeda(opcao_mercado):
    if opcao_mercado == "Nacional":
        return "BRL"
    else:
        return "USD"

# Título principal
st.title("Gráfico de Ações")

# Descrição do aplicativo
st.write("""
    Insira o Ticker e a data desejada para obter informações detalhadas sobre uma ação no período selecionado.
""")

# Opção para escolher entre ações da B3 ou ações globais
opcao_mercado = st.sidebar.radio("Escolha o mercado:", ("Nacional", "Global"))

# Campo para inserir o símbolo da ação
exemplo_simbolo = "PETR4.SA" if opcao_mercado == "Nacional" else "AAPL"
ticker_symbol = st.sidebar.text_input(f"Insira o Ticker da ação (Utilize .SA ao final caso seja uma ação nacional. Ex.: {exemplo_simbolo}):", exemplo_simbolo)

# Campos para inserir o período de tempo
start_date = st.sidebar.text_input("Data de início (YYYY-MM-DD):", "2010-05-31")
end_date = st.sidebar.text_input("Data de término (YYYY-MM-DD):", "2020-05-31")

# Botão para atualizar os dados
if st.sidebar.button("Visualizar Gráficos"):
    try:
        # Adicionando mensagem de aguarde
        with st.spinner('Aguarde... Carregando dados'):
            # Validar entrada
            if not ticker_symbol:
                raise ValueError("Por favor, insira um ticker.")

            # Obtendo os dados da ação
            ticker_data = yf.Ticker(ticker_symbol)
            ticker_df = ticker_data.history(period='1d', start=start_date, end=end_date)

            if ticker_df.empty:
                raise ValueError(f"Não foram encontrados dados para o ticker {ticker_symbol} no período especificado.")

            # Obtendo informações sobre a moeda
            moeda_pais = obter_moeda(opcao_mercado)

            # Exibindo gráficos
            st.subheader(f"Gráfico de Fechamento para {ticker_symbol} ({moeda_pais})")
            st.markdown("Este gráfico mostra a variação do preço de fechamento da ação ao longo do tempo.")
            st.line_chart(round(ticker_df.Close, 2), use_container_width=True)

            # Cores de valores máximos e mínimos
            max_value = round(ticker_df.Close.max(), 2)
            min_value = round(ticker_df.Close.min(), 2)

            st.text(f"Valor Máximo: {max_value} | Valor Mínimo: {min_value}")

            st.subheader(f"Outros Elementos do Gráfico para {ticker_symbol} ({moeda_pais})")

            # Função para exibir gráfico com rótulo e contexto
            def show_chart_with_context(chart_data, label, max_value_label=None, min_value_label=None):
                st.subheader(f"{label}")
                st.markdown(f"Este gráfico mostra a variação do {label.lower()} ao longo do tempo.")

                # Adicionando insights
                insights = {
                    'Cotação (Preço) de Abertura': 'O preço de abertura representa o valor da ação no início do período de negociação.',
                    'Média Móvel': 'A média móvel suaviza as flutuações diárias, ajudando a identificar tendências de longo prazo.',
                    'Faixa de Variação Diária': 'A faixa de variação diária mostra a diferença entre os preços mais baixo e mais alto em cada dia.',
                    'Volume Diário': 'O volume diário indica a quantidade total de ações negociadas em um dia, podendo sugerir o interesse do mercado.',
                    'Relação entre Preço de Fechamento e Volume': 'O gráfico de dispersão revela se há correlação entre o preço de fechamento e o volume de negociação.',
                    'Linha de Tendência': 'A linha de tendência ajuda a identificar padrões e direções possíveis do preço no futuro.'
                }

                st.line_chart(round(chart_data, 2), use_container_width=True)

                # Indicadores de valor máximo
                max_value = round(chart_data.max(), 2)
                max_value_indicator = f"**Valor Máximo:** {max_value}"
                if max_value_label:
                    max_value_indicator += f" | **Total {max_value_label}:** {max_value}"
                st.markdown(max_value_indicator)

                # Indicadores de valor mínimo
                min_value = round(chart_data.min(), 2)
                min_value_indicator = f"**Valor Mínimo:** {min_value}"
                if min_value_label:
                    min_value_indicator += f" | **Total {min_value_label}:** {min_value}"
                st.markdown(min_value_indicator)

                # Adicionando insights ao gráfico
                if label in insights:
                    st.markdown(f"**O que o gráfico representa:** {insights[label]}")

        
            show_chart_with_context(ticker_df.Open, "Preço de Abertura", max_value_label="Preço de Abertura Máximo", min_value_label="Preço de Abertura Mínimo")
            show_chart_with_context(ticker_df.Close.rolling(window=20).mean(), "Média Móvel")
            show_chart_with_context(ticker_df, "Faixa de Variação Diária")
            show_chart_with_context(ticker_df.Volume, "Volume Diário")
            show_chart_with_context(ticker_df.Close[['Close', 'Volume']], "Relação entre Preço de Fechamento e Volume")
            show_chart_with_context(ticker_df.Close, "Linha de Tendência")

    except yf.YFinanceError as e:
        st.error(f"Erro ao carregar dados: {e}")
    except pd.errors.EmptyDataError:
        st.error("Os dados para o período especificado são vazios. Por favor, escolha um período diferente.")
    except ValueError as e:
        st.error(f"Erro: {e}")
    except Exception as e:
        st.error(f"Ocorreu um erro inesperado: {e}")


