# cuobiezi_http_api
cuobiezi http api


错别字网 CuoBieZi.net 的API调用说明：

API采用HTTP协议，是一个与语言无关的Json　API.

一．　下面是　python 3 的使用方法：

import requests
r = requests.post("http://www.cuobiezi.net/api/v1/zh_spellcheck/json", data={'content': '我最喜欢的就是元霄节吃烫圆。中国共产当的政策好。 ', 'check_mode': 'advanced', 'action': 'show'})
print(r.text)

返回结果：
{"json":"我最喜欢的就是元霄节吃\u003cspan class=\"error\"\u003e烫\u003c/span\u003e\u003cspan class=\"error\"\u003e圆\u003c/span\u003e。\u003cspan class=\"error\"\u003e中\u003c/span\u003e\u003cspan class=\"error\"\u003e国\u003c/span\u003e\u003cspan class=\"error\"\u003e共\u003c/span\u003e\u003cspan class=\"error\"\u003e产\u003c/span\u003e\u003cspan class=\"error\"\u003e当\u003c/span\u003e\u003cspan class=\"error\"\u003e的\u003c/span\u003e\u003cspan class=\"error\"\u003e政\u003c/span\u003e\u003cspan class=\"error\"\u003e策\u003c/span\u003e好。 "}



``````````````````````````````

下面是　php 的使用方法：
具体可以参考页面：
http://www.oschina.net/code/snippet_729516_33065



