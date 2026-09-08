import requests
def exploit_step2(base_url):

    resp_post = requests.post(base_url)
    return resp_post.text

url = 'http://ctflab.iytzx.com/Mini_Challenge.php'
url_step2 = url + "?step=2"
print(exploit_step2(url_step2))