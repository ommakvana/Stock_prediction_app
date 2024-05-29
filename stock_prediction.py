import yfinance as yf
from sklearn.linear_model import LinearRegression
import pandas as pd

def predict_stock_price(stock_symbol):
    df = yf.download(stock_symbol, period='1y')
    df['Date'] = df.index
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].map(pd.Timestamp.timestamp)

    X = df['Date'].values.reshape(-1, 1)
    y = df['Close'].values

    model = LinearRegression()
    model.fit(X, y)

    future_date = pd.Timestamp.now().timestamp()
    prediction = model.predict([[future_date]])

    return prediction[0]
