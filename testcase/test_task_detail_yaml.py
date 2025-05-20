import time
from io import StringIO

import allure
import pytest
import yaml

from common.ddt_utils import read_case_yaml
from common.request_utils import RequestUtils
from common.files_path import data_path
from common.yaml_utils import read_yaml, write_yaml
from datetime import datetime,timedelta
import datetime
from common.query_utils import QueryUtils
from hotloads.debug_talk import DebugTalk

"""测试数据路径"""
data_path0=data_path
data_path = data_path0 + 'task_detail.yaml'
data_path1 = data_path0 + 'task_create.yaml'


timeout = 180  # 3分钟（180秒）
interval = 5  # 每5秒查询一次

@allure.epic("任务明细查询")
@allure.feature("查询我的任务-查询中心任务-查询全部任务")
class Test1:
    pass

    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                                         'test_task_query_6'))
    # def test_task_query_6_1(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     caseinfo["request"]["json"]["authQueryParam1"] = 1
    #     caseinfo["request"]["json"]["taskName"] = ''
    #     caseinfo["request"]["json"]["taskTimeFrom"] = str(datetime.date.today())
    #     caseinfo["request"]["json"]["taskTimeTo"] =  str(datetime.date.today())
    #     QueryUtils().wait_until_total_positive(caseinfo)
    #
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                                         'test_task_query_6'))
    # def test_task_query_6_2(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     caseinfo["request"]["json"]["authQueryParam1"] = 2
    #     caseinfo["request"]["json"]["taskName"] = ''
    #     caseinfo["request"]["json"]["taskTimeFrom"] = str(datetime.date.today())
    #     caseinfo["request"]["json"]["taskTimeTo"] = str(datetime.date.today())
    #     QueryUtils().wait_until_total_positive(caseinfo)
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                                         'test_task_query_6'))
    # def test_task_query_6_3(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     caseinfo["request"]["json"]["authQueryParam1"] = 3
    #     caseinfo["request"]["json"]["taskName"] = ''
    #     caseinfo["request"]["json"]["taskTimeFrom"] = str(datetime.date.today())
    #     caseinfo["request"]["json"]["taskTimeTo"] = str(datetime.date.today())
    #     QueryUtils().wait_until_total_positive(caseinfo)

@allure.feature("任务定制发布任务-任务明细查询我的任务-查询任务详情-详情查看执行记录-重新执行-修改结束时间-手工确认")
@pytest.mark.parallel
class Test2:
    #任务定制
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_get_model'))
    def test_task_get_model(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_pre_save'))
    def test_task_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_save_xcpmodel'))
    def test_task_save_xcpmodel(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["xcpInfo"]["body"]["fieldList"] = DebugTalk().set_xcpmodel()
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_query_theme'))
    def test_task_query_theme(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_get_single_step'))
    def test_task_get_single_step(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_get_frequencyinfo'))
    def test_task_get_frequencyinfo(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_add'))
    def test_task_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["caseDefBody"] = DebugTalk().set_casebody(read_yaml('taskname'),
                                                                              read_yaml('stepcode'))
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_get_block'))
    def test_task_get_block(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["blockType"] = '02'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_saveblock'))
    def test_task_saveblock(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_check'))
    def test_task_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_acceptance'))
    def test_task_acceptance(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_get_casebody'))
    def test_task_get_casebody(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["url"] = "api/agnes-ac/v1/ac/case/def/case-body?caseDefId=" + read_yaml('casedefid')
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_query_theme_task'))
    def test_task_query_theme_task(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_publish'))
    def test_task_publish(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    #任务明细
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_6'))
    def test_task_query_6(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["authQueryParam1"] = 1
        caseinfo["request"]["json"]["taskTimeFrom"] = str(datetime.date.today())
        caseinfo["request"]["json"]["taskTimeTo"] = str(datetime.date.today())
        QueryUtils().wait_until_total_positive(caseinfo)

    time.sleep(30)
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_breif'))
    def test_task_get_breif(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["bizDate"] = str(datetime.date.today())
        RequestUtils().standard_yaml_case(caseinfo)

        breif=read_yaml('breif')
        breif=yaml.safe_load(StringIO(breif))
        write_yaml({"breiflist":breif})
        stepcode=read_yaml('breiflist')['caseSteps'][0]['stepCode']
        stepexecid=read_yaml('breiflist')['caseSteps'][0]['stepExecId']
        stepstatus=read_yaml('breiflist')['caseSteps'][0]['stepStatus']
        taskid=read_yaml('breiflist')['caseSteps'][0]['taskId']
        caseid=read_yaml('breiflist')['caseSteps'][0]['caseId']
        write_yaml({"stepcode":stepcode})
        write_yaml({"stepexecid":stepexecid})
        write_yaml({"stepstatus": stepstatus})
        write_yaml({"taskid": taskid})
        write_yaml({"caseid": caseid})


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_breif_execlog'))
    def test_task_get_breif_execlog(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_breif_exec'))
    def test_task_get_breif_exec(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_breif_edit_planendtime'))
    def test_task_get_breif_edit_planendtime(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["planEndTime"] = str(datetime.date.today())+" 23:59:00"
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_breif_commit'))
    def test_task_get_breif_commit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)
