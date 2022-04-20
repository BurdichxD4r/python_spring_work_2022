#todo: Создайте функцию compute_bill, считывающая итоговую сумму товаров в чеке.
# Функция должна принимать 1 параметр - словарь, в котором указано количество единиц товара.
# Цены хранятся в словаре:
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

def new_buy(buy):
  buy.append(input('Введите какой товар и в каком количестве Вы хотите приобрести (banana 4): ').split())
  while buy[-1] != ['stop']:
    buy.append(input('Введите какой товар и в каком количестве Вы хотите приобрести (banana 4),'
                     'чтобы завершить напишите stop: ').split())
  buy.remove(['stop'])
  buy = tuple(buy)
  return buy
buy_1 = []
new_buy(buy_1)
total = []
total_price = 0
def compute_bill(buy):
  for product in buy:
    total.append(int(prices.get(product[0])) * int(product[1]))
compute_bill(buy_1)
for i in total:
  total_price += int(i)
print(total_price)

