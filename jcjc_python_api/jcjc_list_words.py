# coding=utf8

import requests,json


from jcjc_python_api import host_and_port


def call_jcjc_list_words_api():
    '''
    在线SaaS用户　，　不提供　添加新词功能．

    主要是因为：　有些用户　随意属于一些字符串，　会影响线上系统的稳定性！

    还有一些竞争对手，直接用来测试，抓取本系统，　我们也是迫于无奈，就关闭了本功能．

    程序员不欺负程序员！

    谢谢大家支持！

    田春峰　　weibo.com/TianChunFeng



    :return:
    '''
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