import http.client
conn = http.client.HTTPConnection("www.cbr.ru")
conn.request("GET", "/")
# Получить ответ сервера
response = conn.getresponse()
# Получить заголовки сервера
headers = response.getheaders()

print(response.status, response.reason)

data = list((response.read().decode('UTF-8')).split('\n'))

for i in range(len(data)):
    if "Ключевая ставка" in data[i]:
        print('Ключевая ставка:', data[i + 2][9:21], data[i + 4][38:44])

conn.close()


from yadisk import *
connection_yandex = YaDisk(token='d25c1991-5493-49c4-8545-36ec7df55182 ')


# conn2 = http.client.HTTPConnection('www.api-developer.tech.yandex.net')
# conn2.request("GET", "https://api.weather.yandex.ru/v2/informers?lat=55.75396&lon=37.620393\nX-Yandex-API-Key: d25c1991-5493-49c4-8545-36ec7df55182",)
# response2 = conn2.getresponse()
# headers2 = response2.getheaders()
# print(response2.status, response2.reason)
# data2 = response2.read().decode('UTF-8')
# with open("weather_yandex_ru.json", 'w', encoding='UTF-8') as file2:
#     file2.write(data)
# conn.close()