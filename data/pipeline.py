
import pandas as pd

from .data_loader import *
from .data_processing import *


def build_dataset(ticker="V"):
  
  # Load financial statements
  data = get_financial_statements(ticker)

  income = data["income"]
  balance = data["balance"]
  cashflow = data["cashflow"]

  # Load market data
  price_data = get_price_data(ticker, income.index)

  # Build historical financial dataset
  df = build_historical_df(income, balance, cashflow, price_data)

  print(f"{ticker} dataset built successfully")

  return df
