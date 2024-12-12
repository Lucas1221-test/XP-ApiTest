import allure
import pytest

from common.ddt_utils import read_case_yaml
from common.request_utils import RequestUtils
from common.files_path import data_path
from common.yaml_utils import read_yaml, write_yaml

"""测试数据路径"""
data_path = data_path + 'task_approval.yaml'

@allure.epic("审批中心")
@allure.feature("查询任务-催办-通过")
class Test1:

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_approval_list'))
    def test_task_approval_list1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["pageType"] = '1'
        RequestUtils().standard_yaml_case(caseinfo)

        list1 = read_yaml('approvallist')
        dict1 = list1[0]

        write_yaml({"applydata": dict1['applyData']})
        write_yaml({"applydate": dict1['applyDate']})
        write_yaml({"applyusername": dict1['applyUsername']})
        write_yaml({"approvalusername": dict1['approvalUsername']})
        write_yaml({"isagency": dict1['isAgency']})
        write_yaml({"reason": dict1['reason']})
        write_yaml({"status": dict1['status']})
        write_yaml({"summary": dict1['summary']})
        write_yaml({"type": dict1['type']})
        write_yaml({"urgenum ": dict1['urgeNum']})
        write_yaml({"idd": dict1['id']})

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_approval_list'))
    def test_task_approval_list2(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["pageType"] = '2'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_approval_urge'))
    def test_task_approval_urge(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_approval_pass'))
    def test_task_approval_pass(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

@allure.feature("查询任务-拒绝")
class Test2:
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_approval_list'))
    def test_task_approval_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["pageType"] = '1'
        RequestUtils().standard_yaml_case(caseinfo)

        list1 = read_yaml('approvallist')
        dict1 = list1[0]

        write_yaml({"applydata": dict1['applyData']})
        write_yaml({"applydate": dict1['applyDate']})
        write_yaml({"applyusername": dict1['applyUsername']})
        write_yaml({"approvalusername": dict1['approvalUsername']})
        write_yaml({"isagency": dict1['isAgency']})
        write_yaml({"reason": dict1['reason']})
        write_yaml({"status": dict1['status']})
        write_yaml({"summary": dict1['summary']})
        write_yaml({"type": dict1['type']})
        write_yaml({"urgenum ": dict1['urgeNum']})
        write_yaml({"idd": dict1['id']})

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_approval_refuse'))
    def test_task_approval_refuse(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)