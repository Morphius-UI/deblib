with open('ktylib/sahara_adlist') as f:
    _sahara_adlist = f.read().splitlines()

class JunkTxSender:
    def __init__(self, acc):
        self.acc = acc
        self.w3 = acc.w3
    def _send_random_tx(self, to_address=None, value=None):
        self.w3('sahara_testnet')
        if not value:
            value = random.randint(100000000000000, 300000000000000)
        if not to_address:
            to_address = random.choice(_sahara_adlist)
        return 0, self.w3.eth.send_transaction({'to': to_address, 'value': value}).to_0x_hex()

    def send_random_tx(self, to_address=None, value=None):
        try:
            return self._send_random_tx(to_address, value)
        except Exception as e:
            return -1, f'{e}'




class SaharaManager:
    def __init__(
        self,
        acc: Account,
        ref_code: str | None,
        rpc: str = "https://legends.saharalabs.ai/api/v1",
        wallet_name: str = "MetaMask",
        wallet_uuid: str = "811ce742-eecd-4f6d-b408-27ba99a8ff29"
    ):
        self.acc = acc
        self.ref_code = ref_code
        self.wallet_name = wallet_name
        self.wallet_uuid = wallet_uuid
        self.rpc = rpc
        self.referrals = []
        self.authorized = False
        self.session = requests.Session()
        print("Sahara Manager was successfully initialized")

    @property
    def addr(self) -> str:
        return self.acc.address.lower()

    @property
    def _wallet_uuid(self) -> str:
        return self.user_info["walletUUID"]

    @property
    def user_info(self) -> str:
        if not self.authorized: return
        url = f"{self.rpc}/user/info"
        return self.session.post(url, json={}).json()

    def _get_challenge(self) -> str:
        url = f"{self.rpc}/user/challenge"
        body = { "address": self.addr }
        response = self.session.post(url, json=body)
        return response.json()["challenge"]

    def _get_message(self) -> str:
        return f"Sign in to Sahara!\nChallenge:{self._get_challenge()}"

    def _sign_message(self, message: str) -> str:
        return self.acc.sign_text_message(message).signature.to_0x_hex()

    def login(self) -> dict:
        if self.authorized: return
        sig = self._sign_message(self._get_message())
        url = f"{self.rpc}/login/wallet"
        body = {
            "address": self.addr,
            "referralCode": self.ref_code,
            "sig": sig,
            "walletName": self.wallet_name,
            "walletUUID": self.wallet_uuid,
        }
        response = self.session.post(url, json=body).json()
        self.access_token = response["accessToken"]
        self.refresh_token = response["refreshToken"]
        self.session.headers.update({ "authorization": f"Bearer {response["accessToken"]}" })
        print("Login success")
        self.authorized = True
        return response

    @property
    def map_states(self) -> list:
        if not self.authorized: return
        url = f"{self.rpc}/user/info"
        response = self.session.post(url, json={}).json()
        return response["mapStates"]

    @property
    def maps(self) -> list:
        if not self.authorized: return
        url = f"{self.rpc}/system/configTable"
        response = self.session.post(url, json={}).json()
        return response["maps"]

    def get_ref_code(self) -> str:
        url = f"{self.rpc}/referral/code"
        response = self.session.post(url, json={}).json()
        return response["code"]

    def daily_referral(self, refs: list[Account]):
        code = self.get_ref_code()
        for ref in refs:
            manager = SaharaManager(ref, code)
            manager.login()
            # TODO: add other activity
            self.referrals.append(manager)

    def generate_transaction(self, rand_addr: str, value: str = 1):
        tx = self.acc.w3("sahara_testnet").get_full_tx_data(
            rand_addr,
            value=value,
            gas_price=acc.w3.eth.gas_price
        )
        print(f"Sending {from_wei(value, "ether")} from {self.acc.address} to {rand_addr}")
        tx_hash = self.acc.w3.eth.send_transaction(tx).to_0x_hex()
        print(f"Transaction sent: {tx_hash}")

    # status 1 - not completed, 2 - completed, 3 - reward claimed
    def flush(self, task_id: str) -> int:
        url = f"{self.rpc}/task/flush"
        body = {"taskID": task_id}
        response = self.session.post(url, json=body).json()
        return response

    # status 1 - not completed, 2 - completed, 3 - reward claimed
    # doesn't work without flush method
    def task_status(self, task_id: str) -> str:
        url = f"{self.rpc}/task/dataBatch"
        body = {"taskIDs": [task_id]}
        response = self.session.post(url, json=body).json()
        return response[task_id]["status"]

    def claim_reward(self, task_id: str) -> str:
        self.flush(task_id)
        status = self.task_status(task_id)
        if status == '1':
            return -1, 'TryAgainLater'
        if status == '3':
            return 1, 'AlreadyClaimed'
        url = f"{self.rpc}/task/claim"
        body = {"taskID": task_id}
        response = self.session.post(url, json=body).json()
        # print(response)
        if "code" in response and response["code"] == -1:
            print(response["message"])
            return -1, response
        # print(f"Claimed {response[0]["amount"]} shards")
        return 0, f'Claimed: {response}'
