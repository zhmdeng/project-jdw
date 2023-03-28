"""
for this file:
1.cleaning data
2.analysis data
"""
import json

import  pandas as pd
from wms.view import View

class Clean:

    def get_history(self):
        """
        :arg: none
        :return: historic order's data
        """
        view = View()
        with open('./parameters.json','r',encoding='utf8') as path:
            paramters = json.load(path)
        paramters = paramters['history']
        url = 'http://gw.api.taobao.com/router/rest'
        data = view.obtain_json(url,paramters)
        # for key,value in data.items():
        #     print(key)
        # print(data)
        return data

    def latest_3month(self):
        """
        :arg: none
        :return: latest 3 months data of orders
        """
        view = View()
        with open('./parameters.json', 'r', encoding='utf8') as path:
            paramters = json.load(path)
        paramters = paramters['latest']
        url = 'http://gw.api.taobao.com/router/rest'
        data = view.obtain_json(url, paramters)
        return data

    def increment(self):
        """
        notes:end_modified - start_modified <= 1
        :return:
        """
        view = View()
        with open('./paramenters.json','r',encoding='utf8') as path:
            paramters = json.load(path)
        paramters = paramters['increment']
        url = 'http://gw.api.taobao.com/router/rest'
        data = view.obtain_json(url,paramters)
        return data

    def item_detail(self):
        view = View()
        with open('./parameters.json', 'r', encoding='utf8') as path:
            paramters = json.load(path)
        paramters = paramters['products']
        url = 'http://gw.api.taobao.com/router/rest'
        data = view.obtain_json(url, paramters)
        return data

    def sku_detail(self):
        view = View()
        with open('./parameters.json','r',encoding='utf8') as path:
            paramters = json.load(path)
        paramters = paramters['sku']
        print(paramters)
        url = 'http://gw.api.taobao.com/router/rest'
        data = view.obtain_json(url,paramters)
        return data

    def sku_update(self):
        view = View()
        with open('./parameters.json','r',encoding='utf8') as path:
            paramters = json.load(path)
        paramters = paramters['sku_update']
        url = 'http://gw.api.taobao.com/router/rest'
        data = view.obtain_json(url,paramters)
        return data

    def refund(self):
        view = View()
        with open('./parameters.json','r',encoding='utf8') as path:
            paramters = json.load(path)
        paramters = paramters['refund']
        url = 'http://gw.api.taobao.com/router/rest'
        data = view.obtain_json(url,paramters)
        return data

    def inventory(self):
        view = View()
        with open('./parameters.json','r',encoding='utf8') as path:
            paramters = json.load(path)
        paramters = paramters['inventory']
        url = 'http://gw.api.taobao.com/router/rest'
        data = view.obtain_json(url,paramters)
        return data

    def comments(self):
        """
        :arg: none
        :return: got comments data of item by item number
        """
        view = View()
        with open('./parameters.json','r',encoding='utf8') as path:
            paramters = json.load(path)
        paramters = paramters['comments']
        url = 'http://gw.api.taobao.com/router/rest'
        data = view.obtain_json(url,paramters)
        return data

if __name__ == '__main__':
    clean = Clean()
    clean = clean.get_history()
    print(clean)