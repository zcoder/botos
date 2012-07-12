# This Python file uses the following encoding: utf-8
import Skype4Py, datetime, re, httplib
from urllib import urlencode
import subprocess
import StringIO, sys
from datetime import *

skype = Skype4Py.Skype(Transport='x11')
skype.Attach()

def fucking_great_advice(v,body):
    import simplejson, urllib, random
    n = random.getrandbits(4)
    if n == 1:
        url = 'http://www.fucking-bad-advice.ru/api'
    else:
        url = 'http://fucking-great-advice.ru/api/random/censored/'
    d = urllib.urlopen(url)
    json = simplejson.loads(d.read())
    msg = json['text'].replace('&nbsp;',' ')
    return msg

def bash_im(v, body):
    import re, HTMLParser, urllib2
    """Random quote from bash.im"""
    url = 'http://bash.im/forweb/'
    reg = re.compile ("""padding: 1em 0;">(.*)<'\s\+\s'/div><""")
    s = urllib2.urlopen(url).read ().decode ('cp1251')
    msg = HTMLParser.HTMLParser().unescape(reg.search(s).group (1).replace("<' + 'br />","\n").replace("<' + 'br>","\n"))
    return msg

def rss_habr(v,body):
    import feedparser
    tn = body.split(' ', 2)[-1]
    if tn == 'habr':
        n = 1
    else:
        n = int(tn)
    d = feedparser.parse('http://habrahabr.ru/rss/hubs/')
    f = d.entries[n].title +'  ' + d.entries[n].link
    return f

def tr(v, body):
    body = body.split(' ', 1)[1]
    process = subprocess.Popen('modules/mod_translate/run.sh '+ body, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    return process.stdout.read()

def sl(v, body):
    body = body.split(' ', 1)[1]
    process = subprocess.Popen('modules/mod_slogan/run.sh '+ body, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    return process.stdout.read()

def pie(v, body):
    process = subprocess.Popen('modules/mod_pie/run.sh', shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    return process.stdout.read()

def _help(v, body):
    return 'Usage botos:\
                                            \n совет                  -for sovet\
                                            \n баш                    -for bash.org\
                                            \n habr                   -for habrahabr\
                                            \n tr                     -for translate\
                                            \n pie                    -for pie\
                                            \n реклам                 -for slogan'

com = {"совет": fucking_great_advice,'help':_help, 'баш':bash_im, 'habr':rss_habr, 'tr':tr, 'реклам':sl, 'pie':pie}
def message(msg, status):
    print 'msg: '+ msg.Body+':'+status 
    chat_name = msg.ChatName
    print 'user: '+ msg.FromHandle + chat_name
    new_chat = skype.Chat(chat_name)
    flag = 1

    if status == 'RECEIVED':
        for item in com:
                if re.search(item,str(msg.Body.encode('utf-8'))):
                    message = com[item](flag, msg.Body)
                    new_chat.SendMessage(message)
            
skype.OnMessageStatus = message

while(True): pass
