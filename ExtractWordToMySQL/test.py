import re

str = re.sub('[^\w\u4e00-\u9fff()（）]+', '','江苏 » （无锡市）:婚礼司仪(rogerWWW)')
print(str)