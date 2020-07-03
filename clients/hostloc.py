from libs.base import BaseClient
from libs.discuz import Discuz


class Hostloc(Discuz):

    def __init__(self):
        super(Hostloc, self).__init__()
        self.base_url = 'https://www.hostloc.com'

    def _handler(self, username, password, **kwargs):
        data = self.login(username, password)
        self.log(data['message'])
        if not self.is_ok(data):
            return

        # self.log(self.user_info())
        self.views()
        self.log(self.user_info()['message'])
