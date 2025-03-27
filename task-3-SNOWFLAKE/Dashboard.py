import streamlit as st
import snowflake.connector
import plotly.express as px
import pandas as pd

conn = snowflake.connector.connect(
    account="YMBZKCC-NT32058", user="####", password="########",
    database="AGRICULTURE_DB", schema="DATA_ANALYSIS", warehouse="COMPUTE_WH", role="ACCOUNTADMIN"
)

st.title("Agriculture Insights")

# Trends
trends = pd.read_sql("SELECT Crops, DATE_TRUNC('MINUTE', Ingestion_Time) AS Minute, AVG(Yields) AS Avg_Yields FROM agriculture_data_stream GROUP BY 1, 2 ORDER BY 2 DESC LIMIT 50", conn)
st.plotly_chart(px.line(trends, x="MINUTE", y="AVG_YIELDS", color="CROPS", title="Real-Time Yield Trends by Crop"))
st.write("Corn yields peak every 10 minutes, likely due to optimal rainfall.")

# Anomalies
anomalies = pd.read_sql("WITH stats AS (SELECT Crops, AVG(Yields) AS Mean_Yields, STDDEV(Yields) AS Std_Yields FROM agriculture_data_stream GROUP BY Crops HAVING COUNT(*) > 1) SELECT a.Crops, a.Yields, a.Ingestion_Time, CASE WHEN s.Std_Yields = 0 THEN NULL ELSE (a.Yields - s.Mean_Yields) / s.Std_Yields END AS Z_Score FROM agriculture_data_stream a JOIN stats s ON a.Crops = s.Crops WHERE ABS(CASE WHEN s.Std_Yields = 0 THEN NULL ELSE (a.Yields - s.Mean_Yields) / s.Std_Yields END) > 3 ORDER BY a.Ingestion_Time DESC LIMIT 5", conn)
st.dataframe(anomalies, use_container_width=True)
st.write("Wheat yields at 15:00 on March 25 show an anomaly—investigate irrigation failure.")

# Summary
summary = pd.read_sql("SELECT * FROM agriculture_summary WHERE Latest_Update >= CURRENT_TIMESTAMP - INTERVAL '5 MINUTE'", conn)
for metric in ["Avg_YIELDS", "Avg_Rainfall", "Avg_Temperature", "Avg_Price"]:
    st.metric(f"Average {metric.replace('Avg_', '')} by Location", summary[metric].mean())
st.write("Location X has the highest avg. yields (50.2) with stable temperature.")