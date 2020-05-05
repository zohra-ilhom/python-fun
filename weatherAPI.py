import requests
import pprint

# creating a dictionary of language abbreviations that the api call requires 

language_list = {
    'english': "en",
    'russian': "ru",
    'turkish': "tr",
    'farsi': "fa",
}
select_lang = input("Select language. Type one of the follwoing options IN LOWER CASE: english, russian, turkish and farsi >>>  ").lower()
select_lang = str(select_lang)

select_city = input("tell me which city you want to know today's weather for >>> ")
select_city = str(select_city)

print("\n")

#creating some logic for when the users language entry matches one of the supported languages that we defined in the dictionary above to append the abbreviation in the API url end point 

for languages in language_list:
    if select_lang == languages:
        lang = language_list[select_lang]
        lang = str(lang)
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + select_city + '&appid=fefc84eb710a1684994faf664dcfe26f&lang=' + lang

r = requests.get(url)
response = r.json()

# we want to print out the city name in the selected langauge, description. temp, feels like temp, max and min temp

print('City name: ' + (response['name']))
print('Actual tempreture: ' + str(response['main']['temp']))
print('Tempreture feels like: ' + str(response['main']['feels_like']))
print('Min tempreture: ' + str(response['main']['temp_min']))
print('Max tempreture: ' + str(response['main']['temp_max']))

print('tada')
