# cuobiezi_http_api
cuobiezi http api


采用 json 方式 post 提交数据， linux  命令行模式 ，使用 curl 提交数据：

	URL="http://api.CuoBieZi.net/spellcheck/json_check/json_phrase"

	curl -X POST --header "Content-Type: application/json" --header "Accept: application/json;charset=utf-8" -d "{
	\"content\": \"腾讯今年中国人民共和国下半年上世纪将在微信账户钱包帐户的“九宫格”中开设快速的笑着保险入口，并上线保险产品。台万第二大金融控股公司富邦金控已与腾讯谈成合作，上述保险产品将由富邦金控旗下内地子公司富邦财险开发或引进。\",
	\"mode\": "advanced",
	\"username\": "tester",
	\"biz_type\": \"show\"
	}"  $URL



	字段一："content", 填写需要检查的文字内容
	字段二："mode", 固定值，填写："advanced"
	字段三："biz_type", 固定值，填写："show"
	字段四："username", 固定值，填写："tester"

	返回 json 格式的结果：
	{"Cases":[{"Error":"中国人民共和国","Tips":"中华人民共和国","Sentence":"中国人民共和国下半年上世纪将在微信账户钱包帐户的“九宫格”中开设快速的笑着保险入口，","ErrInfo":"","Pos":4}]}
	
	
	json 结果说明：
	Error 是错误词
	Tips 是正确词语
	Sentence 是错误词与所在的句子
	Pos 是错误词在文章中的位置
	其他是测试字段，未来会取消




=================================== 下面是一个 linux 脚本例子 =========================================

	$ cat jcjc_test.sh 
	#!/bin/bash
	URL="http://api.CuoBieZi.net/spellcheck/json_check/json_phrase"


	curl -X POST --header "Content-Type: application/json" --header "Accept: application/json;charset=utf-8" -d "{
	\"content\": \"腾讯今年中国人民共和国下半年上世纪将在微信账户钱包帐户的“九宫格”中开设快速的笑着保险入口，并上线保险产品。台万第二大金融控股公司富邦金控已与腾讯谈成合作，上述保险产品将由富邦金控旗下内地子公司富邦财险开发或引进。\",
	\"mode\": \"advanced\",
	\"username\": \"tester\",
	\"biz_type\": \"show\"
	}"  $URL

=================================== 上面是一个 linux 脚本例子 =========================================




=================================== 上面是一个 php  脚本例子 =========================================


	<?php
	    //Get the JSON data POSTed to the page

		//The JSON data.
	$jsonData = array(
	    'content' => '腾讯今年中国人民共和国下半年上世纪将在微信账户钱包帐户的“九宫格”中开设快速的笑着保险入口，并上线保险产品。',
	    'mode' => 'advanced',
	    'username' => 'tester',
	    'biz_type' =>  'show'
	);

		//Encode the array into JSON.
		$jsonDataEncoded = json_encode($jsonData);

	    //$request = file_get_contents('php://input');

	    //Send the JSON data to the right server
	    $ch = curl_init();
	    curl_setopt($ch, CURLOPT_URL, "http://api.CuoBieZi.net/spellcheck/json_check/json_phrase");
	    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	    curl_setopt($ch, CURLOPT_POST, 1);
	    curl_setopt($ch, CURLOPT_HTTPHEADER, array("Content-Type: application/json; charset=utf-8"));
	    curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonDataEncoded);
	    $data = curl_exec($ch);
	    curl_close($ch);

	    //Send the response back to the Javascript code
	    echo $data;
	?>





=================================== 上面是一个 php  脚本例子 =========================================


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



