from datetime import datetime
import requests
import time
from chea import headers


class Game:
    def __init__(self, rpc:str='https://moonveil.gg/api/oauth2/authorize'):
        self.rpc = rpc
    def auth(self):
        url = self.rpc
        headers = {
            'accept': '*/*',
            'accept-language': 'ru,en;q=0.9',
            'authorization': 'f73f1773-37e1-4c60-a441-2f83661bc928',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            # 'cookie': '_ga=GA1.1.1419321922.1734734299; _ga_S033BWR07Y=GS1.1.1740691813.58.0.1740691813.0.0.0',
            'origin': 'https://moonveil.gg',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://moonveil.gg/oauth?landing_url=https%3A%2F%2Fgoldminer.moonveil.gg&response_type=code&client_id=1bcb51aa-bab1-476d-b09a-f20d103d16d0&redirect_uri=https%3A%2F%2Fgoldminer-api.moonveil.gg%2FauthCallback&scope=userinfo&state=7ba74ce3-d036-4e5c-a161-282513200344&client_name=Puffy%20Miner&icon_url=https%3A%2F%2Fd3dhz6pjw7pz9d.cloudfront.net%2Fgame%2Fgoldminer%2Ficon.png',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "YaBrowser";v="25.2", "Yowser";v="2.5"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 YaBrowser/25.2.0.0 Safari/537.36',
        }

        json_data = {
            'landing_url': 'https://goldminer.moonveil.gg',
            'response_type': 'code',
            'client_id': '1bcb51aa-bab1-476d-b09a-f20d103d16d0',
            'redirect_uri': 'https://goldminer-api.moonveil.gg/authCallback',
            'scope': 'userinfo',
            'state': '7ba74ce3-d036-4e5c-a161-282513200344',
            'client_name': 'Puffy Miner',
            'icon_url': 'https://d3dhz6pjw7pz9d.cloudfront.net/game/goldminer/icon.png',
        }
        r = requests.post(url, headers=headers, json=json_data)
        return r.text
    def play(self):
        url = 'https://goldminer-api.moonveil.gg/deductTicket'
        headers = {
            'accept': '*/*',
            'accept-language': 'ru,en;q=0.9',
            'authorization': 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..dO0uSyWRyJFm3bQp.s1TlyEEmMUz_kYwL88tvpIM1caJ088iJAf-bNIpewnBt2ppVQOI_DepiUteDg2bMCjBDHoQuaRxQ2ydTEh7PbL2If-TpJO_PTSC8mMJtkDZcmhSBsZNG3JldRwfjlKllrmAHcvrtV0R-8fq0QQ9Y4AriNcbFUdBrvMRJtdwQITeG2cYdbKoALeeXN2IQQDYtOJHcwioiyl8CvSFwUpk3tj4WXccIxu5We5wKWcpOtb0rMHJShqQmWbWTAaPdi5v7wA.Ebre3KaApVKqaIIEcbRQOg',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://goldminer.moonveil.gg',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://goldminer.moonveil.gg/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "YaBrowser";v="25.2", "Yowser";v="2.5"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 YaBrowser/25.2.0.0 Safari/537.36',
        }
        data = {
            'uid': '65b24e79-43d8-4fcb-acd4-c9b85dcf3bed',
            'num': '1',
        }
        response = requests.post('https://goldminer-api.moonveil.gg/deductTicket', headers=headers, data=data)
        return response.text
    def update(self):
        headers = {
            'accept': '*/*',
            'accept-language': 'ru,en;q=0.9',
            'authorization': 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..dO0uSyWRyJFm3bQp.s1TlyEEmMUz_kYwL88tvpIM1caJ088iJAf-bNIpewnBt2ppVQOI_DepiUteDg2bMCjBDHoQuaRxQ2ydTEh7PbL2If-TpJO_PTSC8mMJtkDZcmhSBsZNG3JldRwfjlKllrmAHcvrtV0R-8fq0QQ9Y4AriNcbFUdBrvMRJtdwQITeG2cYdbKoALeeXN2IQQDYtOJHcwioiyl8CvSFwUpk3tj4WXccIxu5We5wKWcpOtb0rMHJShqQmWbWTAaPdi5v7wA.Ebre3KaApVKqaIIEcbRQOg',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://goldminer.moonveil.gg',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://goldminer.moonveil.gg/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "YaBrowser";v="25.2", "Yowser";v="2.5"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 YaBrowser/25.2.0.0 Safari/537.36',
        }
        data = {
            'uid': '65b24e79-43d8-4fcb-acd4-c9b85dcf3bed',
            'num': '0',
        }
        response = requests.post('https://goldminer-api.moonveil.gg/updateGold', headers=headers, data=data)
        return response.text
    def claimpoint(self):
        json_data = {
            'data': [
                {
                    '#type': 'user_set',
                    '#time': datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
                    '#distinct_id': '9816578015-1740426481277',
                    '#account_id': '65b24e79-43d8-4fcb-acd4-c9b85dcf3bed',
                    'properties': {},
                    '#uuid': '06d28398-8811-4616-a617-80722abcb5d3',
                },
            ],
            '#app_id': '273f2da463c6433899e842fe53f11ae7',
            "#flush_time": int(time.time() * 1000)
        }

        response = requests.post('https://datacollector.moonveil.gg/sync_xcx', json=json_data)
        return response.text



manager = Game()

print(manager.auth())
print(manager.play())
time.sleep(45)
print(manager.claimpoint())
print(manager.update())