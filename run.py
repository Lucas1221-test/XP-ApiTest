import subprocess
import os

if __name__=='__main__':
    case_path=os.path.join(os.path.dirname(os.path.realpath(__file__)),"testcase/")
    p=subprocess.Popen("pytest",cwd=case_path)
    p.wait()
