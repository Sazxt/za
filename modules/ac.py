import os
import sys
import time
from urllib2 import *
i="\033[32m" #hijau
cg="\033[36m" #cyan gelap
k="\033[33;1m" #kuning
p="\033[0m" #putih
ba="\033[96;1m" #biruaqua
pu="\033[35m" # #purple
gr="\033[37m" #putih terang
pb="\033[47m" #putihbold
m="\033[31m" #merah
b="\033[34m" # Biru
def px():
	os.system('python /data/data/com.termux/files/home/.za/modules/embf.py ~')
def tx(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 1000)
def infog():
	try:
		print "%s<%s/%s> %sMasukan ip Bisa juga link tapi lebih efektif id !"%(b,m,b,gr)
		target = raw_input("%s<%s\%s> %sMasukan Ip Target : %s"%(b,m,b,i,gr))
		inx = "http://api.hackertarget.com/whois/?q=" + target
		gsx = urlopen(inx).read()
		print "\n%s<%s/%s> %sWhois Lockup%s"%(b,i,b,i,gr)
		print (gsx)
		maz = "http://api.hackertarget.com/nmap/?q=" + target
		masz = urlopen(maz).read()
		print "\n%s<%s/%s> %sNmap Scan Port%s"%(b,i,b,i,gr)
		print (masz)
		head = "http://api.hackertarget.com/httpheaders/?q=" + target
		xo = urlopen(head).read()
		print "\n%s<%s/%s> %sHttp Header%s"%(b,i,b,i,gr)
		print (xo)
		kx = "https://api.hackertarget.com/mtr/?q=" + target
		sox = urlopen(kx).read()
		print "\n%s<%s/%s> %sTracer Router ip%s"%(b,i,b,i,gr)
		print (sox)
	except KeyboardInterrupt:
		print "Error"
	except Traceback:
		print "back"
def nmap():
	nmap = raw_input("%s<%s\%s> %sMasukan Ip Target : %s"%(b,m,b,i,gr))
	os.system('nmap ' + nmap)
def back():
	print "\n%sWelcome Tools"%(p)
	print "%sAuthor %sS4S.Z34"%(i,ba)
	print "%sUpdate Tanggal 16-04-2019"%(k)
	print """
%s__  ____ ___   _____ _ __    __  __
\ \/ / _` \ \ / / _ \ '__|___\ \/ /
 >  < (_| |\ V /  __/ | |_____>  <
/_/\_\__,_| \_/ \___|_|      /_/\_\\
"""%(cg)
	print "%s"%(cg)
	bn()
