import pickle
import json
import yaml
from yaml import SafeLoader
def from_pickle(file):
    with open(file, 'rb') as f:
        object = pickle.load(f)
    return object
def from_json(file):
    with open(file, 'rt') as f:
        object = json.load(f)
    return object
def from_yaml():
    file = input('Введите название файла: ')
    with open(file + '.yaml', 'rt') as f:
        object = yaml.load(f, Loader=SafeLoader)
    return object