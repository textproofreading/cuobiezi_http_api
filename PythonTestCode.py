# coding=utf8

import requests,json



msg_str = "漏字： 中华人民共和这根邮寄达老旧烟囱已走到生命进头，她的离去让哦们很悲伤， 中华人民共和台万第二大金融控股公司富邦金控已与腾讯谈成合作，上述保险产品将由富邦金控旗下内地子公司富邦财险开发或引进。 "
payload = {
    "content" : msg_str,
    "mode": "advanced",
    "biz_type": "show"
}



url = 'http://117.121.10.43:8234/spellcheck/json_check/json_phrase'

headers = {'content-type': 'application/json'}

print("====>cal==>",json.dumps(payload))
response = requests.post(url, data=json.dumps(payload), headers=headers)
returned_json_str=response.json()
print(response.json())
print( json.dumps(returned_json_str, indent=4, sort_keys=True, ensure_ascii=False) )
