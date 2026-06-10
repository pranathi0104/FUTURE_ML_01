import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="Sales Forecast Dashboard",
    layout="wide"
)

st.title("📈 Sales Forecast Dashboard")

st.markdown("""
This dashboard predicts future sales using a Random Forest Regression model trained on historical sales data.
""")
# Load historical sales
history = pd.read_csv("data/history.csv")

# Load forecast
forecast_df = pd.read_csv("data/forecast_df.csv")

# Convert dates
history["Order Date"] = pd.to_datetime(history["Order Date"])
forecast_df["Date"] = pd.to_datetime(forecast_df["Date"])



st.sidebar.title(
    "Dashboard Information"
)

st.sidebar.write(
    "Future Interns ML Task 1"
)

st.sidebar.write(
    "Sales Forecasting Project"
)

st.sidebar.write(
    f"Historical Records: {len(history)}"
)

st.sidebar.write(
    f"Forecast Days: {len(forecast_df)}"
)


# KPI Cards

total_sales = history["Sales"].sum()
avg_sales = history["Sales"].mean()
max_sales = history["Sales"].max()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Sales",
    f"{total_sales:,.0f}"
)

col2.metric(
    "Average Sales",
    f"{avg_sales:,.0f}"
)

col3.metric(
    "Maximum Sales",
    f"{max_sales:,.0f}"
)

col4, col5, col6 = st.columns(3)

col4.metric(
    "Highest Forecast",
    f"{forecast_df['Forecasted Sales'].max():,.0f}"
)

col5.metric(
    "Lowest Forecast",
    f"{forecast_df['Forecasted Sales'].min():,.0f}"
)

col6.metric(
    "Average Forecast",
    f"{forecast_df['Forecasted Sales'].mean():,.0f}"
)


st.subheader(
    "Historical Sales Trend"
)


# Historical Sales Chart
fig = px.line(
    history,
    x="Order Date",
    y="Sales",
    title="Historical Sales Trend",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)
# Forecast Chart






st.subheader(
    "30-Day Sales Forecast"
)

fig2 = px.line(
    forecast_df,
    x="Date",
    y="Forecasted Sales",
    title="Forecasted Sales"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.subheader(
    "Forecast Insights"
)

highest = forecast_df[
    "Forecasted Sales"
].max()

lowest = forecast_df[
    "Forecasted Sales"
].min()

average = forecast_df[
    "Forecasted Sales"
].mean()

st.write(
    f"Highest Forecast: {highest:,.2f}"
)

st.write(
    f"Lowest Forecast: {lowest:,.2f}"
)

st.write(
    f"Average Forecast: {average:,.2f}"
)

st.subheader(
    "Historical + Forecast Sales"
)

history_plot = history[
    ["Order Date", "Sales"]
].copy()

history_plot.columns = [
    "Date",
    "Sales"
]

forecast_plot = forecast_df.copy()

forecast_plot.columns = [
    "Date",
    "Sales"
]

combined = pd.concat(
    [
        history_plot,
        forecast_plot
    ]
)

fig3 = px.line(
    combined,
    x="Date",
    y="Sales",
    title="Historical and Forecast Sales"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.subheader(
    "Forecast Summary"
)

col6, col7, col8 = st.columns(3)

col6.metric(
    "Highest Forecast",
    f"{forecast_df['Forecasted Sales'].max():,.0f}"
)

col7.metric(
    "Lowest Forecast",
    f"{forecast_df['Forecasted Sales'].min():,.0f}"
)

col8.metric(
    "Average Forecast",
    f"{forecast_df['Forecasted Sales'].mean():,.0f}"
)
# Forecast Table
st.subheader("Forecast Data")
st.dataframe(forecast_df)



# Download Button
csv = forecast_df.to_csv(
    index=False
)

st.download_button(
    "Download Forecast CSV",
    forecast_df.to_csv(index=False),
    "sales_forecast.csv",
    "text/csv"
)



st.markdown("---")

st.success(
    "Sales forecast generated successfully."
)

st.markdown(
    "Developed by Pranathi | Future Interns ML Task 1"
)
