from requests.models import Response
import code
import requests

#Коды
#2xx - все ок
#4xx - Чото не так с юзером
#5xx - Чото не так с сервером
def get_github_user(username: str) -> None:   
    response = requests.get(f"https://api.github.com/users/{username}") 
    payload = response.json()

    if (response.status_code) == 404:  
        print ("Пользователь не найден")
        return

    if 400 <= (response.status_code) <= 499:
        raise ConnectionError(response.status_code)

    print(f"Имя: {payload["name"]}")
    print(f"Репозиториев: {payload["public_repos"]}")
    print(f"Подписчиков:{payload["followers"]}")
    print(f"Локация: {response.json()["location"] or "Не указана"}")
    print(f"Профиль: {payload["html_url"]}")


def get_pokemon(name: str) -> None:
    poke = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}") 
    payload = poke.json()

    if (poke.status_code) == 404:  
        print ("Покемон не найден")
        return

    if 400 <= (poke.status_code) <= 499:
        raise ConnectionError (poke.status_code)

    print(f"Покемон: {payload["name"].capitalize()}")
    print(f"Рост: {payload["height"]}")
    print(f"Вес: {payload["weight"]}")

    types = []
    for pokemon_type in payload["types"]:            
        types.append(pokemon_type["type"]["name"])
    print(f"Типы: {'/'.join(types)}")

    abilities = []
    for pokemons_abilities in payload["abilities"]:
        abilities.append(pokemons_abilities["ability"]["name"])
    print(f"Способности: {', '.join(abilities)}") 


def get_country(name: str) -> None:
    counrty = requests.get(f"https://restcountries.com/v3.1/name/{name}") 

    if (counrty.status_code) == 404:  
        print ("Страна не найдена")
        return

    if 400 <= (counrty.status_code) <= 499:
        raise ConnectionError (counrty.status_code)

    payload = counrty.json()[0]

    print(f"Страна: {payload["name"]["common"].capitalize()}")
    print(f"Столица: {payload["capital"]}")
    print(f"Население: {payload['population']:,}")
    print(f"Регион: {payload["region"]}")

    counrty_currencies = []
    for code, currency_info in payload.get("currencies", {}).items():       
        name = currency_info.get("name")
        symbol = currency_info.get("symbol", "")
        counrty_currencies.append(f"{name} ({symbol})")
    
    print(f"Валюта: {' / '.join(counrty_currencies)}")


def get_weather(city: str, api_key: str) -> None:
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru") 
    payload = response.json()

    print(f"Погода в {payload["name"]}")
    print(f"Температура: {payload["main"]["temp"]}°C,", f"ощущается как {payload["main"]["feels_like"]}°C")
    print(f"Влажность: {payload["main"]["humidity"]}%")
    print(f"Ветер: {payload["wind"]["speed"]} м/с")
    print(f"Описание: {payload["weather"][0]["description"]}")

get_weather("bishkek", "15a9c68e8d46ff45e299418027744474")






# get_github_user("Barnacle322")
# print ("------------------------------------------------------")   
# get_github_user("Nagiev")
# print ("------------------------------------------------------")   
# get_pokemon("charizard")
# print ("------------------------------------------------------")   
# get_pokemon("Nagiev")
# print ("------------------------------------------------------")  
get_country("kyrgyzstan")
print ("------------------------------------------------------")  
get_country("Nagiev")
print ("------------------------------------------------------") 
get_weather("bishkek", "15a9c68e8d46ff45e299418027744474")