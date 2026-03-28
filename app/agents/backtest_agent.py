import pandas as pd

def backtest_strategy(df):
    df = df.copy()

    # Calculate daily returns
    df['returns'] = df['Close'].pct_change()

    # Define Signal (1 if MA20 > MA50, else 0)
    df['signal'] = 0
    df.loc[df['MA20'] > df['MA50'], 'signal'] = 1

    # Strategy returns (Shift signal by 1 day to avoid look-ahead bias)
    df['strategy_returns'] = df['signal'].shift(1) * df['returns']

    # Calculate Cumulative Returns (Starting from 1.0)
    df['cum_market'] = (1 + df['returns']).cumprod()
    df['cum_strategy'] = (1 + df['strategy_returns']).cumprod()

    # Final percentage returns for the metrics
    strategy_final = round((df['cum_strategy'].iloc[-1] - 1) * 100, 2)
    market_final = round((df['cum_market'].iloc[-1] - 1) * 100, 2)

    return {
        "strategy_return": strategy_final,
        "market_return": market_final,
        "cumulative_df": df[['cum_market', 'cum_strategy']].dropna() # Send the data for plotting
    }