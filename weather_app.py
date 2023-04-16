import json
import requests

lang = input("Press 1 to select Turkish ")
if lang == "1":
    lang = "tr"
else:
    lang = "en"

while True:
    if lang == "tr:":
        city_name = input("Çıkmak için 0'a basın\nŞehir: ")
    else:
        city_name = input("Press 0 to exit\nCity: ")

    if city_name == "0":
        break

    api_key = "d96ad5992cbd2cd19bc75d904ec0b60a"
    api_call = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang={}&units=metric".format(city_name,api_key,lang)
    result = requests.get(api_call)
    result = result.json()

    if result['cod'] == 200:
        my_weather_description = result["weather"][0]["description"]
        my_temperature = result["main"]["temp"]
        my_feels_like = result["main"]["feels_like"]
        my_min_temp = result["main"]["temp_min"]
        my_max_temp = result["main"]["temp_max"]
        my_humidity = result["main"]["humidity"]

        if lang != "tr":
            print("City:{}\nDesciptpon: {}\nTemperature: {}°\nFeels like: {}°\nMinimum Temp: {}°\nMaximum Temp: {}°\nHumidity: {}".format(city_name.capitalize(),my_weather_description.title(),my_temperature,my_feels_like, my_min_temp,my_max_temp,my_humidity))
        else:
            print(
                "Şehir:{}\nDurum: {}\nSıcaklık: {}°\nHissedilen Sıcaklık: {}°\nEn düşük sıcaklık: {}°\nEn yüksek sıcaklık: {}°\nNem: {}".format(city_name.capitalize(), my_weather_description.title(), my_temperature, my_feels_like, my_min_temp,my_max_temp, my_humidity))

    else:
        if lang != "tr":
            print("{} not found".format(city_name))
        else:
            print("{} isminde şehir bulunamadı".format(city_name))
