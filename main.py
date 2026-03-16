import os
import subprocess
from pathlib import Path
from common.files_path import temps_path, allure_path

if __name__ == '__main__':
    # 定义两次运行的临时目录
    temp_parallel = os.path.join(temps_path, "parallel")
    temp_serial = os.path.join(temps_path, ""
                                           ""
                                           ""
                                           ""
                                           "")

    # 确保目录存在
    Path(temp_parallel).mkdir(parents=True, exist_ok=True)
    Path(temp_serial).mkdir(parents=True, exist_ok=True)

    # 并行执行标记parallel的测试（首次清理目录）
    subprocess.run([
        "pytest",
        "-v",
        "--alluredir", temp_parallel,
        "--clean-alluredir",
        "-m", "parallel",
        "-n", "auto",
        "--dist", "loadscope"
    ], check=False)

    # 执行未标记的测试（清理自己的目录）
    subprocess.run([
        "pytest",
        "-v",
        "--alluredir", temp_serial,
        "--clean-alluredir",
        "-m", "not parallel",
        "-p", "no:xdist"
    ], check=False)

    # 合并两次结果生成报告
    merge_cmd = f"allure generate {temp_parallel} {temp_serial} -o {allure_path} --clean"
    os.system(merge_cmd)