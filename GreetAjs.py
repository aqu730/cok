#================================#
#GREET_TEAM_MUTANT : AGUS 2019_004
#GREET_TATA__ID LINE : greetolala990
#================================#
from linepy import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from thrift import transport, protocol, server
from datetime import datetime, timedelta
import pytz, pafy, livejson, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, tweepy, codecs, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, goslate, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
import youtube_dl
from time import sleep
import pyimgflip
from zalgo_text import zalgo
from threading import Thread,Event
import requests,uvloop
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()
loop = uvloop.new_event_loop()

cl = LINE("EMAIL","PASSWORD")
cl.log("Auth Token : " + str(cl.authToken))

k1 = LINE()
k1.log("Auth Token : " + str(k1.authToken))
#==========GREET_TEMPLATE========
print ("♒♒♒♒♒♒♒🔰🔰♒♒♒♒♒♒♒")
print ("================================")
print ("┌──────────────────┐\n│  ⬜ OPEN ORDER ⬜ \n├──────────────────\n│🎧FITUR LINE & SMULE🎤\n├──────────────────\n┝[🛡️]►Coin Line\n┝[🛡️]►Coin Gift\n┝[🛡️]►Vip Smule Android\n┝[🛡️]►Beku Akun Smule\n┝[🛡️]►Follower Smule\n┝[🛡️]►Songbook Smule\n│☛🏧Via Bank & Pulsa📱\n│♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛\n├──────────────────\n│⚙️PROTECT & SELFBOT 🔧\n├──────────────────\n┝[🛡️]►Selfbot Only\n┝[🛡️]►Selfbot Only + Ajs\n┝[🛡️]►Selfbot Template\n┝[🛡️]►Selfbot Template + Ajs\n┝[🛡️]►Bot Protect Rom Smule\n┝[🛡️]►Bot Protect Rom Event\n│☛If Order Creator\n│WA: 082135759022\n│♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛\n├──────────────────\n│Suport:⭕GʀᴇᴛSʜᴏᴘ⭕\n└──────────────────")
print ("================================")
print("╔•══════════════════════\n╠•☛LOGIN TEMPLATE SUKSES\n╚•══════════════════════")
print ("♒♒♒♒♒♒♒🔰🔰♒♒♒♒♒♒♒")

oepoll = OEPoll(cl)
call = cl
creator = ["u9e7b95e0fe30d1b8a23a6c83e73a5d8f"]
owner = ["u9e7b95e0fe30d1b8a23a6c83e73a5d8f"]
admin = ["uc5a1f2e068afce3a18b68590e28c78b4"]
staff = ["uc5a1f2e068afce3a18b68590e28c78b4"]

lineProfile = cl.getProfile()
mid = cl.getProfile().mid
Amid = k1.getProfile().mid
KAC = [cl,k1]
Bots = [mid,Amid]
Saints = admin + owner + staff
Team = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

welcome = []
targets = []
protectname = []
prohibitedWords = ['Asu', 'Jancuk', 'Tai', 'Kickall', 'Ratakan', 'Cleanse']
userTemp = {}
userKicked = []
msg_dict = {}
msg_dict1 = {}
dt_to_str = {}
temp_flood = {}
groupName = {}
groupImage = {}
list = []
ban_list = []
offbot = []

settings = {
    "welcome": False,
    "leave": False,
    "mid": False,
    "Aip": True,
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": {},
    "postingan":{},
    "checkPost": False,
    "autoRead": False,
    "autoJoinTicket": False,
    "setKey": False,
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }, 
    "unsendMessage": False,
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changevp": False,
    "changeCover":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "checkmid": False,
    "getMid": False,
    "invite":False,
    "Invi":False,
    "staff":{},
    "Timeline": False,
    "likePost": False,
    "likeOn": True,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "readPoint":{},
    "readMember":{},
    "lang":False,
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "tumbal":True,
    "backup":True,
    "contact":False,
    "autoRead": False,
    "autoBlock": False,
    "autoJoin":True,
    "autoAdd":False,
    'autoCancel':{"on":True, "members":1},
    "autoReject":False,
    "autoLeave":False,
    "detectMention":False,
    "detectMention2":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "Unsend":False,
    "sticker":False,
    "selfbot":True,
    "mention":"🚺ʜᴇᴍᴍ ɴɢɪɴᴛɪᴘ",
    "Respontag":"🚺ʜᴀᴅɪʀ ʙᴇʙ ᴍᴜᴀᴄʜ",
    "Respontag2":"🚺ᴋᴏᴊᴏᴍ ʏᴜᴄʜ ʙᴇʙᴢ",
    "welcome":"🚹sᴇᴍᴏɢᴀ ʙᴇᴛᴀʜ ɢᴀᴇᴢ",
    "autoLeave":"🚺sᴇʟᴀᴍᴀᴛ ᴊᴀʟᴀɴ ᴛᴇᴍᴀɴ",
    "comment":"┌──────────────────┐\n│     🔳 OPEN ORDER 🔳 \n├──────────────────\n│🎧FITUR LINE & SMULE🎤\n├──────────────────\n┝[]►Coin Line\n┝[]►Coin Gift\n┝[]►Vip Smule Android\n┝[]►Beku Akun Smule\n┝[]►Follower Smule\n┝[]►Songbook Smule\n│☛🏧Via Bank & Pulsa📱\n│♛♛♛♛♛♛♛♛♛♛♛♛♛♛\n├──────────────────\n│⚙️PROTECT & SELFBOT 🔧\n├──────────────────\n┝[]►Selfbot Only\n┝[]►Selfbot Only + Ajs\n┝[]►Selfbot Template\n┝[]►Selfbot Template + Ajs\n┝[]►Bot Protect Rom Smule\n┝[]►Bot Protect Rom Event\n│☛If Order Creator:\n│http://line.me/ti/p/~slanker123456\n│♛♛♛♛♛♛♛♛♛♛♛♛♛♛\n├──────────────────\n│Suport:⭕GʀᴇᴛQᴜᴇᴇɴ Sʜᴏᴘ⭕\n└──────────────────",
    "message1":"ᴛʜᴀɴᴋᴢ ғᴏʀᴅ ᴀᴅᴅ ᴍᴇ\n┌──────────────────┐\n│     🔳 OPEN ORDER 🔳 \n├──────────────────\n│🎧FITUR LINE & SMULE🎤\n├──────────────────\n┝[]►Coin Line\n┝[]►Coin Gift\n┝[]►Vip Smule Android\n┝[]►Beku Akun Smule\n┝[]►Follower Smule\n┝[]►Songbook Smule\n│☛🏧Via Bank & Pulsa📱\n│♛♛♛♛♛♛♛♛♛♛♛♛♛♛\n├──────────────────\n│⚙️PROTECT & SELFBOT 🔧\n├──────────────────\n┝[]►Selfbot Only\n┝[]►Selfbot Only + Ajs\n┝[]►Selfbot Template\n┝[]►Selfbot Template + Ajs\n┝[]►Bot Protect Rom Smule\n┝[]►Bot Protect Rom Event\n│☛If Order Creator:\n│http://line.me/ti/p/~slanker123456\n│♛♛♛♛♛♛♛♛♛♛♛♛♛♛\n├──────────────────\n│Suport:⭕GʀᴇᴛQᴜᴇᴇɴ Sʜᴏᴘ⭕\n└──────────────────",
}
protect = {
    "pqr":[],
    "pinv":[],
    "proall":[],
    "antijs":[],
    "protect":[]
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
clProfile = cl.getProfile()
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


imagesOpen = codecs.open("image.json","r","utf-8")
images = json.load(imagesOpen)
videosOpen = codecs.open("video.json","r","utf-8")
videos = json.load(videosOpen)
stickersOpen = codecs.open("sticker.json","r","utf-8")
stickers = json.load(stickersOpen)
audiosOpen = codecs.open("audio.json","r","utf-8")
audios = json.load(audiosOpen)
mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
           
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

def autolike():
    for zx in range(0,500):
      hasil = cl.activity(limit=500)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == True:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postid'],wait["comment"])
          print ("✪[]► Like Success")
        except:
          pass
      else:
          print ("Already Liked")
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
        
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items

def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            cl.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def changeProfileVideo(to):
    if settings['changevp']['picture'] == True:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changevp']['video'] == True:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changevp']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changevp']['picture']
        settings['changevp']['status'] = True
        cl.updateProfilePicture(path_p, 'vp')
                     
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'GEGE.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)

