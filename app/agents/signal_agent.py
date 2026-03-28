def generate_signal(df):
    """
    Generate BUY / SELL / HOLD signal based on indicators
    """
    latest = df.iloc[-1]

    ma20 = latest['MA20']
    ma50 = latest['MA50']
    rsi = latest['RSI']
    macd = latest['MACD']
    macd_signal = latest['MACD_signal']

    signal = "HOLD"
    reason = []

    # 🔥 BUY Conditions
    if (ma20 > ma50) and (rsi < 70) and (macd > macd_signal):
        signal = "BUY"
        reason.append("Uptrend (MA20 > MA50)")
        reason.append("RSI indicates strength but not overbought")
        reason.append("MACD bullish crossover")

    # 🔻 SELL Conditions (improved)
    elif (ma20 < ma50) and (macd < macd_signal):
        signal = "SELL"
        reason.append("Downtrend (MA20 < MA50)")
        reason.append("MACD bearish crossover")

    # ⚖️ HOLD
    else:
        reason.append("No strong signal detected")

    return {
        "signal": signal,
        "reason": reason,
        "rsi": float(round(rsi, 2)),
        "ma20": float(round(ma20, 2)),
        "ma50": float(round(ma50, 2))
    }