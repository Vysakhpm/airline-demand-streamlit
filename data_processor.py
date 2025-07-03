# data_processor.py
import pandas as pd

def process_insights(df):
    if df.empty:
        return {}, {}

    top_countries = df['origin_country'].value_counts().head(5).to_dict()

    avg_velocity = (
        df.dropna(subset=["velocity"])
        .groupby("origin_country")["velocity"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
        .round(2)
        .to_dict()
    )
    return top_countries, avg_velocity
