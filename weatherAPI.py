import requests
import pprint

# creating a dictionary of language abbreviations that the api call requires 
language_list = {
    'english': "en",
    'russian': "ru",
    'turkish': "tr",
    'farsi': "fa",
}

select_lang = input("Select language. Type one of the follwoing options IN LOWER CASE: english, russian, turkish and farsi >>>  ")
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

# we want to print out the city name in the selected langauge, description. temp, feels like temp, max and min temp
print('City name')
pprint.pprint(r.json()['name'])
print('Actual tempreture')
print(r.json()['main']['temp'])
print('Tempreture feels like')
print(r.json()['main']['feels_like'])
print('Min tempreture')
print(r.json()['main']['temp_min'])
print('Max tempreture')
print(r.json()['main']['temp_max'])



