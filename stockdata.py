import yfinance as yf
import pandas as pd
import json
import matplotlib.pyplot as plt

# Creating Ticker Object for Apple
apple = yf.Ticker("AAPL")

# Loading Stock Info for Apple from JSON File
with open('apple.json') as json_file:
    apple_info = json.load(json_file)

# Accessing Stock Information
print("Apple Stock Information:")
print("Country:", apple_info['country'])
print("Sector:", apple_info.get('sector', 'N/A'))

# Extracting Historical Share Price Data for Apple
apple_share_price_data = apple.history(period="max")
apple_share_price_data.reset_index(inplace=True)

# Plotting the Share Price Data (Opening Price vs. Date)
plt.figure(figsize=(10, 5))
plt.plot(apple_share_price_data["Date"], apple_share_price_data["Open"], label="Open Price")
plt.title("Apple Stock Opening Price Over Time")
plt.xlabel("Date")
plt.ylabel("Opening Price")
plt.legend()
plt.show()

# Extracting Dividends Data for Apple and Plotting
plt.figure(figsize=(10, 5))
apple.dividends.plot(title="Apple Dividends Over Time")
plt.xlabel("Date")
plt.ylabel("Dividends")
plt.show()

# Exercise: Creating Ticker Object for AMD
amd = yf.Ticker("AMD")

# Loading AMD Stock Info from JSON File
with open('amd.json') as json_file:
    amd_info = json.load(json_file)

# Accessing AMD Stock Information
print("\nAMD Stock Information:")
print("Country:", amd_info['country'])
print("Sector:", amd_info['sector'])

# Obtain and Inspect Historical Data for AMD
amd_share_price_data = amd.history(period="max")
first_day_volume = amd_share_price_data['Volume'].iloc[0]
print("First day volume traded for AMD:", first_day_volume)