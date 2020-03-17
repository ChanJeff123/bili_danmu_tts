#coding=utf-8
import urllib.request
import urllib.parse
import json
import time
import datetime
import win32com.client as wincl
# 手机版Qpython
# import androidhelper

def text2Speech(text):
	speak = wincl.Dispatch("SAPI.SpVoice") 
	speak.Speak(text)


# def tts(msg):
#     '''手机版qpython用tts 
#     '''
#     droid = androidhelper.Android()
#     droid.ttsSpeak(msg)
def get_time():
    str_time = time.strftime("%Y{}%m{}%d{} %X")
    return str_time.format("年", "月", "日")

def main(rid):
 
    url = "https://api.live.bilibili.com/ajax/msg"
 
    data = {
            "roomid":rid,
            "csrf_token":"",
            "csrf":"",
            "visit_id":""
    }
     
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url,data = data)
     
    content = urllib.request\
    .urlopen(req).read()
     
    content = content.decode('utf-8')
    data = json.loads(content)['data']['room']

    list1=[]
    f = open(fpath, "r",encoding="utf-8")
    for line in f.readlines():
        list1.append(line.replace("\n",""))
    for content in data:
        try:
            print("%s 网友:%s  评论了:%s"%(content['timeline'],content['nickname'],content['text']))
            msg = content['text']
            if ("%s 网友:%s  评论了:%s"%(content['timeline'],content['nickname'],content['text'])) in list1:
                print("已经有了")
            else:
                print("新弹幕:")

                print("%s 网友:%s  评论了:%s"%(content['timeline'],content['nickname'],content['text']),file=open(fpath,"a",encoding="utf-8"))
            # print(msg)
                text2Speech(msg)
        except Exception as e:
            print(e)
     
 
if __name__ == '__main__':
    today= datetime.date.today()
    fpath=str(today)+"danmu.txt"
    try:
        a=open(fpath,"r")
    except:
        fp = open(fpath,"w")
    
    # rid=13355
    print("哔哩哔哩 弹幕播报酱\n")
    print("直接输入房间号,退出按 ctrl + c\n\n")

    rid=input("输入直播房间号:\n")
        
    while 1:
        main(rid)
        time.sleep(3)