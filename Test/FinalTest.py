import json

class FileAction():

    def write_data(self, contents):
        with open('Data.txt', 'w') as file_object:
            for content in contents.values():
                file_object.write(str(content) + '\n')

    def read_data(self):
        with open('Data.txt', 'r') as f:
            for line in f:
# result = json.loads(line)
                result = eval(line)
                print(result)
            return result
    def stringCom(self, string):
        count_Upper, count_Lower, count_Number = 0, 0, 0
        count_1, count_2, count_3 = 0, 0, 0
        for i in string:
            if i.isupper():
                count_Upper += 1
            elif i.islower():
                count_Lower += 1
            elif i == '1':
                count_Number += 1
                count_1 += 1
            elif i == '2':
                count_Number += 1
                count_2 += 1
            elif i == '3':
                count_Number += 1
                count_3 += 1
            else:
                count_Number += 1
        print("大写字母个数为：" + str(count_Upper) + ' \n'
              + "小写字母个数为：" + str(count_Lower) + ' \n'
              + "数字个数为：" + str(count_Number) + ' \n'
              + "1出现的次数为：" + str(count_1) + ' \n'
              + "2出现的次数为：" + str(count_2) + ' \n'
              + "3出现的次数为：" + str(count_3) + ' \n')

dict = {
    '001': {
        'name': '张三',
        'age': 23,
        'num': '001'
    },
    '002': {
        'name': '李四',
        'age': 25,
        'num': '002'
    }
}
fa = FileAction()
fa.write_data(dict)
dict_result = fa.read_data()
print(type(dict_result))
fa.stringCom('fdadsaSADSA123154')


