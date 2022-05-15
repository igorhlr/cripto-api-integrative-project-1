import numpy as np
import pandas as pd

import yfinance as yf

import plotly.graph_objs as go

data = yf.download(tickers='BTC-USD', period='22h', interval='15m')

fig = go.Figure()

# Candlestick
fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'], name='market data'))

# Add titles
fig.update_layout(
    title='Evolução do preço das açoes do bitcoin',
    yaxis_title='Bitcoin em $ (kUS Dollars)')

# X-Axes
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=6, label="6h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)

# Show
fig.show()
