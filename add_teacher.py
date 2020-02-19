import xlwt
from generate_random_data import *
from generate_random_num import *
def add_teacher(n):
    #num=input("请输入你要添加的老师数量:")
    num=n
    phone_fore=generate_random_nums(5)
    n="老师"+generate_random_str(5)
    name=[]
    phones=[]
    i=1
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(0, 0, label="教师姓名")
    worksheet.write(0, 1, label="手机号")
    y=1
    for i in range(0,int(num)): 
        name.append(n+str(i))
        phone="1"+phone_fore+ str(i).zfill(10-len(phone_fore))
        phones.append(phone)
    for i in range(0,int(num)):
        worksheet.write(y, 0, label=name[i])
        worksheet.write(y, 1, label=phones[i])
        y=y+1
    workbook.save('D:\\test_data.xls')
