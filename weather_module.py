<<<<<<< HEAD
import requests
import logging

# Optional: Set up logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace with your actual OpenWeatherMap API key
API_KEY = "your_openweathermap_api_key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(lat: float, lon: float, units: str = "metric") -> dict:
    """
    Fetches current weather data for a given latitude and longitude.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        units (str): Units of measurement. 'metric' or 'imperial'.

    Returns:
        dict: Parsed weather data or error message.
    """
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": units
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        weather_info = {
            "location": f"{data.get('name')}, {data['sys'].get('country')}",
            "temperature": data["main"].get("temp"),
            "humidity": data["main"].get("humidity"),
            "pressure": data["main"].get("pressure"),
            "weather": data["weather"][0].get("description"),
            "icon": data["weather"][0].get("icon"),
            "wind_speed": data["wind"].get("speed")
        }

        logger.info(f"Weather fetched for {lat}, {lon}: {weather_info}")
        return weather_info

    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        return {"error": f"Failed to fetch weather data: {str(e)}"}

    except (KeyError, TypeError) as e:
        logger.error(f"Parsing error: {e}")
        return {"error": f"Unexpected response format: {str(e)}"}
=======
import requests
import logging

# Optional: Set up logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace with your actual OpenWeatherMap API key
API_KEY = "your_openweathermap_api_key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(lat: float, lon: float, units: str = "metric") -> dict:
    """
    Fetches current weather data for a given latitude and longitude.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        units (str): Units of measurement. 'metric' or 'imperial'.

    Returns:
        dict: Parsed weather data or error message.
    """
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": units
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        weather_info = {
            "location": f"{data.get('name')}, {data['sys'].get('country')}",
            "temperature": data["main"].get("temp"),
            "humidity": data["main"].get("humidity"),
            "pressure": data["main"].get("pressure"),
            "weather": data["weather"][0].get("description"),
            "icon": data["weather"][0].get("icon"),
            "wind_speed": data["wind"].get("speed")
        }

        logger.info(f"Weather fetched for {lat}, {lon}: {weather_info}")
        return weather_info

    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        return {"error": f"Failed to fetch weather data: {str(e)}"}

    except (KeyError, TypeError) as e:
        logger.error(f"Parsing error: {e}")
        return {"error": f"Unexpected response format: {str(e)}"}
>>>>>>> 2b8aff5549bdbc9daa821b8e613b52d0b7149112
