import sys
import xlwt
import pymysql
import requests
import time
import json
from generate_random_data import *
def add_class_lesson(a,b,c):
    school_id=a
    #subject_num=input("请输入每个班的行政课数量：")
    #class_name = input("请输入要导入的行政班课程对应的班级名称（多个以中文逗号隔开）：")
    class_name=b
    subject_num=c
    class_names=class_name.split('，')
    conn1=pymysql.connect(host='sr-test-mysql-uc-master.gz.cvte.cn',user='seewo',password='seewo@cvte',db='seewo_class')
    mycursor1=conn1.cursor()
    sql0='select name from seewo_class.seewo_subject_info where type=1;'
    x_num=mycursor1.execute(sql0)
    rs0 = mycursor1.fetchall()
    names=[]
    for i in range(0,x_num):
        t=str(rs0[i]).strip('(,)')
        t=t.strip("'")
        names.append(t)
    sql1='SELECT s.name FROM seewo_class.seewo_subject_info s left join seewo_class.seewo_unit_subject_rel r on s.resource_id=r.subject_id where r.unit_id="%s" and r.is_deleted=0;'%school_id
    num=mycursor1.execute(sql1)
    rs = mycursor1.fetchall()
    for i in range(0,num):
        t=str(rs[i]).strip('(,)')
        t=t.strip("'")
        names.append(t)
    s_num=x_num+num
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(0, 0, label="科目\n(必填)")
    worksheet.write(0, 1, label="任课班级\n（行政班必填）")
    worksheet.write(0, 2, label="课程名称\n（走班必填）")
    worksheet.write(0, 3, label="老师姓名\n（非必填）")
    worksheet.write(0, 4, label="手机号码\n（非必填）")
    worksheet.write(1, 0, label="需与科目库保持一致")
    worksheet.write(1, 1, label="需与班级信息保持一致")
    worksheet.write(1, 3, label="需和组织架构保持一致")
    worksheet.write(1, 4, label="需和老师信息保持一致")
    y=2
    if int(subject_num)<=s_num:
        for c_n in class_names:
            for i in range(0,int(subject_num)):
                worksheet.write(y, 0, label=names[i])
                worksheet.write(y, 1, label=c_n)
                y=y+1
        workbook.save('D:\Excel_Workbook.xls')
    else:
        url = "https://id.test.seewo.com/login"
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        request_param = {
            "username": "13719444867",
            "password": "e10adc3949ba59abbe56e057f20f883e",
            "system": "mis-admin",
            "clientType": "pc",
            "isReMe": 1
        }
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url, data=json.dumps(request_param), headers=headers,verify=False)
        token = response.json()["data"]["data"]["token"]
        url1="https://campus.test.seewo.com/class/apis.json?action=POST_SCHOOLCOMMON_V1_BYSCHOOLUID_SUBJECT&timestamp=1577501479525"
        headers1 = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': 'x-auth-token=%s'%token
            }
        for i in range(0,int(subject_num)-s_num):
            request_param1={"params":{"schoolUid":school_id,"name":"测试学科"+generate_random_str(8)+str(i)}}
            response1 = requests.post(url1, data=json.dumps(request_param1), headers=headers1,verify=False)
        time.sleep(1)
        sql20='select name from seewo_class.seewo_subject_info where type=1;'
        x_num20=mycursor1.execute(sql20)
        rs20 = mycursor1.fetchall()
        names2=[]
        sql2='SELECT s.name FROM seewo_class.seewo_subject_info s left join seewo_class.seewo_unit_subject_rel r on s.resource_id=r.subject_id where r.unit_id="%s" and r.is_deleted=0;'%school_id
        num2=mycursor1.execute(sql2)
        rs = mycursor1.fetchall()
        conn1.commit()
        mycursor1.close()
        conn1.close()
        for i in range(0,x_num20):
            t=str(rs20[i]).strip('(,)')
            t=t.strip("'")
            names2.append(t)
        for i in range(0,num2):
            t=str(rs[i]).strip('(,)')
            t=t.strip("'")
            names2.append(t)
        for c_n in class_names:
            for i in range(0,int(subject_num)):
                worksheet.write(y, 0, label=names2[i])
                worksheet.write(y, 1, label=c_n)
                y=y+1
        workbook.save('D:\\test_data.xls')
