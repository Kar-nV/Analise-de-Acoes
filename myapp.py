import yfinance as yf
import streamlit as st
import pandas as pd 

st.write("""
    # Aplicativo de Ações Simples com YFinance
    
    Mostra o valor das ações do Google fechadas em cada ano.
    
    """)


#define o simbolo do ticker google
tickerSymbol = 'GOOGL'
#pega os dados desse ticker
tickerData = yf.Ticker(tickerSymbol)
#pega os dados históricos do Google para o ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividendos	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)