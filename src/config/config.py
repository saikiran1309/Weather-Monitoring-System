from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
INTERVAL = 300  # Default interval for fetching weather data in seconds (5 minutes)

# Optional: Debugging
print(f"API Key: {API_KEY}, Cities: {CITIES}, Fetch Interval: {INTERVAL}")
