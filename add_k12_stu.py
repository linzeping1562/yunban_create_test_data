import xlwt
from generate_random_data import *
def add_k12_stu(a,b,c):
    name=[]
    stu_code=[]
    card_num=[]
    ran_name=generate_random_str(8)
    xueduan=a
    class_num=b
    num=c
    n="学生"+ran_name
    stu_num=generate_random_str(8)
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write_merge(0,0,0,8,'填写须知：\n<1>新增学生必填蓝色字段；\n<2>修改系统已存在学生的信息，仅需填写学号和修改项。')
    worksheet.write(1, 0, label="学段")
    worksheet.write(1, 1, label="学生姓名")
    worksheet.write(1, 2, label="学号")
    worksheet.write(1, 3, label="年级")
    worksheet.write(1, 4, label="班级")
    worksheet.write(1, 5, label="班级名称")
    worksheet.write(1, 6, label="一卡通卡号")
    worksheet.write(1, 7, label="家长姓名1")
    worksheet.write(1, 8, label="家长电话1")
    worksheet.write(1, 9, label="家长姓名2")
    worksheet.write(1, 10, label="家长电话2")
    worksheet.write(1, 11, label="家长姓名3")
    worksheet.write(1, 12, label="家长电话3")
    worksheet.write(1, 13, label="家长姓名4")
    worksheet.write(1, 14, label="家长电话4")
    y=2
    for i in range(0,int(class_num)*int(num)):
        name.append(n+str(i))
        stu_code.append(stu_num+str(i))
    if xueduan=='小学':
        grades=['一年级','二年级','三年级','四年级','五年级','六年级']
        for i in range(0,int(class_num)):
            grade=grades[random.randint(0, 5)]
            for j in range(0,int(num)):
                worksheet.write(y, 0, label='小学')
                worksheet.write(y, 1, label=name[j+i*int(num)])
                worksheet.write(y, 2, label=stu_code[j+i*int(num)])
                worksheet.write(y, 3, label=grade)
                worksheet.write(y, 4, label=i+1)
                y=y+1
 
    if xueduan=='初中':
        grades=['七年级','八年级','九年级']
        for i in range(0,int(class_num)):
            grade=grades[random.randint(0, 2)]
            for j in range(0,int(num)):
                worksheet.write(y, 0, label='初中')
                worksheet.write(y, 1, label=name[j+i*int(num)])
                worksheet.write(y, 2, label=stu_code[j+i*int(num)])
                worksheet.write(y, 3, label=grade)
                worksheet.write(y, 4, label=i+1)
                y=y+1
    if xueduan=='高中':
        grades=['高一','高二','高三']
        for i in range(0,int(class_num)):
            grade=grades[random.randint(0, 2)]
            for j in range(0,int(num)):
                worksheet.write(y, 0, label='高中')
                worksheet.write(y, 1, label=name[j+i*int(num)])
                worksheet.write(y, 2, label=stu_code[j+i*int(num)])
                worksheet.write(y, 3, label=grade)
                worksheet.write(y, 4, label=i+1)
                y=y+1
    workbook.save('D:\\test_data.xls')
