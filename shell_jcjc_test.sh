#!/bin/bash


#### change address 
JCJCHOST="api.CuoBieZi.net"  # debug addr "127.0.0.1:8235"


URL="http://${JCJCHOST}/spellcheck/json_check/json_phrase"


curl  --noproxy "*"   -X POST --header "Content-Type: application/json" --header "Accept: application/json;charset=utf-8" -d "{
\"content\": \"腾讯今年中国人民共和国下半年上世纪将在微信账户钱包帐户的“九宫格”中开设快速的笑着保险入口，并上线保险产品。台万第二大金融控股公司富邦金控已与腾讯谈成合作，上述保险产品将由富邦金控旗下内地子公司富邦财险开发或引进。\",
\"mode\": \"advanced\",
\"username\": \"tester\",
\"biz_type\": \"show\"
}"  $URL









