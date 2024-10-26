# Real-Time Weather Monitoring and Data Processing System

## Objective
This project aims to create a real-time data processing system to monitor and analyze weather conditions using data from the OpenWeatherMap API. By processing incoming weather data, the system will provide summarized insights through rollups and aggregates, allowing for efficient monitoring and quick access to key weather metrics.

## Project Structure
```csharp
    Weather-Monitoring-System/
	│
	├── src/
	│   ├── config/
	│   │   └── config.py                # Configuration file for API key and settings
	│   ├── data/
	│   │   └── api.py                   # Module for fetching weather data
	│   ├── processing/
	│   │   └── aggregator.py            # Module for processing and aggregating data
	│   ├── database.py                  # Module for database interactions
	│   ├── app.py                       # Main FastAPI application
	│
	├── frontend/                        # Directory for front-end files
	│   ├── index.html                   # HTML file for displaying data
	│   ├── styles.css                   # CSS file for styling
	│   └── script.js                    # JavaScript file for fetching and displaying data
	│
	└── README.md                        # Project documentation
```

## Project Overview
When we run the project using the command uvicorn src.app:app, it generates a host link. Upon accessing this link, we see buttons representing major metros in India: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad. Clicking on any city button displays detailed weather information, including the average temperature, minimum and maximum temperatures, humidity, wind speed, and a 5-day forecast for that particular city. Additionally, each click on these buttons stores the data in the database, which is helpful for future data processing.

### Project Process Overview
1. Launch the Application: Run the project with the command uvicorn src.app:app, generating a host link.
2. User Interface: The application displays buttons for major Indian cities.
3. Weather Data Retrieval: When a city button is clicked, the application retrieves and displays weather details such as average, minimum, and maximum temperatures, humidity, wind speed, and a 5-day forecast.
4. Data Storage: Each interaction (button click) stores the retrieved weather data in the database for future processing and analysis.

## Key Features

- Data Integration: Continuously pulls real-time weather data from the OpenWeatherMap API for specified locations.
- Data Aggregation: Applies rollups and aggregates to condense the data, providing summary metrics such as average temperature, humidity trends, and weather condition counts.
- Real-Time Insights: Displays concise, up-to-date weather insights, enabling quick access to meaningful weather patterns and trends.
  
## Getting Started

### Prerequisites

- Make sure you have **Python** and **MySQL** installed on your system.
- For Python
  
   ```bash
   python --version
   ```
- For MySQL

  ```bash
   mysql -V
   ```
  
### Installation
1. **Clone the Repository**
   ```bash
   git clone "https://github.com/saikiran1309/Weather-Monitoring-System.git"
   cd Weather-Monitoring-System
   ```

2. **Create a new virtual environment for the project**
   ```bash
   pip install virtualenv
   virtualenv venv         # Create a new venv
   venv\Scripts\activate    # Activate the virtual environment
   ```

3. **Install the required packages:**
   ```bash
   pip install fastapi uvicorn requests mysql-connector-python
   pip install python-dotenv
   ```
   
4. **Add this Database Schema**
   ```bash
   # Create the weather_db database
   CREATE DATABASE weather_db;
   
   # Select the weather_db database
   USE weather_db;

   # Show all tables in the current database
   SHOW TABLES;
   
   # Create the daily_weather table
   CREATE TABLE daily_weather (
        id INT AUTO_INCREMENT PRIMARY KEY,
        city VARCHAR(255),
        date DATE,
        avg_temp FLOAT,
        max_temp FLOAT,
        min_temp FLOAT,
        dominant_condition VARCHAR(255),
        feels_like FLOAT,
        humidity INT,
        wind_speed FLOAT,
        timestamp DATETIME
   );
   ```
   
5. **To run the app, use:**
   ```bash
   uvicorn src.app:app
   ```

## Finally
The Real-Time Weather Monitoring and Data Processing System is ready.
```
Created By : Sai Kiran

