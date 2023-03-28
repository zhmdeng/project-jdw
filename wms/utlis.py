"""
assistant tools
"""

import json
from wms.view import View


class Utils:

    def get_sessionkey(self):

        view = View()
        with open('./parameters.json','r',encoding='utf8') as path:
            paramters = json.load(path)
        paramters = paramters['session']
        url = ' https://oauth.taobao.com/token'
        sessionkey = view.obtain_json(url,paramters)
        return sessionkey

    def get_code(self):

        return self

    @get_code
    def get_tooken(self):
        print("tooken")

if __name__ == '__main__':
    utils = Utils()
    utils.get_tooken()