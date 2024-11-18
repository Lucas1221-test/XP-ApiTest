import yaml,os

def read_yml(yml_path):
    f=open(yml_path,'r',encoding='utf-8')
    readf=f.read()
    d=yaml.safe_load(readf)
    f.close()
    return d

def get_login_data():
    current_path = os.path.dirname(os.path.realpath(__file__))
    ymlpath = os.path.join(os.path.dirname(current_path), 'data', 'login_data.yaml')
    with open(ymlpath, 'r') as stream:
        return yaml.safe_load(stream)['tests']


if __name__=='__main__':
    current_path=os.path.dirname(os.path.realpath(__file__))
    ymlp=os.path.join(os.path.dirname(current_path),'data','environments.yaml')
    ymlp2 = os.path.join(os.path.dirname(current_path), 'data', 'login_data.yaml')
    r=read_yml(ymlp)
    s=r['environments']['active']['base_url']
    print(s)
