import yfinance as yf
import matplotlib.pyplot as plt

tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA']  # your 5 stocks

for ticker in tickers:
    # Download data for 1 month
    data = yf.download(ticker, period='1mo', interval='1d')
    
    # Save CSV for evidence
    data.to_csv(f"{ticker}.csv")
    
    # Plot closing price
    plt.plot(data.index, data['Close'], marker='o', label=ticker)

# Finalize graph
plt.title("Closing Prices - Last Month")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Save the graph for evidence folder
plt.savefig("StockClosingPrices.png")

# Show the graph
plt.show()
