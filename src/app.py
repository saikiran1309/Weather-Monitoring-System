from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .processing.aggregator import calculate_daily_summary
from .database import store_daily_summary
from .data.api import fetch_weather_data, fetch_forecast_data

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# get_weathe
@app.get("/weather/{city}")
async def get_weather(city: str):
    weather_data = fetch_weather_data(city)
    daily_summary = calculate_daily_summary([weather_data])
    
    if daily_summary:
        store_daily_summary(city, daily_summary)  # Store summary with the city in DB
        print(f"Daily summary for {city} stored.")  # Confirm storage
    else:
        print(f"No valid daily summary to store for {city}.")  # Indicate no summary was created

    return weather_data

# get_forecast
@app.get("/forecast/{city}")
async def get_forecast(city: str):
    forecast_data = fetch_forecast_data(city)
    return forecast_data

# read_root
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("frontend/index.html") as f:
        return f.read()