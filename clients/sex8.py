import json

from libs.discuz import Discuz


class Sex8(Discuz):

    def __init__(self):
        super(Sex8, self).__init__()
        self.gwf_url = 'https://www.sex8.cc'
        self.base_url = 'https://www.sex8.cc'
        self.sign_url = 'dasp.php?u=Signin&a=sign_enter_click'
        self.do_sing_url = 'plugin.php?id=signin:signin_reg'
        self.invite_url = 'https://www.sex8.cc/90207742'

    def _handler(self, username, password, **kwargs):
        data = self.login(username, password)
        self.logger.info(data['message'])
        markdown = f"Sex8 {username}\n{data['message']}"
        if not self.is_ok(data):
            self.send_tg(markdown)
            return

        sign_data = self.sign()
        markdown = f'{markdown}\n{str(sign_data)}'
        self.logger.info(sign_data)
        self.send_tg(markdown)
        self.logger.info(self.user_info()['message'])

    def sign(self):
        sign_url = f'{self.base_url}/{self.sign_url}'
        self.fetch(sign_url)

        do_sign_url = f'{self.base_url}/{self.do_sing_url}'
        html = self.fetch(do_sign_url, {'ac': 'regsign'}).text
        if html.find('status') != -1:
            res = json.loads(html)
            if res.get('sign_tips'):
                del res['sign_tips']
            return res
        return html
