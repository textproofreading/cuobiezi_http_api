# coding=utf8

import requests,json


from jcjc_python_api import host_and_port


def call_jcjc_list_words_api():
    msg_str = ""
    payload = {
        "content" : msg_str,
        "mode": "advanced",
        "username" : "tester",
        "biz_type": "show",
        "is_return_sentence": True,
        "lets_kill_them_all": True , # 严格模式，误判会多
        "check_sensitive_word":True, # 检查敏感词
    }
    url = 'http://'+ host_and_port +'/spellcheck/list_words'
    headers = {'content-type': 'application/json'}
    print("====>cal==>",json.dumps(payload))
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    returned_json_str=response.json()
    print(response.json())
    print( json.dumps(returned_json_str, indent=4, sort_keys=True, ensure_ascii=False) )


if __name__ == "__main__":
    call_jcjc_list_words_api()