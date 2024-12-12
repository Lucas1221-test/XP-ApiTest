
import allure
import pytest

from common.ddt_utils import read_case_yaml
from common.request_utils import RequestUtils
from common.files_path import data_path
from common.yaml_utils import read_yaml, write_yaml

"""测试数据路径"""
data_path0=data_path
data_path = data_path0 + 'task_center.yaml'
data_path1 = data_path0 + 'task_approval.yaml'
data_path2 = data_path0 + 'task_create.yaml'

@allure.epic("任务中心")
@allure.feature("查询今日必办-置顶-取消置顶-查询超时任务-查询今日异常-查询可提前办-查询我的分布-查询仅待办-查询仅转交-查询仅协作")
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
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_task'))
    def test_task_query_task2(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["taskCls"] = '02'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_task'))
    def test_task_query_task3(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["taskCls"] = '03'
        RequestUtils().standard_yaml_case(caseinfo)

@allure.feature("新增单节点岗位任务-绑定积木-审核-验收-发布-转办-拒绝")
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
        RequestUtils().standard_yaml_case(caseinfo)

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
        approvallist=read_yaml('approvallist')
        caseid = read_yaml('caseid')
        dict = {}
        for i in approvallist:
            if caseid in i['applyData']:
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
        write_yaml({"urgenum ": dict['urgeNum']})
        write_yaml({"idd": dict['id']})
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_approval_refuse'))
    def test_task_approval_refuse(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

@allure.feature("新增单节点岗位任务-绑定积木-审核-验收-发布-延期-通过")
class Test3:
    # 任务定制
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

    # 任务中心
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_fortaskname'))
    def test_task_query_fortaskname(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_approval_type'))
    def test_task_approval_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["type"] = '1'
        RequestUtils().standard_yaml_case(caseinfo)

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
            approvallist = read_yaml('approvallist')
            caseid = read_yaml('caseid')
            dict = {}
            for i in approvallist:
                if caseid in i['applyData']:
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
            write_yaml({"urgenum ": dict['urgeNum']})
            write_yaml({"idd": dict['id']})
            RequestUtils().standard_yaml_case(caseinfo)

        @pytest.mark.parametrize("caseinfo",
                                 read_case_yaml(data_path1,
                                                'test_task_approval_pass'))
        def test_task_approval_pass(self, caseinfo):
            allure.dynamic.story(caseinfo['story'])
            allure.dynamic.title(caseinfo['title'])
            RequestUtils().standard_yaml_case(caseinfo)

@allure.feature("新增单节点岗位任务-绑定积木-审核-验收-发布-完成")
class Test4:
    # 任务定制
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

    # 任务中心
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_fortaskname'))
    def test_task_query_fortaskname(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_submit'))
    def test_task_submit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

@allure.feature("新增单节点岗位任务-绑定积木-审核-验收-发布-作废")
class Test5:
    # 任务定制
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

    # 任务中心
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_fortaskname'))
    def test_task_query_fortaskname(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

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
        caseinfo["request"]["json"]["taskTime"] = read_yaml('tasktimefrom')[:-3] + " 至 " + read_yaml('tasktimeto')[:-3]
        RequestUtils().standard_yaml_case(caseinfo)