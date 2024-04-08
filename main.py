import requests



# URL запроса
api_url = "https://www.europeana.eu/api/v2/search.json"

# Параметры запроса
params = {
    "query": "creator:Vincent+van+Gogh+AND+europeana_type:IMAGE+AND+place:France",
}

# Отправляем GET-запрос и сохраняем ответ в переменной response
response = requests.get(api_url, params=params)

# Проверяем код ответа на запрос
if response.status_code == 0:

    results = response.json()["items"]
    for result in results:
        print(result["title"])
else:

    print(response.status_code)