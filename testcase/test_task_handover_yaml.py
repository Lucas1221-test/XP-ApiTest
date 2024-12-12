import allure
import pytest

from common.ddt_utils import read_case_yaml
from common.request_utils import RequestUtils
from common.files_path import data_path
from common.yaml_utils import read_yaml, write_yaml
from hotloads.debug_talk import DebugTalk


from datetime import datetime,timedelta
import datetime

"""测试数据路径"""
data_path0=data_path
data_path = data_path0 + 'task_handover.yaml'
data_path1 = data_path0 + 'task_approval.yaml'

@allure.epic("交接管理")
@allure.feature("查询我的交接-查询交接给我的-新增交接-取消交接")
class Test1:

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_fromuser_list'))
    def test_handover_fromuser_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["fromUser"] = 'agnes'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_touser_list'))
    def test_handover_touser_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["toUser"] = 'agnes'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_createdoc'))
    def test_handover_createdoc(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_prdtlist'))
    def test_handover_get_prdtlist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["zhugangren"] = 'agnes'
        caseinfo["request"]["json"]["beginDate"] = str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z"
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today())+"T15:59:59.999Z"
        RequestUtils().standard_yaml_case(caseinfo)
        prdtlist = read_yaml('prdtlist')
        prdtcodelist = []
        if len(prdtlist) != 0:
            for i in prdtlist:
                prdtcodelist.append(i['productCode'])
        write_yaml({"prdtcodelist": prdtcodelist})


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_prdt_alluser'))
    def test_handover_get_prdt_alluser(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["zhugangren"] = 'agnes'
        caseinfo["request"]["json"]["beginDate"] = str(datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
        RequestUtils().standard_yaml_case(caseinfo)

        prdtuserlist = read_yaml('prdtuserlist')
        prdtuserid = ''
        prdtusername = ''
        if len(prdtuserlist) != 0:
            prdtuserid = prdtuserlist[0]['userId']
            prdtusername = prdtuserlist[0]['userName']
        write_yaml({'prdtuserid':prdtuserid})
        write_yaml({'prdtusername': prdtusername})



    @pytest.mark.parametrize("caseinfo",
                                 read_case_yaml(data_path,
                                                'test_handover_get_grouplist'))
    def test_handover_get_grouplist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
        RequestUtils().standard_yaml_case(caseinfo)

        grouplist = read_yaml('grouplist')
        groupidlist = []
        groupuserlist = []
        groupusernamelist = []
        if len(grouplist) != 0:
            for i in grouplist:
                groupidlist.append(i['userGroupId'])
                groupuserlist.append(i['userList'])

            for i in groupuserlist:
                if i[0]['userName'] not in groupusernamelist:
                    groupusernamelist.append(i[0]['userName'])
        write_yaml({"groupidlist":groupidlist})
        write_yaml({"groupuserlist":groupuserlist})
        write_yaml({"groupusernamelist":groupusernamelist})



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_rolelist'))
    def test_handover_get_rolelist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
        RequestUtils().standard_yaml_case(caseinfo)

        rolelist = read_yaml('rolelist')
        roleidlist = []
        if len(rolelist) != 0:
            for i in rolelist:
                roleidlist.append(i['orgId'])
        write_yaml({"roleidlist":roleidlist})



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_role_alluser'))
    def test_handover_get_role_alluser(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
        RequestUtils().standard_yaml_case(caseinfo)

        roleuserlist = read_yaml('roleuserlist')
        roleuserid = ''
        roleusername = ''

        if len(roleuserlist) != 0:
            roleuserid = roleuserlist[0]['userId']
            roleusername = roleuserlist[0]['userName']
        write_yaml({"roleuserid":roleuserid})
        write_yaml({"roleusername":roleusername})



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_templist'))
    def test_handover_get_templist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["attUser"] = 'agnes'
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
        caseinfo["request"]["json"]["taskTimeFrom"] = str(datetime.date.today())
        caseinfo["request"]["json"]["taskTimeTo"] = str(datetime.date.today())
        RequestUtils().standard_yaml_case(caseinfo)

        templist = read_yaml('templist')
        tempidlist = []
        if len(templist) != 0:
            for i in templist:
                if i['taskExecAuth'] == '1111':
                    tempidlist.append(i['pkId'])
        write_yaml({"tempidlist":tempidlist})



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_temp_alluser'))
    def test_handover_get_temp_alluser(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["attUser"] = 'agnes'
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today())+"T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
        caseinfo["request"]["json"]["taskTimeFrom"] = str(datetime.date.today())
        caseinfo["request"]["json"]["taskTimeTo"] = str(datetime.date.today())
        RequestUtils().standard_yaml_case(caseinfo)

        tempuserlist = read_yaml('tempuserlist')
        tempuserid = ''
        tempusername = ''
        if len(tempuserlist) != 0:
            tempuserid = tempuserlist[0]['userId']
            tempusername = tempuserlist[0]['userName']
        write_yaml({"tempuserid":tempuserid})
        write_yaml({"tempusername":tempusername})

        detail=DebugTalk.get_handover_detail(read_yaml('prdtcodelist'),read_yaml('prdtuserid'),read_yaml('prdtusername'),read_yaml('groupidlist'),read_yaml('groupuserlist'),read_yaml('groupusernamelist'),read_yaml('roleidlist'),read_yaml('roleuserid'),read_yaml('roleusername'),read_yaml('tempidlist'),read_yaml('tempuserid'),read_yaml('tempusername'))
        write_yaml({"detail":detail})



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_submit'))
    def test_handover_submit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["zhugangren"] = 'agnes'
        caseinfo["request"]["json"]["beginDate"] = str(datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_add1'))
    def test_handover_add1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["approvalUser"] = 'agnes'
        caseinfo["request"]["json"]["applyUser"] = 'agnes'
        caseinfo["request"]["json"]["fromUser"] = 'agnes'
        caseinfo["request"]["json"]["beginDate"] = str(datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
        caseinfo["request"]["json"]["detailList"] = read_yaml('detail')['detaillist']
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_isneedapproval'))
    def test_handover_isneedapproval(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["type"] = '3'
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_add2'))
    def test_handover_add2(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["applyData"]["approvalUser"] = 'agnes'
        caseinfo["request"]["json"]["applyData"]["applyUser"] = 'agnes'
        caseinfo["request"]["json"]["applyData"]["fromUser"] = 'agnes'
        caseinfo["request"]["json"]["applyData"]["beginDate"] = str(datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["applyData"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
        caseinfo["request"]["json"]["applyData"]["detailList"] = read_yaml('detail')['detaillist']
        caseinfo["request"]["json"]["approvalUser"] = 'agnes'
        caseinfo["request"]["json"]["applyUser"] = 'agnes'
        caseinfo["request"]["json"]["summary"] =  "开始时间: "+str(datetime.date.today())+" 00:00:00"+" \n结束时间: "+str(datetime.date.today())+" 23:59:59"+"\n交出人:致宇小智, 交接人: "+read_yaml('detail')['handoveruser']+"\n交接任务类型: "+read_yaml('detail')['handovertype']

        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_cancel'))
    def test_handover_cancel(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

@allure.feature("新增交接-任务中心查看交接详情-任务中心审核通过-撤销交接")
class Test2:

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_fromuser_list'))
    def test_handover_fromuser_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["toUser"] = 'agnes'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_touser_list'))
    def test_handover_touser_list2(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["toUser"] = 'agnes'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_createdoc'))
    def test_handover_createdoc(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_prdtlist'))
    def test_handover_get_prdtlist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["zhugangren"] = 'agnes'
        caseinfo["request"]["json"]["beginDate"] = str(
            datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["startDate"] = str(
            datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"

        prdtlist = read_yaml('prdtlist')
        prdtcodelist = []
        if len(prdtlist) != 0:
            for i in prdtlist:
                prdtcodelist.append(i['productCode'])
        write_yaml({"prdtcodelist": prdtcodelist})

        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_prdt_alluser'))
    def test_handover_get_prdt_alluser(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["zhugangren"] = 'agnes'
        caseinfo["request"]["json"]["beginDate"] = str(
            datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["startDate"] = str(
            datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"

        prdtuserlist = read_yaml('prdtuserlist')
        prdtuserid = ''
        prdtusername = ''
        if len(prdtuserlist) != 0:
            prdtuserid = prdtuserlist[0]['userId']
            prdtusername = prdtuserlist[0]['userName']
        write_yaml({'prdtuserid': prdtuserid})
        write_yaml({'prdtusername': prdtusername})

        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_grouplist'))
    def test_handover_get_grouplist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["startDate"] = str(
            datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"

        grouplist = read_yaml('grouplist')
        groupidlist = []
        groupuserlist = []
        groupusernamelist = []
        if len(grouplist) != 0:
            for i in grouplist:
                groupidlist.append(i['userGroupId'])
                groupuserlist.append(i['userList'])

            for i in groupuserlist:
                if i[0]['userName'] not in groupusernamelist:
                    groupusernamelist.append(i[0]['userName'])
        write_yaml({"groupidlist": groupidlist})
        write_yaml({"groupuserlist": groupuserlist})
        write_yaml({"groupusernamelist": groupusernamelist})

        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_rolelist'))
    def test_handover_get_rolelist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["startDate"] = str(
            datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"

        rolelist = read_yaml('rolelist')
        roleidlist = []
        if len(rolelist) != 0:
            for i in rolelist:
                roleidlist.append(i['orgId'])
        write_yaml({"roleidlist": roleidlist})

        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_role_alluser'))
    def test_handover_get_role_alluser(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["startDate"] = str(
            datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"

        roleuserlist = read_yaml('roleuserlist')
        roleuserid = ''
        roleusername = ''

        if len(roleuserlist) != 0:
            roleuserid = roleuserlist[0]['userId']
            roleusername = roleuserlist[0]['userName']
        write_yaml({"roleuserid": roleuserid})
        write_yaml({"roleusername": roleusername})

        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_templist'))
    def test_handover_get_templist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["attUser"] = 'agnes'
        caseinfo["request"]["json"]["startDate"] = str(
            datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
        caseinfo["request"]["json"]["taskTimeFrom"] = str(datetime.date.today())
        caseinfo["request"]["json"]["taskTimeTo"] = str(datetime.date.today())

        templist = read_yaml('templist')
        tempidlist = []
        if len(templist) != 0:
            for i in templist:
                if i['taskExecAuth'] == '1111':
                    tempidlist.append(i['pkId'])
        write_yaml({"tempidlist": tempidlist})

        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_temp_alluser'))
    def test_handover_get_temp_alluser(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["attUser"] = 'agnes'
        caseinfo["request"]["json"]["startDate"] = str(datetime.date.today()) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
        caseinfo["request"]["json"]["taskTimeFrom"] = str(datetime.date.today())
        caseinfo["request"]["json"]["taskTimeTo"] = str(datetime.date.today())

        tempuserlist = read_yaml('tempuserlist')
        tempuserid = ''
        tempusername = ''
        if len(tempuserlist) != 0:
            tempuserid = tempuserlist[0]['userId']
            tempusername = tempuserlist[0]['userName']
        write_yaml({"tempuserid": tempuserid})
        write_yaml({"tempusername": tempusername})

        detail = DebugTalk().get_handover_detail(read_yaml('prdtcodelist'), read_yaml('prdtuserid'),
                                               read_yaml('prdtusername'), read_yaml('groupidlist'),
                                               read_yaml('groupuserlist'), read_yaml('groupusernamelist'),
                                               read_yaml('roleidlist'), read_yaml('roleuserid'),
                                               read_yaml('roleusername'), read_yaml('tempidlist'),
                                               read_yaml('tempuserid'), read_yaml('tempusername'))
        write_yaml({"detail": detail})

        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_submit'))
    def test_handover_submit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["userId"] = 'agnes'
        caseinfo["request"]["json"]["zhugangren"] = 'agnes'
        caseinfo["request"]["json"]["beginDate"] = str(
            datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["startDate"] = str(
            datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_add1'))
    def test_handover_add1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["approvalUser"] = 'agnes'
        caseinfo["request"]["json"]["applyUser"] = 'agnes'
        caseinfo["request"]["json"]["fromUser"] = 'agnes'
        caseinfo["request"]["json"]["beginDate"] = str(
            datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
        caseinfo["request"]["json"]["detailList"] = read_yaml('detail')['detaillist']
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_isneedapproval'))
    def test_handover_isneedapproval(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["type"] = '3'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_add2'))
    def test_handover_add2(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["applyData"]["approvalUser"] = 'agnes'
        caseinfo["request"]["json"]["applyData"]["applyUser"] = 'agnes'
        caseinfo["request"]["json"]["applyData"]["fromUser"] = 'agnes'
        caseinfo["request"]["json"]["applyData"]["beginDate"] = str(
            datetime.date.today() - datetime.timedelta(days=1)) + "T16:00:00.000Z"
        caseinfo["request"]["json"]["applyData"]["endDate"] = str(datetime.date.today()) + "T15:59:59.999Z"
        caseinfo["request"]["json"]["applyData"]["detailList"] = read_yaml('detail')['detaillist']
        caseinfo["request"]["json"]["approvalUser"] = 'agnes'
        caseinfo["request"]["json"]["applyUser"] = 'agnes'
        caseinfo["request"]["json"]["summary"] = "开始时间: " + str(
            datetime.date.today()) + " 00:00:00" + " \n结束时间: " + str(
            datetime.date.today()) + " 23:59:59" + "\n交出人:致宇小智, 交接人: " + read_yaml('detail')[
                                                     'handoveruser'] + "\n交接任务类型: " + read_yaml('detail')[
                                                     'handovertype']

        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_approval_list'))
    def test_task_approval_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["pageType"] = '1'

        list1 = read_yaml('approvallist')
        objectid=read_yaml('objectid')
        dict1 = {}
        for i in list1:
            if objectid in i['applyData']:
                dict1 = i

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

        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                                 read_case_yaml(data_path1,
                                                'test_task_handover_get_doc'))
    def test_task_handover_get_doc(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["url"] = "api/ecm-server/v1/ecm/doc/get/order-by-name?docId="+read_yaml('objectid')
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_task_approval_pass'))
    def test_task_approval_pass(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_fromuser_list'))
    def test_handover_fromuser_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["fromUser"] = 'agnes'

        list2 = read_yaml('handoverlist')
        id=read_yaml('id')
        dict2 = {}
        for i in list2:
            if i['id'] == id:
                dict2 = i

        write_yaml({"applyuser":dict2['applyUser']})
        write_yaml({"approvalstatus":dict2['approvalStatus']})
        write_yaml({"approvaluser":dict2['approvalUser']})
        write_yaml({"begindate":dict2['beginDate']})
        write_yaml({"crtts":dict2['crtTs']})
        write_yaml({"detaillist":dict2['detailList']})
        write_yaml({"enddate ":dict2['endDate']})
        write_yaml({"folderpath":dict2['folderPath']})
        write_yaml({"fromuser":dict2['fromUser']})
        write_yaml({"reason":dict2['reason']})
        write_yaml({"type":dict2['type']})
        write_yaml({"updatets":dict2['updateTs']})

        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_task_01'))
    def test_handover_get_task_01(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["changeUser"] = 'agnes'
        caseinfo["request"]["json"]["taskTimeFrom"] = str(datetime.date.today()-datetime.timedelta(days=1))
        caseinfo["request"]["json"]["taskTimeTo"] = str(datetime.date.today())
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_get_task_02'))
    def test_handover_get_task_02(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["changeUser"] = 'agnes'
        caseinfo["request"]["json"]["taskTimeFrom"] = str(datetime.date.today() - datetime.timedelta(days=1))
        caseinfo["request"]["json"]["taskTimeTo"] = str(datetime.date.today())

        taskidlist = []
        tasklist01=read_yaml('tasklist01')
        tasklist02 = read_yaml('tasklist02')
        if len(tasklist01) != 0:
            for i in tasklist01:
                taskidlist.append(i['pkId'])
        if len(tasklist02) != 0:
            for i in tasklist02:
                taskidlist.append(i['pkId'])
        write_yaml({"taskidlist":taskidlist})

        RequestUtils().standard_yaml_case(caseinfo)



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_handover_revoke'))
    def test_handover_revoke(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["revokeDate"] = DebugTalk().get_current_time()
        caseinfo["request"]["json"]["remark"] = "撤销人: "+read_yaml('approvaluser')+"; 撤销时间: "+DebugTalk().get_current_time()
        caseinfo["request"]["json"]["userId"]= "agnes"
        RequestUtils().standard_yaml_case(caseinfo)


