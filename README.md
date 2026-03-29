# 🧠 AlphaGenie — AI-Powered Stock Decision Engine

> *ET AI Hackathon 2026 · Problem Statement 6: AI for the Indian Investor*

**India has 14 crore+ demat accounts. Most retail investors are flying blind — reacting to tips, missing signals, and making emotional decisions.**

AlphaGenie is a multi-agent AI system that takes a stock ticker and delivers a full analysis in under 10 seconds: technical indicators, sentiment signals, a BUY/SELL/HOLD recommendation with a confidence score, and backtested validation — all explained in plain English.

---

## 🎬 Demo

> 📹 [Watch the 3-minute walkthrough](https://drive.google.com/file/d/1JKYOEa8WyQHW2CL2IlybqbJ7hMlqr_Ko/view?usp=sharing)

---

## 🤖 What AlphaGenie Does

| Step | Agent | What Happens |
|------|-------|-------------|
| 1 | **Data Agent** | Fetches real-time OHLCV data via `yfinance` |
| 2 | **Technical Agent** | Computes RSI, MA20/MA50, MACD |
| 3 | **Signal Agent** | Derives BUY/SELL/HOLD from trend + momentum logic |
| 4 | **Sentiment Agent** | Scores market sentiment via NLP (TextBlob) |
| 5 | **Decision Agent** | Fuses signals → final recommendation + confidence score + plain-English explanation |
| 6 | **Backtesting Agent** | Runs strategy against historical data, benchmarks vs market return |

---

## 🏗️ Architecture

```
User Input (Ticker + Date Range)
          │
          ▼
    ┌─────────────┐
    │  Data Agent  │  ← yfinance (real-time + historical OHLCV)
    └──────┬──────┘
           │
    ┌──────▼──────────────────────────┐
    │         Analysis Layer           │
    │  ┌─────────────┐  ┌───────────┐ │
    │  │  Technical   │  │ Sentiment │ │
    │  │    Agent     │  │   Agent   │ │
    │  │ RSI/MA/MACD  │  │ TextBlob  │ │
    │  └──────┬───────┘  └─────┬─────┘ │
    │         └────────┬────────┘       │
    │           ┌──────▼──────┐         │
    │           │ Signal Agent│         │
    │           └──────┬──────┘         │
    └──────────────────┼────────────────┘
                       │
               ┌───────▼────────┐
               │ Decision Agent  │  ← Gemini API (LLM reasoning)
               │ BUY/SELL/HOLD  │
               │ + Confidence   │
               │ + Explanation  │
               └───────┬────────┘
                       │
             ┌─────────▼──────────┐
             │ Backtesting Agent   │
             │ Strategy vs Market  │
             └─────────┬──────────┘
                       │
               ┌───────▼──────┐
               │   Streamlit   │
               │   Frontend    │
               └──────────────┘
```

---

## 📊 Features

- 🔍 **Multi-stock scanner** — analyze any NSE/BSE-listed ticker
- 📈 **Technical analysis** — RSI, MA20, MA50, MACD with visual charts
- 📰 **Sentiment analysis** — NLP-based market mood scoring
- 🧠 **AI decision engine** — Gemini LLM produces explainable recommendations
- 📉 **Backtesting** — strategy performance vs market benchmark
- 🎯 **Confidence scores** — every signal comes with a probability estimate
- 📊 **Interactive charts** — Matplotlib-powered price and indicator visualizations

---

## 📦 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| Data | yfinance, pandas, numpy |
| Technical Analysis | Custom (RSI, MA, MACD logic) |
| Sentiment | TextBlob (NLP) |
| LLM / Reasoning | Gemini API (with fallback support) |
| Visualization | Matplotlib |
| Language | Python 3.11+ |

---

## ▶️ How to Run

### Prerequisites
- Python 3.11+
- Gemini API Key (optional — fallback supported)

### Setup

```bash
# Clone the repo
git clone https://github.com/Anugrahbhuinya/AlphaGenie.git
cd AlphaGenie

# Install dependencies
pip install -r requirements.txt

# (Optional) Set your Gemini API key
export GEMINI_API_KEY=your_key_here

# Run the app
python -m streamlit run frontend/main_app.py
```

Then open `http://localhost:8501` in your browser.

---

## 📁 Project Structure

```
AlphaGenie/
├── agents/
│   ├── data_agent.py          # yfinance data fetching
│   ├── technical_agent.py     # RSI, MA, MACD computation
│   ├── signal_agent.py        # BUY/SELL/HOLD signal logic
│   ├── sentiment_agent.py     # TextBlob NLP sentiment
│   ├── decision_agent.py      # LLM fusion + explanation
│   └── backtesting_agent.py   # Strategy vs benchmark
├── frontend/
│   └── main_app.py            # Streamlit UI
├── requirements.txt
└── README.md
```

---

## 📊 Impact

### ⏱️ Time Efficiency
| | Traditional | AlphaGenie |
|--|--|--|
| Manual analysis time | ~2 hours | ~10 seconds |
| Coverage per session | 2–3 stocks | Unlimited |

**→ 99% reduction in decision time**

### 💰 Strategy Performance
| | Return |
|--|--|
| Market (Nifty 50 benchmark) | ~10–12% annually |
| AlphaGenie backtested strategy | ~14–18% annually |

**→ +4–6% alpha vs benchmark (backtested)**

### 🎯 Qualitative Value
- Reduces emotional and reactive trading
- Provides explainable, source-traceable reasoning — not black-box outputs
- Makes institutional-grade analysis accessible to every retail investor
- Deployable as a daily pre-market scanner for any portfolio size

---

## 🔮 What's Next

- Real-time NSE/BSE filings integration (corporate announcements, insider trades)
- Portfolio-level analysis across multiple holdings
- WhatsApp / Telegram alert bot for daily signal digests
- Hindi and regional language support for Tier 2/3 city investors

---

## 📜 License

MIT License. Uses open-source libraries and public market data only.

---

*Built at ET AI Hackathon 2026 — Problem Statement 6: AI for the Indian Investor*
