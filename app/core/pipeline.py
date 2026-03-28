from app.agents.data_agent import fetch_stock_data
from app.agents.technical_agent import add_technical_indicators
from app.agents.signal_agent import generate_signal
from app.agents.sentiment_agent import analyze_sentiment
from app.agents.decision_agent import generate_decision
from app.agents.backtest_agent import backtest_strategy


def run_alpha_genie(ticker: str):
    """
    Complete AlphaGenie pipeline
    """

    try:
        # 🔹 Step 1: Fetch data
        df = fetch_stock_data(ticker)

        if df.empty:
            return {"error": "No data found for this ticker"}

        # 🔹 Step 2: Add indicators
        df = add_technical_indicators(df)

        # 🔹 Step 3: Generate signal
        signal_data = generate_signal(df)

        # 🔹 Step 4: Sentiment analysis
        sentiment_data = analyze_sentiment()

        # 🔹 Step 5: AI decision
        decision = generate_decision(signal_data, sentiment_data)
        backtest_data = backtest_strategy(df)

        # 🔹 Final Output
        result = {
            "ticker": ticker,
            "signal": signal_data,
            "sentiment": sentiment_data,
            "decision": decision
        }

        return result

    except Exception as e:
        return {"error": str(e)}