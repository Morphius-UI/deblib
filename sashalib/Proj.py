solver = TwoCaptcha('ef8a6e8675cfcf33786dc34b17eeae7c')

class SaharaFaucet:
    def __init__(
        self,
        acc: Account,
        rpc: str = "https://testnet.saharalabs.ai/",
        wallet_name: str = "MetaMask",
        wallet_uuid: str = ""
    ):
        self.acc = acc
        self.wallet_name = wallet_name
        self.wallet_uuid = wallet_uuid
        self.rpc = rpc
        self.authorized = False
        self.session = requests.Session()
        print("Sahara Faucet was successfully initialized")

    @property
    def addr(self) -> str:
        return self.acc.address.lower()

    def _sign_message(self, message: str) -> str:
        return self.acc.sign_text_message(message).signature.to_0x_hex()

    def login(self):
        if self.authorized: return
        url = f"{self.rpc}"
        json_data = {
            'jsonrpc': '2.0',
            'id': 1,
            'method': 'eth_getBalance',
            'params': [
                self.addr,
                'latest',
            ],
        }
        response = self.session.post(url, json=json_data).json()
        print("Login success")
        self.authorized = True
        return response

    def resultcaptcha(self):
        return solver.turnstile(sitekey="0x4AAAAAAA8hNPuIp1dAT_d9",url='https://faucet.saharalabs.ai/')

    def veryfi_captha(self):
        url = 'https://faucet-api.saharaa.info/api/claim2'
        res = self.resultcaptcha()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': 'https://faucet.saharalabs.ai/',
            'Content-Type': 'application/json',
            'cf-turnstile-response': res['code'],
            'Origin': 'https://faucet.saharalabs.ai',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'DNT': '1',
            'Priority': 'u=0',
            'TE': 'trailers',
        }

        data = {"address": "0xE822b17be0BC7AA706f681371Bf72af2d9bB5eca"} #{"address": self.acc.address}
        request = self.acc._rpost(url, headers=headers, json=data)
        return request.text



class MoonveilFaucet:
    def __init__(
        self,
        acc: Account,
        rpc: str = "https://faucet.testnet.moonveil.gg/api/claim",
    ):
        self.acc = acc
        self.rpc = rpc

    def claim(self):
        url = f'{self.rpc}'
        json_data = {
            'address': self.acc.address
        }
        request = self.acc._rpost(url, json=json_data)
        return request.text