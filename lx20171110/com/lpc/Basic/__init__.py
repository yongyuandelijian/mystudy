import itchat
import requests
import time


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    KEY = 'd346c0902e254de0822eed15c0fc3c49'
    data = {
        'key': KEY,
        'info': msg,
        'userid': '空空',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return


@itchat.msg_register(itchat.content.TEXT)
def print_c(msg):
    haoyou = itchat.get_friends(update=True)

    for i in haoyou:

        if i['UserName'] == msg['FromUserName']:
            name = i['NickName']
            name1 = i['RemarkName']
            break
    xiaoxi = name1 + '(' + name + ')' + ":" + msg['Text']
    print(xiaoxi)
    k = get_response(msg['Text'])
    print("机器人:" + k)
    itchat.send(xiaoxi, toUserName='filehelper')
    itchat.send(k, toUserName='filehelper')
    time.sleep(1)
    return k


itchat.auto_login(hotReload=True)
# u = itchat.search_friends()
# u = u[0]['UserName']
# print(u)
# itchat.send('微信已开启机器人自动回复模式,可以查询天气,讲笑话,搜索功能等...,toUserName=u)
itchat.run()