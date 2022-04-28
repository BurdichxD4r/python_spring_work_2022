#todo: Создайте объект сериализации любым методом для соседа, запишите его в файл,
# педайте его ему для считывания. Соседу необходимо десириализовать полученый объект.


#todo: Заданы два списка. Необходимо их сериализовать в один файл.
import pickle
import json
import yaml
from yaml import SafeLoader

list_one = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
list_two = [False, 'Sparse is better than dense.', {'age': 90}]
list_all = [list_one, list_two]

with open('task1.pkl', 'wb') as task1_pkl:
    pickle.dump(list_all, task1_pkl, pickle.HIGHEST_PROTOCOL)
task1_pkl.close()
with open('task1.pkl', 'rb') as task1_pkl:
    task1 = pickle.load(task1_pkl)
task1_pkl.close()
for list_namber in task1:
    print(list_namber)

with open('task1.json', 'wt') as task1_json:
    json.dump(list_all, task1_json)
task1_json.close()
with open('task1.json', 'rt') as task1_json:
    task1 = json.load(task1_json)
task1_json.close()
for list_namber in task1:
    print(list_namber)


with open('task1.yaml', 'wt') as task1_yaml:
    yaml.dump(list_all, task1_yaml)
task1_yaml.close()
with open('task1.yaml', 'rt') as task1_yaml:
    task1 = yaml.load(task1_yaml, Loader=SafeLoader)
task1_yaml.close()
for list_namber in task1:
    print(list_namber)