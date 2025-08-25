import requests
import streamlit as st

# 🔑 OpenWeatherMap API Key
API_KEY = "b0d034eb892dae9982a38d162361361f"

# 🌍 Global Weather Stations
stations = {
    "North America": [{"name": "New York, USA", "lat": 40.7128, "lon": -74.0060}],
    "Europe": [{"name": "Berlin, Germany", "lat": 52.5200, "lon": 13.4050}],
    "Asia": [{"name": "Tokyo, Japan", "lat": 35.6895, "lon": 139.6917}],
    "Australia & Oceania": [{"name": "Sydney, Australia", "lat": -33.8688, "lon": 151.2093}],
    "South America": [{"name": "São Paulo, Brazil", "lat": -23.5505, "lon": -46.6333}],
    "Africa": [{"name": "Nairobi, Kenya", "lat": -1.2921, "lon": 36.8219}],
    "Northern Europe": [{"name": "Oslo, Norway", "lat": 59.9139, "lon": 10.7522}],
    "Middle East": [{"name": "Dubai, UAE", "lat": 25.276987, "lon": 55.296249}]
}

# 🔄 Fetch Weather Data
def fetch_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"].title(),
            "wind_speed": data["wind"]["speed"],
            "pressure": data["main"]["pressure"],
            "visibility": data.get("visibility", 0) / 1000
        }
    except Exception as e:
        return {"error": str(e)}

# 📊 Streamlit Dashboard
def display_weather_dashboard():
    st.set_page_config(page_title="Global Weather Dashboard", page_icon="🌐", layout="wide")
    st.title("🌐 Global Weather Station Dashboard")
    st.caption("Live weather data from representative cities across major regions")

    for region, locations in stations.items():
        with st.expander(f"📍 {region}", expanded=True):
            for loc in locations:
                weather = fetch_weather(loc["lat"], loc["lon"])
                if "error" in weather:
                    st.error(f"{loc['name']}: ❌ {weather['error']}")
                else:
                    st.subheader(f"📌 {loc['name']}")
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("🌡️ Temp (°C)", f"{weather['temperature']}")
                    col2.metric("💧 Humidity (%)", f"{weather['humidity']}")
                    col3.metric("🌬️ Wind (m/s)", f"{weather['wind_speed']}")
                    col4.metric("🔎 Visibility (km)", f"{weather['visibility']}")
                    st.write(f"**Condition:** {weather['condition']}")
                    st.write(f"**Pressure:** {weather['pressure']} hPa")
                    st.markdown("---")

# 🚀 Run Dashboard
if __name__ == "__main__":
    display_weather_dashboard()
