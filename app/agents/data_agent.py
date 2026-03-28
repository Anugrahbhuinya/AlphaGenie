import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, period="6mo", interval="1d"):
    try:
        df = yf.download(ticker, period=period, interval=interval)

        if df.empty:
            raise ValueError("No data found for ticker")

        # 🔥 FIX: Flatten multi-index columns
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df.dropna(inplace=True)

        return df

    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()