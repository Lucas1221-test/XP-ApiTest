import yaml,os
import random,time
import datetime
from datetime import datetime

def read_yml(yml_path):
    f=open(yml_path,'r',encoding='utf-8')
    readf=f.read()
    d=yaml.safe_load(readf)
    f.close()
    return d

#获取当前时间y-m-d h:m:s
def get_current_time():
    # 获取当前时间的时间戳
    timestamp = time.time()
    # 将时间戳转换为本地时间
    local_time = time.localtime(timestamp)
    # 将本地时间转换为易读的字符串形式
    readable_time = time.asctime(local_time)
    # 格式化当前时间
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
    return formatted_time

def get_timestamp(time):
    # 获取当前时间
    now = datetime.datetime.now()
    time=datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    # 转换为时间戳
    timestamp = round(time.mktime(now.timetuple()))
    return timestamp

if __name__=='__main__':
    current_path=os.path.dirname(os.path.realpath(__file__))
    ymlp=os.path.join(os.path.dirname(current_path),'data','environments.yaml')
    r=read_yml(ymlp)
    s=r['environments']['active']['base_url']
    print(s)
