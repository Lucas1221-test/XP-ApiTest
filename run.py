
import os
import time
import pytest

from common.files_path import temps_path, allure_path

if __name__ == '__main__':
    # pytest.main(["-vs", "-m", "smoke", '--alluredir', temps_path])
    pytest.main(["-vs",'./testcase/test_task_detail_yaml.py','--alluredir', temps_path])
    #pytest.main(["-vs",'./testcase/test_task_create_yaml.py', './testcase/test_task_center_yaml.py','./testcase/test_task_approval_yaml.py','--alluredir', temps_path])
    time.sleep(3)
    split = ' allure ' + ' generate ' + temps_path + ' -o ' + allure_path + ' --clean'
    os.system(split)
    # os.system("allure open ./report")
