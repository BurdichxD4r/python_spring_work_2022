import http.client
conn = http.client.HTTPConnection("www.cbr.ru")
conn.request("GET", "/")
# Получить ответ сервера
response = conn.getresponse()
# Получить заголовки сервера
headers = response.getheaders()

print(response.status, response.reason)

data = response.read().decode('UTF-8')

with open("cbr_ru.json", 'w', encoding='UTF-8') as file:
    file.write(data)

with open("cbr_ru.json", 'r', encoding='UTF-8') as file:
    key = file.readlines()
    for i in range(len(key)):
        if "Ключевая ставка" in key[i]:
            print('Ключевая ставка:', key[i + 4][9:21], key[i + 8][38:44])

conn.close()

conn2 = http.client.HTTPConnection('www.api.weather.yandex.ru')
conn2.request("GET", "https://api.weather.yandex.ru/v2/informers?lat=55.75396&lon=37.620393\nX-Yandex-API-Key: 3fc...7",)
response2 = conn2.getresponse()
headers2 = response2.getheaders()
print(response2.status, response2.reason)
data2 = response2.read().decode('UTF-8')
with open("weather_yandex_ru.json", 'w', encoding='UTF-8') as file2:
    file2.write(data)
conn.close()