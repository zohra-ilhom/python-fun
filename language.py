language_list = {
    'english': "en",
    'russian': "ru",
    'turkish': "tr",
    'farsi': "fa",
}

select_lang = input("Select a language. Type one of the follwoing: english, russian, turkish and farsi >>>  ")
select_lang = str(select_lang)

select_city = input("tell me which city you want to know the weather for >>> ")
select_city = str(select_city)


print("\n")

for items in language_list:

    if select_lang == items:
        lang = language_list[select_lang]
        lang = str(lang)
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + select_city + '&appid=fefc84eb710a1684994faf664dcfe26f&lang=' + lang
        print(url)
    
