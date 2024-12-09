import subprocess
import os

# if __name__=='__main__':
#     case_path=os.path.join(os.path.dirname(os.path.realpath(__file__)),"testcase/")
#     p=subprocess.Popen("pytest",cwd=case_path)
#     p.wait()
import os
import time
import pytest

from common.files_path import temps_path, allure_path

if __name__ == '__main__':
    # pytest.main(["-vs", "-m", "smoke", '--alluredir', temps_path])
    pytest.main(["-vs", '--alluredir', temps_path])
    time.sleep(3)
    split = ' allure ' + ' generate ' + temps_path + ' -o ' + allure_path + ' --clean'
    os.system(split)
    # os.system("allure open ./report")
