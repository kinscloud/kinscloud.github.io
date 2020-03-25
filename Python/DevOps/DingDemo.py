import urllib
import requests
import json
import os
import sys

'''
钉钉管理后台 : http://open-dev.dingtalk.com
CorpId       : 企业应用ID
secrect      : corpSecret管理列表下面 企业应用的凭证密钥
'''
corpid = 'ding9a6c128b5d48bf44ee0f45d8e4f7c288'
secrect = '4ZtPITcZ7W2ohl124hKF15pk-D8nWEp0-i8OPVpm6jqymYYT4DWGzug-ZJgS_bkI'

#获取access_token
def getToken():
    url          = 'https://oapi.dingtalk.com/gettoken?corpid=%s&corpsecret=%s' % (corpid, secrect)
    req          = urllib.request.Request(url)
    result       = urllib.request.urlopen(req)
    access_token = json.loads(result.read())
    return access_token['access_token']

#默认情况下第一次创建群组 并获取群组id chatid并写入文件里
def getChatid(access_token):
    file_name = "/tmp/.chatid" 
    #判断群组id文件是否存在
    if not os.path.exists(file_name):
        url = 'https://oapi.dingtalk.com/chat/create?access_token=%s' % access_token
        '''
        name : 群组名字
        owner: 群主userid
        useridlist: 群成员userId列表 也可以写群主userid
        '''
        data = {
                "name": "test1",
                "owner": "manager302",
                "useridlist": ["manager302"]
        }
        data   = json.dumps(data)
        req    = requests.post(url, data)
        chatid = json.loads(req.text)['chatid']
        with open(file_name,'w') as fd:
            fd.write(chatid)
    else:
        with open(file_name) as fd:
            chatid = fd.read()
    return chatid

#access_token 访问令牌 chatid 群组id content 发送的内容
def tonews(access_token, chatid, content):
    '''
    chatid  : 群组id
    msgtype : 类型
    content : 内容
    '''
    url    = "https://oapi.dingtalk.com/chat/send?access_token=%s" % access_token
    msgtype = 'text'
    values  = {
               "chatid": chatid,
               "msgtype": msgtype,
               msgtype: {
                   "content": content
               }
    }
    values = json.dumps(values)
    data   = requests.post(url, values)
    errmsg = json.loads(data.text)['errmsg']
    if errmsg == 'ok':
        return "ok"
    return "fail: %s" % data.text

if __name__ == '__main__':
    access_token = getToken()
    chatid = getChatid(access_token)
    content = '\\\\\\\\n'.join(sys.argv[1:])
    if not content:
        content = '测试'
    print(tonews(access_token, chatid, content))