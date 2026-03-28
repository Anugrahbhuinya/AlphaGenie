import pandas as pd
import ta

def add_technical_indicators(df: pd.DataFrame):
    """
    Add RSI, Moving Averages, MACD
    """
    try:
        # Moving Averages
        df['MA20'] = df['Close'].rolling(window=20).mean()
        df['MA50'] = df['Close'].rolling(window=50).mean()

        # RSI
        df['RSI'] = ta.momentum.RSIIndicator(df['Close']).rsi()

        # MACD
        macd = ta.trend.MACD(df['Close'])
        df['MACD'] = macd.macd()
        df['MACD_signal'] = macd.macd_signal()

        df.dropna(inplace=True)
        return df

    except Exception as e:
        print(f"Error computing indicators: {e}")
        return df