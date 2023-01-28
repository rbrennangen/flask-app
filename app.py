from flask import Flask, request, abort
import requests

app = Flask(__name__)

API_Key = "aa78d8dcce1009d15624839f84b4dce9"

url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_Key}"


@app.route('/weather', methods=['GET'])
def weather():
    locale = request.args.get('locale')
    response = requests.get(url + "&q=" + locale + "&units=metric")
    res = response.json()

    app.logger.info(res)

    # Checking if the city is found
    if res["cod"] != "404" or res["cod"] != "400" or res["cod"] != "500":
        data = res["main"]

        # Storing the live temperature data
        live_temperature = data["temp"]

        # Storing the live pressure data
        live_pressure = data["pressure"]

        # Storing the humidity
        live_humidity = data["humidity"]

        # Storing the weather description
        desc = res["weather"]
        weather_description = desc[0]["description"]

        return {
            "name": res['name'],
            "temp": live_temperature,
            "pressure": live_pressure,
            "humidity": live_humidity,
            "desc": weather_description
        }

    abort(500, 'Some error...')
