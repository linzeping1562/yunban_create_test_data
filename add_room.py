import xlwt
from generate_random_data import *
def add_room(a,b):
    #building_num=input("请输入你要添加的建筑数量:")
    #room_num=input("请输如每栋建筑的场地数:")
    building_num=a
    room_num=b
    building_name="建筑"+generate_random_str(8)
    room_name="场地"+generate_random_str(8)
    building=[]
    room=[]
    i=1
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(0, 0, label="所在建筑（必填）")
    worksheet.write(0, 1, label="场地名称（必填）")
    worksheet.write(0, 2, label="场地编号")
    worksheet.write(0, 3, label="可容纳人数")
    worksheet.write(0, 4, label="面积（平方米）")
    worksheet.write(0, 5, label="对应年级")
    worksheet.write(0, 6, label="对应班级")
    worksheet.write(0, 7, label="管理员（以，,、分割最多三个）")
    worksheet.write(0, 8, label="备注（最多100个字）")
    worksheet.write(0, 9, label="异常原因")
    y=1
    for i in range(0,int(building_num)):
        building.append(building_name+str(i))
    for i in range(0,int(building_num)*int(room_num)):
        room.append(room_name+str(i))
    for i in range(0,int(building_num)):
        for j in range(0,int(room_num)):
            worksheet.write(y, 0, label=building[i])
            worksheet.write(y, 1, label=room[j+i*int(room_num)])
            y=y+1
    workbook.save('D:\\test_data.xls')
