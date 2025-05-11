import pandas as pd
import plotly.express as px
import preswald

# Load the actual dataset
df = pd.read_csv('data/seattle weather.csv')  

# Define the color mapping for each weather type
color_map = {
    'drizzle': 'pink',
    'rain': 'orange',
    'sun': 'grey',
    'snow': 'red',
    'fog': 'green'
}

# Create a scatter plot: Max Temperature vs. Rainfall
fig = px.scatter(
    df,
    x='temp_max',
    y='precipitation',
    text='weather',
    color='weather',
    title='🌦 Seattle Weather Dashboard - Temperature vs Rainfall',  # Custom Title
    labels={'temp_max': 'Max Temp (°C)', 'precipitation': 'Rainfall (mm)'},
    color_discrete_map=color_map  # Correct color mapping applied
)

# Customize plot appearance
fig.update_traces(textposition='top center', marker=dict(size=10))
fig.update_layout(
    template='plotly_white',
    title=dict(font=dict(family='Arial', size=24, color='blue'), x=0.5, xanchor='center')
)

# Display via Preswald
preswald.text("# 🌦 Seattle-Weather Dashboard")
preswald.text("Visualizing the relationship between temperature and rainfall using real Seattle weather data.")
preswald.plotly(fig)

# Show days with high rainfall
high_rain_df = df[df['precipitation'] > 10]
preswald.text("## ☔ Days with Heavy Rainfall (>10 mm)")
preswald.table(high_rain_df)

