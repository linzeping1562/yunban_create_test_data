import xlwt
from generate_random_data import *
import datetime
current_year=datetime.datetime.now().year
def add_college_stu(a,b,c,d):
    name=[]
    stu_code=[]
    card_num=[]
    academy=[]
    major=[]
    entrance_years=[str(current_year-3),str(current_year-2),str(current_year-1),str(current_year),str(current_year+1)]
    #academy_num=input("请输入生成的学院数量:")
    #major_num=input("请输入每个学院的专业数量:")
    #class_num=input("请输入每个专业的班级数量:")
    #num=input("请输入每个班级的学生数量:")
    academy_num=a
    major_num=b
    class_num=c
    num=d
    n="学生"+generate_random_str(8)
    stu_num=generate_random_str(8)
    academy_name="学院"+generate_random_str(8)
    major_name="专业"+generate_random_str(8)
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write_merge(0,0,0,9,'填写须知：\n<1>新增学生必填蓝色字段；\n<2>修改系统已存在学生的信息，仅需填写学号和修改项。')
    worksheet.write(1, 0, label="学生姓名")
    worksheet.write(1, 1, label="学号")
    worksheet.write(1, 2, label="学院")
    worksheet.write(1, 3, label="专业")
    worksheet.write(1, 4, label="入学年份")
    worksheet.write(1, 5, label="班级")
    worksheet.write(1, 6, label="手机号")
    worksheet.write(1, 7, label="一卡通卡号")
    worksheet.write(1, 8, label="家长姓名")
    worksheet.write(1, 9, label="家长电话")
    y=2
    for i in range(0,int(academy_num)*int(major_num)*int(class_num)*int(num)):
        name.append(n+str(i))
        stu_code.append(stu_num+str(i))
    for i in range(0,int(academy_num)):
        academy.append(academy_name+str(i))
    for i in range(0,int(major_num)):
        major.append(major_name+str(i))
    for i in range(0,int(academy_num)):
        for j in range(0,int(major_num)):
            for m in range(0,int(class_num)):
                entrance_year=entrance_years[random.randint(0, 4)]
                for n in range(0,int(num)):
                    worksheet.write(y, 0, label=name[n+m*int(num)+j*int(num)*int(class_num)+i*int(major_num)*int(class_num)*int(num)])
                    worksheet.write(y, 1, label=stu_code[n+m*int(num)+j*int(num)*int(class_num)+i*int(major_num)*int(class_num)*int(num)])
                    worksheet.write(y, 2, label=academy[i])
                    worksheet.write(y, 3, label=major[j])
                    worksheet.write(y, 4, label=entrance_year)
                    worksheet.write(y, 5, label=str(m+1)+'班')
                    y=y+1
    workbook.save('D:\\test_data.xls')#文件存储路径可自行修改成你自己想修改的路径

