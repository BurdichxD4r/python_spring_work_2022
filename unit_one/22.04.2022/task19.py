#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#  – id - номер по порядку (от 1 до 10);
#  – текст из списка algoritm

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

#  Каждое значение из списка должно находится на отдельной строке.


algoritm_csv = open('algoritm.csv', 'w')
id = 0
for string in algoritm:
    id += 1
    algoritm_csv.write(str(id) + ',' + str(string) + '\n')
algoritm_csv.close()