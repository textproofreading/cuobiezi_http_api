# coding=utf8

import requests,json

'''

pip install request


url = 'http://api.CuoBieZi.net/spellcheck/json_check/json_phrase'

字段一："content", 填写需要检查的文字内容
字段二："mode", 固定值，填写："advanced"  预留参数，固定值
字段三："biz_type", 固定值，填写："show"  预留参数，固定值

返回 json 格式的结果：
{"Cases":[{"Error":"中国人民共和国","Tips":"中华人民共和国","Sentence":"中国人民共和国下半年上世纪将在微信账户钱包帐户的“九宫格”中开设快速的笑着保险入口，","ErrInfo":"","Pos":4}]}

json 结果说明：
Error 是错误词
Tips 是正确词语
Sentence 是错误词与所在的句子
Pos 是错误词在文章中的位置
其他是测试字段，未来会取消

'''

msg_str = "漏字： 中国人民共和国这根邮寄达老旧烟囱已走到生命进头，她的离去让哦们很悲伤， 中华人民共和台万第二大国家主席近平金融控股公司富邦金控已与腾讯谈成合作，上述保险产品将由富邦金控旗下内地子公司富邦财险开发或引进。 "
payload = {
    "content" : msg_str,
    "mode": "advanced",
    "username" : "tester",
    "biz_type": "show",
    "is_return_sentence": True,
    "lets_kill_them_all": True , # 严格模式，误判会多
    "check_sensitive_word":True, # 检查敏感词

}

url = 'http://api.CuoBieZi.net/spellcheck/json_check/json_phrase'

headers = {'content-type': 'application/json'}

print("====>cal==>",json.dumps(payload))
response = requests.post(url, data=json.dumps(payload), headers=headers)
returned_json_str=response.json()
print(response.json())
print( json.dumps(returned_json_str, indent=4, sort_keys=True, ensure_ascii=False) )
