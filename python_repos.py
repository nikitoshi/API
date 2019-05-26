import requests

# Создание выхова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

# Сохоанение ответа в переменной.
response_dict = r.json()

# Обработка результатов.
print(response_dict.keys())
