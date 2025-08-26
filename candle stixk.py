import yfinance as yf
import mplfinance as mpf
import pandas as pd

print("\nWelcome to the Candlestick Chart Viewer!")
print("This program will display a candlestick chart for a given stock ticker.")
print("Example: 'AAPL' for Apple, 'MSFT' for Microsoft, 'TSLA' for Tesla.\n")

# Get ticker from user
ticker = input("Enter the stock ticker symbol: ").strip().upper()

# Date range for the chart
start_date = "2024-08-01"
end_date = "2025-09-01"

try:
    # Download data from Yahoo
    df = yf.download(ticker, start=start_date, end=end_date)

    # Ensure price columns are numeric
    for col in ["Open", "High", "Low", "Close"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows with missing values
    df.dropna(subset=["Open", "High", "Low", "Close"], inplace=True)

    if df.empty:
        print("⚠ No valid price data found for this ticker in the given date range.")
    else:
        # Plot candlestick chart
        mpf.plot(
            df,
            type="candle",
            style="charles",
            title=f"{ticker} Candlestick Chart",
            ylabel="Price",
            ylabel_lower="Volume",
            volume=True,
        )

except Exception as e:
    print(f"❌ An error occurred: {e}")
