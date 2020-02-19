import sys
import xlwt
from generate_random_data import *
def add_lesson(a):
    #lesson_name=input("请输入你想要的走班课程名称前缀:")
    lesson_name='走班'+generate_random_str(8)
    subjects=['语文','数学','英语','历史','地理','生物','音乐','美术','体育','化学','物理','政治']
    #num = input("请输入每个科目的走班课程数量:")
    num=a
    name=[]
    #subject_name=subject.split('，')
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
    for i in range(0,int(num)):
        na=lesson_name+str(i)
        name.append(na)
    for i in range(0,int(num)):
        subject_name=subjects[random.randint(0, 11)]
        worksheet.write(y, 0, label=subject_name)
        worksheet.write(y, 2, label=name[i])
        y=y+1
    workbook.save('D:\\test_data.xls')
