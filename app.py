<<<<<<< HEAD
from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)
API_KEY = "b0d034eb892dae9982a38d162361361f"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "lat": data["coord"]["lat"],
                "lon": data["coord"]["lon"],
                "description": data["weather"][0]["description"].title(),
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind_speed": data["wind"]["speed"],
                "visibility": data.get("visibility", 0) / 1000,  # Convert to km
                "icon": data["weather"][0]["icon"],
                "updated": datetime.utcfromtimestamp(data["dt"]).strftime('%Y-%m-%d %H:%M UTC')
            }
        else:
            weather_data = {"error": "City not found or API error."}
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)
API_KEY = "b0d034eb892dae9982a38d162361361f"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "lat": data["coord"]["lat"],
                "lon": data["coord"]["lon"],
                "description": data["weather"][0]["description"].title(),
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind_speed": data["wind"]["speed"],
                "visibility": data.get("visibility", 0) / 1000,  # Convert to km
                "icon": data["weather"][0]["icon"],
                "updated": datetime.utcfromtimestamp(data["dt"]).strftime('%Y-%m-%d %H:%M UTC')
            }
        else:
            weather_data = {"error": "City not found or API error."}
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 2b8aff5549bdbc9daa821b8e613b52d0b7149112
