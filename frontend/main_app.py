import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import sys
import os

# Adds the root directory (AplhaGenie) to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.pipeline import run_alpha_genie

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="AlphaGenie AI", layout="centered")

st.title("🚀 AlphaGenie: AI-Powered Stock Decision Engine")
st.markdown("Get intelligent BUY/SELL signals with reasoning, confidence & backtested performance")

# =========================
# 🔍 MULTI-STOCK SCANNER
# =========================
st.markdown("### 🔍 Quick Market Scan")

default_stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS"]

if st.button("Scan Top Stocks"):
    scan_results = []

    for stock in default_stocks:
        result = run_alpha_genie(stock)

        if "error" not in result:
            decision = result["decision"]
            confidence = decision["confidence"] if isinstance(decision, dict) else "-"

            scan_results.append({
                "Stock": stock,
                "Signal": result["signal"]["signal"],
                "RSI": result["signal"]["rsi"],
                "Confidence": confidence
            })

    st.dataframe(scan_results)

# =========================
# 🎯 SINGLE STOCK ANALYSIS
# =========================
ticker = st.text_input("Enter Stock Ticker (e.g., RELIANCE.NS)")

if st.button("Analyze"):

    if ticker:
        with st.spinner("Analyzing market data..."):
            result = run_alpha_genie(ticker)

        if "error" in result:
            st.error(result["error"])

        else:
            signal = result["signal"]
            sentiment = result["sentiment"]
            decision = result["decision"]

            # =========================
            # 🎯 FINAL ACTION BOX
            # =========================
            if isinstance(decision, dict):
                st.markdown("### 🎯 Final Action")

                action = decision["recommendation"]
                confidence = decision["confidence"]

                if action == "BUY":
                    st.success(f"📈 STRONG BUY | Confidence: {confidence}%")
                elif action == "SELL":
                    st.error(f"📉 STRONG SELL | Confidence: {confidence}%")
                else:
                    st.info(f"⚖️ HOLD / WAIT | Confidence: {confidence}%")
            else:
                confidence = 60

            # =========================
            # 📈 SIGNAL SECTION
            # =========================
            st.subheader("📈 Trading Signal")

            if signal["signal"] == "BUY":
                st.success("BUY SIGNAL 🚀")
            elif signal["signal"] == "SELL":
                st.error("SELL SIGNAL 🔻")
            else:
                st.info("HOLD ⚖️")

            col1, col2, col3 = st.columns(3)
            col1.metric("RSI", signal["rsi"])
            col2.metric("MA20", signal["ma20"])
            col3.metric("MA50", signal["ma50"])

            st.write("**Reasons:**")
            for r in signal["reason"]:
                st.write(f"- {r}")

            # =========================
            # 📊 PRICE CHART
            # =========================
            st.subheader("📊 Price Chart")

            data = yf.download(ticker, period="3mo")

            fig, ax = plt.subplots()
            ax.plot(data['Close'], label="Close", linewidth=2)
            ax.plot(data['Close'].rolling(20).mean(), label="MA20", linestyle="--")

            ax.set_title(f"{ticker} Price & Trend")
            ax.legend()

            st.pyplot(fig)

            # 🔥 PRICE INSIGHT
            latest_price = data['Close'].iloc[-1]
            prev_price = data['Close'].iloc[-2]

            change = round(((latest_price - prev_price) / prev_price) * 100, 2)

            st.write(f"📊 Latest Price: ₹{round(latest_price,2)} ({change}%)")

            # =========================
            # 📰 SENTIMENT
            # =========================
            st.subheader("📰 Market Sentiment")

            col1, col2 = st.columns(2)
            col1.metric("Sentiment", sentiment["sentiment"])
            col2.metric("Score", sentiment["score"])

            # =========================
            # 🧠 AI DECISION
            # =========================
            st.subheader("🧠 AI Decision")

            if isinstance(decision, dict):
                st.write(f"**Recommendation:** {decision['recommendation']}")
                st.write(f"**Explanation:** {decision['explanation']}")
                st.write(f"**Confidence:** {decision['confidence']}%")
            else:
                st.write(decision)

            # =========================
            # 🔥 CONFIDENCE BADGE
            # =========================
            if confidence > 75:
                st.success("High Confidence Signal 🔥")
            elif confidence > 60:
                st.info("Moderate Confidence")
            else:
                st.warning("Low Confidence")

            # =========================
            # 📉 BACKTESTING
            # =========================
            if "backtest" in result:
                st.subheader("📉 Strategy Performance")

                bt = result["backtest"]

                col1, col2 = st.columns(2)
                col1.metric("AlphaGenie Return", f"{bt['strategy_return']}%")
                col2.metric("Market Return", f"{bt['market_return']}%")

                # --- ADDED EQUITY CURVE CHART ---
                if "cumulative_df" in bt:
                    st.write("**Strategy Growth vs Market**")
                    fig_bt, ax_bt = plt.subplots(figsize=(10, 4))
                    chart_data = bt["cumulative_df"]
                    ax_bt.plot(chart_data['cum_strategy'], label="Strategy", color="green")
                    ax_bt.plot(chart_data['cum_market'], label="Market", color="gray", linestyle="--")
                    ax_bt.legend()
                    st.pyplot(fig_bt)

                if bt["strategy_return"] > bt["market_return"]:
                    st.success("AlphaGenie Outperformed Market 🚀")
                else:
                    st.warning("Market Outperformed Strategy")

    else:
        st.warning("Please enter a stock ticker")


# =========================
# 💡 INSIGHT SECTION
# =========================
st.markdown("### 💡 Why This Matters")

st.write("""
- Eliminates emotional trading  
- Combines technical + sentiment signals  
- Provides explainable AI decisions  
- Validates strategy via backtesting  
""")

# =========================
# ⚙️ SYSTEM EXPLANATION
# =========================
st.markdown("### ⚙️ How AlphaGenie Works")

st.write("""
AlphaGenie uses a multi-agent architecture:
- Data Agent → Fetches real-time stock data  
- Technical Agent → Computes indicators (RSI, MA, MACD)  
- Signal Agent → Generates trading signals  
- Sentiment Agent → Evaluates market sentiment  
- Decision Agent → Produces explainable AI decisions  
""")

# =========================
# 🚀 IMPACT
# =========================
st.markdown("### 🚀 Impact")

st.write("Reduces decision time from hours to seconds and improves trading confidence using AI-driven insights.")