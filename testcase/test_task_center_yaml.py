import time

import allure
import pytest

from common.ddt_utils import read_case_yaml
from common.query_utils import QueryUtils
from common.request_utils import RequestUtils
from common.files_path import data_path
from common.yaml_utils import read_yaml, write_yaml
from datetime import datetime,timedelta
import datetime

from hotloads.debug_talk import DebugTalk


timeout = 180  # 3分钟（180秒）
interval = 5  # 每5秒查询一次

"""测试数据路径"""
data_path0=data_path
data_path = data_path0 + 'task_center.yaml'
data_path1 = data_path0 + 'task_approval.yaml'
data_path2 = data_path0 + 'task_create.yaml'

@allure.epic("任务中心")
@allure.feature("查询今日必办-置顶-取消置顶-查询超时任务-查询今日异常-查询可提前办-查询我的分布-查询仅待办-查询仅转交-查询仅协作")
@pytest.mark.parallel
class Test1:
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_1'))
    def test_task_query_1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_topping'))
    def test_task_topping(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_cancelTopping'))
    def test_task_cancelTopping(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_2'))
    def test_task_query_2(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_3'))
    def test_task_query_3(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_4'))
    def test_task_query_4(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_5'))
    def test_task_query_5(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_task'))
    def test_task_query_task1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["taskCls"] = '01'
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today())
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today())
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_task'))
    def test_task_query_task2(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["taskCls"] = '02'
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today())
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today())
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_task'))
    def test_task_query_task3(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["taskCls"] = '03'
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today())
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today())
        RequestUtils().standard_yaml_case(caseinfo)

@allure.feature("新增单节点岗位任务-绑定积木-审核-验收-发布-转办-拒绝")
@pytest.mark.parallel
class Test2:
    #任务定制
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_model'))
    def test_task_get_model(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_pre_save'))
    def test_task_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_save_xcpmodel'))
    def test_task_save_xcpmodel(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["xcpInfo"]["body"]["fieldList"] = DebugTalk().set_xcpmodel()
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_query_theme'))
    def test_task_query_theme(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_single_step'))
    def test_task_get_single_step(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_frequencyinfo'))
    def test_task_get_frequencyinfo(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_add'))
    def test_task_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["caseDefBody"] = DebugTalk().set_casebody(read_yaml('taskname'),
                                                                              read_yaml('stepcode'))
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_block'))
    def test_task_get_block(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["blockType"] = '01'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_saveblock'))
    def test_task_saveblock(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_check'))
    def test_task_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_acceptance'))
    def test_task_acceptance(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_casebody'))
    def test_task_get_casebody(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["url"] = "api/agnes-ac/v1/ac/case/def/case-body?caseDefId=" + read_yaml('casedefid')
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_query_theme_task'))
    def test_task_query_theme_task(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_publish'))
    def test_task_publish(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    #任务中心
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_fortaskname'))
    def test_task_query_fortaskname(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        QueryUtils().wait_until_total_positive(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_memberlist'))
    def test_task_get_memberlist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_approval_type'))
    def test_task_approval_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["type"] = '4'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_approval_approval'))
    def test_task_approval_approval(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"][0][ "approvalUser"] = 'agnes'
        caseinfo["request"]["json"][0][ "applyData"]["approver"] = 'agnes'
        caseinfo["request"]["json"][0][ "applyData"]["taskTime"]=read_yaml('tasktimefrom')[:-3] + " 至 " +read_yaml('tasktimeto')[:-3]
        caseinfo["request"]["json"][0]["summary"] = "任务标题: "+read_yaml('taskname')+"\n任务日期: "+read_yaml('tasktimefrom')[:-3]+" 至 "+read_yaml('tasktimeto')[:-3]+"\n转办人: "+read_yaml('membername')
        RequestUtils().standard_yaml_case(caseinfo)

   #审批中心
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_approval_list'))
    def test_test_task_approval_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        QueryUtils().wait_until_total_positive(caseinfo)

        approvallist = read_yaml('approvallist')
        taskname = read_yaml('taskname')
        dict = {}
        for i in approvallist:
            if taskname in i['summary']:
                dict = i
        write_yaml({"applydata":dict['applyData']})
        write_yaml({"applydate": dict['applyDate']})
        write_yaml({"applyusername": dict['applyUsername']})
        write_yaml({"approvalusername": dict['approvalUsername']})
        write_yaml({"isagency": dict['isAgency']})
        write_yaml({"reason": dict['reason']})
        write_yaml({"status": dict['status']})
        write_yaml({"summary": dict['summary']})
        write_yaml({"type": dict['type']})
        write_yaml({"urgenum": dict['urgeNum']})
        write_yaml({"idd": dict['id']})

    time.sleep(30)
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_approval_refuse'))
    def test_task_approval_refuse(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_approval_list3'))
    def test_task_approval_list3(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["typeList"] = '4'  #转办
        RequestUtils().standard_yaml_case(caseinfo)
        approval_list = read_yaml('approval_list')
        caseid = read_yaml('caseid')
        status = ''
        for i in approval_list:
            if caseid in i['applyData']:
                status = i['status']
        assert status == '3'  # 状态为已拒绝

@allure.feature("新增单节点岗位任务-绑定积木-审核-验收-发布-延期-通过")
@pytest.mark.parallel
class Test3:
    #任务定制
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_model'))
    def test_task_get_model(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_pre_save'))
    def test_task_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_save_xcpmodel'))
    def test_task_save_xcpmodel(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["xcpInfo"]["body"]["fieldList"] = DebugTalk().set_xcpmodel()
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_query_theme'))
    def test_task_query_theme(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_single_step'))
    def test_task_get_single_step(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_frequencyinfo'))
    def test_task_get_frequencyinfo(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_add'))
    def test_task_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["caseDefBody"] = DebugTalk().set_casebody(read_yaml('taskname'),
                                                                              read_yaml('stepcode'))
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_block'))
    def test_task_get_block(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["blockType"] = '01'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_saveblock'))
    def test_task_saveblock(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_check'))
    def test_task_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_acceptance'))
    def test_task_acceptance(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_casebody'))
    def test_task_get_casebody(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["url"] = "api/agnes-ac/v1/ac/case/def/case-body?caseDefId=" + read_yaml('casedefid')
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_query_theme_task'))
    def test_task_query_theme_task(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_publish'))
    def test_task_publish(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    #任务中心
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_fortaskname'))
    def test_task_query_fortaskname(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        QueryUtils().wait_until_total_positive(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_approval_type'))
    def test_task_approval_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["type"] = '1'
        RequestUtils().standard_yaml_case(caseinfo)

    time.sleep(30)
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_approval_delay'))
    def test_task_approval_delay(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"][0]["approvalUser"] = 'agnes'
        caseinfo["request"]["json"][0]["applyData"]["approver"] = 'agnes'
        caseinfo["request"]["json"][0]["summary"] = "任务标题 : " + read_yaml('taskname') + "\n任务日期 : " + read_yaml(
            'tasktimefrom')[:-3] + " 至 " + read_yaml('tasktimeto')[:-3] + "\n延期时间 : 2025-12-30 00:00:00\n"
        RequestUtils().standard_yaml_case(caseinfo)

    # 审批中心
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_approval_list'))
    def test_test_task_approval_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

        approvallist = read_yaml('approvallist')
        taskname = read_yaml('taskname')
        dict = {}
        for i in approvallist:
            if taskname in i['summary']:
                dict = i
        write_yaml({"applydata": dict['applyData']})
        write_yaml({"applydate": dict['applyDate']})
        write_yaml({"applyusername": dict['applyUsername']})
        write_yaml({"approvalusername": dict['approvalUsername']})
        write_yaml({"isagency": dict['isAgency']})
        write_yaml({"reason": dict['reason']})
        write_yaml({"status": dict['status']})
        write_yaml({"summary": dict['summary']})
        write_yaml({"type": dict['type']})
        write_yaml({"urgenum": dict['urgeNum']})
        write_yaml({"idd": dict['id']})

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_approval_pass'))
    def test_task_approval_pass(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_approval_list3'))
    def test_task_approval_list3(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["typeList"] = '1'
        RequestUtils().standard_yaml_case(caseinfo)
        approval_list=read_yaml('approval_list')
        caseid = read_yaml('caseid')
        status=''
        for i in approval_list:
            if caseid in i['applyData']:
                status= i['status']
        assert status=='2'  #状态为已审核

@allure.feature("新增单节点岗位任务-绑定积木-审核-验收-发布-完成")
@pytest.mark.parallel
class Test4:
    #任务定制
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_model'))
    def test_task_get_model(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_pre_save'))
    def test_task_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_save_xcpmodel'))
    def test_task_save_xcpmodel(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["xcpInfo"]["body"]["fieldList"] = DebugTalk().set_xcpmodel()
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_query_theme'))
    def test_task_query_theme(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_single_step'))
    def test_task_get_single_step(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_frequencyinfo'))
    def test_task_get_frequencyinfo(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_add'))
    def test_task_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["caseDefBody"] = DebugTalk().set_casebody(read_yaml('taskname'),
                                                                              read_yaml('stepcode'))
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_block'))
    def test_task_get_block(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["blockType"] = '01'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_saveblock'))
    def test_task_saveblock(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_check'))
    def test_task_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_acceptance'))
    def test_task_acceptance(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_casebody'))
    def test_task_get_casebody(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["url"] = "api/agnes-ac/v1/ac/case/def/case-body?caseDefId=" + read_yaml('casedefid')
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_query_theme_task'))
    def test_task_query_theme_task(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_publish'))
    def test_task_publish(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    #任务中心
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_fortaskname'))
    def test_task_query_fortaskname(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        QueryUtils().wait_until_total_positive(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_submit'))
    def test_task_submit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])

        item=read_yaml('item')
        item['remark']='完成'
        write_yaml({"item_submit":item})

        RequestUtils().standard_yaml_case(caseinfo)

@allure.feature("新增单节点岗位任务-绑定积木-审核-验收-发布-作废")
@pytest.mark.parallel
class Test5:
    #任务定制
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_model'))
    def test_task_get_model(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_pre_save'))
    def test_task_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_save_xcpmodel'))
    def test_task_save_xcpmodel(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["xcpInfo"]["body"]["fieldList"] = DebugTalk().set_xcpmodel()
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_query_theme'))
    def test_task_query_theme(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_single_step'))
    def test_task_get_single_step(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_frequencyinfo'))
    def test_task_get_frequencyinfo(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_add'))
    def test_task_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["caseDefBody"] = DebugTalk().set_casebody(read_yaml('taskname'),
                                                                              read_yaml('stepcode'))
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_block'))
    def test_task_get_block(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["blockType"] = '01'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_saveblock'))
    def test_task_saveblock(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_check'))
    def test_task_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_acceptance'))
    def test_task_acceptance(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_get_casebody'))
    def test_task_get_casebody(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["url"] = "api/agnes-ac/v1/ac/case/def/case-body?caseDefId=" + read_yaml('casedefid')
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_query_theme_task'))
    def test_task_query_theme_task(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_task_publish'))
    def test_task_publish(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    #任务中心
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_fortaskname'))
    def test_task_query_fortaskname(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        QueryUtils().wait_until_total_positive(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_approval_type'))
    def test_task_approval_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["type"] = '2'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_cancel'))
    def test_task_cancel(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["taskTime"] = read_yaml('tasktimefrom') + " 至 " + read_yaml('tasktimeto')
        RequestUtils().standard_yaml_case(caseinfo)

