import requests
import json

print("欢迎使用老魔法师翻译(由有道支持)!")
while True:
    word = input("请输入您要翻译的内容(输入0以退出):")
    if word == '0':
        break
    url = "https://fanyi.youdao.com/translate"
    headerua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    data = {
        'i':word,
        'doctype':'json',
    }
    response = requests.post(url,headers=headerua,data=data)
    target = json.loads(response.content.decode())
    result = target['translateResult'][0][0]['tgt']
    print(result)
