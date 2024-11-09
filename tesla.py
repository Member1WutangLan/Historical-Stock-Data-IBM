import yfinance as yf
import pandas as pd

# Question 1: Extract Tesla Stock Data
# -------------------------------------
# Create the Ticker object for Tesla
tesla = yf.Ticker("TSLA")

# Extract historical data for Tesla
tesla_data = tesla.history(period="max")

# Reset the index to make 'Date' a column
tesla_data.reset_index(inplace=True)

# Display the first five rows of the DataFrame for Question 1
print("Question 1 - First Five Rows of Tesla Data:")
print(tesla_data.head())


# Question 2: Extract Tesla Revenue Data using yfinance
# -----------------------------------------------------
# Extract Tesla's financials data (income statement)
tesla_financials = tesla.financials.T  # Transpose to have dates as rows

# Select only the 'Total Revenue' column
tesla_revenue = tesla_financials[['Total Revenue']].copy()

# Reset index to make dates a column, and rename columns for clarity
tesla_revenue.reset_index(inplace=True)
tesla_revenue.columns = ["Date", "Revenue"]

# Display the last five rows of the tesla_revenue DataFrame for Question 2
print("\nQuestion 2 - Last Five Rows of Tesla Revenue Data:")
print(tesla_revenue.tail())