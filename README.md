# 📈 Stock Next-Day Close Price Predictor (Linear Regression)

A simple Python CLI tool that downloads the last **60 days of stock data** using Yahoo Finance, trains a **Linear Regression model**, predicts the **next closing price**, and visualizes the result.

> ⚠️ This project is for educational purposes only — not financial advice.

---

## ✨ Features

- Download historical stock data via `yfinance`
- Train a **Linear Regression** model
- Predict the **next day closing price**
- Clean terminal output
- Data visualization with `matplotlib`

---

## 🧠 How It Works

1. User enters a stock ticker (e.g., `TSLA`)
2. Script downloads last 60 days of close prices
3. Creates:
   - Feature → today's close  
   - Target → next day's close
4. Trains the model
5. Predicts the next closing price
6. Plots the results

---

## 🖼️ Example Result

📅 **Run Date:** 2026-02-19  
📊 **Stock:** TSLA  
⏱️ **Data Period:** Last 60 Days

---

### Terminal Output

Enter Stock Symbol (e.g., AAPL, TSLA): TSLA
[*********************100%***********************]  1 of 1 completed

Predicted next closing price for TSLA: $414.36

---

### Visualization

![TSLA Prediction](assets/tsla_prediction.png)

The chart shows:

- 🔵 Actual closing prices  
- 🔴 Predicted next closing price (dashed line)
