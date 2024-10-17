import requests

# 接口测试示例
# 1. 准备接口测试数据
url = "http://apihcc.fecmall.com/v1/account/login"
data = {"username": "admin", "password": "admin123"}

# 2.模拟请求
res = requests.post(url=url, json=data)

res = requests.get(url=url,params=data)
res = requests.post()
res = requests.put()
res = requests.delete()
# 3. 解析响应的结果，并进行校验
print(res.text) # 响应结果
print(res.status_code) # 响应状态码
