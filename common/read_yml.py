import yaml,os

def read_yml(yml_path):
    f=open(yml_path,'r',encoding='utf-8')
    readf=f.read()
    d=yaml.safe_load(readf)
    f.close()
    return d

#host_url=yaml.load(open('/test_data/host.yml','r',encoding='utf-8'),Loader=yaml.FullLoader)
#excel_file=ExcelUtil('/test_data/dropweb/'+host_url['excel']['excel_name'])




if __name__=='__main__':
    current_path=os.path.dirname(os.path.realpath(__file__))
    ymlp=os.path.join(os.path.dirname(current_path),'data','file_yml.yaml')
    r=read_yml(ymlp)
    print(r)
