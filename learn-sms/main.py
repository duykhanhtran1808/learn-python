import requests
from twilio.rest import Client

api_key = "" #removed

my_lat = 21.007456
my_long = 105.841464

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}
# SMS
account_sid = '' #removed
auth_token = '' #removed



response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data['hourly'][0]['weather'][0]['id'])
weather_slice = weather_data['hourly'][:12]
# weather_12_hours_status = [hour['weather'][0]['id'] for hour in weather_slice]
# print(weather_12_hours_status)

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
        break


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain. From Duy Khanh",
        from_='',#removed
        to=''
    )
    print(message.status)
