import requests

API_KEY = 'PgEf8hGaSPHXDdhZOGx1fM6DgwA1HhiA'

class WeatherModel:
    def __init__(self, api_key):
        self.API_KEY = api_key

    def get_location_key(self, city):
        url_location = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={self.API_KEY}&q={city}"
        response = requests.get(url_location)
        location_key = response.json()[0]['Key']
        return location_key

    def get_weather_data(self, location_key):
        url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={self.API_KEY}&details=true"
        response = requests.get(url)
        data = response.json()
        weather = {}
        weather['precipitation_probability']= data[0]['PrecipitationProbability']
        weather['temperature'] = data[0]['Temperature']['Metric']['Value']
        weather['humidity'] = data[0]['RelativeHumidity']
        weather['wind'] = data[0]['Wind']['Speed']['Metric']['Value']
        return weather

    def weather_model(self, weather):
        switcher = {
            'precipitations': weather['precipitation_probability'] > 0.5,
            'too hot': weather['temperature'] > 30,
            'too cold': weather['temperature'] < -10,
            'humidity': weather['humidity'] > 80,
            'wind' : weather['wind'] > 55,
        }
        if switcher['precipitations'] or switcher['too hot'] or switcher['too cold'] or switcher['humidity'] or switcher['wind']:
            return False  #True значит, что погода хорошая, False, что плохая
        else:
            return True

    def get_prediction(self, location_from, location_to):
        location_key_from = self.get_location_key(location_from)
        location_key_to = self.get_location_key(location_to)
        weather_from = self.get_weather_data(location_key_from)
        weather_to = self.get_weather_data(location_key_to)
        prediction_from = self.get_prediction(weather_from)
        prediction_to = self.get_prediction(weather_to)
        if prediction_from and prediction_to :
            return True #True значит, что погода хорошая, False, что плохая
        else:
            return False












