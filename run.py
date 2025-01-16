
import os
import time
import pytest

from common.files_path import temps_path, allure_path

if __name__ == '__main__':
    # pytest.main(["-vs", "-m", "smoke", '--alluredir', temps_path])
    pytest.main(["-vs",'./aaa.py','--alluredir', temps_path])
    time.sleep(3)
    split = ' allure ' + ' generate ' + temps_path + ' -o ' + allure_path + ' --clean'
    os.system(split)
    # os.system("allure open ./report")
