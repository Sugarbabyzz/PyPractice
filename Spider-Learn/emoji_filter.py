s = '🧡🧡🧡🧡🧡🎡🎡🎡🎡🎡冬天的古'

import re


def filter_emoji(desstr, restr=''):
    '''
    过滤表情
    '''
    res = re.compile(u'[\U00010000-\U0010ffff\\uD800-\\uDBFF\\uDC00-\\uDFFF]')
    return res.sub(restr, desstr)


s = filter_emoji(s)
print(s)