import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# Load data
current = os.path.dirname(__file__)
csv_path = os.path.join(current, "bitcoin_dataset.csv")
df = pd.read_csv(csv_path)

# Preprocessing
df['Timestamp'] = pd.to_numeric(df['Timestamp'], errors='coerce')
df['Date'] = pd.to_datetime(df['Timestamp'], unit='s')
df.sort_values('Date', inplace=True)
df.reset_index(drop=True, inplace=True)

# Moving averages
df['MA7'] = df['Close'].rolling(window=7).mean()
df['MA30'] = df['Close'].rolling(window=30).mean()

# Debug print
print("Preview:")
print(df[['Date', 'Close', 'MA7', 'MA30']].tail(15))


df['Volatility'] = df['High'] - df['Low']
max_vol_day = df[df['Volatility'] == df['Volatility'].max()]
print("بیشترین نوسان روزانه:")
print(max_vol_day[['Date', 'High', 'Low', 'Volatility']])

# Plot
plt.figure(figsize=(14, 7))
plt.plot(df['Date'], df['Close'], label='Close Price',
         color='orange', linewidth=2)
plt.plot(df['Date'], df['MA7'], label='7-Day MA',
         color='blue', linewidth=2, linestyle='--')
plt.plot(df['Date'], df['MA30'], label='30-Day MA',
         color='green', linewidth=2, linestyle=':')
plt.plot(df['Date'], df['Volatility'],
         label='Daily Volatility', color='purple')

plt.title("Bitcoin Price with 7-Day and 30-Day Moving Averages")
plt.xlabel("Date")
plt.ylabel("USD")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
