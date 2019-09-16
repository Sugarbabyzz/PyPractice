import openpyxl

hot_column_dict = {
    '34': 'GB要目',
    '37': '经济金融',
    '60': '社会民生',
    '61': '生态环保',
    '62': '行业要目',
    '63': '通信、互联网、科技',
    '66': '农村农业',
    '68': '教育科研',
    '69': '劳动就业',
    '70': '房地产市场',
    '71': '市场监管',
    '72': '医疗卫生',
    '73': '贸易摩擦',
    '74': '财政税收',
    '75': '新经济',
    '76': '对外经贸',
    '77': '国际经济动态',
    '78': '其它',
}

'''
线上推送数据.xlsx ； 要目选题文本20181120.xlsx
'''

filename = '要目选题文本20181120.xlsx'

wb = openpyxl.load_workbook(filename)

ws = wb.active

cell_list = []  # 每行的内容
row_list = []  # 每行的集合

if filename == '线上推送数据.xlsx':
    for row in list(ws.rows)[2:]:
        for cell in row[::-2]:   # 列表切片，步长2取值，反向取
            if cell.value in hot_column_dict.keys():   # 将id换成对应类别
                cell_list.append(hot_column_dict[cell.value])
            else:
                cell_list.append(cell.value)
        row_list.append(cell_list)
        cell_list = []

elif filename == '要目选题文本20181120.xlsx' :
    for row in list(ws.rows)[2:]:
        for cell in row[3::-2]:  # 列表切片，步长2取值，反向取
            cell_list.append(cell.value)
        row_list.append(cell_list)
        cell_list = []

# 存入txt
with open(filename.split('.')[0] + '.txt', 'a') as file_object:
    for row in row_list:
        for cell in row:
            if cell is not None:
                file_object.write(cell + '\t')
        file_object.write("\n")



