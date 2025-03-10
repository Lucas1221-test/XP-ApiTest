import datetime

import allure
import pytest


from common.ddt_utils import read_case_yaml
from common.request_utils import RequestUtils
from common.yaml_utils import write_yaml, read_yaml
from common.files_path import data_path
from hotloads.debug_talk import DebugTalk
"""测试数据路径"""
data_path = data_path + 'test_org.yaml'

@allure.epic("任务中心")
@allure.feature("组织架构")
class Test:

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_add_product_parameter'))
    def test_add_product_parameter(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_org_framework_list'))
    def test_org_framework_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r1=RequestUtils().standard_yaml_case(caseinfo)
        orglist = r1.json()['data']['rows']
        id1 = orglist[0]['id']
        data = {"id1": id1}
        write_yaml(data)

        new_org_case = {}
        for item in orglist:
            try:
                if item['orgName'] == '自动化一级测试部门':
                    new_org_case = item
            except IndexError:
                print('没有查询到组织')
        data = {"new_org_case": new_org_case}
        write_yaml(data)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_edit_org'))
    def test_edit_org(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo['request']['json'] = read_yaml("new_org_case")
        RequestUtils().standard_yaml_case(caseinfo)



    """组织架构-用户设置"""
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_org_framework_get_userinfo'))
    def test_org_framework_get_userinfo(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r=RequestUtils().standard_yaml_case(caseinfo)
        userlist = r.json()['data']
        userid = {}
        username = {}
        for i in userlist:
            if i['userName'] == '致宇小智':
                userid = i['userId']
                username = i['userName']
        data = {"userid5": userid}
        write_yaml(data)
        data = {"username5": username}
        write_yaml(data)



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_org_framework_member_add'))
    def test_org_framework_member_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today())
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_org_framework_member_list'))
    def test_org_framework_member_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today())
        r2 = RequestUtils().standard_yaml_case(caseinfo)
        data = r2.json()['data']['rows']
        organization_user_information = {}
        for i in data:
            if i['userId'] == read_yaml("userid5"):
                organization_user_information = i
        data = {"organization_user_information": organization_user_information}
        write_yaml(data)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_org_framework_member_edit'))
    def test_org_framework_member_edit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"] = read_yaml("organization_user_information")
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_org_framework_member_delete'))
    def test_org_framework_member_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"] = read_yaml("organization_user_information")
        RequestUtils().standard_yaml_case(caseinfo)


#岗位设置-岗位设置
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_group_getorgtree'))
    def test_group_getorgtree(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r=RequestUtils().standard_yaml_case(caseinfo)
        orglist = r.json()['data']
        orgid = {}
        for i in orglist:
            if i['orgName'] == '自动化一级测试部门':
                orgid = i['id']
        data = {"orgid": orgid}
        write_yaml(data)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_group_getorg_member'))
    def test_group_getorg_member(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_group_config_add'))
    def test_group_config_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_group_config_list'))
    def test_group_config_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r2=RequestUtils().standard_yaml_case(caseinfo)
        grouplist1 = r2.json()['data']['rows']
        group_config_info = {}
        for item in grouplist1:
            try:
                if item['userGroupName'] == '自动化测试岗位':
                    group_config_info = item
            except IndexError:
                print('没有查询到岗位')
        data = {"group_config_info": group_config_info}
        write_yaml(data)
        groupid = group_config_info['userGroupId']
        data = {"groupid": groupid}
        write_yaml(data)



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_group_config_edit'))
    def test_group_config_edit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"] = read_yaml("group_config_info")
        RequestUtils().standard_yaml_case(caseinfo)


# 岗位设置-用户管理
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_group_config_list'))
    def test_group_config_list1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r=RequestUtils().standard_yaml_case(caseinfo)
        # grouplist = r.json()['data']['rows']
        # print(grouplist)
        # groupid = {}
        # groupname = {}
        # orgid1 = {}
        # orgname1 = {}
        # for i in grouplist:
        #     if i['userGroupName'] == '自动化测试岗位':
        #         groupid = i['userGroupId']
        #         groupname = i['userGroupName']
        #         orgid = i['orgId']
        #         orgname = i['orgName']
        # data = {"groupid": groupid}
        # write_yaml(data)
        # data = {"groupname": groupname}
        # write_yaml(data)
        # data = {"orgid1": orgid1}
        # write_yaml(data)
        # data = {"orgname1": orgname1}
        # write_yaml(data)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_group_ref_get_org'))
    def test_group_ref_get_org(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today())
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_group_save_ref'))
    def test_group_save_ref(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_group_ref_get_user_query'))
    def test_group_ref_get_user_query(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_group_edit_ref'))
    def test_group_edit_ref(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        # json = read_yaml("group_ref_get_user_info").strip("'")
        # caseinfo["request"]["json"] = json
        RequestUtils().standard_yaml_case(caseinfo)






#产品分工表
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_prdt_prdtselect'))
    def test_prdt_prdtselect(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_prdt_productuser'))
    def test_prdt_productuser(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_prdt_divide_add'))
    def test_prdt_divide_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_prdt_divide_query'))
    def test_prdt_divide_query(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r4=RequestUtils().standard_yaml_case(caseinfo)
        prdtlist = r4.json()['data']['rows']
        selectobjid = {}
        for i in prdtlist:
            if i['productCode'] == read_yaml('productCode'):
                selectobjid = i['id']
        data = {"selectobjid": selectobjid}
        write_yaml(data)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_prdt_divide_update'))
    def test_prdt_divide_update(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["prdtCode"] = str(read_yaml("productCode")) + '-'+ read_yaml("productCode")
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_prdt_divide_delete'))
    def test_prdt_divide_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


        @pytest.mark.parametrize("caseinfo",
                                 read_case_yaml(data_path,
                                'test_prdt_divide_downloadtemplate'))
        def test_prdt_divide_downloadtemplate(self, caseinfo):
            allure.dynamic.story(caseinfo['story'])
            allure.dynamic.title(caseinfo['title'])
            RequestUtils().standard_yaml_case(caseinfo)


        @pytest.mark.parametrize("caseinfo",
                                 read_case_yaml(data_path,
                                'test_prdt_divide_export'))
        def test_prdt_divide_export(self, caseinfo):
            allure.dynamic.story(caseinfo['story'])
            allure.dynamic.title(caseinfo['title'])
            RequestUtils().standard_yaml_case(caseinfo)


        @pytest.mark.parametrize("caseinfo",
                                 read_case_yaml(data_path,
                                'test_prdt_divide_import'))
        def test_prdt_divide_import(self, caseinfo):
            allure.dynamic.story(caseinfo['story'])
            allure.dynamic.title(caseinfo['title'])
            RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_group_delete'))
    def test_group_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"] = read_yaml("group_config_info")
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_org_framework_delete'))
    def test_org_framework_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo['request']['json'] = read_yaml("new_org_case")
        RequestUtils().standard_yaml_case(caseinfo)
#交接管理
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_handover_touser_list'))
    # def test_handover_touser_list(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     RequestUtils().standard_yaml_case(caseinfo)
    #
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_handover_fromuser_list'))
    # def test_handover_fromuser_list(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     RequestUtils().standard_yaml_case(caseinfo)
    #
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_handover_get_user_info'))
    # def test_handover_get_user_info(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     RequestUtils().standard_yaml_case(caseinfo)
    #
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_handover_createdoc'))
    # def test_handover_createdoc(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     RequestUtils().standard_yaml_case(caseinfo)
    #
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_handover_get_prdtlist'))
    # def test_handover_get_prdtlist(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     caseinfo["request"]["json"]["beginDate"] = str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z"
    #     caseinfo["request"]["json"]["startDate"] =str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z"
    #     caseinfo["request"]["json"]["endDate"] = str(datetime.date.today())+"T15:59:59.999Z"
    #     RequestUtils().standard_yaml_case(caseinfo)
    #
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_handover_get_grouplist'))
    # def test_handover_get_grouplist(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     caseinfo["request"]["json"]["startDate"] =str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z"
    #     caseinfo["request"]["json"]["endDate"] = str(datetime.date.today())+"T15:59:59.999Z"
    #     RequestUtils().standard_yaml_case(caseinfo)
    #
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_handover_get_rolelist'))
    # def test_handover_get_rolelist(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     caseinfo["request"]["json"]["startDate"] = str(datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
    #     caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
    #     RequestUtils().standard_yaml_case(caseinfo)
    #
    #
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_handover_get_templist'))
    # def test_handover_get_templist(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     caseinfo["request"]["json"]["taskTimeFrom"] =str(datetime.date.today())
    #     caseinfo["request"]["json"]["taskTimeTo"] = str(datetime.date.today())
    #     caseinfo["request"]["json"]["startDate"] = str(datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
    #     caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
    #     RequestUtils().standard_yaml_case(caseinfo)
    #
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_handover_get_prdt_alluser'))
    # def test_handover_get_prdt_alluser(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     caseinfo["request"]["json"]["beginDate"] = str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z"
    #     caseinfo["request"]["json"]["startDate"] = str(datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
    #     caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
    #     RequestUtils().standard_yaml_case(caseinfo)
    #
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'handover_get_role_alluser'))
    # def handover_get_role_alluser(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     caseinfo["request"]["json"]["startDate"] = str(datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
    #     caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
    #     RequestUtils().standard_yaml_case(caseinfo)
    #
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_handover_get_temp_alluser'))
    # def test_handover_get_temp_alluser(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     caseinfo["request"]["json"]["taskTimeFrom"] = str(datetime.date.today())
    #     caseinfo["request"]["json"]["taskTimeTo"] = str(datetime.date.today())
    #     caseinfo["request"]["json"]["startDate"] = str(datetime.date.today())+"T16:00:00.000Z"
    #     caseinfo["request"]["json"]["endDate"] = str(datetime.date.today())+"T15:59:59.999Z"
    #     RequestUtils().standard_yaml_case(caseinfo)
    #
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_handover_get_userlist'))
    # def test_handover_get_userlist(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     RequestUtils().standard_yaml_case(caseinfo)
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_handover_submit'))
    # def test_handover_submit(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     caseinfo["request"]["json"]["beginDate"] = str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z"
    #     caseinfo["request"]["json"]["startDate"] = str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z"
    #     caseinfo["request"]["json"]["endDate"] = str(datetime.date.today())+"T15:59:59.999Z"
    #     RequestUtils().standard_yaml_case(caseinfo)


