import requests


def pushplus_message(token, message):
    payload = {'token': token, "channel": "wechat", "template": "html", "content": message, "title": "glados checkin status"}
    resp = requests.post("http://www.pushplus.plus/send", params=payload)
    if resp.status_code == 200:
        print('pushplus success code:', resp.status_code)
    else:
        print('push message to pushplus error,the code is:', resp.status_code)
    resp.close()


def server_messgae(token, title, message):
    payload = {"title": title, "desp": message, }
    resp = requests.post(f"https://sctapi.ftqq.com/{token}.send", params=payload)
    result = resp.json()
    if result["code"] == 0:
        print("Push the message to server success(code:0),the code is:" + str(result["code"]))
    if result["code"] != 0:
        print("Push the message to server error(code!=0),The error message is " + str(result["code"]) + str(result["message"]))
    code = resp.status_code
    resp.close()
    return code
