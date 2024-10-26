from datetime import datetime

# calculate_daily_summary
def calculate_daily_summary(weather_entries):
    if not weather_entries:
        print("No weather entries provided.")
        return None

    temps = []
    feels_like_list = []
    conditions = []
    main_conditions = []  
    humidities = []
    wind_speeds = []
    timestamps = []

    for entry in weather_entries:
        if isinstance(entry, dict):
            if 'temp' in entry:
                temps.append(entry['temp'])
            if 'feels_like' in entry:
                feels_like_list.append(entry['feels_like'])
            if 'condition' in entry:
                conditions.append(entry['condition'])
            if 'main_condition' in entry:
                main_conditions.append(entry['main_condition'])
            if 'humidity' in entry:
                humidities.append(entry['humidity'])
            if 'wind_speed' in entry:
                wind_speeds.append(entry['wind_speed'])
            if 'timestamp' in entry:
                timestamps.append(entry['timestamp'])
    if not temps:
        print("No valid temperatures found.")
        return None
    summary = {
        'date': datetime.now().date(),
        'avg_temp': sum(temps) / len(temps),
        'max_temp': max(temps),
        'min_temp': min(temps),
        'dominant_condition': determine_dominant_condition(conditions),
        'main_condition': main_conditions[0] if main_conditions else None,
        'feels_like': sum(feels_like_list) / len(feels_like_list) if feels_like_list else None,
        'humidity': sum(humidities) / len(humidities) if humidities else None,
        'wind_speed': sum(wind_speeds) / len(wind_speeds) if wind_speeds else None,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S') if timestamps else None
    }
    print(f"Calculated Summary: {summary}")
    return summary

# determine_dominant_condition
def determine_dominant_condition(conditions):
    condition_count = {}
    for condition in conditions:
        condition_count[condition] = condition_count.get(condition, 0) + 1
    if not condition_count:
        print("No conditions found.")
        return None
    return max(condition_count, key=condition_count.get)