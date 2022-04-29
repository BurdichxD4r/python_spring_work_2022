import pickle
import json
import yaml
def to_pickle(file, object):
    with open(file, 'wb') as f:
        pickle.dump(object, f, pickle.HIGHEST_PROTOCOL)
    f.close()
def to_json(file, object):
    with open(file, 'wt') as f:
        json.dump(object, f)
    f.close()
def to_yaml(object):
    file = input('Введите название файла: ')
    with open(file + '.yaml', 'wt') as f:
        yaml.dump(object, f)
    f.close()