def pdx(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(60. / 1000)
def pwd():
	import pwd
def bn():
	os.system('sh /data/data/com.termux/files/home/.za/modules/banners/bn ~')
#-------------------------------Instalasi
def dork():
	try:
		print """
[+] Applications : Dork
[+] Autor : ciku370
[ Fungsi ]
+ Dorking
+ Test Sql"""
		dk = raw_input("Mau Install N/Y : ")
		if dk =="y" or dk =="Y":
			print "Install Dork"
			os.system('git clone https://github.com/ciku370/ko-dork.git')
		elif dk =="n" or dk =="N":
			sys.exit()
	except KeyboardInterrupt:
		print "Exit"
	except EOFError:
		print "Exit"
def DTech():
	try:
		print """
[+] Applications : D-TECT
[+] Autor : Shawar Khan
[ Fungsi ]
* Sub-domain Scanning
* Port Scanning
* Wordpress Scanning
* Wordpress Username Enumeration
* Wordpress Backup Grabbing
* Sensitive File Detection
* Same-Site Scripting Scanning
* Click Jacking Detection
* Powerful XSS vulnerability scanning
* SQL Injection vulnerability scanning
* User-Friendly UI"""
		dt = raw_input("Mau Install N/Y : ")
		if dt =="y" or dt =="Y":
			print "Install D-Tech"
			os.system('git clone https://github.com/bibortone/D-Tech')
		elif dt =="n" or dt =="N":
			sys.exit()
	except KeyboardInterrupt:
		print "Exit"
	except EOFError:
		print "Exit"
def websploit():
	try:
		print """
[+] Applications : WebSploit Advanced MITM Framework
[+] Autor : Fardin Allahverdinazhand
[+] CodeName : Katana
[ Fungsi ]
+ Scan Directory Of Apache Users
+ Directory Scanner
+ Information Gathering From Victim Web Using (Metasploit Wmap)
+ PHPMyAdmin Login Page Scanner
+ CloudFlare Resolver
+ ARP Cache Denial Of Service Attack
+ Middle Finger Of Doom Attack
+ Man In The Middle Attack
+ Man Left In The Middle Attack
+ TCP Kill Attack
+ Fake Update Attack Using DNS Spoof
+ Arp Poisoner
+ Metasploit Autopwn Service
+ Metasploit Browser Autopwn Service
+ Java Applet Attack (Using HTML)
+ Wifi Jammer
+ Wifi Dos Attack
+ Wireless Honeypot(Fake AP)
+ Mass Deauthentication Attack
+ Bluetooth Ping Of Death Attack"""
		wb = raw_input("Mau Install N/Y : ")
		if wb =="Y" or wb =="y":
			print "Install websploit"
			os.system('git clone https://github.com/websploit/websploit.git')
		if wb =="N" or wb =="n":
			sys.exit()
	except KeyboardInterrupt:
		print "Exit"
	except EOFError:
		print "Exit"
def mdork():
	try:
		print """
[+] Applications : M-Dork
[+] Autor : Ms.ambari
[+] CodeName : M.dork
[ Fungsi ]
+ Dork....^_^"""
		md = raw_input('Mau Install Y-N')
		if md =="y" or md =="Y":
			print "Install M-dork"
			os.system('https://github.com/ws-s/M-dork')
		elif md =="n" or md =="N":
			sys.exit()
	except KeyboardInterrupt:
		print "Exit"
	except EOFError:
		print "Exit"
def rhawk():
	try:
		print """
[+] Applications : RED HAWK
[+] Autor : By R3D#@0R_2H1N A.K.A Tuhinshubhra
[+] Version 2.0.0
[ Fungsi ]
+ Basic Scan
	- Site Title **NEW**
	- IP Address
	- Web Server Detection `IMPROVED`
	- CMS Detection
	- Cloudflare Detection
	- robots.txt Scanner
+ Whois Lookup `IMPROVED`
+ Geo-IP Lookup
+ Grab Banners `IMPROVED`
+ DNS Lookup
+ Subnet Calculator
+ Nmap Port Scan
+ Sub-Domain Scanner `IMPROVED`
	- Sub Domain
	- IP Address
+ Reverse IP Lookup & CMS Detection `IMPROVED`
	- Hostname
	- IP Address
	- CMS
+ Error Based SQLi Scanner
+ Bloggers View **NEW**
	- HTTP Response Code
	- Site Title
	- Alexa Ranking
	- Domain Authority
	- Page Authority
	- Social Links Extractor
	- Link Grabber
+ WordPress Scan **NEW**
	- Sensitive Files Crawling
	- Version Detection
	- Version Vulnerability Scanner
+ Crawler
+ MX Lookup **NEW**
+ Scan For Everything - _The Old Lame Scanner_"""
		rd = raw_input("Mau Install Y-N : ")
		if rd =="y" or rd =="Y":
			print "install Red_hawk"
			os.system('https://github.com/Tuhinshubhra/RED_HAWK')
		elif rd =="n" or rd =="N":
			sys.exit()
	except KeyboardInterrupt:
		print "Exit"
	except EOFError:
		print "Exit"
#--------------Facebook Brute
def fbphp():
	print "install fbbrutephp"
	os.system('git clone https://github.com/FR13ND8/fbbrute')
def fbcracker():
	print "install Fb-Cracker-v.3"
	os.system('git clone https://github.com/FR13ND8/Fb-Cracker-v.3')
def iqbalz():
	print "Install IqbalzNoobs brute"
	os.system('git clone https://github.com/IqbalzNoobs/fb-brute')
def mbf():
	print "Install Mbf"
	os.system('git clone https://github.com/FR13ND8/mbf')
def night420():
	print "Install FaceBrute-night420"
	os.system('git clone https://github.com/N1ght420/FaceBrute')
def bruterrot():
	print "Install bruteRoot"
	os.system('git clone https://github.com/thelinuxchoice/facebash.git')
def fbclone():
	print "Install Facebok Yahoo-cloning-email"
	os.system('git clone https://github.com/FR13ND8/EmailVuln')
#---------------Info Fb
def guard():
	print "Install ProfileGuardFb"
	os.system('git clone https://github.com/FR13ND8/ProfileGuardFb')
def report():
	print "Install Auto-Report"
	os.system('git clone https://github.com/IlayTamvan/Report')
def autorect():
	print "Install Fb-React"
	os.system('git clone https://github.com/AMVengeance/FB-React')
def osif():
	print "Install Osif"
	os.system('git clone https://github.com/ciku370/OSIF')
def botkomen():
	print "Install BotKomen"
	os.system('git clone https://github.com/Senitopeng/Botkomena.git')
def autolike():
	print "Install AutoLike"
	os.system('git clone https://github.com/FR13ND8/autolike')
#--------- phising
def shelphis():
	print "Install Shelphis"
	os.system('git clone https://github.com/thelinuxchoice/shellphish.git')
def blacleye():
	print "Install BlackEye"
	os.system('git clone https://github.com/thelinuxchoice/blackeye.git')
def socialfish():
	print "Install SocialFhish"
	os.system('git clone https://github.com/UndeadSec/SocialFish.git')
def wemman():
	print "Install Wemman"
	os.system('https://github.com/evait-security/weeman.git')
#------exploit
def yuki():
	print "Install Yuki-Chan"
	os.system('git clone https://github.com/Yukinoshita47/Yuki-Chan-The-Auto-Pentest.git')
def operative():
	print "Install Operative"
	os.system('git clone https://github.com/graniet/operative-framework-HD')
def Metasploit():
	print "Install Metasploit"
	os.system("wget https://gist.githubusercontent.com/Gameye98/d31055c2d71f2fa5b1fe8c7e691b998c/raw/09e43daceac3027a1458ba43521d9c6c9795d2cb/msfinstall.sh")
	os.system("mv msfinstall.sh ~;cd ~;sh msfinstall.sh")
def Routersp():
	print "Install RouterSploit"
	os.system('git clone https://github.com/reverse-shell/routersploit')
#-------tools instal
def bajing():
	os.system('sh /data/data/com.termux/files/home/.za/modules/tools-ins/bajing')
def badut():
	os.system('bash /data/data/com.termux/files/home/.za/modules/tools-ins/1')
def lazymux():
	os.system('python2 /data/data/com.termux/files/home/.za/modules/tools-ins/Lazymux/lazymux.py ~')
#------Tools-Spam
def jdid():
	os.system('php /data/data/com.termux/files/home/.za/modules/tools/kntl.php')
def call():
	os.system('python2 /data/data/com.termux/files/home/.za/modules/tools/call.py ~')
def call2():
	os.system('php /data/data/com.termux/files/home/.za/modules/tools/crot.php')
def bukalapak():
	os.system('php /data/data/com.termux/files/home/.za/modules/tools/1')
def tsel():
	os.system('php /data/data/com.termux/files/home/.za/modules/tools/2.php')
def grab():
	os.system('php /data/data/com.termux/files/home/.za/modules/tools/3.php')
def toped():
	os.system('php /data/data/com.termux/files/home/.za/modules/tools/4.php')
def codashp():
	os.system('php /data/data/com.termux/files/home/.za/modules/tools/5.php')
def survyon():
	os.system('php /data/data/com.termux/files/home/.za/modules/tools/6.php')
def grab2():
	os.system('python2 /data/data/com.termux/files/home/.za/modules/tools/spammer.py ~')
def smsid():
	os.system('cd /data/data/com.termux/files/home/.za/modules/tools && apt install ./smsid_1.1_all.deb')
	os.system('smsid bom -y')
def multibom():
	os.system('php /data/data/com.termux/files/home/.za/modules/tools/sms.php')
def geolokup():
	try:
		glockup = raw_input("%s<%s\%s> %sMasukan link Target : %s"%(b,m,b,i,gr))
		glink = "http://api.hackertarget.com/geoip/?q=" + glockup
		glink = urlopen(glink).read()
		print "\n%s<%s/%s> %sGeo Ip Lockup%s"%(b,i,b,i,gr)
		print (glink)
		if 'Request Rejected' in glink:
			print "back"
	except IOError:
		print "</> sory Pliss on data !"