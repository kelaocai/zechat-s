import TLSSigAPIv2
import requests, random, json


sdkappid = "1400638786"
admin = "kelaocai"
rand = str(random.randint(0, 4294967295))

api = TLSSigAPIv2.TLSSigAPIv2(
    1400638786, "5aa9ddba8d884869326c32e8c404d9e4c3350b259c65611fa26270ace81242cd"
)

sig = api.gen_sig("kelaocai")

# print(sig)


# 拉取用户信息


def getUserProfile():
    url = (
        "https://console.tim.qq.com/v4/profile/portrait_get?sdkappid="
        + sdkappid
        + "&identifier="
        + admin
        + "&usersig="
        + sig
        + "&random="
        + rand
        + "&contenttype=json"
    )

    postData = {
        "To_Account": ["kelaocai", "orOt85WmpwGwcj-f9hNse6i6-0lk"],
        "TagList": ["Tag_Profile_IM_Nick"],
    }
    r = requests.post(url, data=json.dumps(postData))
    print(r.text)


# getUserProfile()


# 设置用户信息


def setUserProfile():
    url = (
        "https://console.tim.qq.com/v4/profile/portrait_set?sdkappid="
        + sdkappid
        + "&identifier="
        + admin
        + "&usersig="
        + sig
        + "&random="
        + rand
        + "&contenttype=json"
    )
    postData = {
        "From_Account": "orOt85dr0Gx219mEaqvBFG7Gl-vU",
        "ProfileItem": [{"Tag": "Tag_Profile_IM_Nick", "Value": "2x"}],
    }
    r = requests.post(url, data=json.dumps(postData))
    print(r.text)


# setUserProfile()


# 撤回消息
def msgwithdraw():

    url = (
        "https://console.tim.qq.com/v4/openim/admin_msgwithdraw?sdkappid="
        + sdkappid
        + "&identifier="
        + admin
        + "&usersig="
        + sig
        + "&random="
        + rand
        + "&contenttype=json"
    )

    postData = {
        "From_Account": "orOt85WmpwGwcj-f9hNse6i6-0lk",
        "To_Account": "orOt85dr0Gx219mEaqvBFG7Gl-vU",
        "MsgKey": "3655500011_95772375_1649374839",
    }

    # print(url)

    r = requests.post(url, data=json.dumps(postData))
    print(r.text)


# msgwithdraw()


# 查询聊天记录
def getMsg():
    url = (
        "https://console.tim.qq.com/v4/openim/admin_getroammsg?sdkappid="
        + sdkappid
        + "&identifier="
        + admin
        + "&usersig="
        + sig
        + "&random="
        + rand
        + "&contenttype=json"
    )

    postData = {
        "From_Account": "orOt85dr0Gx219mEaqvBFG7Gl-vU",
        "To_Account": "orOt85WmpwGwcj-f9hNse6i6-0lk",
        "MaxCnt": 100,
        "MinTime": 1651318865,
        "MaxTime": 1751329695,
    }
    r = requests.post(url, data=json.dumps(postData))

    res = json.loads(r.text)
    msgList = res["MsgList"]
    for m in msgList:
        # 
        #     print(m["MsgBody"]["Text"])
        for n in m["MsgBody"]:
            if n["MsgType"] == "TIMTextElem":
                print(n['MsgContent'])


getMsg()
