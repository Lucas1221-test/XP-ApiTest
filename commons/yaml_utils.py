

import yaml

from commons.files_path import extract_path, token_path


#读
def read_yaml(key):
    with open(extract_path, encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


#写
def write_yaml(data):
    with open(extract_path, encoding='utf-8', mode='a') as f:
        yaml.dump(data, stream=f, allow_unicode=True)



#清空
def clear_yaml():
    with open(extract_path, encoding='utf-8', mode='w') as f:
        f.truncate()

#清空
def clear_token_yaml():
    with open(token_path, encoding='utf-8', mode='w') as f:
        f.truncate()

