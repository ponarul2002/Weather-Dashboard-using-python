<<<<<<< HEAD
import streamlit as st
import requests

# 🔑 OpenWeatherMap API Key
API_KEY = "b0d034eb892dae9982a38d162361361f"

# 🌦️ Function to fetch weather by city name
def get_weather(city: str, api_key: str) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# 🖥️ Streamlit UI
st.set_page_config(page_title="City Weather", page_icon="🌤️")
st.title("🌍 City Weather Dashboard")
st.caption("Enter any city name to get live weather data")

city = st.text_input("Enter city name", "Chennai")

if city:
    data = get_weather(city, API_KEY)
    if "error" in data:
        st.error(f"❌ Error: {data['error']}")
    else:
        st.subheader(f"📍 Weather in {data['name']}")
        st.metric("🌡️ Temperature (°C)", data["main"]["temp"])
        st.metric("💧 Humidity (%)", data["main"]["humidity"])
        st.metric("🌬️ Wind Speed (m/s)", data["wind"]["speed"])
        st.write(f"**Condition:** {data['weather'][0]['description'].title()}")
        st.write(f"**Pressure:** {data['main']['pressure']} hPa")
        st.write(f"**Visibility:** {data.get('visibility', 0)/1000} km")
=======
import streamlit as st
import requests

# 🔑 OpenWeatherMap API Key
API_KEY = "b0d034eb892dae9982a38d162361361f"

# 🌦️ Function to fetch weather by city name
def get_weather(city: str, api_key: str) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# 🖥️ Streamlit UI
st.set_page_config(page_title="City Weather", page_icon="🌤️")
st.title("🌍 City Weather Dashboard")
st.caption("Enter any city name to get live weather data")

city = st.text_input("Enter city name", "Chennai")

if city:
    data = get_weather(city, API_KEY)
    if "error" in data:
        st.error(f"❌ Error: {data['error']}")
    else:
        st.subheader(f"📍 Weather in {data['name']}")
        st.metric("🌡️ Temperature (°C)", data["main"]["temp"])
        st.metric("💧 Humidity (%)", data["main"]["humidity"])
        st.metric("🌬️ Wind Speed (m/s)", data["wind"]["speed"])
        st.write(f"**Condition:** {data['weather'][0]['description'].title()}")
        st.write(f"**Pressure:** {data['main']['pressure']} hPa")
        st.write(f"**Visibility:** {data.get('visibility', 0)/1000} km")
>>>>>>> 2b8aff5549bdbc9daa821b8e613b52d0b7149112
