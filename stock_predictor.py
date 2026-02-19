import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 1. Get user input
ticker = input("Enter Stock Symbol (e.g., AAPL, TSLA): ").upper()

# 2. Download past 60 days of data
data = yf.download(ticker, period='60d',)
data = data[['Close']]
data.dropna(inplace=True)

# 3. Create features and labels
data['Target'] = data['Close'].shift(-1)  # next day's close
data.dropna(inplace=True)

X = data[['Close']].values
y = data['Target'].values

# 4. Train model
model = LinearRegression()
model.fit(X, y)

# 5. Predict next day
last_close = data['Close'].iloc[-1].item()
predicted_price = model.predict([[last_close]])[0]
print(f"\nPredicted next closing price for {ticker}: ${predicted_price:.2f}")

# 6. Plot
plt.figure(figsize=(10, 5))
plt.plot(data['Close'], label='Actual Close')
plt.axhline(y=predicted_price, color='r', linestyle='--', label='Predicted Next Close')
plt.title(f'{ticker} - Close Price & Prediction')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.show()

