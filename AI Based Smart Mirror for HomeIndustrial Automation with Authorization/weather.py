import requests
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "cityName"
API_KEY = "your API key"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(URL)
def temp(temp):
   temper=temp-273.15
   return temper
#if response.status_code == 200:
data = response.json()
#print(data)
main = data['main']
temper = main['temp']
temperature=temp(temper)
humidity = main['humidity']
pressure = main['pressure']
wind=data['wind']['speed']
report = data['weather']
#print(f"{CITY}")
T=(f"Temperature in {CITY}: {temperature:.2f}°C")
H=(f"Humidity in {CITY}: {humidity}%")
P=(f"Pressure in {CITY}: {pressure}")
w_s=(f"Wind_Speed in {CITY}: {wind}m/s")
W=(f"Weather in {CITY}: {report[0]['description']}")
# else:
#print(T)
#    print("Error in the HTTP request")