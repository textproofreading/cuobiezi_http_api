# coding=utf8

import requests,json


from jcjc_python_api import host_and_port


def call_jcjc_add_one_words_api():
    msg_str_content = "毛泽东"
    payload = {
        "content" : msg_str_content,
        "mode": "advanced",
        "username" : "tester",
        "biz_type": "show",
        "is_return_sentence": True,
        "lets_kill_them_all": True , # 严格模式，误判会多
        "check_sensitive_word":True, # 检查敏感词
    }
    url = 'http://'+ host_and_port +'/spellcheck/add_important_words'
    headers = {'content-type': 'application/json'}
    print("====>call payload ==>",json.dumps(payload))
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    print("status:", response.status_code , response.encoding)

    returned_json_str=response.content

    print("raw http return string:", returned_json_str.decode('utf8'))

    print("if 乱码　please encoding : https://github.com/sunuslee/practical-python-utf8 ")


if __name__ == "__main__":
    call_jcjc_add_one_words_api()