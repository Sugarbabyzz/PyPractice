

#****** 17.1 使用Web API ******
#   Web API是网站的一部分，用于与使用非常具体的URL请求特定信息的程序交互。
#   请求的数据将以易于处理的格式（JSON或CSV）返回

# 1、Git和Github
#   本章中，将使用GitHub的API来请求有关该网站中Python项目的信息，即自动下载GitHub上星级最高的Python项目的信息，
#   然后使用Pygal生成交互式可视化，以呈现这些项目的受欢迎程度

# 2、使用API调用请求数据
#   https://api.github.com/search/repositories?q=language:python&sort=stars
#   这个调用返回GitHub当前托管了多少个Python项目，还有有关最受欢迎的Python仓库的信息。
#   API的结构分析，在书上P339

# 3、安装requests
#   requests包让Python程序能够轻松地向网站请求信息以及检查返回的响应
#   pip3 install --user requests

# 4、处理API响应
#   编写一个程序，执行API调用并处理结果，找出GitHub上星级最高的Python项目
import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)  # 使用requests的get()调用并将URL传递给它，再将响应对象存储在变量r中
print("Status code:", r.status_code)   # 响应对象包含一个名为status_code的属性，能够知道是否请求成功（200为成功）

# 将API响应存储在一个变量中
response_dict = r.json()  # 这个API返回JSON格式的信息，使用json()方法将其转换为一个Python字典
print("Total repositories: ",response_dict['total_count'])

# 处理结果
print(response_dict.keys())

# 5、处理响应字典

#   暂留，见书P340