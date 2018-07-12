# coding=utf8

import requests,json

'''
添加重要领导职务搭配，比如： 国家主席习近平
url = 'http://api.CuoBieZi.net/spellcheck/add_mingci_words'
字段一："content", 填写需要检查的文字内容
字段二："mode", 固定值，填写："advanced"  预留参数，固定值
字段三："biz_type", 固定值，填写："show"  预留参数，固定值
'''

msg_str = "国家主席习近平"
payload = {
    "content" : msg_str,
    "mode": "advanced",
    "username" : "tester",
}
url = 'http://api.CuoBieZi.net/spellcheck/add_mingci_words'
headers = {'content-type': 'application/json'}
print("====>call content==>",json.dumps(payload))
response = requests.post(url, data=json.dumps(payload), headers=headers)
print("result:",response.content)

