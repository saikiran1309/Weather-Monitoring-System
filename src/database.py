import mysql.connector

# connect_db
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Saikiran@1309",
        database="weather_db"
    )

# store_daily_summary
def store_daily_summary(city, summary):
    db = connect_db()
    cursor = db.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO daily_weather 
            (city, date, avg_temp, max_temp, min_temp, dominant_condition, feels_like, humidity, wind_speed, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            city, 
            summary['date'],  # Should be of type DATE
            float(summary['avg_temp']),  # Ensure it's a float
            float(summary['max_temp']),  # Ensure it's a float
            float(summary['min_temp']),  # Ensure it's a float
            summary['dominant_condition'], 
            float(summary['feels_like']) if summary['feels_like'] is not None else None,  # Ensure it's a float
            int(summary['humidity']) if summary['humidity'] is not None else None,  # Ensure it's an int
            float(summary['wind_speed']) if summary['wind_speed'] is not None else None,  # Ensure it's a float
            summary['timestamp']  # Should be a valid date or timestamp
        ))
        
        db.commit()
        print(f"Daily summary for {city} stored successfully.")
    except Exception as e:
        print(f"Error storing daily summary: {e}")
    finally:
        cursor.close()
        db.close()


