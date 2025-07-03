# app.py
import streamlit as st
import plotly.graph_objects as go
from opensky_api import fetch_flight_data
from data_processor import process_insights

st.set_page_config(page_title="Airline Demand Dashboard", layout="centered")

st.title("✈️ Airline Market Demand Tracker")
st.write("Powered by OpenSky API – Realtime Flight Demand Insights")

# Fetch and display data
with st.spinner("Fetching live flight data..."):
    df = fetch_flight_data()

if df.empty:
    st.error("No data retrieved. Try again later.")
    st.stop()

st.success(f"✅ Loaded {len(df)} live flight records")

# Display insights
top_countries, avg_velocity = process_insights(df)

st.subheader("🌍 Top Countries by Active Flights")
fig1 = go.Figure([go.Bar(x=list(top_countries.keys()), y=list(top_countries.values()))])
fig1.update_layout(title="Top 5 Countries by Flights", xaxis_title="Country", yaxis_title="Flight Count")
st.plotly_chart(fig1)

st.subheader("💨 Average Velocity by Country")
fig2 = go.Figure([go.Bar(x=list(avg_velocity.keys()), y=list(avg_velocity.values()), marker_color='orange')])
fig2.update_layout(title="Top 5 Countries by Avg. Velocity", xaxis_title="Country", yaxis_title="Velocity (m/s)")
st.plotly_chart(fig2)

# Show raw data (optional)
with st.expander("📄 Show Raw Data"):
    st.dataframe(df[['callsign', 'origin_country', 'latitude', 'longitude', 'velocity']])
