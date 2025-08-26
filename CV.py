import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Download Stock Data
ticker = "AAPL"  # Apple stock (you can change to MSFT, TSLA, etc.)
df = yf.download(ticker, start="2023-01-01", end="2025-01-01")

# 2. Prepare Data (use Close price for prediction)
df = df[["Close"]]  # Only keep closing prices
df["Target"] = df["Close"].shift(-1)  # Next day's price as target

# Drop the last row (NaN target)
df = df.dropna()

# 3. Train/Test Split
X = df[["Close"]]  # Features = today’s close
y = df["Target"]  # Target = tomorrow’s close

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# 4. Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Make Predictions
predictions = model.predict(X_test)

# 6. Evaluate
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse:.2f}")

# 7. Plot Real vs Predicted
plt.figure(figsize=(10, 5))
plt.plot(y_test.values, label="Actual Price")
plt.plot(predictions, label="Predicted Price")
plt.legend()
plt.title(f"{ticker} Stock Price Prediction (Linear Regression)")
plt.show()
