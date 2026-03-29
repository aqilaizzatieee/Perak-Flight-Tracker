import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import time

st.set_page_config(page_title="Perak IoT Flight Tracker", layout="wide")
st.title("✈️ Perak Real-Time IoT Flight Tracker")

def get_data():
    try:
        conn = sqlite3.connect('perak_flights.db')
        df = pd.read_sql_query("SELECT * FROM flights", conn)
        conn.close()
        return df
    except:
        return pd.DataFrame()

df = get_data()

if df.empty:
    st.warning("Database is currently empty. Waiting for Perak air traffic...")
    # This empty map keeps the view on Perak while you wait
    fig = px.scatter_mapbox(lat=[4.5], lon=[101.0], zoom=7, mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)
else:
    st.metric("Total Observations Recorded", len(df))
    
    fig = px.scatter_mapbox(df, 
                            lat="lat", lon="lon", 
                            color="alt", hover_name="callsign",
                            color_continuous_scale=px.colors.cyclical.IceFire, 
                            size_max=15, 
                            zoom=7,
                            center={"lat": 4.5, "lon": 101.0}, # FORCES map to Perak
                            mapbox_style="carto-positron")
    
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Recent Data Logs")
    st.write(df.tail(10))

# Refresh logic
time.sleep(10) # Set to 10 seconds so you see updates faster
st.rerun()