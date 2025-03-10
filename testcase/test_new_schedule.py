import datetime
from io import StringIO
from pickletools import read_uint2

import allure
import pytest
import yaml
from dateutil.utils import today

from common.ddt_utils import read_case_yaml
from common.request_utils import RequestUtils
from common.yaml_utils import write_yaml, read_yaml
from common.files_path import data_path
from hotloads.debug_talk import DebugTalk
"""测试数据路径"""
data_path = data_path + 'test_schedule.yaml'

@allure.epic("业务配置")
@allure.feature("时间表")
class Test:
#
# 排班管理方案
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_shedule_get_orglist'))
    def test_shedule_get_orglist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r=RequestUtils().standard_yaml_case(caseinfo)
        orglist = []
        data1 = r.json()['data']
        for i in data1:
            orglist.append(i['orgId'])
        data = {"orglist": orglist}
        write_yaml(data)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_shedule_get_orgidlist'))
    def test_shedule_get_orgidlist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r1=RequestUtils().standard_yaml_case(caseinfo)
        orgidlist = []
        data2 = r1.json()['data']
        for i in data2:
            orgidlist.append(i['id'])
        data = {"orgidlist": orgidlist}
        write_yaml(data)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_shedule_get_org_post'))
    def test_shedule_get_org_post(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title("查询org列表2")
        r2=RequestUtils().standard_yaml_case(caseinfo)
        list = r2.json()['data']['rows']
        usergroupid = {}
        for i in list:
            if i['userGroupName'] == '测试岗位001':
                usergroupid = i['userGroupId']
        data = {"usergroupid": usergroupid}
        write_yaml(data)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_shedule_get_org_group'))
    def test_shedule_get_org_group(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_shedule_add'))
    def test_shedule_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["endDate"] = today + datetime.timedelta(days=1)
        caseinfo["request"]["json"]["detailList"][0]["smallPerList"] = read_yaml("grouplist1")
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_shedule_get_list'))
    def test_shedule_get_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_shedule_edit'))
    def test_shedule_edit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["detailList"][0]["smallPerList"] = read_yaml("grouplist1")
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_shedule_get_list1'))
    def test_shedule_get_list1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_shedule_preview'))
    def test_shedule_preview(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_shedule_audit'))
    def test_shedule_audit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_shedule_get_list1'))
    def test_shedule_get_list2(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

@allure.feature("排班日历")
class Test_memo:
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_memo_listmonth'))
    def test_memo_listmonth(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_memo_getauditor'))
    def test_memo_getauditor(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_memo_getauditor_all'))
    def test_memo_getauditor_all(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_memo_get_roster_postlist'))
    def test_memo_get_roster_postlist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_memo_get_roster_typelist'))
    def test_memo_get_roster_typelist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_memo_get_roster_userlist'))
    def test_memo_get_roster_userlist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_memo_checklist'))
    def test_memo_checklist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["postList"] = read_yaml("postlist")
        caseinfo["request"]["json"]["personList"] = read_yaml("personlist")
        caseinfo["request"]["json"]["rosterTypeDict"] = read_yaml("personlist")
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_memo_get_roster_isneedapproval'))
    def test_memo_get_roster_isneedapproval(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_memo_add'))
    def test_memo_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["summary"] = "岗位: "+read_yaml("postname")+", 班次: "+read_yaml("rostertypename")+"\n申请人: 覃云, 调出日期: "+"2024-12-26"+"\n对调人: "+read_yaml("targetusername")+", 调入日期: "+"2024-12-27"
        # caseinfo["request"]["json"]["applyData"]["postList"] = read_yaml("postlist")
        # caseinfo["request"]["json"]["applyData"]["personList"] = read_yaml("personList")
        # caseinfo["request"]["json"]["applyData"]["rosterTypeDict"] = read_yaml("rosterTypeDict")
        RequestUtils().standard_yaml_case(caseinfo)