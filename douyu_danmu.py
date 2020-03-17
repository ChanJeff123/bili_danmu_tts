import requests

headers = {
    'authority': 'yuba.douyu.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'sec-fetch-dest': 'empty',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://yuba.douyu.com/iframe/tab/93589?iframeUrlGid=4459&timesTamp=15844406',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'cookie': 'smidV2=2019112916223926319a51dae5353321edcd7c5a2744cf00a8f93e6649005c0; dy_did=a3759fb9641c553be66cd78100001501; acf_yb_did=a3759fb9641c553be66cd78100001501; loginrefer=pt_i2ifcn9jg69h; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1584293014,1584333171,1584440604; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1584440611; Hm_lvt_e0374aeb9ac41bee98043654e36ad504=1584293138,1584440631; Hm_lpvt_e0374aeb9ac41bee98043654e36ad504=1584440631',
}

params = (
    ('page', '1'),
    ('group_id', '4459'),
    ('room_id', '93589'),
)

response = requests.get('https://yuba.douyu.com/wbapi/web/room/group/postdetaillist', headers=headers, params=params)

results=response.json()["list"]
for data in results:
    print(data['title'])