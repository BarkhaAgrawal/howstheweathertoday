# Download libraries for the projects
import requests
import json

def get_weather_data(city):
    api_key = 'yourAPIKey'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        raise Exception("Error fetching weather data from OpenWeatherMap API")

#Function to parse weather data and return required fields
def parse_weather_data(weather_data):
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    return temperature, description

#Function to handle user input
def get_city_name():
    city_name = input("Enter the name of city to get weather information: ")
    if not city_name.isalpha():
        raise ValueError("Invalid city name entered. City name should contain only alphabets")
    return city_name

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        city = get_city_name()
        weather_data = get_weather_data(city)
        temperature, description = parse_weather_data(weather_data)
        print(
            "Temperature in " + city + " is " + str(temperature) + " degree Celsius and the weather is " + description)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)