def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "╔═════[ Sider Members ]═══════\n║ Sini Gabung Chat ka 😊..\n╠☛ 1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠☛  {}. ".format(str(no))
            else:
                textx += "╚══════════════════\n╔══════════════════\n  「 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀ : {} 」\n╚══════════════════".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = (str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
       # cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
       # cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
    #    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error)) 

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" wib\nNama Group : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nExpired : In "+hari+"\n Version :「Gaje Bots」  \nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)                     
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost


#=====DEF HELP MENU =======
def sendTextTemplate25(to, text):
    data = {
                                        "type": "flex",
                                        "altText": "G⃠R⃠E⃠E⃠T⃠",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#ff0000" #0000" #cc9999"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": "✴️C̸͟͞R̸͟͞E̸͟͞A̸͟͞T̸͟͞O̸͟͞R̸͟͞ B̸͟͞O̸͟͞T̸͟͞ G̸͟͞R̸͟͞E̸͟͞E̸͟͞T̸͟͞✴️", #ᴘᴇʟᴀᴋᴜ:{} ".format(cl.getContact(mid).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#ffff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [              
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": " ", #format(cl.getContact(sender).displayName),
           "size": "xs",
           "align": "center",
           "color": "#000000",
           "wrap": True,
           "weight": "bold",
           "type": "text"
           },
           {
          "text": text,
           "size": "xxs",
          # "align": "center",
           "color": "#33ffff",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {          
        "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
#=========DEF COMEN PUBLIK=======
def sendTextTemplate300(to, text): #Def baca: 1
    data = {
                                       "type": "flex",
                                       "altText": "G⃠R⃠E⃠E⃠T⃠",
                                       "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true", 
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.jimphicdesigns.com/downloads/imgs-mockup/bouncy-ball-change-colors-animation.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQNbHeKfKZ9ITF6-xfqowdmMB3nvzZHwsnny59tKTZRecWqFqny",
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "ʀᴇsᴘᴏɴ", 
"align": "center",
"color": "#000000",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "19px",
"backgroundColor": "#ffd700",
"offsetStart": "20px",
"height": "14px",
"width": "45px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.gifer.com/THMv.gif", #https://thumbs.gfycat.com/RawThirstyJanenschia-size_restricted.gif",
"size": "full",
"action": {
"type": "uri",
"uri": "https://wa.me/6282135759022",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "13px",
"offsetStart": "115px",
"height": "43px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/timeline",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~slanker123456",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/__TRSC_OLALA__",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "37px",
"offsetStart": "14px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "⏰"+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#93ff00",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "128px",
"backgroundColor": "#4b4b4b",
"offsetStart": "80px",
"height": "16px",
"width": "61px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🚹{} ".format(contact.displayName),
"weight": "bold",
"color": "#93ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "148px",
#"backgroundColor": "#000000",
"offsetStart": "20px",
"height": "18px",
"width": "121px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": text,
"weight": "bold",
"color": "#ff0000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "165px",
#"backgroundColor": "#ac00c8",
"offsetStart": "20px",
"height": "16px",
"width": "121px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
    cl.postTemplate(to, data)

def sendTextTemplate(to, text):
    data = {
            "type": "flex",
            "altText": "G⃠R⃠E⃠E⃠T⃠",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
             {
            "type": "separator",
            "color": "#33ffff"            
            },
            {
            "contents": [
            {
            "type": "separator",
            "color": "#33ffff" 
   },
   {
            "text": text,
           "size": "xxs",
           "color": "#00ff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)

def sendTextTemplate28(to, text):
    data = {
                                        "type": "flex",
                                        "altText": "G⃠R⃠E⃠E⃠T⃠",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#ff0000" #0000" #cc9999"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": "✴️sᴇᴛᴛɪɴɢ ʙᴏᴛ ᴏɴ/ᴏғғ✴️", #ᴘᴇʟᴀᴋᴜ:{} ".format(cl.getContact(mid).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#33ffff",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [             
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
          "text": text,
           "size": "xxs",
          # "align": "center",
           "color": "#00ff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [             
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)

def sendTextTemplate1(to, text):
    data = {
                                        "type": "flex",
                                        "altText": "G⃠R⃠E⃠E⃠T⃠",
                                        "contents": {
"styles": {"body": {
"backgroundColor": "#000000"
},
"footer": 
{"backgroundColor": "#000000"
}},
"type": "bubble",
"size": "micro",
"body":
{
"contents": [
{
"contents": [
{
"type": "separator",
"color": "#33ffff"
},{
"type": "separator",
"color": "#33ffff"
},{
"contents": [
{
"type": "separator",
"color": "#33ffff"
},{
"contents": [
{
"text": text,
"size": "xxs",
"align": "center",
"color": "#00ff00",
"wrap": True,
"weight": "bold",
"type": "text"
}],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},{
"type": "separator",
"color": "#33ffff"
}],
"type": "box",
"layout": "horizontal"
},{
"type": "separator",
"color": "#33ffff"
},{
"contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)

def sendTextTemplate2(to, text):
    data = {
                                        "type": "flex",
                                        "altText": "G⃠R⃠E⃠E⃠T⃠",
                                        "contents": {
  "styles": {"body": {
            "backgroundColor": "#000000"},"footer": {"backgroundColor": "#000000"}},
            "type": "bubble","size": "micro","body": {"contents": [{"contents": [{
             "type": "separator","color": "#33ffff"},{"type": "separator","color": "#33ffff"
              },{"contents": [{   "type": "separator","color": "#33ffff"
              },{"contents": [
              {"text": text, "size": "xxs",
              "color": "#00ff00","wrap": True,"weight": "bold","type": "text"
              }],"type": "box","spacing": "md","layout": "vertical"},{
              "type": "separator","color": "#33ffff"}],"type": "box","layout": "horizontal"},{"type": "separator","color": "#33ffff"},{
              "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
def sendTextTemplate23(to, text):
    data = {
                                        "type": "flex",
                                        "altText": "G⃠R⃠E⃠E⃠T⃠",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#ff0000" #0000" #cc9999"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": "✴️ᴄᴇᴋ ɢʀᴏᴜᴘ_ғʀɪᴇɴᴅ✴️", #ᴘᴇʟᴀᴋᴜ:{} ".format(cl.getContact(mid).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#ffff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
          "text": text,
           "size": "xxs",
          # "align": "center",
           "color": "#33ffff",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate00(to, text):
    data = {
                                        "type": "flex",
                                        "altText": "B̸͟͞R̸͟͞O̸͟͞A̸͟͞D̸͟͞C̸͟͞A̸͟͞S̸͟͞T̸͟͞",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
 "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#33ffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ³",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#33ffff"
          },
          {
          "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "type": "image",
            "size": "xxs",
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#33ffff"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": "🔊ʙʀᴏᴀᴅᴄᴀsᴛ🔊",
"weight": "bold",
"color": "#33ffff",
"align": "center",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": "🕙"+ datetime.strftime(timeNow,'%H:%M:%S'+"🕙"),
"weight": "bold",
"color": "#ccffff",
"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {     
       "contents": [           
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#33ffff"
            },
           {
          "type": "text",
"text": "{}".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": "#ffff00",
"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {          
         "contents": [
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#33ffff"
            },
           {
          "text": text,
           "size": "xxs",
          "align": "center",
           "color": "#00ff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          },
         {
        "type": "separator",
        "color": "#33ffff"
         }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
      "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com",
           }, 
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat" #"http://line.me/ti/p/~greetolala999",
            },         
            "flex": 1          
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
        },{
        "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {          
            "contents": [
               {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
    },{
 "type": "text",
"text": "ᴛʜᴀɴᴋᴢ ғᴏʀ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "sᴜᴘᴏʀᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴀᴍ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator", #batas APK
        "color": "#33ffff"     
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
   #Def Musik
   
def sendTextTemplate10(to, text):
    data = {
                                "type": "flex",
                                "altText": "G⃠R⃠E⃠E⃠T⃠",
                                "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "nano",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 1
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"gravity": "bottom",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true",
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "140px",
"width": "110px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "140px",
"width": "110px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "Hiburan",
"align": "center",
"color": "#000000",
"weight": "bold",
"size": "xxs",
"weight": "bold",
"offsetTop": "1px"
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "9px",
"backgroundColor": "#ffd700",
"offsetStart": "7px",
"height": "15px",
"width": "45px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://thumbs.gfycat.com/UnkemptWhiteKakapo-max-1mb.gif",
"size": "xxl",
"action": {
"type": "uri",
"uri": "https://wa.me/6282135759022",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "5px",
"offsetStart": "92px",
"height": "43px",
"width": "22px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://thumbs.gfycat.com/UnkemptWhiteKakapo-max-1mb.gif",
"size": "xxl",
"action": {
"type": "uri",
"uri": "https://joox.com"
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "5px",
"offsetStart": "67px",
"height": "43px",
"width": "22px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/__TRSC_OLALA__",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/ZHtFDts/20190427-185307.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/chat",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~slanker123456",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
"size": "full",
"action": {
"type": "uri",
"uri": "https://youtube.com",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "25px",
"offsetStart": "5px",
"height": "180px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🕙 "+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#ffffff",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "98px",
"backgroundColor": "#ff0000",
"offsetStart": "50px",
"height": "16px",
"width": "63px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": text, #📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#ffffff",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "115px",
"backgroundColor": "#0000ff",
"offsetStart": "33px",
"height": "14px",
"width": "80px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🔰ɢʀᴇᴇt_ʙᴏᴛᴢ",
"weight": "bold",
"color": "#00ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "130px",
#"backgroundColor": "#33ffff",
"offsetStart": "8px",
"height": "50px",
"width": "110px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
    cl.postTemplate(to, data)
   
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain['keyCommand']):
        cmd = pesan.replace(Setmain['keyCommand'],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╔═════════🚫\n"+\
                  "┣1️⃣► " + key + "ʜᴇʟᴘ ᴄʀᴇᴀᴛᴏʀ\n" + \
                  "┣2️⃣► " + key + "ʜᴇʟᴘ sᴇᴛᴛɪɴɢ\n" + \
                  "┣3️⃣► " + key + "ʜᴇʟᴘ ᴍᴇᴅɪᴀ\n" + \
                  "┣4️⃣► " + key + "ʜᴇʟᴘ ɢʀᴏᴜᴘ\n" + \
                  "┣5️⃣► " + key + "ʜᴇʟᴘ ᴀᴅᴍɪɴ\n" + \
                  "╚═════════🚫"
    return helpMessage
def helpcreator():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╭「⏺️ᴄᴏᴍᴀɴᴅ ʙᴏᴛ⏺️」\n"+\
                  "│⏺️" + key + "ᴍᴇ\n" + \
                  "│⏺️" + key + "ᴄᴠᴘ\n" + \
                  "│⏺️" + key + "sᴇᴛᴛɪɴɢ\n" + \
                  "│⏺️" + key + "ʀᴜɴᴛɪᴍᴇ\n" + \
                  "│⏺️" + key + "sᴘᴇᴇᴅ-sᴘ\n" + \
                  "│⏺️" + key + "sᴀɴᴛᴇᴛ ᴍᴀɴᴛᴀɴ\n" + \
                  "│⏺️" + key + "ʙʏᴇᴍᴇ\n" + \
                  "│⏺️" + key + "ʀᴇᴊᴇᴄᴛ\n" + \
                  "│⏺️" + key + "ʟᴇᴀᴠᴇᴀʟʟ\n" + \
                  "│⏺️" + key + "ʟɪsᴛғʀɪᴇɴᴅ\n" + \
                  "│⏺️" + key + "ғʀɪᴇɴᴅʟɪsᴛ\n" + \
                  "│⏺️" + key + "ɢʀᴜᴘʟɪsᴛ\n" + \
                  "│⏺️" + key + "ᴏᴘᴇɴ ǫʀ\n" + \
                  "│⏺️" + key + "ᴄʟᴏsᴇ ǫʀ\n" + \
                  "│⏺️" + key + "ᴛᴀɢᴀʟʟ\n" + \
                  "│⏺️" + key + ".ɪɴᴠɪᴛᴇ @\n" + \
                  "│⏺️" + key + "ʙʟᴏᴄᴋ「@」\n" + \
                  "│⏺️" + key + "ᴀᴅᴅᴍᴇ「@」\n" + \
                  "│⏺️" + key + "ᴍʏʙᴏᴛ\n" + \
                  "│⏺️" + key + "ʟɪsᴛᴘᴇɴᴅɪɴɢ\n" + \
                  "│⏺️" + key + "ʙʟᴏᴄᴋᴄᴏɴᴛᴀᴄᴛ\n" + \
                  "│⏺️" + key + "ʟᴋsᴛʙʟᴏᴄᴋ\n" + \
                  "│⏺️" + key + "ʟɪsᴛᴍɪᴅ\n" + \
                  "│⏺️" + key + "ᴀᴅᴅᴀsɪs\n" + \
                  "│⏺️" + key + "ʙʀᴏᴀᴅᴄᴀsᴛ:「ᴛᴇxᴛ」\n" + \
                  "╰「⏺️sᴇʟғ ᴘʏᴛʜᴏɴ³⏺️」"
    return helpMessage1

def helpadmin():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage5 = "╭「⏺️ᴄᴏᴍᴀɴᴅ ʙᴏᴛ⏺️」\n"+\
                  "│⏺️"  + key + "ʙᴏᴛᴀᴅᴅ「@」\n" + \
                  "│⏺️"  + key + "ʙᴏᴛᴅᴇʟʟ「@」\n" + \
                  "│⏺️"  + key + "sᴛᴀғғ「@」\n" + \
                  "│⏺️"  + key + "sᴛᴀғᴅᴇʟʟ「@」\n" + \
                  "│⏺️"  + key + "ᴀᴅᴍɪɴ「@」\n" + \
                  "│⏺️"  + key + "ᴀᴅᴍɪɴᴅᴇʟʟ「@」\n" + \
                  "│⏺️"  + key + "ʀᴇʙᴏᴏᴛ\n" + \
                  "│⏺️"  + key + "ʙᴀɴ「@」\n" + \
                  "│⏺️"  + key + "ʙʟᴄ\n" + \
                  "│⏺️"  + key + "ʙᴀɴ:ᴏɴ\n" + \
                  "│⏺️"  + key + "ᴜɴʙᴀɴ:oɴ\n" + \
                  "│⏺️"  + key + "ᴜɴʙᴀɴ「@」\n" + \
                  "│⏺️"  + key + "ʙᴀɴʟɪsᴛ\n" + \
                  "│⏺️"  + key + "ᴄʙᴀɴ\n" + \
                  "│⏺️"  + key + "ʀᴇғʀᴇsʜ\n" + \
                  "╰「⏺️sᴇʟғ ᴘʏᴛʜᴏɴ³⏺️」"
    return helpMessage5
  
def helpgroup():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage4 = "╭「⏺️sᴇʟғ ᴘʏᴛʜᴏɴ³⏺️」\n"+\
                  "│⏺️" + key + "ɢᴍɪᴅ @\n" + \
                  "│⏺️" + key + "ɢᴇᴛ ɪᴅ @\n" + \
                  "│⏺️" + key + "ɢᴇᴛᴍɪᴅ @\n" + \
                  "│⏺️" + key + "ɢᴇᴛʙɪᴏ @\n" + \
                  "│⏺️" + key + "ɢᴇᴛɪɴғᴏ @\n" + \
                  "│⏺️" + key + "ɢᴇᴛᴘʀᴏғɪʟᴇ @\n" + \
                  "│⏺️" + key + "ɢᴇᴛᴘɪᴄᴛᴜʀᴇ @\n" + \
                  "│⏺️" + key + "ɪɴғᴏ @\n" + \
                  "│⏺️" + key + "ᴋᴇᴘᴏ @\n" + \
                  "│⏺️" + key + "ᴘᴘᴠɪᴅᴇᴏ @\n" + \
                  "│⏺️" + key + "ᴋᴏɴᴛᴀᴋ @\n" + \
                  "│⏺️" + key + "ᴄᴏɴᴛᴀᴄᴛ:「ᴍɪᴅ」\n" + \
                  "│⏺️" + key + "ɢɴᴀᴍᴇ「ᴛᴇxᴛ」\n" + \
                  "│⏺️" + key + "ᴍʏᴍɪᴅ\n" + \
                  "│⏺️" + key + "ᴍʏʙɪᴏ\n" + \
                  "│⏺️" + key + "ᴍʏғᴏᴛᴏ\n" + \
                  "│⏺️" + key + "ᴍʏɴᴀᴍᴇ\n" + \
                  "│⏺️" + key + "ᴍʏᴘʀᴏғɪʟᴇ\n" + \
                  "│⏺️" + key + "ᴍʏᴘɪᴄᴛᴜʀᴇ\n" + \
                  "│⏺️" + key + "ᴍʏᴄᴏᴠᴇʀ\n" + \
                  "│⏺️" + key + "ᴍʏᴠɪᴅᴇᴏ\n" + \
                  "│⏺️" + key + "ᴋᴀʟᴇɴᴅᴇʀ\n" + \
                  "│⏺️" + key + "ᴍᴇᴍᴘɪᴄᴛ\n" + \
                  "│⏺️" + key + "ᴜᴘᴅᴀᴛᴇɢʀᴜᴘ\n" + \
                  "│⏺️" + key + "ɢʀᴜᴘᴘɪᴄᴛ\n" + \
                  "│⏺️" + key + "ɪɴғᴏɢʀᴏᴜᴘ「ɴᴏ」\n" + \
                  "│⏺️" + key + "ɪɴғᴏᴍᴇᴍ「ɴᴏ」\n" + \
                  "╰「⏺️sᴇʟғ ᴘʏᴛʜᴏɴ³⏺️」"
    return helpMessage4
def helpsetting():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "╭「⏺️sᴇʟғ ᴘʏᴛʜᴏɴ³⏺️」\n"+\
                  "│⏺️" + key + "ᴄᴇᴋ sɪᴅᴇʀ\n" + \
                  "│⏺️" + key + "ᴄᴇᴋ ʟᴇᴀᴠᴇ \n" + \
                  "│⏺️" + key + "ᴄᴇᴋ ᴘᴇsᴀɴ \n" + \
                  "│⏺️" + key + "ᴄᴇᴋ ʀᴇsᴘᴏɴ \n" + \
                  "│⏺️" + key + "ᴄᴇᴋ ʀᴇsᴘᴏɴ² \n" + \
                  "│⏺️" + key + "sᴇᴛ sɪᴅᴇʀ:「ᴛᴇxᴛ」\n" + \
                  "│⏺️" + key + "sᴇᴛ ᴘᴇsᴀɴ:「ᴛᴇxᴛ」\n" + \
                  "│⏺️" + key + "sᴇᴛ ʀᴇsᴘᴏɴ:「ᴛᴇxᴛ」\n" + \
                  "│⏺️" + key + "sᴇᴛ ʀᴇsᴘᴏɴ²:「ᴛᴇxᴛ」\n" + \
                  "│⏺️" + key + "sᴇᴛ ᴡᴇʟᴄᴏᴍᴇ:「ᴛᴇxᴛ」\n" + \
                  "│⏺️" + key + "sᴇᴛ ʟᴇᴀᴠᴇ:「ᴛᴇxᴛ」\n" + \
                  "│⏺️" + key + "ʟɪᴋᴇ「ᴏɴ/ᴏғғ」\n" + \
                  "│⏺️" + key + "ᴘᴏsᴛ「oɴ/oғғ」\n" + \
                  "│⏺️" + key + "sᴛɪᴄᴋᴇʀ「oɴ/oғғ」\n" + \
                  "│⏺️" + key + "ɪɴᴠɪᴛᴇ「oɴ/ᴏғғ」\n" + \
                  "│⏺️" + key + "ᴜɴsᴇɴᴅ「oɴ/oғғ」\n" + \
                  "│⏺️" + key + "ʀᴇsᴘᴏɴ「oɴ/oғғ」\n" + \
                  "│⏺️" + key + "ʀᴇsᴘᴏɴ²「oɴ/oғғ」\n" + \
                  "│⏺️" + key + "ᴀᴜᴛᴏᴀᴅᴅ「oɴ/oғғ」\n" + \
                  "│⏺️" + key + "ᴡᴇʟᴄᴏᴍᴇ「oɴ/oғғ」\n" + \
                  "│⏺️" + key + "ᴄᴏɴᴛᴀᴄᴛ「oɴ/oғғ」\n" + \
                  "│⏺️" + key + "ᴀᴜᴛᴏᴊᴏɪɴ「oɴ/oғғ」\n" + \
                  "│⏺️" + key + "ᴀᴜᴛᴏʀᴇᴊᴇᴄᴛ「oɴ/oғғ」\n" + \
                  "│⏺️" + key + "ᴀᴜᴛᴏʟᴇᴀᴠᴇ「oɴ/oғғ」\n" + \
                  "│⏺️" + key + "ᴀᴜᴛᴏʙʟᴏᴄᴋ「oɴ/oғғ」\n" + \
                  "│⏺️" + key + "ᴊᴏɪɴᴛɪᴄᴋᴇᴛ「oɴ/oғғ」\n" + \
				  "╰「⏺️sᴇʟғ ᴘʏᴛʜᴏɴ³⏺️」"
    return helpMessage2
def media():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "╔═══════════\n" + \
"┣[🇧🇩]► " + key + "Addsticker\n" + \
"┣[🇧🇩]► " + key + "Addmp3\n" + \
"┣[🇧🇩]► " + key + "Addaudio\n" + \
"┣[🇧🇩]► " + key + "Addimg\n" + \
"┣[🇧🇩]► " + key + "Dellsticker\n" + \
"┣[🇧🇩]► " + key + "Dellaudio\n" + \
"┣[🇧🇩]► " + key + "Dellmp3\n" + \
"┣[🇧🇩]► " + key + "Dellvideo\n" + \
"┣[🇧🇩]► " + key + "Dellimg\n" + \
"┣[🇧🇩]► " + key + "Liststicker\n" + \
"┣[🇧🇩]► " + key + "Listimage\n" + \
"┣[🇧🇩]► " + key + "Listvideo\n" + \
"┣[🇧🇩]► " + key + "Listaudio\n" + \
"┣[🇧🇩]► " + key + "Listmp3\n" + \
"┣[🇧🇩]► " + key + "Lihat「No」\n" + \
"┣[🇧🇩]► " + key + "Cctv metro\n" + \
"┣[🇧🇩]► " + key + "Smule「id」\n" + \
"┣[🇧🇩]► " + key + "Joox「text」\n" + \
"┣[🇧🇩]► " + key + "mp4「text」\n" + \
"┣[🇧🇩]► " + key + "mp3「text」\n" + \
"┣[🇧🇩]► " + key + "Yutube「text」\n" + \
"┣[🇧🇩]► " + key + "Youtube「text」\n" + \
"╚═══════════"
    return helpMessage3

def helphost():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage6 = "╭「⏺️ᴄᴏᴍᴀɴᴅ ɢʜᴏsᴛ⏺️」\n"+\
                  "│⏺️"  + key + "ᴀᴊsɴᴀᴍᴇ:「ᴛᴇxᴛ」\n" + \
                  "│⏺️"  + key + "ᴀᴊsғᴏᴛᴏ\n" + \
                  "│⏺️"  + key + "ᴀᴊs ᴄᴀɴᴄᴇʟ\n" + \
                  "│⏺️"  + key + "ᴀᴊs ᴋɪᴄᴋᴀʟ\n" + \
                  "│⏺️"  + key + "ᴀᴊs ᴀʙsᴇɴ\n" + \
                  "│⏺️"  + key + "ᴘᴀs ʙᴀɴᴅ「ʙᴏᴍ」\n" + \
                  "│⏺️"  + key + "ᴄᴀɴᴄᴇʟᴀʟʟ\n" + \
                  "│⏺️"  + key + "ᴄʀᴏᴛ「@」\n" + \
                  "│⏺️"  + key + "ɢᴋɪᴄᴋ「@」\n" + \
                  "│⏺️"  + key + "ᴋɪᴄᴋ「@」\n" + \
                  "│⏺️"  + key + "ᴊs sᴛᴀʏ\n" + \
                  "│⏺️"  + key + "ᴊs ɪɴ-ᴏᴜᴛ\n" + \
                  "│⏺️"  + key + "ɢʟɪsᴛᴊs1\n" + \
                  "│⏺️"  + key + "ᴋ1-ɪɴᴠɪᴛ「ɴᴏᴍᴇʀ」\n" + \
                  "╰「⏺️sᴇʟғ ᴘʏᴛʜᴏɴ³⏺️」"
    return helpMessage6

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)
                cl.sendMessage(op.param1,"ᴛʜᴀɴᴋᴢ ғᴏʀᴅ ᴀᴅᴅ ᴍᴇ\n┌──────────────────┐\n│     🔳 OPEN ORDER 🔳 \n├──────────────────\n│🎧FITUR LINE & SMULE🎤\n├──────────────────\n┝[]►Coin Line\n┝[]►Coin Gift\n┝[]►Vip Smule Android\n┝[]►Beku Akun Smule\n┝[]►Follower Smule\n┝[]►Songbook Smule\n│☛🏧Via Bank & Pulsa📱\n│♛♛♛♛♛♛♛♛♛♛♛♛♛♛\n├──────────────────\n│⚙️PROTECT & SELFBOT 🔧\n├──────────────────\n┝[]►Selfbot Only\n┝[]►Selfbot Only + Ajs\n┝[]►Selfbot Template\n┝[]►Selfbot Template + Ajs\n┝[]►Bot Protect Rom Smule\n┝[]►Bot Protect Rom Event\n│☛If Order Creator:\n│http://line.me/ti/p/~slanker123456\n│♛♛♛♛♛♛♛♛♛♛♛♛♛♛\n├──────────────────\n│Suport:⭕GʀᴇᴛQᴜᴇᴇɴ Sʜᴏᴘ⭕\n└──────────────────")

        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate1(op.param1,"eмooн coĸ" +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate1(op.param1,"ᴛʜᴀɴᴋs" + str(ginfo.name))

        if op.type == 13:
            if wait["autoJoin"] and mid in op.param3:
                group = cl.getGroup(op.param1)
                group.notificationDisabled = False
                cl.acceptGroupInvitation(op.param1)
                cl.updateGroup(group)
                ginfo = cl.getGroup(op.param1)
                data = {
   "contents": [{
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": "ғᴏᴛᴏ ᴘᴇɴɢᴜɴᴅᴀɴɢ",
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [                      
{
"type": "separator",
"color": "#33ffff"
},{
"contents": [{"type": "separator","color": "#33ffff"},{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
"size": "full",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~slanker123456",
            },
            "flex": 0
}
],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},
{"type": "separator",
"color": "#33ffff"
}
],
"type": "box",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
         },
         {
        "contents": [ 
        { 
        "type": "separator",
         "color": "#33ffff"
         },
         {
            "contents": [
              {
"text": "{}".format(cl.getContact(op.param2).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         #natase
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/4N1BjnV/20190427-175005.png", #watshaphttps://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://wa.me/6282135759022",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat" #"http://line.me/ti/p/~greetolala999",
            },         
            "flex": 1          
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://call/contacts"
          },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "C̸͟͞R̸͟͞E̸͟͞A̸͟͞T̸͟͞O̸͟͞R̸͟͞ B̸͟͞O̸͟͞T̸͟͞Z̸͟͞",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~slanker123456",
          },
           "align": "center"
          }
        ]
      }
    }, #Batas1
    {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": "ᴘʀᴏғɪʟᴇ ɢʀᴏᴜᴘ",
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         
{
"type": "separator",
"color": "#33ffff"
}, #Fotoprofile
{
"contents": [{"type": "separator","color": "#33ffff"},{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(cl.getGroup(op.param1).pictureStatus),
"size": "full",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~slanker123456",
            },
            "flex": 0
}
],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},
{"type": "separator",
"color": "#33ffff"
}
],
"type": "box",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
         },
         {
        "contents": [
        { 
        "type": "separator",
         "color": "#33ffff"
         },
         {
            "contents": [
              {
"text": "{}".format(ginfo.name),
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {
       "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/fxWzxcR/20190428-232352.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/settings"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/cb7WqMS/20190428-232825.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/profile"   
          },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/7YVnNPF/20190625-190410.png", #https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://joox.com"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "C̸͟͞R̸͟͞E̸͟͞A̸͟͞T̸͟͞O̸͟͞R̸͟͞ B̸͟͞O̸͟͞T̸͟͞Z̸͟͞",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~slanker123456",
          },
           "align": "center"
          }
        ]
      }
 }, #Batas1
    {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text":"ᴛʜᴀɴᴋs ғᴏʀ ɪɴᴠɪᴛᴇ",
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         
{
"type": "separator",
"color": "#33ffff"
}, #Fotoprofile
{
"contents": [{"type": "separator","color": "#33ffff"},{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
"size": "full",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~slanker123456",
            },
            "flex": 0
}
],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},
{"type": "separator",
"color": "#33ffff"
}
],
"type": "box",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
         },
         {
        "contents": [         
        { 
        "type": "separator",
         "color": "#33ffff"
         },
         {
            "contents": [
              {
"text": "{}".format(cl.getContact(mid).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {
       "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },{
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~slanker123456",             
           }, 
            "flex": 1            
          },{
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },{
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },{
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },{
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "C̸͟͞R̸͟͞E̸͟͞A̸͟͞T̸͟͞O̸͟͞R̸͟͞ B̸͟͞O̸͟͞T̸͟͞Z̸͟͞",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~slanker123456",
          },
           "align": "center"
          }
        ]
      }
    }
  ],
  "type": "carousel"
}

                cl.postFlex(op.param1, data)

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message1"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message1"])

        if op.type == 13:
            if mid in op.param3:
               if wait["autoReject"] == True:
                   if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                       cl.rejectGroupInvitation(op.param1)

        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                try:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                except:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _dn in gMembMids:
                          if _dn in wait["blacklist"]:
                            cl.cancelGroupInvitation(op.param1,[_dn])
                    except:
                        cl.cancelGroupInvitation(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        
            if op.param3 in wait["blacklist"]:
                try:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                except:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _dn in gMembMids:
                          if _dn in wait["blacklist"]:
                            cl.cancelGroupInvitation(op.param1,[_dn])
                    except:
                        cl.cancelGroupInvitation(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
               try:
                   cl.kickoutFromGroup(op.param1,[op.param2])
                   cl.sendMessage(op.param1,"そ、[ʙʟᴀᴄᴋʟɪsᴛ]そうですか(｀・ω・´)")
               except:
                   pass

        if op.type == 19:
            if mid in op.param3:
            	if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        k1.acceptGroupInvitation(op.param1)
                        k1.inviteIntoGroup(op.param1,[mid])
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        cl.acceptGroupInvitation(op.param1)
                        k1.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Amid])
                        wait["blacklist"][op.param2] = True
                    except:
                        pass

        if op.type == 19:
            if Amid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[Amid])
                    except:
                        pass

        if op.type == 32:
            if op.param3 in Amid:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                  wait["blacklist"][op.param2] = True
                  try:
                      if op.param3 not in wait["blacklist"]:
                          cl.kickoutFromGroup(op.param1,[op.param2])
                          cl.inviteIntoGroup(op.param1,[Amid])
                          k1.kickoutFromGroup(op.param1,[op.param2])
                          sendTextTemplate1(op.param1,"Anjirrr...di cancel")
                  except:
                      pass

        if op.type == 32:
            if wait["backup"] == True:
              if op.param3 in Bots:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                    	pass
                return

        if op.type == 19 or op.type == 32:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in creator:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.acceptGroupInvitation(op.param1)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                    	pass
                return

        if op.type == 19 or op.type == 32:
            if op.param3 in creator:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                cl.findAndAddContactsByMid(op.param3)
                cl.inviteIntoGroup(op.param1,[op.param3])
                cl.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True

        if op.type == 19 or op.type == 32:
            if op.param3 in admin:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                cl.findAndAddContactsByMid(op.param3)
                cl.inviteIntoGroup(op.param1,[op.param3])
                cl.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True

        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass
                
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
               try:
                   cl.kickoutFromGroup(op.param1,[op.param2])
                   cl.sendMessage(op.param1,"そ、[ʙʟᴀᴄᴋʟɪsᴛ]そうですか(｀・ω・´)")
               except:
                   pass

        if op.type == 65:
            if wait["Unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'ɢᴀᴍʙᴀʀʏᴀ ɪʟᴀɴɢ':
                                ginfo = cl.getGroup(at)
                                ika = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "ᴘᴇsᴀɴ ᴅɪʜᴀᴘᴜs\nᴘᴇɴɢɪʀɪᴍ: "
                                ret_ = "ɴᴀᴍᴀ ɢʀᴜᴘ: {}".format(str(ginfo.name))
                                ret_ += "\nᴊᴀᴍ sʜᴀʀᴇ: {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ik = str(ika.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ika.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                           else:
                                ginfo = cl.getGroup(at)
                                ika = cl.getContact(msg_dict[msg_id]["from"])
                                ika1 = "🚹{}".format(str(ika.displayName))
                                ika2 = "🏠:{}".format(str(ginfo.name))
                                ika3 = "🕙{}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                seber = "═══「 ᴘᴇsᴀɴ ᴅɪʜᴀᴘᴜs 」═══\n{}".format(str(msg_dict[msg_id]["text"]))
                                data = {
                                        "type": "flex",
                                        "altText": "CIEee di Urungkan",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
 "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#33ffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ³",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#33ffff"
          },
          {
          "url": "https://obs.line-scdn.net/{}".format(str(ika.pictureStatus)),
            "type": "image",
            "size": "xxs",
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#33ffff"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": ika1,
"weight": "bold",
"color": "#33ffff",
"align": "center",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": ika3, #"🕙"+ datetime.strftime(timeNow,'%H:%M:%S'+"🕙"),
"weight": "bold",
"color": "#ccffff",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {     
       "contents": [           
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#33ffff"
            },
           {
          "type": "text",
"text": ika2, #"{}".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": "#ffff00",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {          
         "contents": [
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#33ffff"
            },
           {
          "text": seber,
           "size": "xxs",
       #   "align": "center",
           "color": "#00ff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          },
         {
        "type": "separator",
        "color": "#33ffff"
         }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
      "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com",
           }, 
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat" #"http://line.me/ti/p/~greetolala999",
            },         
            "flex": 1          
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
        },{
        "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {          
            "contents": [
               {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
    },{
 "type": "text",
"text": "ᴛʜᴀɴᴋᴢ ғᴏʀ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "sᴜᴘᴏʀᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴀᴍ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator", #batas APK
        "color": "#33ffff"     
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
                                cl.postTemplate(at, data)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["Unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "╔══「✯sᴛɪᴄᴋᴇʀ ɪɴғᴏ✯」\n"
                                ret_ += "┣[]►🚹: {}".format(str(ryan.displayName))
                                ret_ += "\n┣[]►🏠: {}".format(str(ginfo.name))
                                ret_ += "\n┣[]►🕘: {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\n╚══「✯ᴜɴsᴇɴᴅ ғɪɴɪsʜ✯」"
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                sendTextTemplate2(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'ɢᴀᴍʙᴀʀʏᴀ ᴅɪʙᴀᴡᴀʜ',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n╔══「✯sᴛɪᴄᴋᴇʀ ɪɴғᴏ✯]"
                   ret_ += "\n┣[]►sᴛɪᴄᴋᴇʀ ɪᴅ: {}".format(stk_id)
                   ret_ += "\n┣[]►sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ: {}".format(stk_ver)
                   ret_ += "\n┣[]►sᴛɪᴄᴋᴇʀ: {}".format(pkg_id)
                   ret_ += "\n┣[]►ᴜʀʟ:{}".format(pkg_id)
                   ret_ += "\n╚══「✯ᴜɴsᴇɴᴅ ғɪɴɪsʜ✯」"
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
#____________________________________________________________________
        if op.type == 17:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
             #   cl.updateGroup(group)
                contact = cl.getContact(op.param2)
                cover = cl.getProfileCoverURL(op.param2)
                welcomeMembers(op.param1, [op.param2])
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                data = {
                                       "type": "flex",
                                       "altText": "G⃠R⃠E⃠E⃠T⃠",
                                       "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true", 
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.gifer.com/Ui00.gif", #https://www.jimphicdesigns.com/downloads/imgs-mockup/bouncy-ball-change-colors-animation.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "ᴡᴇʟᴄᴏᴍᴇ", 
"align": "center",
"color": "#000000",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "19px",
"backgroundColor": "#ffd700",
"offsetStart": "20px",
"height": "14px",
"width": "45px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.gifer.com/THMv.gif", #https://thumbs.gfycat.com/RawThirstyJanenschia-size_restricted.gif",
"size": "full",
"action": {
"type": "uri",
"uri": "https://wa.me/6282135759022",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "13px",
"offsetStart": "115px",
"height": "43px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/timeline",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~slanker123456",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/__TRSC_OLALA__",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "37px",
"offsetStart": "14px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "⏰"+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#93ff00",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "128px",
"backgroundColor": "#4b4b4b",
"offsetStart": "80px",
"height": "16px",
"width": "61px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🚺{} ".format(cl.getContact(op.param2).displayName),
"weight": "bold",
"color": "#93ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "148px",
#"backgroundColor": "#000000",
"offsetStart": "20px",
"height": "18px",
"width": "121px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": wait["welcome"],
"weight": "bold",
"color": "#ff0000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "165px",
#"backgroundColor": "#ac00c8",
"offsetStart": "20px",
"height": "16px",
"width": "125px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true", 
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.gifer.com/Ui00.gif", #https://www.jimphicdesigns.com/downloads/imgs-mockup/bouncy-ball-change-colors-animation.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "ᴡᴇʟᴄᴏᴍᴇ", 
"align": "center",
"color": "#000000",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "19px",
"backgroundColor": "#ffd700",
"offsetStart": "20px",
"height": "14px",
"width": "45px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.gifer.com/THMv.gif", #https://thumbs.gfycat.com/RawThirstyJanenschia-size_restricted.gif",
"size": "full",
"action": {
"type": "uri",
"uri": "https://wa.me/6282135759022",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "13px",
"offsetStart": "115px",
"height": "43px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
"size": "full",
"action": {
"type": "uri",
"uri": "https://youtube.com",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/chat",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/cameraRoll/multi"
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "37px",
"offsetStart": "14px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🏡ɢʀᴏᴜᴘ",
"weight": "bold",
"color": "#93ff00",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "128px",
"backgroundColor": "#4b4b4b",
"offsetStart": "90px",
"height": "16px",
"width": "52px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🚺{} ".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": "#93ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "148px",
#"backgroundColor": "#000000",
"offsetStart": "20px",
"height": "18px",
"width": "121px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🏠{}".format(ginfo.name),
"weight": "bold",
"color": "#ff0000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "165px",
#"backgroundColor": "#ac00c8",
"offsetStart": "20px",
"height": "16px",
"width": "125px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
                cl.postTemplate(op.param1, data)
        if op.type == 15:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
              #  cl.updateGroup(group)
                contact = cl.getContact(op.param2)
                cover = cl.getProfileCoverURL(op.param2)
                leaveMembers(op.param1, [op.param2])
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                data = {
                                       "type": "flex",
                                       "altText": "G⃠R⃠E⃠E⃠T⃠",
                                       "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true", 
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.gifer.com/Ui00.gif", #https://www.jimphicdesigns.com/downloads/imgs-mockup/bouncy-ball-change-colors-animation.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "ᴀᴜᴛᴏʟᴇᴀᴠᴇ", 
"align": "center",
"color": "#000000",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "19px",
"backgroundColor": "#ffd700",
"offsetStart": "20px",
"height": "14px",
"width": "57px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.gifer.com/THMv.gif", #https://thumbs.gfycat.com/RawThirstyJanenschia-size_restricted.gif",
"size": "full",
"action": {
"type": "uri",
"uri": "https://wa.me/6282135759022",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "13px",
"offsetStart": "115px",
"height": "43px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/timeline",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~slanker123456",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/__TRSC_OLALA__",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "37px",
"offsetStart": "14px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "⏰"+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#93ff00",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "128px",
"backgroundColor": "#4b4b4b",
"offsetStart": "80px",
"height": "16px",
"width": "61px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🚺{} ".format(cl.getContact(op.param2).displayName),
"weight": "bold",
"color": "#93ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "148px",
#"backgroundColor": "#000000",
"offsetStart": "20px",
"height": "18px",
"width": "121px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": wait["autoLeave"],
"weight": "bold",
"color": "#ff0000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "165px",
#"backgroundColor": "#ac00c8",
"offsetStart": "20px",
"height": "16px",
"width": "125px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true", 
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.gifer.com/Ui00.gif", #https://www.jimphicdesigns.com/downloads/imgs-mockup/bouncy-ball-change-colors-animation.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "ᴀᴜᴛᴏʟᴇᴀᴠᴇ", 
"align": "center",
"color": "#000000",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "19px",
"backgroundColor": "#ffd700",
"offsetStart": "20px",
"height": "14px",
"width": "57px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.gifer.com/THMv.gif", #https://thumbs.gfycat.com/RawThirstyJanenschia-size_restricted.gif",
"size": "full",
"action": {
"type": "uri",
"uri": "https://wa.me/6282135759022",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "13px",
"offsetStart": "115px",
"height": "43px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
"size": "full",
"action": {
"type": "uri",
"uri": "https://youtube.com",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/chat",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/cameraRoll/multi"
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "37px",
"offsetStart": "14px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🏡ɢʀᴏᴜᴘ",
"weight": "bold",
"color": "#93ff00",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "128px",
"backgroundColor": "#4b4b4b",
"offsetStart": "90px",
"height": "16px",
"width": "52px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🚺{} ".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": "#93ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "148px",
#"backgroundColor": "#000000",
"offsetStart": "20px",
"height": "18px",
"width": "121px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🏠{}".format(ginfo.name),
"weight": "bold",
"color": "#ff0000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "165px",
#"backgroundColor": "#ac00c8",
"offsetStart": "20px",
"height": "16px",
"width": "125px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
                cl.postTemplate(op.param1, data)

        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        cover = cl.getProfileCoverURL(op.param2)
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        data = {
                                       "type": "flex",
                                       "altText": "G⃠R⃠E⃠E⃠T⃠",
                                       "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://gifimage.net/wp-content/uploads/2018/06/ukuran-gif-dp-bbm-5.gif", 
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.gifer.com/Ui00.gif",
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",  #"https://em.wattpad.com/4c7e5d80bb78b4c9abde154708b4efdb4e71c0c6/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f6b63787836516f3833615a7a43413d3d2d3639323032383336312e313538306535356565336436353532663138343830393632343530302e676966?s=fit&w=720&h=720", #https://thumbs.gfycat.com/WickedMeekGazelle-size_restricted.gif",
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "21px",
"offsetStart": "21px",
"height": "157px",
"width": "117px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://em.wattpad.com/4c7e5d80bb78b4c9abde154708b4efdb4e71c0c6/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f6b63787836516f3833615a7a43413d3d2d3639323032383336312e313538306535356565336436353532663138343830393632343530302e676966?s=fit&w=720&h=720",
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "27px",
"offsetStart": "27px",
"height": "145px",
"width": "105px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "27px",
"offsetStart": "27px",
"height": "145px",
"width": "105px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "text",
"text": "ᴄᴄᴛᴠ", 
"align": "center",
"color": "#000000",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "29px",
"backgroundColor": "#ffd700",
"offsetStart": "30px",
"height": "13px",
"width": "34px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/timeline",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~slanker123456",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/__TRSC_OLALA__",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "42px",
"offsetStart": "24px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "⏰"+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#93ff00",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "3px",
"offsetTop": "120px",
"backgroundColor": "#4b4b4b",
"offsetStart": "70px",
"height": "16px",
"width": "61px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": wait["mention"],
"weight": "bold",
"color": "#93ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "3px",
"offsetTop": "138px",
"backgroundColor": "#4b4b4b",
"offsetStart": "47px",
"height": "16px",
"width": "84px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🚹{} ".format(cl.getContact(op.param2).displayName),
"weight": "bold",
"color": "#ff0000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "155px",
#"backgroundColor": "#ac00c8",
"offsetStart": "29px",
"height": "16px",
"width": "105px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
                        cl.postTemplate(op.param1, data),
#========={{{{{MENTION}}}}}===========
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if settings ["Aip"] == True:
                if msg.text in [".tes","@zona","!otong","!curut","Cleanse","!cleanse",".cleanse","zona","!kickall",".kickall","mayhem","Ratakan","bubarkan","Nuke","nuke",".nuke","Bypass","bypass",".bypass","#bypass","#jancok","hancurkan","!malam","winebot",".malam","bubar",".bubar","86"]:
                    cl.kickoutFromGroup(receiver,[sender])
            if wait["selfbot"] == True:
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              cl.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              try:
                                  cl.kickoutFromGroup(msg.to, [msg._from])
                              except:
                                  try:
                                  	cl.kickoutFromGroup(msg.to, [msg._from])
                                  except:
                                      pass
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   cover = cl.getProfileCoverURL(sender)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           data = {
                                       "type": "flex",
                                       "altText": "G⃠R⃠E⃠E⃠T⃠",
                                       "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true", 
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.gifer.com/Ui00.gif", #"https://www.jimphicdesigns.com/downloads/imgs-mockup/bouncy-ball-change-colors-animation.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "ʀᴇsᴘᴏɴ", 
"align": "center",
"color": "#000000",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "19px",
"backgroundColor": "#ffd700",
"offsetStart": "20px",
"height": "14px",
"width": "45px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.gifer.com/THMv.gif", #https://thumbs.gfycat.com/RawThirstyJanenschia-size_restricted.gif",
"size": "full",
"action": {
"type": "uri",
"uri": "https://wa.me/6282135759022",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "13px",
"offsetStart": "115px",
"height": "43px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/timeline",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~slanker123456",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/__TRSC_OLALA__",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "37px",
"offsetStart": "14px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "⏰"+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#93ff00",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "128px",
"backgroundColor": "#4b4b4b",
"offsetStart": "80px",
"height": "16px",
"width": "61px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🚹{} ".format(contact.displayName),
"weight": "bold",
"color": "#93ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "148px",
#"backgroundColor": "#000000",
"offsetStart": "20px",
"height": "18px",
"width": "121px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": wait["Respontag"],
"weight": "bold",
"color": "#ff0000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "165px",
#"backgroundColor": "#ac00c8",
"offsetStart": "20px",
"height": "16px",
"width": "121px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
                           cl.postTemplate(to, data)
                        #   cl.sendMessage(msg.to, None, contentMetadata={"STKID":"155808605","STKPKGID":"6700627","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           sendTextTemplate1(msg.to,"j̸͟͞a̸͟͞n̸͟͞g̸͟͞a̸͟͞n̸͟͞ t̸͟͞a̸͟͞g̸͟͞ g̸͟͞u̸͟͞a̸͟͞ n̸͟͞a̸͟͞n̸͟͞t̸͟͞i̸͟͞ k̸͟͞e̸͟͞j̸͟͞i̸͟͞t̸͟͞a̸͟͞k̸͟͞")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:
                   contact = cl.getContact(msg._from)
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   cover = cl.getProfileCoverURL(sender)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           data = {
                                       "type": "flex",
                                       "altText": "G⃠R⃠E⃠E⃠T⃠",
                                       "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.gifer.com/Ui00.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.jimphicdesigns.com/downloads/imgs-mockup/bouncy-ball-change-colors-animation.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "ʀᴇsᴘᴏɴ²", 
"align": "center",
"color": "#000000",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "19px",
"backgroundColor": "#ffd700",
"offsetStart": "20px",
"height": "14px",
"width": "45px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.gifer.com/THMv.gif", #https://thumbs.gfycat.com/RawThirstyJanenschia-size_restricted.gif",
"size": "full",
"action": {
"type": "uri",
"uri": "https://wa.me/6282135759022",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "13px",
"offsetStart": "115px",
"height": "43px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/timeline",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~slanker123456",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/__TRSC_OLALA__",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "37px",
"offsetStart": "14px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "⏰"+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#93ff00",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "128px",
"backgroundColor": "#4b4b4b",
"offsetStart": "80px",
"height": "16px",
"width": "61px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🚹{} ".format(contact.displayName),
"weight": "bold",
"color": "#93ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "148px",
#"backgroundColor": "#000000",
"offsetStart": "20px",
"height": "18px",
"width": "121px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": wait["Respontag2"],
"weight": "bold",
"color": "#ff0000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "165px",
#"backgroundColor": "#ac00c8",
"offsetStart": "20px",
"height": "16px",
"width": "121px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
                           cl.postTemplate(to, data)
                           break

               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n°❂° STKID : " + msg.contentMetadata["STKID"] + "\n°❂° STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n°❂° STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"°❂° Nama : " + msg.contentMetadata["displayName"] + "\n°❂° MID : " + msg.contentMetadata["mid"] + "\n°❂° Status Msg : " + contact.statusMessage + "\n°❂° Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 and msg.toType == 2:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            elif msg.toType == 1:
                to = receiver
            elif msg.toType == 2:
                to = receiver
            if msg.contentType == 0:
                to = receiver
            if msg.contentType == 16:
              if settings["checkPost"] == True:
                url = msg.contentMetadata["postEndUrl"]
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                cl.likePost(url[25:58], url[66:], likeType=1004)
                cl.createComment(url[25:58], url[66:], wait["comment"])
                cover = cl.getProfileCoverURL(sender)
                data = {
                                "type": "flex",
                                "altText": "G⃠R⃠E⃠E⃠T⃠",
                                "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "nano",
"body": {
"backgroundColor": "#ff0000",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 1
"url": "https://i.gifer.com/Ui00.gif",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "4:4",
"gravity": "bottom",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:2",
"offsetTop": "0px",
"action": {
"uri": "http://www.mawoenabraids.com/images/ajax-circular.gif",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "8px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "110px",
"width": "110px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:2",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "8px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "110px",
"width": "110px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🕘 "+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#ffff00",
"align": "center",
"size": "xxs",
"offsetTop": "3px"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "9px",
#"backgroundColor": "#33ffff",
"offsetStart": "7px",
"height": "20px",
"width": "75px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #weh
{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~slanker123456",   
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/__TRSC_OLALA__",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/cameraRoll/multi"
},
"flex": 0
},{
"type": "image",
 "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/chat",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "9px",
"offsetStart": "90px",
"height": "200px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "👍ʟɪᴋᴇ sᴜᴄᴄᴇs",
"weight": "bold",
"color": "#ff0000",
"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "84px",
#"backgroundColor": "#ff0000",
"offsetStart": "7px",
"height": "15px",
"width": "75px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#00ffff",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "98px",
#"backgroundColor": "#0000ff",
"offsetStart": "7px",
"height": "15px",
"width": "85px"
}
],
#"backgroundColor": "#ff0000",
"paddingAll": "0px"
}
},
]
}
}
                cl.postTemplate(to, data)
            if msg.contentType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            sendTextTemplate1(msg.to, "ʟɪsᴛ ʙʟ")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  cl.findAndAddContactsByMid(target)
                                  cl.inviteIntoGroup(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 sᴜᴋsᴇs ɪɴᴠɪᴛᴇ 」\nɴᴀᴍᴀ"
                                  ret_ = "ᴋᴇᴛɪᴋ ɪɴᴠɪᴛᴇ ᴏғғ ᴊɪᴋᴀ sᴜᴅᴀʜ ᴅᴏɴᴇ"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  sendTextTemplate1(msg.to,"ᴀɴᴅᴀ ᴛᴇʀᴋᴇɴᴀ sᴛʀᴜᴋ")
                                  wait["invite"] = False
                                  break
                                  
               if msg.contentType == 13:
                 if wait["Invi"] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = cl.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                cl.sendMessage(msg.to,"-> " + _name + " was here")
                                wait["Invi"] = False
                                break         
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoGroup(msg.to,[target])
                                sendTextTemplate1(msg.to,"ᴅᴏɴᴇ ᴊᴇᴘɪᴛ ᴊᴏᴍʙʟᴏ\n➡" + _name)
                                wait["Invi"] = False
                                break
#=============MEDIA FOTOBOT=============

               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','video.mp4')
                            sendTextTemplate1(msg.to,"Send gambarnya...")
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','image.jpg')
                            cl.nadyacantikimut('video.mp4','image.jpg')
                            sendTextTemplate1(msg.to,"ᴠɪᴅᴇᴏ ᴘʀᴏғɪʟᴇ ᴅᴏɴᴇ")
               if msg.contentType == 1:
                  if msg._from in admin:
                     if settings["Addimage"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate1(msg.to, "ᴅᴏɴᴇ ɢᴀᴍʙᴀʀ {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
               if msg.contentType == 2:
                  if msg._from in admin:
                     if settings["Addvideo"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate1(msg.to, "Berhasil menambahkan video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                  if msg._from in admin:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate1(msg.to, "ᴅᴏɴᴇ sᴛɪᴄᴋᴇʀ {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                  if msg._from in admin:
                     if settings["Addaudio"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate1(msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      cl.sendChatChecked(msg.to, msg_id)
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               cl.sendSticker(to, spkg, sid)
                         for image in images:
                            if text.lower() == image:
                               cl.sendImage(msg.to, images[image])
                         for audio in audios:
                            if text.lower() == audio:
                               cl.sendAudio(msg.to, audios[audio])
                         for video in videos:
                            if text.lower() == video:
                               cl.sendVideo(msg.to, videos[video])
               if msg.contentType == 13:
                 if msg._from in owner:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        sendTextTemplate1(msg.to,"Already in bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        sendTextTemplate1(msg.to,"Succes add bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        sendTextTemplate1(msg.to,"Succes delete bot")
                    else:
                        wait["dellbots"] = True
                        sendTextTemplate1(msg.to,"Nothing in bot")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        sendTextTemplate1(msg.to,"ᴡᴇs ᴊᴀᴅɪ sᴛᴀғғ")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        sendTextTemplate1(msg.to,"ᴅᴏɴᴇ ᴀᴅᴅsᴛᴀғғ")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        sendTextTemplate1(msg.to,"✅sᴛᴀғғ ᴅɪʜᴀᴘᴜs")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        sendTextTemplate1(msg.to,"❎Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        sendTextTemplate1(msg.to,"✅Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        sendTextTemplate1(msg.to,"ᴅᴏɴᴇ ᴀᴅᴅᴀᴅᴍɪɴ")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        sendTextTemplate1(msg.to,"✅ᴀᴅᴍɪɴ ᴅɪʜᴀᴘᴜs")
                    else:
                        wait["delladmin"] = True
                        sendTextTemplate1(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        sendTextTemplate1(msg.to,"❎Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        sendTextTemplate1(msg.to,"✅Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate1(msg.to,"✅Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        sendTextTemplate1(msg.to,"❎Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        sendTextTemplate1(msg.to,"✅Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        sendTextTemplate2(msg.to,"✅Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate2(msg.to,"✅Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        sendTextTemplate1(msg.to,"❎Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in owner:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            sendTextTemplate1(msg.to, "Succes add picture")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False
               if msg.contentType == 2:
               	if settings["changevp"] == True:
               		contact = cl.getProfile()
               		path = cl.downloadFileURL("https://obs.line-scdn.net/{}".format(contact.pictureStatus))
               		path1 = cl.downloadObjectMsg(msg_id)
               		settings["changevp"] = False
               		changeVideoAndPictureProfile(path, path1)
               		sendTextTemplate1(to, "ᴅᴏɴᴇ vɪᴅᴇᴏ ᴘʀᴏғɪʟᴇ")
               if msg.contentType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     sendTextTemplate1(msg.to, "ᴅᴏɴᴇ ᴘɪᴄᴛ ɢʀᴜᴘ")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if mid in Setmain["RAfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            cl.updateProfilePicture(path)
                            sendTextTemplate1(msg.to,"ғᴏᴛᴏ ʙᴇʀʜᴀsɪʟ")
                        if Amid in Setmain["RAfoto"]:
                            path = k1.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Amid]
                            k1.updateProfilePicture(path1)
                            k1.sendMessage(msg.to,"ғᴏᴛᴏ ʙᴇʀʜᴀsɪʟ ᴅɪ'ʀᴜʙᴀʜ")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = k1.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     k1.updateProfilePicture(path1)
                     k1.sendMessage(msg.to, "✓ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ\nsᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ")


               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path5 = cl.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     cl.updateProfilePicture(path)
                     cl.sendMessage(msg.to, "Sukses..")
               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               sendTextTemplate25(msg.to, str(helpMessage))
                        if cmd == "bot on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                sendTextTemplate1(msg.to, "ʙᴏᴛ ᴡᴇs ᴏɴ")
                        elif cmd == "bot off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                sendTextTemplate25(msg.to, "ʙᴏᴛ ᴡᴇs ᴍᴏᴅᴀʀ")
                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	settings["changevp"] = True
                            	sendTextTemplate1(to, "sʜᴀʀᴇ ᴠɪᴅᴇᴏɴʏᴀ")
                        elif cmd == "help creator":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage1 = helpcreator()
                               sendTextTemplate25(msg.to, str(helpMessage1))
                        elif cmd == "help setting":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = helpsetting()
                               sendTextTemplate25(msg.to, str(helpMessage2))
                        elif cmd == "help media":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage3 = media()
                               sendTextTemplate25(msg.to, str(helpMessage3))
                        elif cmd == "help group":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage4 = helpgroup()       
                               sendTextTemplate25(msg.to, str(helpMessage4))
                        elif cmd == "help admin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage5 = helpadmin()
                               sendTextTemplate25(msg.to, str(helpMessage5))
                        elif cmd == "help ghost":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage6 = helpghost()
                               sendTextTemplate25(msg.to, str(helpMessage6))

                        elif cmd.startswith("rname "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        cl.renameContact(ls,sep[1])
                                        cl.sendReplyMention(msg_id, to, "Succes change @! display name to {}".format(sep[1]), [ls])

                        elif text.lower() == "setting":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                md = ""
                                if settings["checkPost"] == True: md+="║║⏹️ Post : ✅\n"
                                else: md+="║║⏹️ Post : ❌\n"
                                if wait["likeOn"] == True: md+="║║⏹️ Like : ✅\n"
                                else: md+="║║⏹️ Like ❌\n"
                                if wait["contact"] == True: md+="║║⏹️ Contact : ✅\n"
                                else: md+="║║⏹️ Contact : ❌\n"
                                if wait["Mentionkick"] == True: md+="║║⏹️ Notag : ✅\n"
                                else: md+="║║⏹️ Notag : ❌\n"
                                if wait["detectMention"] == True: md+="║║⏹️ Respontag : ✅\n"
                                else: md+="║║⏹️ Respontag : ❌\n"
                                if wait["detectMention2"] == True: md+="║║⏹️ Respontag2 : ✅\n"
                                else: md+="║║⏹️ Respontag2 : ❌\n"
                                if wait["Unsend"] == True: md+="║║⏹️ Unsend : ✅\n"
                                else: md+="║║⏹️ Unsend : ❌\n"
                                if wait["autoAdd"] == True: md+="║║⏹️ Autoadd : ✅\n"
                                else: md+="║║⏹️ Autoadd : ❌\n"
                                if wait["autoLeave"] == True: md+="║║⏹️ Autoleave : ✅\n"
                                else: md+="║║⏹️ Autoleave : ❌\n"
                                if wait["autoJoin"] == True: md+="║║⏹️ Autojoin : ✅\n"
                                else: md+="║║⏹️ Autojoin : ❌\n"
                                if wait["sticker"] == True: md+="║║⏹️ Sticker : ✅\n"
                                else: md+="║║⏹️ Sticker ❌\n"
                                if settings["autoJoinTicket"] == True: md+="║║⏹️ Jointicket : ✅\n"
                                else: md+="║║⏹️ Jointicket : ❌\n"
                                if wait["autoReject"] == True: md+="║║⏹️ Autoreject : ✅\n"
                                else: md+="║║⏹️ Autoreject : ❌\n"
                                if wait["autoBlock"] == True: md+="║║⏹️ Autoblock : ✅\n"
                                else: md+="║║⏹️ Autoblock : ❌\n"
                                if settings["welcome"] == True: md+="║║⏹️ Welcome : ✅\n"
                                else: md+="║║⏹️ Welcome : ❌\n"
                                sendTextTemplate28(msg.to, "╔═════════🚫\n"+ md +"╚═════════🚫")

                        elif text.lower() == "mid":
                          if wait["selfbot"] == True:
                               middd = "Name : " +cl.getContact(msg._from).displayName + "\nMid : " +msg._from
                               cl.sendMessage(msg.to,middd)

                        elif ("Gname " in msg.text):
                          if msg._from in admin:
                              X = cl.getGroup(msg.to)
                              X.name = msg.text.replace("Gname ","")
                              cl.updateGroup(X)

                        elif "Gruppict" in msg.text:
                          if msg._from in admin:
                                group = cl.getGroup(msg.to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                cl.sendImageWithURL(msg.to,path)

                        elif "Getprofile " in msg.text:
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys() != None:
                                names = re.findall(r'@(\w+)', msg.text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    try:
                                        profile = cl.getContact(mention['M'])
                                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+profile.pictureStatus)
                                    except Exception as e:
                                        pass

                        elif "Getinfo " in msg.text:
                          if msg._from in admin:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = cl.getContact(key1)
                            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            try:
                                sendTextTemplate1(msg.to,"Nama:\n" + contact.displayName)
                                sendTextTemplate1(msg.to,"Bio:\n" + contact.statusMessage)
                                cl.sendImageWithURL(msg.to,image)
                            except:
                                pass

                        elif cmd == 'listblock':
                          if msg._from in admin:
                            blockedlist = cl.getBlockedContactIds()
                            kontak = cl.getContacts(blockedlist)
                            num=1
                            msgs="List Blocked"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Blocked : %i" % len(kontak)
                            sendTextTemplate2(to, msgs)

                        elif "Getbio " in msg.text:
                          if msg._from in admin:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = cl.getContact(key1)
                            try:
                                sendTextTemplate1(msg.to,contact.statusMessage)
                            except:
                                sendTextTemplate1(msg.to,"⟦ʙɪᴏ ᴇᴍᴘᴛʏ⟧")

                        elif text.lower() == 'kalender':
                          if msg._from in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                            sendTextTemplate2(msg.to, readTime)

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': Amid}, contentType=13)

                        elif cmd == "myname":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            sendTextTemplate1(to, "[ ᴅɪsᴘʟᴀʏ ɴᴀᴍᴇ ]\n{}".format(contact.displayName))

                        elif cmd == "mybio":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            sendTextTemplate1(to, "[ sᴛᴀᴛᴜs ʟɪɴᴇ ]\n{}".format(contact.statusMessage))

                        elif cmd == "Picture":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            cl.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))

                        elif cmd == "myvideo":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            cl.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))

                        elif cmd == "mycover":
                          if msg._from in admin:
                            channel = cl.getProfileCoverURL(sender)
                            path = str(channel)
                            cl.sendImageWithURL(to, path)

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   sendTextTemplate00(group," " + str(pesan))

                        elif cmd == "Profile":
                          if msg._from in admin:
                            text = "~ Profile ~"
                            contact = cl.getContact(sender)
                            cover = cl.getProfileCoverURL(sender)
                            result = "╔══[ Details Profile ]"
                            result += "\n├≽ Display Name : @!"
                            result += "\n├≽ Mid : {}".format(contact.mid)
                            result += "\n├≽ Status Message : {}".format(contact.statusMessage)
                            result += "\n├≽ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            result += "\n├≽ Cover : {}".format(str(cover))
                            result += "\n╚══[ Finish ]"
                            cl.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            cl.sendMentionWithFooter(to, text, result, [sender])

                        elif cmd.startswith("block"):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.blockContact(ls)
                                cl.generateReplyMessage(msg.id)
                                cl.sendReplyMessage(msg.id, to, "sᴜᴋsᴇs ʙʟᴏᴄᴋ ᴋᴏɴᴛᴀᴋ" + str(contact.displayName) + "ᴍᴀsᴜᴋ ᴅᴀғᴛᴀʀ ʙʟᴏᴄᴋʟɪsᴛ")

                        elif cmd.startswith("addme "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.findAndAddContactsByMid(ls)
                                cl.generateReplyMessage(msg.id)
                                cl.sendReplyMessage(msg.id, to, "ʙᴇʀʜᴀsɪʟ ᴀᴅᴅ" + str(contact.displayName) + "ᴋᴜʀɪɴᴇᴍ ᴅᴜʟᴜ ʏᴀᴄʜ")

                        elif "Getmid " in msg.text:
                            if 'MENTION' in msg.contentMetadata.keys() != None:
                                names = re.findall(r'@(\w+)', msg.text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    try:
                                        cl.sendMessage(msg.to,str(mention['M']))
                                    except Exception as e:
                                        pass

                        elif "Contact: " in msg.text:
                           if msg._from in admin:
                              mmid = msg.text.replace("Contact: ","")
                              msg.contentType = 13
                              msg.contentMetadata = {"mid":mmid}
                              cl.sendMessage(msg.to, None, contentMetadata={'mid': mmid}, contentType=13)
                              path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                              image = 'http://dl.profile.line.naver.jp'+path
                              cl.sendImageWithURL(msg.to, image)

                        elif cmd.startswith("kontak"):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    cl.sendContact(to,str(ls))

                        elif cmd.startswith("ppvideo"):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                    cl.sendVideoWithURL(to, str(path))

                        elif text.lower() == "santet mantan":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   sendTextTemplate1(msg.to,"mantan berhasil disantet")
                               except:
                                   pass

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               sendTextTemplate1(msg.to, "☛ Nama : "+str(mi.displayName)+"\n☛ Mid : " +key1+"\n☛ Status Msg"+str(mi.statusMessage))
                               sendTextTemplate1(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "key Now「 " + str(wait["keyCommand"]) + " 」")

                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendTextTemplate1(msg.to, "ɢᴀɢᴀʟ ɴɢᴜʙᴀʜ ᴋᴇʏ")
                               else:
                                   wait["keyCommand"] = str(key).lower()
                                   sendTextTemplate1(msg.to, "sᴜᴋsᴇs ɢᴀɴᴛɪ ᴋᴇʏ「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               wait["keyCommand"]=""
                               sendTextTemplate1(msg.to, "succes resset key command")

                        elif cmd == "reboot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "ʀᴇsᴛᴀʀᴛ ʙᴏᴛ")
                               wait["restartPoint"] = msg.to
                               restartBot()
                               sendTextTemplate1(msg.to, "ᴅᴏɴᴇ ʙᴏs")

                        elif cmd == "byeme":
                              if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                cover = cl.getProfileCoverURL(sender)
                                G = cl.getGroup(to)
                                data = {
                                "type": "flex",
                                "altText": "G⃠R⃠E⃠E⃠T⃠",
                                "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "nano",
"body": {
"backgroundColor": "#ff0000",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 1
"url": "https://des.chinabrands.com/uploads/pdm-desc-pic/Clothing/image/2017/05/10/1494385657631195.gif",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "4:4",
"gravity": "bottom",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": cover, #https://obs.line-scdn.net/{}".format(cl.getContact(sender).displayName),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:2",
"offsetTop": "0px",
"action": {
"uri": "http://www.mawoenabraids.com/images/ajax-circular.gif",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "8px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "110px",
"width": "110px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:2",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "8px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "110px",
"width": "110px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🖐️ ɪᴢɪɴ ᴘᴀᴍɪᴛ",
"weight": "bold",
"color": "#ff0000",
"align": "center",
"size": "xxs",
"offsetTop": "3px"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "9px",
#"backgroundColor": "#33ffff",
"offsetStart": "7px",
"height": "20px",
"width": "80px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #weh
{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~slanker123456",   
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/__TRSC_OLALA__",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/cameraRoll/multi"
},
"flex": 0
},{
"type": "image",
 "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/chat",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "9px",
"offsetStart": "90px",
"height": "200px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🕘 "+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#ff00ff",
"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "87px",
#"backgroundColor": "#ff0000",
"offsetStart": "1px",
"height": "15px",
"width": "75px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#ff00ff",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "98px",
#"backgroundColor": "#0000ff",
"offsetStart": "7px",
"height": "15px",
"width": "90px"
}
],
#"backgroundColor": "#ff0000",
"paddingAll": "0px"
}
},
]
}
}
                                cl.postTemplate(to, data)
                                cl.leaveGroup(to)

                        elif text.lower() == "leaveall":
                            if msg._from in admin:
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    cl.leaveGroup(i)
                                    print ("Pamit semua group")

                        elif text.lower() == "rejectall":
                            if msg._from in admin:
                                ginvited = cl.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                    sendTextTemplate1(msg.to, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                else:
                                    sendTextTemplate1(msg.to, "Nothing Invited")

                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "🔽ʙᴏᴛ ʀᴜɴ : " +waktu(eltime)
                               sendTextTemplate1(msg.to,bot)

                        elif cmd == "listpending":
                          if wait["selfbot"] == True:
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                ret_ = "╭───「 Pending List 」"
                                no = 0
                                if group.invitee is None or group.invitee == []:
                                    return cl.sendReplyMessage(msg_id, to, "Tidak ada pendingan")
                                else:
                                    for pending in group.invitee:
                                        no += 1
                                        ret_ += "\n├≽ {}. {}".format(str(no), str(pending.displayName))
                                    ret_ += "\n╰───「 Total {} Pending 」".format(str(len(group.invitee)))
                                    #cl.sendReplyMessage(msg_id, to, str(ret_))
                                    data = {
                                        "type": "text",
                                        "text": "{}".format(str(ret_)),
                                        "sentBy": {
                                            "label": " ♀ɢʀᴇᴇᴛ ʙᴏᴛs♀",
                                            "iconUrl": "https://cdn140.picsart.com/296661791123201.gif?c256x256",
                                            "linkUrl": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f"
                                        }
                                    }
                                    cl.postTemplate(to, data)



                        elif cmd == "listmember":
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                num = 0
                                ret_ = "╔══[ List Member ]"
                                for contact in group.members:
                                    num += 1
                                    ret_ += "\n╠ {}. {}".format(num, contact.displayName)
                                ret_ += "\n╚══[ Total {} Members]".format(len(group.members))
                                sendTextTemplate2(to, ret_)

                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                sendTextTemplate23(msg.to, "  •⌻「Grup Info」⌻•\n\n Nama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                sendTextTemplate2(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                sendTextTemplate23(msg.to, str(e))

                        elif cmd.startswith("infogrup"):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(danil.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╔══「 Info Group 」"
                                ret_ += "\n┣[]► Nama Group : {}".format(G.name)
                                ret_ += "\n┣[]► ID Group : {}".format(G.id)
                                ret_ += "\n┣[]► Pembuat : {}".format(gCreator)
                                ret_ += "\n┣[]► Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n┣[]► Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n┣[]► Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┣[]► Group Qr : {}".format(gQr)
                                ret_ += "\n┣[]► Group Ticket : {}".format(gTicket)
                                ret_ += "\n╚══「 Info Finish 」"
                                sendTextTemplate23(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem"):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = denal.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n┣[]► "+ str(no) + ". " + mem.displayName
                                sendTextTemplate23(to,"╔══「 Group Info 」\n┣[]► Group Name : " + str(G.name) + "\n┣══「Member List」" + ret_ + "\n╚══「Total %i Members」" % len(G.members))
                            except:
                                pass
                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠[]► " + str(a) + ". " +G.displayName+ "\n"
                               sendTextTemplate23(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")
#invite for mention

                        elif "Invite " in msg.text:
                            if msg._from in admin:                                                                                                                                       
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┣[]► " + str(a) + ". " +G.name+ "\n"
                               sendTextTemplate23(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "glistjs1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = k1.getGroupIdsJoined()
                               for i in gid:
                                   G = k1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┣[]► " + str(a) + ". " +G.name+ "\n"
                               k1.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd.startswith("k1-invit "):
                             if msg._from in admin:
                                sep = msg.text.split(" ")
                                number = msg.text.replace(sep[0] + " ","")
                                bolo = k1.getGroupIdsJoined()
                                try:
                                    group = bolo[int(number)-1+0]
                                    G = k1.getGroup(group)
                                    gid = G.id
                                    no = 0 + 1
                                    k1.findAndAddContactsByMid(sender)
                                    k1.inviteIntoGroup(gid, [sender])
                                    k1.sendMessage(to,"✓sᴜᴄᴄᴇss ɪɴᴠɪᴛᴇ: "+str(G.name))
                                except Exception as e:
                                    k1.sendMessage(msg.to, str(e))
#addbots for 7 bots

                        elif cmd == "addbot":
                            try:
                                cl.sendMessage(msg.to, "⏳ᴛᴜɴɢɢᴜ sᴇʟᴀᴍᴀ 5 ᴍᴇɴɪᴛ")
                                cl.findAndAddContactsByMid(Amid)
                                time.sleep(5)
                                cl.findAndAddContactsByMid(Bmid)
                                time.sleep(5)
                                cl.findAndAddContactsByMid(Zmid)
                                time.sleep(5)
                                k1.findAndAddContactsByMid(mid)
                                time.sleep(5)
                                k1.findAndAddContactsByMid(Bmid)
                                time.sleep(5)
                                k1.findAndAddContactsByMid(Zmid)
                                time.sleep(5)
                                cl.sendMessage(to, "✓sᴜᴄᴄᴇss") 
                                k1.sendMessage(to, "✓sᴜᴄᴄᴇss")
                            except:
                                cl.sendMessage(to, "✓sᴜᴄᴄᴇss") 
                                k1.sendMessage(to, "✓sᴜᴄᴄᴇss")

                        if cmd == "friendlist": 
                          if msg._from in admin:
                            contactlist = k1.getAllContactIds()
                            kontak = k1.getContacts(contactlist)
                            num=1
                            msgs="『FRIENDLIST』\n\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friend : %i" % len(kontak)
                            k1.sendMessage(to, msgs)

                        elif cmd == "gurl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                cl.sendMessage(msg.to,"line://ti/g/" + gurl)

                        elif cmd == "open qr":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   if X.preventedJoinByTicket == True:
                                       X.preventedJoinByTicket = False
                                       cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                cl.sendMessage(msg.to, "Nama : "+str(X.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "close qr":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   sendTextTemplate1(msg.to, "Url Closed")

                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  sendTextTemplate1(to, "ᴛᴏᴛᴀʟ {} ɢʀᴏᴜᴘ".format(str(len(ginvited))))
                              else:
                                  sendTextTemplate1(to, "ʙᴇʀsɪʜ")
#===========BOT UPDATE============#
                        elif cmd == "upgrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendTextTemplate1(msg.to,"☛ sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")

                        elif cmd == "myfoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                sendTextTemplate1(msg.to,"☛ sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")
                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate(msg.to, "╔══════════════\n╠[]► sɪᴅᴇʀ ᴅɪʜɪᴅᴜᴘᴋᴀɴ\n╚══════════════\n╔══════════════\n╠[]► ᴅᴀᴛᴇ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠[]► ᴛɪᴍᴇ :"+ datetime.strftime(timeNow,'%H:%M:%S')+"\n╚══════════════")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate(msg.to, "╔══════════════\n╠[]► sɪᴅᴇʀ ᴅɪᴍᴀᴛɪᴋᴀɴ\n╚══════════════\n╔══════════════\n╠[]► ᴅᴀᴛᴇ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠[]► ᴛɪᴍᴇ :"+ datetime.strftime(timeNow,'%H:%M:%S')+"\n╚══════════════")
                              else:
                                  sendTextTemplate(msg.to, "╔══════════════\n╠[]► sɪᴅᴇʀ ᴅɪ ᴏғғ\n╚══════════════")
#=========== [ Hiburan] ============#
                        elif cmd.startswith("cctv metro"):
                          if msg._from in admin:
                            ret_ = "Daftar Cctv Pantura\n"
                            ret_ += "248 = Alternatif - Cibubur\n119 = Ancol - bandara\n238 = Asia afrika - Bandung"
                            ret_ += "\n276 = Asia afrika - Sudirman\n295 = Bandengan - kota\n294 = Bandengan - Selatan"
                            ret_ += "\n102 = Buncit raya\n272 = Bundaran - HI\n93 = Cideng barat\n289 = Cikini raya"
                            ret_ += "\n175 = Ciloto - Puncak\n142 = Daan mogot - Grogol\n143 = Daan mogot - Pesing"
                            ret_ += "\n204 = Mangga besar\n319 = Margaguna raya\n326 = Margonda raya\n309 = Mas Mansyur - Tn. Abang"
                            ret_ += "\n64 = Matraman\n140 = Matraman - Salemba\n284 = Metro Pdk. Indah\n191 = MT Haryono - Pancoran\n160 = Pancoran barat"
                            ret_ += "\n331 = Pejompongan - Slipi\n332 = Pejompongan - Sudirman\n312 = Perempatan pramuka\n171 = Permata hijau - Panjang"
                            ret_ += "\n223 = Pramuka - Matraman\n222 = Pramuka raya\n314 = Pramuka raya - jl. Tambak\n313 = Pramuka - Salemba raya\n130 = Puncak raya KM84"
                            ret_ += "\n318 = Radio dalam raya\n328 = RS Fatmawati - TB\n274 = Senayan city\n132 = Slipi - Palmerah\n133 = Slipi - Tomang"
                            ret_ += "\n162 = S Parman - Grogol\n324 = Sudirman - Blok M\n18 = Sudirman - Dukuh atas\n325 = Sudirman - Semanggi\n112 = Sudirman - Setiabudi"
                            ret_ += "\n246 = Sudirman - Thamrin\n320 = Sultan agung - Sudirman\n100 = Suryo pranoto\n220 = Tanjung duren\n301 = Tol kebon jeruk"
                            ret_ += "\n41 = Tomang/Simpang\n159 = Tugu Pancoran\n205 = Yos Sudarso - Cawang\n206 = Yos Sudarso - Tj. Priuk"
                            ret_ += "\nUntuk melihat cctv,\nKetik Lihat (Nomer)"                            
                            sendTextTemplate2(to, ret_)

                        elif cmd.startswith("lihat"):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            cct = msg.text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                                r = s.get("http://lewatmana.com/cam/{}/bundaran-hi/".format(urllib.parse.quote(cct)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                try:
                                    ret_ = "LIPUTAN CCTV TERKINI \nDaerah "
                                    ret_ += soup.select("[class~=cam-viewer-title]")[0].text
                                    ret_ += "\nCctv update per 5 menit"
                                    vid = soup.find('source')['src']
                                    ret = "Ketik Lihat nomer cctv selanjutnya"
                                    sendTextTemplate1(to, ret_)
                                    cl.sendVideoWithURL(to, vid)
                                except:
                                    sendTextTemplate1(to, "🚦Data cctv tidak ditemukan!")

#============Comen Tag=========
                        elif cmd in ('desah','tagall','bojo'):
                              if msg._from in admin:
                                try:group = cl.getGroup(to);midMembers = [contact.mid for contact in group.members]
                                except:group = cl.getRoom(to);midMembers = [contact.mid for contact in group.contacts]
                                midSelect = len(midMembers)//20
                                for mentionMembers in range(midSelect+1):
                                    no = 0
                                    ret_ = "╭━━━━━╦════════╦━━━━━╮\n│╭━━━━━━━━━━━━━━━━━━━╮\n╠❂࿇➢A̸͟͞B̸͟͞S̸͟͞E̸͟͞N̸͟͞ P̸͟͞A̸͟͞R̸͟͞A̸͟͞ J̸͟͞O̸͟͞N̸͟͞E̸͟͞S̸͟͞\n│╰━━━━━━━━━━━━━━━━━━━╯\n│╭━━━━━━━━━━━━━━━━━━━╮"
                                    dataMid = []
                                    if msg.toType == 2:
                                        for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"╠❂➢ {}. @!".format(str(no))
                                        ret_ += "\n│╰━━━━━━━━━━━━━━━━━━━╯\n│╭━━━━━━━━━━━━━━━━━━━╮\n╠❂࿇➢T̸͟͞O̸͟͞T̸͟͞A̸͟͞L̸͟͞ :🎏{}🎏J̸͟͞O̸͟͞N̸͟͞E̸͟͞S̸͟͞\n│╰━━━━━━━━━━━━━━━━━━━╯\n╰━━━━━╩════════╩━━━━━╯".format(str(len(dataMid)))
                                        cl.sendReplyMention(msg_id, to, ret_, dataMid)
                                    else:
                                        for dataMention in group.contacts[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"╠❂➢ {}. @!".format(str(no))
                                        ret_ += "\n│╰━━━━━━━━━━━━━━━━━━━━╯\n│╭━━━━━━━━━━━━━━━━━━━╮\n╠❂࿇➢T̸͟͞O̸͟͞T̸͟͞A̸͟͞L̸͟͞ :🎏{}🎏J̸͟͞O̸͟͞N̸͟͞E̸͟͞S̸͟͞\n│╰━━━━━━━━━━━━━━━━━━━━╯\n╰━━━━━╩════════╩━━━━━╯".format(str(len(dataMid)))
                                        cl.sendReplyMention(msg_id, to, ret_, dataMid)
                        elif cmd == "hem" or text.lower() == 'cipok':
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                             group = cl.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Zero \n'
                                cl.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                               start = time.time()
                               sendTextTemplate1("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                               elapsed_time = time.time() - start
                               sendTextTemplate1(msg.to, "%s s" % (elapsed_time))

                        elif cmd.startswith("mp3: "):
                         # if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                sendTextTemplate10(msg.to, "📀ᴍᴜsɪᴋ ᴀᴜᴅɪᴏ")
                                cl.sendAudioWithURL(msg.to, me)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))
                        elif cmd.startswith("clone "):
                           if msg._from in admin:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    ryan = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "「 Clone Profile 」\nTarget nya "
                                    ret_ = "Berhasil clone profile target"
                                    ry = str(ryan.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    cl.sendMessage(msg.to, "Gagal clone profile")
                        elif text.lower() == 'restore':
                           if msg._from in admin:
                              try:
                                  clProfile.displayName = str(myProfile["displayName"])
                                  clProfile.statusMessage = str(myProfile["statusMessage"])
                                  clProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  cl.updateProfileAttribute(8, clProfile.pictureStatus)
                                  cl.updateProfile(clProfile)
                                  cl.sendMessage(msg.to, sender, "「 Restore Profile 」\nNama ", " \nBerhasil restore profile")
                              except:
                                  cl.sendMessage(msg.to, "Gagal restore profile")

                        elif cmd.startswith("smule "):
                          if msg._from in admin:
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split(" ")
                            search = str(count[0])
                            r = requests.get("https://www.smule.com/"+search+"/performances/json")
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                ret_ = "╔══[ ✯ ʟɪsᴛsᴍᴜʟᴇ ✯ ]"
                                for aa in data["list"]:
                                    no += 1
                                    ret_ += "\n╠•➣" + str(no) + ". " + str(aa["title"])
                                ret_ += "\n╚══[ ✯ʟɪsᴛsᴍᴜʟᴇ✯ ]"
                                ret_ += "\nᴋᴇᴛɪᴋ: sᴍᴜʟᴇ{}ɴᴏᴍᴏʀ".format(str(search))
                                sendTextTemplate2(msg.to,ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["list"][num - 1]
                                    smule = str(b["web_url"])
                                    c = "\n╠•➣ᴊᴜᴅᴜʟ ʟᴀɢᴜ: "+str(b["title"])
                                    c += "\n╠•➣ᴄʀᴇᴀᴛᴏʀ: "+str(b["owner"]["handle"])
                                    c += "\n╠•➣ʟɪᴋᴇ: "+str(b["stats"]["total_loves"])+" like"
                                    c += "\n╠•➣ᴄᴏᴍᴍᴇɴᴛ: "+str(b["stats"]["total_comments"])+" comment"
                                    c += "\n╠•➣sᴛᴀᴛᴜs ᴏᴄ: "+str(b["message"])
                                    c += "\n╠•➣ᴅɪ ᴅᴇɴɢᴀʀᴋᴀɴ: {}".format(b["stats"]["total_listens"])+" orang"
                                    c += "\n╚══[ ✯ᴡᴀɪᴛ ᴀᴜᴅɪᴏ ᴏʀ ᴠɪᴅᴇᴏ✯ ]"
                                    hasil = "╔══[ ✯ ᴅᴇᴛᴀɪʟsᴍᴜʟᴇ ✯ ]"+str(c)
                                    dl = str(b["cover_url"])
                                    data = {
                                        "type": "flex",
                                        "altText": "Audio Smule",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#0000ff" #2f2f4f" #0000" #cc9999"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
          },{
            "contents": [
              {
            "text": "⚡S̸͟͞E̸͟͞L̸͟͞F̸͟͞B̸͟͞O̸͟͞T̸͟͞ T̸͟͞E̸͟͞M̸͟͞P̸͟͞L̸͟͞A̸͟͞T̸͟͞E̸͟͞⚡",
           "size": "xxs",
           "align": "center",
           "color": "#ffff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
 },
{
"type": "image",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQtKJ9DZZjfaSZtDWapDmdO1bVccjThrGsrLARUW0ZVu2SqHTTI",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~slanker123456",             
           }, 
            "flex": 1   
            },
            {
     "type": "separator",
           "color": "#33ffff"
           },
           {
            "contents": [
            {           
           "type": "separator",
           "color": "#33ffff"
           },
           {
            "type": "image",
            "url": dl, #"https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1
}
],
   "type": "box",
   "spacing": "xs",
   "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
"contents": [{"type":"separator","color": "#33ffff"},{"contents": [{"text": "🎙️ᴊᴇᴍᴘᴏʟ: "+str(b["stats"]["total_loves"])+" like","size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"},{"text": "🎙️ɴʏɪᴍᴀᴋ: {}".format(b["stats"]["total_listens"])+" orang","size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"},{"text": "🎙️ᴠᴏᴄᴀʟ: "+str(b["owner"]["handle"]),"size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"},{"text": "🎙️"+str(b["title"]),"size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"}],"type": "box","spacing": "xs","layout": "vertical"    
},{"type": "separator","color": "#33ffff"}],"type": "box","spacing": "xs","layout": "horizontal"   },{"type": "separator","color": "#33ffff"},{
"contents": [         
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
                                    cl.postTemplate(to, data)
                                    with requests.session() as s:
                                        s.headers['user-agent'] = 'Mozilla/5.0'
                                        r = s.get("https://sing.salon/smule-downloader/?url=https://www.smule.com{}".format(urllib.parse.quote(smule)))
                                        data = BeautifulSoup(r.content, 'html5lib')
                                        get = data.select("a[href*=https://www.smule.com/redir?]")[0]
                                        title = data.findAll('h2')[0].text
                                        imag = data.select("img[src*=https://www.smule.com/redir?]")[0]
                                        if 'Smule.m4a' in get['download']:
                                            cl.sendAudioWithURL(msg.to, get['href'])
                                        else:
                                            cl.sendVideoWithURL(msg.to, get['href'])
                                except Exception as e:
                                    cl.sendReplyMessage(msg.id,msg.to,"Result Error:\n"+str(e))
#===========COMEN PANGGILAN======
                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate1(msg.to,"Total Spamtag Diubah Menjadi " +strnum)
                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate1(msg.to,"Total Spamcall Diubah Menjadi " +strnum)
                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(wait["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        sendTextTemplate1(msg.to,"Jumlah melebihi 1000")
                        elif msg.text.lower().startswith("naik "):
                          if msg._from in admin:
                           if 'MENTION' in msg.contentMetadata.keys()!= None:
                               names = re.findall(r'@(\w+)', text)
                               mention = eval(msg.contentMetadata['MENTION'])
                               mentionees = mention['MENTIONEES']
                               lists = []
                               for mention in mentionees:
                                   if mention["M"] not in lists:
                                       lists.append(mention["M"])
                               for ls in lists:
                                   contact = cl.getContact(ls)                          
                                   jmlh = int(wait["limit"])
                                   sendTextTemplate1(msg.to, "Succes {} Call Grup".format(str(wait["limit"])))
                                   if jmlh <= 1000:
                                     for x in range(jmlh):
                                         try:
                                             mids = [contact.mid]
                                             cl.acquireGroupCallRoute(msg.to)
                                             cl.inviteIntoGroupCall(msg.to,mids)
                                         except Exception as e:
                                             cl.sendMessage(msg.to,str(e))
                                     else:
                                         sendTextTemplate1(msg.to,"")
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                sendTextTemplate1(msg.to, "Sukses Call {} diGrup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    sendTextTemplate1(msg.to,"Jumlah melebihi batas")

#==========Comen Spam==={{{
                        elif cmd.startswith("ajsname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(msg.to,"✓sᴜᴄᴄᴇss " + string + "")

                        elif cmd == "ajsfoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendMessage(msg.to,"📷 Kirim Fotonya...")

                        elif cmd == "js stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Amid])
                                    sendTextTemplate1(msg.to,"[ ɴᴀᴍᴀ ɢʀᴏᴜᴘ ]\n"+str(ginfo.name)+"\nᴅᴏɴᴇ ᴋɪᴄᴋᴇʀ ᴀᴋᴛɪᴠᴇ ᴊs")
                                except:
                                    pass             
                        elif cmd == "js out":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                k1.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                k1.leaveGroup(msg.to)

                        elif cmd == "js in":
                          if msg._from in admin:
                           if msg.toType == 2:
                               group = cl.getGroup(to)
                               group.preventedJoinByTicket = False
                               cl.updateGroup(group)
                               invsend = 0
                               ticket = cl.reissueGroupTicket(to)
                               k1.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                        elif msg.text in ["Ajs absen"]:
                            if msg._from in admin:
                                X = cl.getGroup(msg.to)
                                X.preventedJoinByTicket = False
                                cl.updateGroup(X)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                           #     k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                          #      sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k1.sendMessage(to,"ᴛʜᴀɴᴋᴢ ʙᴏsᴋᴜ")
                             #   k2.sendMessage(to,"ᴛʜᴀɴᴋᴢ ʙᴏsᴋᴜ")
                             #   sw.sendMessage(to,"ᴛʜᴀɴᴋᴢ ʙᴏsᴋᴜ")
                                G = k1.getGroup(msg.to)
                           #     G = k2.getGroup(msg.to)
                            #    G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k1.updateGroup(G)
                            #    k2.updateGroup(G)
                            #    sw.updateGroup(G)
                                k1.sendMessage(to,"ᴋᴀᴍɪ ᴘᴀᴍɪᴛ ʟᴀɢɪ ʙᴏs\n╠❂➢sᴛᴀʏ ᴅɪʟᴜᴀʀ sᴀᴊᴀ\n╠❂➢ᴇᴍᴍᴜᴜᴜᴜᴜᴀᴄᴄʜ")
                          #      k2.sendMessage(to,"ᴋᴀᴍɪ ᴘᴀᴍɪᴛ ʟᴀɢɪ ʙᴏs\n╠❂➢sᴛᴀʏ ᴅɪʟᴜᴀʀ sᴀᴊᴀ\n╠❂➢ᴇᴍᴍᴜᴜᴜᴜᴜᴀᴄᴄʜ")
                            #    sw.sendMessage(to,"ᴋᴀᴍɪ ᴘᴀᴍɪᴛ ʟᴀɢɪ ʙᴏs\n╠❂➢sᴛᴀʏ ᴅɪʟᴜᴀʀ sᴀᴊᴀ\n╠❂➢ᴇᴍᴍᴜᴜᴜᴜᴜᴀᴄᴄʜ")
                                Ticket = k1.reissueGroupTicket(msg.to)
                            #    Ticket = k2.reissueGroupTicket(msg.to)
                            #    Ticket = sw.reissueGroupTicket(msg.to)
                                k1.sendMessage(msg.to,"ʙʏᴇ ʙʏᴇ ғᴀᴍs "+str(G.name))
                            #    k2.sendMessage(msg.to,"ʙʏᴇ ʙʏᴇ ғᴀᴍs "+str(G.name))
                            #    sw.sendMessage(msg.to,"ʙʏᴇ ʙʏᴇ ғᴀᴍs "+str(G.name))
                                k1.leaveGroup(msg.to)
                           #     k2.leaveGroup(msg.to)
                            #    sw.leaveGroup(msg.to)
                                cl.inviteIntoGroup(op.param1, [Amid])
                        elif msg.text in ["Ajs kickall"]:
                            if msg._from in admin:
                                X = cl.getGroup(msg.to)
                                X.preventedJoinByTicket = False
                                cl.updateGroup(X)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                            #    k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                            #    sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                group = k1.getGroup(msg.to)
                            #    group = k2.getGroup(msg.to)
                            #    group = sw.getGroup(msg.to)
                                targets = [contact.mid for contact in group.members]
                                for target in targets:
                                    time.sleep(0.2)
                                    if target not in Bots:
                                        if target not in admin:
                                            try:
                                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                             #   k2.kickoutFromGroup(msg.to,[target])
                                               # sw.kickoutFromGroup(msg.to,[target])
                                            except:
                                                pass
                                G = k1.getGroup(msg.to)
                              #  G = k2.getGroup(msg.to)
                            #    G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k1.updateGroup(G)
                           #     k2.updateGroup(G)
                            #    sw.updateGroup(G)
                                Ticket = k1.reissueGroupTicket(msg.to)
                            #    Ticket = k2.reissueGroupTicket(msg.to)
                             #   Ticket = sw.reissueGroupTicket(msg.to)
                                k1.leaveGroup(msg.to)
                            #    k2.leaveGroup(msg.to)
                            #    sw.leaveGroup(msg.to)
                                cl.inviteIntoGroup(op.param1, [Amid])
                        elif msg.text in ["Ajs cancel"]:
                            if msg._from in admin:
                                X = cl.getGroup(msg.to)
                                X.preventedJoinByTicket = False
                                cl.updateGroup(X)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                          #      k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                          #      sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                group = k1.getGroup(msg.to)
                          #      group = k2.getGroup(msg.to)
                           #     group = sw.getGroup(msg.to)
                                targets = [contact.mid for contact in group.invitee]
                                for target in targets:
                                    time.sleep(0.4)
                                    if target not in Bots:
                                        if target not in admin:
                                            try:
                                                random.choice(KAC).cancelGroupInvitation(msg.to,[target])
                                              #  k2.cancelGroupInvitation(msg.to,[target])
                                                #sw.cancelGroupInvitation(msg.to,[target])
                                            except:
                                                pass
                                G = k1.getGroup(msg.to)
                           #     G = k2.getGroup(msg.to)
                            #    G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k1.updateGroup(G)
                           #     k2.updateGroup(G)
                             #   sw.updateGroup(G)
                                Ticket = k1.reissueGroupTicket(msg.to)
                             #   Ticket = k2.reissueGroupTicket(msg.to)
                            #    Ticket = sw.reissueGroupTicket(msg.to)
                                k1.sendMessage(msg.to, "❂➢ʙʏᴇ ʙʏᴇ ғᴀᴍs "+str(G.name))
                           #     k2.sendMessage(msg.to, "❂➢ʙʏᴇ ʙʏᴇ ғᴀᴍs "+str(G.name))
                            #    sw.sendMessage(msg.to, "❂➢ʙʏᴇ ʙʏᴇ ғᴀᴍs "+str(G.name))
                                k1.leaveGroup(msg.to)
                            #    k2.leaveGroup(msg.to)
                             #   sw.leaveGroup(msg.to)
                                cl.inviteIntoGroup(op.param1, [Amid])
                        elif ("Crot" in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           k1.kickoutFromGroup(msg.to, [target])
                                           k1.leaveGroup(msg.to)
                                           cl.inviteIntoGroup(op.param1, [Amid])
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           k1.sendMessage(to, "Kakiku Struk Boss")
                        elif cmd == "pas band" or text.lower() == '.goo':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "Kosong.....")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in Bots:
                                       klist=[mid,Amid]
                                       random.choice(KAC).cancelGroupInvitation(msg.to, [x])
                                       time.sleep(0.00001)
                                       print (msg.to, [x])
                          if msg._from in admin:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for x in gs.members:
                                    targets.append(x.mid)
                                for a in admin:
                                    if a in targets:
                                        try:
                                            targets.remove(a)
                                        except:
                                            pass
                                for target in targets:
                                    try:
                                        klist=[mid,Amid]
                                        random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                        time.sleep(0.00001)
                                        print (msg.to,[g.mid])
                                    except:
                                        pass

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate1(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    sendTextTemplate1(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif ("Kick" in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in admin:
                                       try:
                                       	cl.kickoutFromGroup(msg.to,[target])
                                       except:
                                           sendTextTemplate1(msg.to,"Sorry kaki saya struk..")

                        elif "Gkick " in msg.text:
                           if msg._from in admin:
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]                                                                                                                                
                              targets = []
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:                                                                                                                                       
                                  try:
                                      cl.kickoutFromGroup(msg.to,[target])
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                  except:
                                      pass
                        elif "Cancelall" in msg.text:
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = cl.getGroup(msg.to)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _dn in gMembMids:
                                  if _dn not in admin:
                                    cl.cancelGroupInvitation(msg.to,[_dn])

#=========COMEN RESPON======#
                        elif msg.text in ["Jepit"]:
                            if msg._from in admin:
                                wait["Invi"] = True
                                sendTextTemplate1(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                wait["detectMention2"] = False
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏʀᴇsᴘᴏɴ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "respon2 on" or text.lower() == 'respon2 on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention2"] = True
                                wait["detectMention"] = False
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏʀᴇsᴘᴏɴ2 ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏʀᴇsᴘᴏɴ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "respon2 off" or text.lower() == 'respon2 off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention2"] = False
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏʀᴇsᴘᴏɴ2 ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                sendTextTemplate1(msg.to,"ʀᴇsᴘᴏɴᴛᴀɢ ᴋɪᴄᴋ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                sendTextTemplate1(msg.to,"ʀᴇsᴘᴏɴᴛᴀɢ ᴋɪᴄᴋ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                sendTextTemplate1(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ʀᴇsᴘᴏɴ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                sendTextTemplate1(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ʀᴇsᴘᴏɴ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏᴊᴏɪɴ ɢʀᴏᴜᴘ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏᴊᴏɪɴ ɢʀᴏᴜᴘ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ ᴍᴏᴅᴇ ᴏn")
                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                sendTextTemplate1(msg.to,"ᴅᴇᴛᴇᴄᴛ sᴛɪᴄᴋᴇʀ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                sendTextTemplate1(msg.to,"ᴅᴇᴛᴇᴄᴛ sᴛɪᴄᴋᴇʀ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                sendTextTemplate1(msg.to,"ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                sendTextTemplate1(msg.to,"ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                sendTextTemplate1(msg.to,"ʙʟᴏᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                sendTextTemplate1(msg.to,"ʙʟᴏᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "post on" or text.lower() == 'post on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["checkPost"] = True
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "post off" or text.lower() == 'post off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["checkPost"] = False
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "like on" or text.lower() == 'like on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["likeon"] = True
                                sendTextTemplate1(msg.to,"ʟɪᴋᴇ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "like off" or text.lower() == 'like off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["likeon"] = False
                                sendTextTemplate1(msg.to,"ʟɪᴋᴇ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                sendTextTemplate1(msg.to, "ᴋɪʀɪᴍ ᴋᴏɴᴛᴀᴋ'ɴʏᴀ")
                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                sendTextTemplate1(msg.to,"ɪɴᴠɪᴛᴇ ᴠɪᴀ ᴄᴏɴᴛᴀᴄᴛ ᴏɴ")
                        if cmd == "unsend on":
                            if msg._from in admin:
                                wait["Unsend"] = True
                                sendTextTemplate1(msg.to, "Unsend message mode on")
                        if cmd == "unsend off":
                            if msg._from in admin:
                                wait["Unsend"] = False
                                sendTextTemplate1(msg.to, "Unsend message mode off")
                        elif "autoreject " in msg.text.lower():
                            xpesan = msg.text.lower()
                            xres = xpesan.replace("autoreject ","")
                            if xres == "off":
                                wait['autoReject'] = False
                                sendTextTemplate1(msg.to,"❎Auto Reject already Off")
                            elif xres == "on":
                                wait['autoReject'] = True
                                sendTextTemplate1(msg.to,"✅Auto Reject already On")
#==================================#
                        elif cmd == "refresh" or text.lower() == 'seger':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                sendTextTemplate1(msg.to,"Clean..")
                                sendTextTemplate1(msg.to,"Refresh done 💯")
#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           sendTextTemplate1(msg.to,"✅Berhasil menambahkan admin")
                                       except:
                                           pass
                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           sendTextTemplate1(msg.to,"✅Berhasil menambahkan staff")
                                       except:
                                           pass
                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           sendTextTemplate1(msg.to,"✅Berhasil menghapus admin")
                                       except:
                                           pass
                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           sendTextTemplate1(msg.to,"✅Berhasil menghapus admin")
                                       except:
                                           pass
#===========COMMAND BLACKLIST============#

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           sendTextTemplate1(msg.to,"✅Berhasil menambahkan blacklist")
                                       except:
                                           pass
                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           sendTextTemplate1(msg.to,"✅Berhasil menghapus blacklist")
                                       except:
                                           pass
                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                sendTextTemplate1(msg.to,"📲Kirim kontaknya...")
                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                sendTextTemplate1(msg.to,"📲Kirim kontaknya...")
                        elif cmd == "wanted" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                sendTextTemplate1(msg.to,"Tak ada daftar buronan")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate2(msg.to,"Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "blc" or text.lower() == 'bl':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                   sendTextTemplate1(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif cmd == "cban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」Bersih" % len(ragets)
                              sendTextTemplate1(msg.to,"Biang kerok " +mc)
#==========Setting bot========
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  sendTextTemplate1(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  sendTextTemplate1(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set autoleave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set autoleave: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Autoleave Msg")
                              else:
                                  wait["autoLave"] = spl
                                  sendTextTemplate1(msg.to, "「Autoleave Msg」\nAutoleave Msg diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  sendTextTemplate1(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set respon2: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon2: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag2"] = spl
                                  sendTextTemplate1(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  sendTextTemplate1(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")
                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")
                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Autoleave Msg」\nAutoleave Msg mu :\n\n「 " + str(wait["autoleave"]) + " 」")
                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")
                        elif text.lower() == "cek respon2":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag2"]) + " 」")
                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")
#___________________HIBURAN____________________
                        elif "youtube" in msg.text.lower():
                          #if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                cover = cl.getProfileCoverURL(mid)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    data = {
                                "type": "flex",
                                "altText": "G⃠R⃠E⃠E⃠T⃠",
                                "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "nano",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 1
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"gravity": "bottom",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true",
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "140px",
"width": "110px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "140px",
"width": "110px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "140px",
"width": "110px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "ʏᴏuᴛᴜʙᴇ",
"align": "center",
"color": "#000000",
"weight": "bold",
"size": "xxs",
"weight": "bold",
"offsetTop": "1px"
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "7px",
"backgroundColor": "#ffd700",
"offsetStart": "7px",
"height": "15px",
"width": "45px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://thumbs.gfycat.com/DependentSleepyHusky-size_restricted.gif",
#"url": "https://thumbs.gfycat.com/UnkemptWhiteKakapo-max-1mb.gif",
"size": "xxl",
"action": {
"type": "uri",
"uri": "https://wa.me/6282135759022",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "5px",
"offsetStart": "92px",
"height": "43px",
"width": "22px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://thumbs.gfycat.com/DependentSleepyHusky-size_restricted.gif",
#"url": "https://thumbs.gfycat.com/UnkemptWhiteKakapo-max-1mb.gif",
"size": "xxl",
"action": {
"type": "uri",
"uri": "https://youtube.com",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "5px",
"offsetStart": "67px",
"height": "43px",
"width": "22px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/__TRSC_OLALA__",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/ZHtFDts/20190427-185307.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/chat",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~slanker123456",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/timeline"
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "25px",
"offsetStart": "5px",
"height": "180px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🕙 "+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#ffffff",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "98px",
"backgroundColor": "#ff0000",
"offsetStart": "50px",
"height": "16px",
"width": "63px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🎙️" + str(vid.author),
"weight": "bold",
"color": "#ffffff",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "115px",
"backgroundColor": "#0000ff",
"offsetStart": "33px",
"height": "16px",
"width": "80px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🔰ɢʀᴇᴇt_ʙᴏᴛᴢ",
"weight": "bold",
"color": "#00ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "130px",
#"backgroundColor": "#33ffff",
"offsetStart": "8px",
"height": "50px",
"width": "110px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
                                cl.postTemplate(to, data)
                                cl.sendVideoWithURL(msg.to, me)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif "yutube" in msg.text.lower():
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    data = {
                                        "type": "flex",
                                        "altText": "B̸͟͞R̸͟͞O̸͟͞A̸͟͞D̸͟͞C̸͟͞A̸͟͞S̸͟͞T̸͟͞",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
 "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#33ffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ³",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#33ffff"
          },
          {
          "type": "image",
            "url": "https://thumbs.gfycat.com/DependentSleepyHusky-max-1mb.gif", 
            "size": "xxs",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com",
          },
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#33ffff"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": "🔊 ʏᴏuᴛᴜʙᴇ 🔊",
"weight": "bold",
"color": "#33ffff",
"align": "center",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": "🕙 "+ str(vid.duration),
"weight": "bold",
"color": "#ccffff",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {     
       "contents": [           
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#33ffff"
            },
           {
          "type": "text",
"text": "voc:" + str(vid.author),
"weight": "bold",
"color": "#ffff00",
"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {          
         "contents": [
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#33ffff"
            },
           {
          "text": "📀ᴊᴜᴅᴜʟ📀\n " + vid.title + " ",
           "size": "xxs",
          "align": "center",
           "color": "#00ff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          },
         {
        "type": "separator",
        "color": "#33ffff"
         }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
      "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com",
           }, 
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat" #"http://line.me/ti/p/~greetolala999",
            },         
            "flex": 1          
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
        },{
        "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {          
            "contents": [
               {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
    },{
 "type": "text",
"text": "ᴛʜᴀɴᴋᴢ ғᴏʀ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "sᴜᴘᴏʀᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴀᴍ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"     
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
                                cl.postTemplate(to, data)
                                cl.sendVideoWithURL(msg.to, me)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

#_______________DATA__YOUTUBE________

#____________DATA_PROMO________        
                        elif cmd == "me2" or text.lower() == 'gue':                            	
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                status = cl.getContact(sender)                   
                          #      cover = cl.getProfileCoverURL(sender)
                                data = {
                                        "type": "flex",
                                        "altText": "GREETOLALA",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
 "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#33ffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ³",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#33ffff"
          },
          {
          "type": "image",
          "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
"size": "xxs",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~slanker123456",
            },
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#33ffff"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": "🚹{}".format(cl.getContact(sender).displayName),
"weight": "bold",
"color": "#33ffff",
#"align": "center",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": "🕙"+ datetime.strftime(timeNow,'%H:%M:%S'+"ᴡɪʙ"),
"weight": "bold",
"color": "#ccffff",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {     
       "contents": [           
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#33ffff"
            },
           {
          "type": "text",
"text": "🎏 sᴛᴀᴛᴜs 🎏",
"weight": "bold",
"color": "#ffff00",
"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {          
         "contents": [
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#33ffff"
            },
           {
          "text": "{}".format(status.statusMessage),
           "size": "xxs",
          "align": "center",
           "color": "#00ff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          },
         {
        "type": "separator",
        "color": "#33ffff"
         }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
      "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com",
           }, 
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat" #"http://line.me/ti/p/~greetolala999",
            },         
            "flex": 1          
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
        },{
        "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {          
            "contents": [
               {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
    },{
 "type": "text",
"text": "ᴛʜᴀɴᴋᴢ ғᴏʀ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "sᴜᴘᴏʀᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴀᴍ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator", #batas APK
        "color": "#33ffff"     
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
                                cl.postTemplate(to, data)
                        elif cmd == "me" or text.lower() == 'aku':                            	
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                status = cl.getContact(sender)                   
                                cover = cl.getProfileCoverURL(sender)
                                data = {
   "contents": [{
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": "P̸͟͞R̸͟͞O̸͟͞F̸͟͞I̸͟͞L̸͟͞M̸͟͞U̸͟͞",
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         
{
"type": "separator",
"color": "#33ffff"
},{
"contents": [{"type": "separator","color": "#33ffff"},{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
"size": "full",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~slanker123456",
            },
            "flex": 0
}
],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},
{"type": "separator",
"color": "#33ffff"
}
],
"type": "box",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
         },
         {
        "contents": [         
        { 
        "type": "separator",
         "color": "#33ffff"
         },
         {
            "contents": [
              {
"text": "{}".format(cl.getContact(sender).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
        "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/4N1BjnV/20190427-175005.png", #watshaphttps://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://wa.me/6282135759022",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat" #"http://line.me/ti/p/~greetolala999",
            },         
            "flex": 1          
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://call/contacts"
          },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "C̸͟͞R̸͟͞E̸͟͞A̸͟͞T̸͟͞O̸͟͞R̸͟͞ B̸͟͞O̸͟͞T̸͟͞Z̸͟͞",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~slanker123456",
          },
           "align": "center"
          }
        ]
      }
    }, #Batas1
    {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": "C̸͟͞O̸͟͞V̸͟͞E̸͟͞R̸͟͞M̸͟͞U̸͟͞",
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
{
"type": "separator",
"color": "#33ffff"
}, #Fotoprofile
{
"contents": [{"type": "separator","color": "#33ffff"},{
"type": "image",
"url": cover, #"https://i.ibb.co/p2RgMDb/20190628-162758.jpg",
"size": "full",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~slanker123456",
            },
            "flex": 0
}
],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},
{"type": "separator",
"color": "#33ffff"
}
],
"type": "box",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
         },
         {
        "contents": [
        { 
        "type": "separator",
         "color": "#33ffff"
         },
         {
            "contents": [
              {
"text": "{}".format(cl.getContact(sender).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [ 
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {
       "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/fxWzxcR/20190428-232352.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/settings"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/cb7WqMS/20190428-232825.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/profile"   
          },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/7YVnNPF/20190625-190410.png", #https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://joox.com"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "C̸͟͞R̸͟͞E̸͟͞A̸͟͞T̸͟͞O̸͟͞R̸͟͞ B̸͟͞O̸͟͞T̸͟͞Z̸͟͞",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~slanker123456",
          },
           "align": "center"
          }
        ]
      }
 }, #Batas1
    {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": "F̸͟͞O̸͟͞T̸͟͞O̸͟͞K̸͟͞U̸͟͞",
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
{
"type": "separator",
"color": "#33ffff"
}, #Fotoprofile
{
"contents": [{"type": "separator","color": "#33ffff"},{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
"size": "full",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~slanker123456",
            },
            "flex": 0
}
],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},
{"type": "separator",
"color": "#33ffff"
}
],
"type": "box",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
         },
         {
        "contents": [
        { 
        "type": "separator",
         "color": "#33ffff"
         },
         {
            "contents": [
              {
"text": "{}".format(cl.getContact(mid).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {
       "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/fxWzxcR/20190428-232352.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/settings"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/cb7WqMS/20190428-232825.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/profile"   
          },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/7YVnNPF/20190625-190410.png", #https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://joox.com"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "C̸͟͞R̸͟͞E̸͟͞A̸͟͞T̸͟͞O̸͟͞R̸͟͞ B̸͟͞O̸͟͞T̸͟͞Z̸͟͞",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~slanker123456",
          },
           "align": "center"
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                cl.postFlex(to, data)
                        elif cmd == "mempict":
                              if msg._from in admin:
                                  kontak = cl.getGroup(to)
                                  group = kontak.members
                                  picall = []
                                  for ids in group:
                                    if len(picall) >= 400:
                                      pass
                                    else:
                                      picall.append({
                                        "imageUrl": "https://os.line.naver.jp/os/p/{}".format(ids.mid),
                                        "action": {
                                          "type": "uri",
                                          "uri": "http://line.me/ti/p/~greetolala999"
                                          }
                                        }
                                      )
                                  k = len(picall)//10
                                  for aa in range(k+1):
                                    data = {
                                      "type": "template",
                                      "altText": "{} membagikan janda".format(cl.getProfile().displayName),
                                      "template": {
                                        "type": "image_carousel",
                                        "columns": picall[aa*10 : (aa+1)*10]
                                      }
                                    }
                                    cl.postTemplate(to, data)

#=================BAGIAN PROMO==================================
                        elif cmd == "bcgrup":
                       #     if msg._from in admin:
                                saya = cl.getGroupIdsJoined()
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                for groups in saya:      
                                    data = {
   "contents": [{
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#33ffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://cdn140.picsart.com/296661791123201.gif?c256x256",
      "size": "xxs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ³",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://cdn140.picsart.com/296661791123201.gif?c256x256",
    "size": "xxs",
        "aspectMode": "cover"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         { 
      "contents": [
              {
            "text": "🇮🇩🇮🇩🇮🇩",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🇮🇩🇮🇩🇮🇩",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator", #batas aplikasi
         "color": "#33ffff"
         },
         {
         "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/4N1BjnV/20190427-175005.png", #watshaphttps://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://wa.me/6282135759022",
            },       
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat" #"http://line.me/ti/p/~greetolala999",
            },
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://call/contacts"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/cb7WqMS/20190428-232825.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/profile"   
          },
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/fxWzxcR/20190428-232352.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/settings"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/7YVnNPF/20190625-190410.png", #https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://joox.com"
          },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },{
       "contents": [
          {
           "type": "separator",
           "color": "#33ffff"
          },
          {
          "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "type": "image",
            "size": "xxs",
        "aspectMode": "cover",
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#33ffff"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": "🕙 "+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#ccccff",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#ccccff",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
        "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "🎗️ᴏʀᴅᴇʀ🎗️",
            "size": "xxs",
            "color": "#ccff00",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },{
            "text": "🎗️ʙᴏᴛ🎗️",
            "size": "xxs",
            "color": "#ccff00",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "⏺️ᴄᴏɪɴ ɢɪғᴛ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "⏺️ʙᴏᴛ ᴏɴʟʏ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "⏺️ᴀᴋᴜɴ ᴄᴏɪɴ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "⏺️sʙ ᴏɴʟʏ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "⏺️ᴏғғ sᴍᴜʟᴇ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "⏺️sʙ ᴛᴇᴍᴘᴇ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "⏺️ᴠɪᴘ sᴍᴜʟᴇ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "⏺️ᴛᴇᴍᴘᴇ ᴊs",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "⏺️ғᴏʟ sᴍᴜʟᴇ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "⏺️ʙᴏᴛᴘʀᴏ ɢᴄ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
              {
            "text": "🇮🇩🇮🇩🇮🇩",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🇮🇩🇮🇩🇮🇩",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator", #batas aplikasi
         "color": "#33ffff"
         },
         {
         "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
        },{
        "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {          
            "contents": [
               {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
    },{
 "type": "text",
"text": "ᴛʜᴀɴᴋᴢ ғᴏʀ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "sᴜᴘᴏʀᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴀᴍ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
            }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "M̸͟͞y̸͟͞ C̸͟͞r̸͟͞e̸͟͞a̸͟͞t̸͟͞o̸͟͞r̸͟͞ B̸͟͞o̸͟͞t̸͟͞s",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~slanker123456",
          },
           "align": "center"
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                    cl.postFlex(groups, data)
                        elif cmd == "order" or text.lower() == 'promo':                            	
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                status = cl.getContact(sender)                   
                                cover = cl.getProfileCoverURL(sender)
                                data = {
   "contents": [{
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#33ffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://cdn140.picsart.com/296661791123201.gif?c256x256",
      "size": "xxs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ³",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://cdn140.picsart.com/296661791123201.gif?c256x256",
    "size": "xxs",
        "aspectMode": "cover"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         { 
      "contents": [
              {
            "text": "🇮🇩🇮🇩🇮🇩",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️??️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🇮🇩🇮🇩🇮🇩",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator", #batas aplikasi
         "color": "#33ffff"
         },
         {
         "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/4N1BjnV/20190427-175005.png", #watshaphttps://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://wa.me/6282135759022",
            },       
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat" #"http://line.me/ti/p/~greetolala999",
            },
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://call/contacts"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/cb7WqMS/20190428-232825.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/profile"   
          },
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/fxWzxcR/20190428-232352.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/settings"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/7YVnNPF/20190625-190410.png", #https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://joox.com"
          },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },{
       "contents": [
          {
           "type": "separator",
           "color": "#33ffff"
          },
          {
          "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "type": "image",
            "size": "xxs",
        "aspectMode": "cover",
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#33ffff"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": "🕙 "+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#ccccff",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#ccccff",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
        "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "🎗️ᴏʀᴅᴇʀ🎗️",
            "size": "xxs",
            "color": "#ccff00",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },{
            "text": "🎗️ʙᴏᴛ🎗️",
            "size": "xxs",
            "color": "#ccff00",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "⏺️ᴄᴏɪɴ ɢɪғᴛ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "⏺️ʙᴏᴛ ᴏɴʟʏ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "⏺️ᴀᴋᴜɴ ᴄᴏɪɴ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "⏺️sʙ ᴏɴʟʏ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "⏺️ᴏғғ sᴍᴜʟᴇ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "⏺️sʙ ᴛᴇᴍᴘᴇ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "⏺️ᴠɪᴘ sᴍᴜʟᴇ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "⏺️ᴛᴇᴍᴘᴇ ᴊs",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "⏺️ғᴏʟ sᴍᴜʟᴇ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "⏺️ʙᴏᴛᴘʀᴏ ɢᴄ",
            "size": "xxs",
            "color": "#00ff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
              {
            "text": "🇮🇩🇮🇩🇮🇩",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🇮🇩🇮🇩🇮🇩",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator", #batas aplikasi
         "color": "#33ffff"
         },
         {
         "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
        },{
        "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {          
            "contents": [
               {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
    },{
 "type": "text",
"text": "ᴛʜᴀɴᴋᴢ ғᴏʀ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "sᴜᴘᴏʀᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴀᴍ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
            }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "M̸͟͞y̸͟͞ C̸͟͞r̸͟͞e̸͟͞a̸͟͞t̸͟͞o̸͟͞r̸͟͞ B̸͟͞o̸͟͞t̸͟͞s",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~slanker123456",
          },
           "align": "center"
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                cl.postFlex(to, data)
                                
#___________________MEMEK________________

                        elif cmd == ".me" or text.lower() == 'aku':                            	
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                status = cl.getContact(sender)                   
                                cover = cl.getProfileCoverURL(sender)
                                data = {
   "contents": [{ 
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#33ffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://cdn140.picsart.com/296661791123201.gif?c256x256",
      "size": "xs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ³",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://cdn140.picsart.com/296661791123201.gif?c256x256",
    "size": "xs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
              {
            "text": "🇮🇩🇮🇩🇮🇩🇮🇩",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️🖼️",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🇮🇩🇮🇩🇮🇩🇮🇩",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#33ffff"
          },
          {
          "url": "https://s3.amazonaws.com/image.blingee.com/images19/content/output/000/000/000/817/861474702_1313336.gif?6",
            "type": "image",
            "size": "xs",
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#33ffff"
      },
      {      
       "contents": [              
          {          
"type": "text",
"text": "🚹{} ".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": "#00ff00",
"size": "xs",
#"align": "center",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": "🕙 "+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#ccccff",
#"align": "center",
"size": "xs",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#ccccff",
#"align": "center",
"size": "xs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
        "contents": [             
        {
          "type": "separator",
         "color": "#33ffff"
         },
         {
         "type": "image",
         "url": "https://i.ibb.co/bPV1WZz/FB-IMG-1567088328385.jpg",
         "size": "4xl",
         "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",
            },
            "flex": 0
          },
          {
        "type": "separator",
         "color": "#33ffff"       
            },
            {
            "contents": [
            {
             "type": "image",
            "url": "https://i.ibb.co/cb7WqMS/20190428-232825.png",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://nv/profile"   
            },
            "flex": 0
          },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
          "type": "image",
            "url": "https://i.ibb.co/fxWzxcR/20190428-232352.png",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://nv/settings"
           }, 
            "flex": 0
        },{
            "type": "separator",
         "color": "#33ffff"
       },
       {
        "type": "image",
            "url": "https://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://call/contacts"
          },
            "flex": 0
          },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {     
            "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat"
            },
            "flex": 0
          },
      {
        "type": "separator",
         "color": "#33ffff"
          },
      {
        "type": "image",
            "url": "https://i.ibb.co/7YVnNPF/20190625-190410.png", #https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "https://joox.com"
          },
            "flex": 0
          }
        ],         
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
              {
            "text": "🇮🇩🇮🇩🇮🇩🇮🇩",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️🖼️",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🇮🇩🇮🇩🇮🇩🇮🇩",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator", #1234
         "color": "#33ffff"
         },
         {
         "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
        },{
        "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {          
            "contents": [
               {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xs"
    },{
 "type": "text",
"text": "ᴛʜᴀɴᴋᴢ ғᴏʀ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
},{
"type": "text",
"text": "sᴜᴘᴏʀᴛ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴀᴍ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator", #batas APK
        "color": "#33ffff"     
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "M̸͟͞y̸͟͞ C̸͟͞r̸͟͞e̸͟͞a̸͟͞t̸͟͞o̸͟͞r̸͟͞ B̸͟͞o̸͟͞t̸͟͞s",
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~slanker123456",
          },
           "align": "center"
          }
        ]
      }
    }, #Batas2 order vps
    {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#33ffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://cdn140.picsart.com/296661791123201.gif?c256x256",
      "size": "xs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ³",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://cdn140.picsart.com/296661791123201.gif?c256x256",
    "size": "xs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
              {
            "text": "🇮🇩🇮🇩🇮🇩🇮🇩",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️🖼️",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🇮🇩🇮🇩🇮🇩🇮🇩",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#33ffff"
          },
          {
          "url": "https://s3.amazonaws.com/image.blingee.com/images19/content/output/000/000/000/817/861474702_1313336.gif?6",
            "type": "image",
            "size": "xs",
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#33ffff"
      },
      {      
       "contents": [              
          {          
"type": "text",
"text": "🚹{} ".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": "#00ff00",
"size": "xs",
#"align": "center",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": "🛡️ᴏᴘᴇɴ ᴏʀᴅᴇʀ ᴠᴘs", #🕙 "+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#ccccff",
#"align": "center",
"size": "xs",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": "🛡️ᴋʟɪᴋ ғᴏᴛᴏ ᴅɪʙᴀᴡᴀʜ", #📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#ccccff",
#"align": "center",
"size": "xs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
        "contents": [             
        {
          "type": "separator",
         "color": "#33ffff"
         },
         {
         "type": "image",
         "url": "https://i.ibb.co/p2RgMDb/20190628-162758.jpg",
         "size": "4xl",
         "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~BYBOTSLINE",
            },
            "flex": 0
          },
          {
        "type": "separator",
         "color": "#33ffff"       
            },
            {
            "contents": [
            {
             "type": "image",
            "url": "https://i.ibb.co/fxWzxcR/20190428-232352.png",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://nv/settings"
           }, 
            "flex": 0
            },{
            "type": "separator",
         "color": "#33ffff"
       },
       {
        "type": "image",
            "url": "https://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://call/contacts"
          },
            "flex": 0
          },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
        "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat",
          },
            "flex": 0
            },
      {
        "type": "separator",
         "color": "#33ffff"
       },
      {
        "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 0
          },
      {
        "type": "separator",
         "color": "#33ffff"
          },
      {
        "type": "image",
            "url": "https://i.ibb.co/7YVnNPF/20190625-190410.png", #https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "https://joox.com"
          },
            "flex": 0
          }
        ],         
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
              {
            "text": "🇮🇩🇮🇩🇮🇩🇮🇩",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️🖼️",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🇮🇩🇮🇩🇮🇩🇮🇩",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator", #1234
         "color": "#33ffff"
         },
         {
         "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/4N1BjnV/20190427-175005.png", #watshaphttps://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://wa.me/6282135759022",
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
        },{
        "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {          
            "contents": [
               {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xs"
    },{
 "type": "text",
"text": "ᴛʜᴀɴᴋᴢ ғᴏʀ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
},{
"type": "text",
"text": "sᴜᴘᴏʀᴛ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴀᴍ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator", #batas APK
        "color": "#33ffff"     
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "M̸͟͞y̸͟͞ C̸͟͞r̸͟͞e̸͟͞a̸͟͞t̸͟͞o̸͟͞r̸͟͞ B̸͟͞o̸͟͞t̸͟͞s",
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~bybotsline",
          },
           "align": "center"
          }
        ]
      }
    }, #Batas3 Open order
    {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#33ffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://cdn140.picsart.com/296661791123201.gif?c256x256",
      "size": "xs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ³",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://cdn140.picsart.com/296661791123201.gif?c256x256",
    "size": "xs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
              {
            "text": "🇮🇩🇮🇩🇮🇩🇮🇩",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️🖼️",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🇮🇩🇮🇩🇮🇩🇮🇩",
            "size": "xs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
         "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/4N1BjnV/20190427-175005.png", #watshaphttps://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://wa.me/6282135759022",
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat"
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/cb7WqMS/20190428-232825.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/profile"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://call/contacts"
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/fxWzxcR/20190428-232352.png",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://nv/settings"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/7YVnNPF/20190625-190410.png", #https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "https://joox.com"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },{
       "contents": [
          {
           "type": "separator",
           "color": "#33ffff"
          },
          {
          "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "type": "image",
            "size": "xs",
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#33ffff"
      },
      {      
       "contents": [              
          {          
"type": "text",
"text": "🚹{} ".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": "#00ff00",
#"align": "center",
"size": "xs",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": "🕙"+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#ccccff",
#"align": "center",
"size": "xs",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": "📆"+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#ccccff",
#"align": "center",
"size": "xs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
        "contents": [           
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "🎗️ᴏᴘᴇɴ ᴏʀᴅᴇʀ🎗️",
            "size": "xs",
            "color": "#ccff00",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },{
            "text": "??️ᴏʀᴅᴇʀ ʙᴏᴛ🎗️",
            "size": "xs",
            "color": "#ccff00",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "🎖ᴄᴏɪɴ ɢɪғᴛ ʟɪɴᴇ",
            "size": "xs",
            "color": "#FF99ff",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "🎖sᴇʟғʙᴏᴛ ᴏɴʟʏ",
            "size": "xs",
            "color": "#FF99ff",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "🎖ᴀᴋᴜɴ ᴄᴏɪɴ ɢɪғᴛ",
            "size": "xs",
            "color": "#FF99ff",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "🎖sʙ ᴏɴʟʏ + ᴀᴊs",
            "size": "xs",
            "color": "#FF99ff",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "🎖ʙᴇᴋᴜ ᴀᴋᴜɴ sᴍᴜʟᴇ",
            "size": "xs",
            "color": "#FF99ff",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "🎖sʙ ᴛᴇᴍᴘʟᴀᴛᴇ",
            "size": "xs",
            "color": "#FF99ff",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "🎖ᴠɪᴘ sᴍᴜʟᴇ ᴀɴᴅʀᴏ",
            "size": "xs",
            "color": "#FF99ff",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "🎖sʙ ᴛᴇᴍᴘᴇ + ᴀᴊs",
            "size": "xs",
            "color": "#FF99ff",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
        {
          "type": "separator",
         "color": "#33ffff"        
         },
         {  
       "contents": [
         {
            "text": "🎖ғᴏʟʟᴏᴡᴇʀs sᴍᴜʟᴇ",
            "size": "xs",
            "color": "#FF99ff",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"  
           },{
            "text": "🎖ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ɢᴄ",
            "size": "xs",
            "color": "#FF99ff",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {
       "contents": [
              {
            "type": "image",
     "url": "https://cdn0-production-images-kly.akamaized.net/G8m36LbT5BVGq7zk2YhyAcVwv_I=/640x640/smart/filters:quality(75):strip_icc():format(jpeg)/kly-media-production/medias/666852/original/22042014-spiderman600.jpg",
      "size": "md"
          },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "type": "image",
     "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTrBMDdtFivkPXDEH1TAqQgPo-r5VrtFqQm6avDI0IqiPYJQHYf",
      "size": "md"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "type": "image",
           "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT5rL6Jt3bRkm7BW2PWVV_ZEWfb0BoDxZF9orG3lcBVD1eLOveJ",
           "size": "md"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator", #batas aplikasi
         "color": "#33ffff"
         },
         {
         "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~greetolala990",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
        },{
        "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {          
            "contents": [
               {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xs"
    },{
 "type": "text",
"text": "ᴛʜᴀɴᴋᴢ ғᴏʀ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
},{
"type": "text",
"text": "sᴜᴘᴏʀᴛ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴀᴍ",
"weight": "bold",
"color": "#ccff00",
"margin": "xs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "M̸͟͞y̸͟͞ C̸͟͞r̸͟͞e̸͟͞a̸͟͞t̸͟͞o̸͟͞r̸͟͞ B̸͟͞o̸͟͞t̸͟͞s",
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~slanker123456",
          },
           "align": "center"
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                cl.postFlex(to, data)


#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     sendTextTemplate2(msg.to, "Masuk : %s" % str(group.name))
                                   #  group1 = ka.findGroupByTicket(ticket_id)
#===========add img============#                                                                                
                        elif text.lower() == "cekbot":
                            if msg._from in admin:
                               try:cl.inviteIntoGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⏹️Normal 💯"
                               else:sil = "⏹️Cidera ❎"
                               if has1 == "OK":sil1 = "⏹️Normal 💯"
                               else:sil1 = "⏹️Cidera ❎"
                               sendTextTemplate2(to, "🔴Dupak: {} \n🔴Invite: {}".format(sil1,sil))
#===============HIBURAN============================#
                        elif cmd.startswith("addmp3 "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in audios:
                                    settings["Addaudio"]["status"] = True
                                    settings["Addaudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(msg.to,"Silahkan kirim mp3 nya...") 
                                else:
                                    sendTextTemplate1(msg.to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in audios:
                                    cl.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(msg.to, "Done hapus mp3 {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate1(msg.to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif cmd == "listmp3":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╔═══❲ My Music ❳════\n"
                                for audio in audios:
                                    ret_ += "┣[]◇  " + audio.title() + "\n"
                                ret_ += "╚═══❲ {} Record  ❳════".format(str(len(audios)))
                                sendTextTemplate2(to, ret_)

                        elif cmd.startswith("addsticker "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["Addsticker"]["status"] = True
                                    settings["Addsticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = ""
                                    f = codecs.open("Sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(to, "Silahkan kirim stickernya...") 
                                else:
                                    sendTextTemplate1(to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate1(to, "Sticker ada di list") 
                                                   
                        elif cmd == "liststicker":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╔═══❲ My Sticker ❳════\n"
                                for sticker in stickers:
                                    ret_ += "┣[]◇  " + sticker.title() + "\n"
                                ret_ += "╚═══❲  {} Stickers  ❳════".format(str(len(stickers)))
                                sendTextTemplate2(to, ret_)

                        elif cmd.startswith("addimg "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addimage"]["status"] = True
                                    settings["Addimage"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(to, "Silahkan kirim fotonya")
                                else:
                                    sendTextTemplate1(to, "Foto Udah dalam list")

                        elif cmd.startswith("dellimg "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("image.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   sendTextTemplate1(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   sendTextTemplate1(to, "Foto ada dalam list")

                        elif cmd == "listimage":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╭───「 Daftar Image 」\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str("├≽") + " " + audio.title() + "\n"
                                ret_ += "╰───「 Total {} Image 」".format(str(len(audios)))
                                sendTextTemplate2(to, ret_)
#==============add video==========================================================================
                        elif cmd.startswith("addvideo"):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addvideo"]["status"] = True
                                    settings["Addvideo"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("video.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(to, "Silahkan kirim video nya...")
                                else:
                                    sendTextTemplate1(to, "video sudah ada")
                        elif cmd.startswith("dellvideo "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("video.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   sendTextTemplate1(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   sendTextTemplate1(to, "video tidak ada")

                        elif cmd == "listvideo":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╭───「 Daftar Video 」\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str("├≽") + " " + audio.title() + "\n"
                                ret_ += "╰───「 Total {} Video 」".format(str(len(audios)))
                                sendTextTemplate2(to, ret_)
    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
    	logError(e)                      