
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


acc = Account(eth_key='0x09ee51b8e542201fde2e703b24fc961f44cfe14ccceb057d5d93b2f411750301', proxy='http://zldgybtw-100:ddz3ec7o9l2g@p.webshare.io:80')
manager = MoonveilFaucet(acc)
print(manager.claim())
