import xlwt
import pymysql
import os
def add_lesson_stu(a,b,c):
    #plan_id=input("请输入课程所在的排课计划id:")
    #school_id=input("请输入学校id:")
    #stu_num=input("请输入每个走班课程的选课学生数（需小于等于本校的学生数）:")
    plan_id=a
    school_id=b
    stu_num=c
    conn=pymysql.connect(host='sr-test-mysql-master-1.gz.cvte.cn',user='seewo',password='seewo@cvte',db='seewo_opener_server')
    mycursor=conn.cursor()
    sql='SELECT course_name FROM seewo_timetable.course where plan_uid="%s"and type=2 and deleted=0;'%plan_id
    course_num=mycursor.execute(sql)
    rs = mycursor.fetchall()
    course_names=[]
    for i in range(0,course_num):
        t=str(rs[i]).strip('(,)')
        t=t.strip("'")
        course_names.append(t)
    conn.commit()
    mycursor.close()
    conn.close()
    print(course_names)
    conn1=pymysql.connect(host='sr-test-mysql-uc-master.gz.cvte.cn',user='seewo',password='seewo@cvte',db='seewo_class')
    mycursor1=conn1.cursor()
    sql1='SELECT cnname FROM seewo_class.seewo_sys_users where unitId="%s" and student_code!="" and isDeleted=0 limit %d;'%(school_id,int(stu_num))
    num=mycursor1.execute(sql1)
    rs = mycursor1.fetchall()
    stu_names=[]
    for i in range(0,num):
        t=str(rs[i]).strip('(,)')
        t=t.strip("'")
        stu_names.append(t)
    sql2='SELECT student_code FROM seewo_class.seewo_sys_users where unitId="%s" and student_code!="" and isDeleted=0 limit %d;'%(school_id,int(stu_num))
    num=mycursor1.execute(sql2)
    rs = mycursor1.fetchall()
    stu_codes=[]
    for i in range(0,num):
        t=str(rs[i]).strip('(,)')
        t=t.strip("'")
        stu_codes.append(t)
    conn1.commit()
    mycursor1.close()
    conn1.close()
    print(stu_names)
    print(stu_codes)
    path='D:\\test_data'
    paths=path.strip()
    isExists=os.path.exists(paths)
    if not isExists:
        os.makedirs(paths)
    for t in range(0,course_num):
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('sheet1')
        worksheet.write(0, 0, label="学生姓名")
        worksheet.write(0, 1, label="学生学号")
        worksheet.write(1, 0, label="必填（请勿删除该行）")
        worksheet.write(1, 1, label="必填（请勿删除该行）")
        y=2
        for i in range(0,int(num)):
            worksheet.write(y,0,label=stu_names[i])
            worksheet.write(y,1,label=stu_codes[i])
            y=y+1
        workbook.save('D:\\test_data\\'+course_names[t]+'.xls')#文件存储路径可自行修改成你自己想修改的路径
