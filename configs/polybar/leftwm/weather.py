#!/usr/bin/env python3
import json
import requests
import os
import sys
from datetime import datetime, timedelta

API_KEY = "8bcd81d07c9ef5a23dd709885254d64c"
LAT = -27.7333
LON = 27.0667
CITY_NAME = "Odendaalsrus"
CACHE_FILE = "/tmp/polybar-weather.json"
FORECAST_CACHE = "/tmp/polybar-forecast.json"

WEATHER_ICONS = {
    200: "⛈️", 300: "🌦️", 500: "🌦️", 501: "️", 600: "🌨️",
    601: "️", 701: "🌫️", 800: "☀️", 801: "🌤️", 802: "⛅",
    803: "☁️", 804: "☁️"
}

def get_current_weather():
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE) as f:
                data = json.load(f)
            if datetime.now().timestamp() - data['time'] < 300:
                return data
    except: pass
    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        return None
    
    data = resp.json()
    data['time'] = datetime.now().timestamp()
    
    with open(CACHE_FILE, 'w') as f:
        json.dump(data, f)
    
    return data

def get_forecast():
    try:
        if os.path.exists(FORECAST_CACHE):
            with open(FORECAST_CACHE) as f:
                data = json.load(f)
            if datetime.now().timestamp() - data['time'] < 1800:  # 30 min cache
                return data['list']
    except: pass
    
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        return None
    
    forecast_data = resp.json()
    forecast_data['time'] = datetime.now().timestamp()
    
    with open(FORECAST_CACHE, 'w') as f:
        json.dump(forecast_data, f)
    
    return forecast_data['list']

def show_bar():
    data = get_current_weather()
    if not data:
        print(" --°")
        return
    
    temp = data['main']['temp']
    code = data['weather'][0]['id']
    icon = WEATHER_ICONS.get(code, "🌡️")
    print(f"{icon} {temp:.0f}°")

def show_details():
    current = get_current_weather()
    forecast = get_forecast()
    
    if not current:
        print("Weather unavailable")
        return
    
    # Current weather
    temp = current['main']['temp']
    feels = current['main']['feels_like']
    humidity = current['main']['humidity']
    pressure = current['main']['pressure']
    wind_speed = current['wind']['speed'] * 3.6
    desc = current['weather'][0]['description'].title()
    code = current['weather'][0]['id']
    icon = WEATHER_ICONS.get(code, "🌡️")
    
    output = f"📍 {CITY_NAME}\n"
    output += f"{icon} {desc}\n"
    output += f"Temperature: {temp:.0f}°C\n"
    output += f"Feels Like: {feels:.0f}°C\n"
    output += f"💧 Humidity: {humidity}%\n"
    output += f"🌡️ Pressure: {pressure} hPa\n"
    output += f"🌬️ Wind: {wind_speed:.1f} km/h\n"
    
    # 5-Day Forecast
    if forecast:
        output += f"\n📅 5-Day Forecast:\n"
        
        # Process forecast into daily data
        daily = {}
        for item in forecast:
            dt = datetime.utcfromtimestamp(item['dt'])
            day_key = dt.strftime("%Y-%m-%d")
            
            if day_key not in daily:
                daily[day_key] = {
                    'date': dt.strftime("%a %d"),
                    'temp_min': item['main']['temp_min'],
                    'temp_max': item['main']['temp_max'],
                    'code': item['weather'][0]['id'],
                    'desc': item['weather'][0]['description'].title()
                }
            else:
                daily[day_key]['temp_min'] = min(daily[day_key]['temp_min'], item['main']['temp_min'])
                daily[day_key]['temp_max'] = max(daily[day_key]['temp_max'], item['main']['temp_max'])
        
        # Show first 5 days
        count = 0
        for day_key in sorted(daily.keys()):
            if count >= 5:
                break
            day = daily[day_key]
            icon = WEATHER_ICONS.get(day['code'], "🌡️")
            output += f"{day['date']} {icon} {day['temp_min']:.0f}°/{day['temp_max']:.0f}° {day['desc']}\n"
            count += 1
    
    output += f"\nLast updated: {datetime.now().strftime('%H:%M:%S')}"
    print(output)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--details":
        show_details()
    else:
        show_bar()
