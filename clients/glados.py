import requests

from libs.base import BaseClient


class Glados(BaseClient):

    def __init__(self):
        super().__init__()

    def run(self, **kwargs):
        self.log(self.checkin(kwargs.get('cookie')))

    def checkin(self, cookie):
        url = "https://glados.rocks/api/user/checkin"
        referer = 'https://glados.rocks/console/checkin'
        result = requests.post(url, headers={'cookie': cookie, 'referer': referer}).json()
        if result['code'] != 0:
            self.send_tg(f'Glados cookie has expired\n{result}')
        return result