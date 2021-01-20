import requests

uPhoneNo = '13001230577'
uPassword = 'caiji123456'
projName = '大众点评'

# 登录
# r = requests.get('http://api.xunyaosoft.com/zc/zhicode/api.php?code=signIn&uPhoneNo={}&uPassword={}'.format(uPhoneNo, uPassword))
# print(r.text)

# 获取一个手机号
r = requests.get('http://api.xunyaosoft.com/zc/zhicode/api.php?code=getPhoneNo&projName={}&uPhoneNo={}&uPassword={}'.format(projName, uPhoneNo, uPassword))
phoneNo = r.text
print(phoneNo)

# 获取短信
# r = requests.get('http://api.xunyaosoft.com/zc/zhicode/api.php?code=getMsg&uPhoneNo={}&uPassword={}&projName={}&phoneNo={}'.format(uPhoneNo, uPassword, projName, phoneNo))
# print(r.text)