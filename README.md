# ✈️ Airline Market Demand Tracker


![Screenshot 2025-07-03 110820](https://github.com/user-attachments/assets/29efbee4-1dd9-4ce0-8c4b-cda746337ad9)
![Screenshot 2025-07-03 115932](https://github.com/user-attachments/assets/09affc7c-105a-41cf-b016-1f74d7f88eca)

![Screenshot 2025-07-03 110740](https://github.com/user-attachments/assets/6caed7f3-a1c2-476a-bf4f-990ae5e20759)

A real-time web dashboard that tracks live airline demand using the [OpenSky Network API](https://opensky-network.org/), built with **Streamlit**.

It displays:
- 🌍 Top 5 countries by active flights
- 💨 Countries with the highest average flight velocity
- 📊 Interactive bar charts
- 🧠 (Bonus) GPT-powered trend summary using ChatGPT API

---

## 🔧 Features
- ✅ Live flight data using OpenSky API
- ✅ Interactive bar charts with Plotly
- ✅ Clean UI with Streamlit
- ✅ Data table with flight metadata
- ✅ GPT-powered summary using your own OpenAI API key

---

## 🚀 How to Run

### 🔗 Requirements:
```bash
pip install -r requirements.txt
▶️ Launch app:
streamlit run app.py

🧠 GPT Trend Summary (Optional)
To use the GPT-powered summary:

1.Get your OpenAI API key

2.Enter it in the input field inside the app

3.You’ll get a short auto-generated summary like:

“India and Australia have the most active flights today, while Germany shows the highest flight speeds, indicating long-haul operations.”

Note: Free-tier keys may show a "quota exceeded" message if usage limits are hit.
