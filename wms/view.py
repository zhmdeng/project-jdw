"""
obtain original api json data
"""
import requests
from bases.date import Date
from bases.logs import Logs

class View:

    def obtain_json(self,url,paramters):
        """
        :param url:
        :param paramters:
        :return: json data
        """
        logs = Logs()
        # url = 'http://gw.api.taobao.com/router/rest'  #api link
        '''
            apikey = 'chgaxvsf88f3858a15fa4426f4cbdd4d2a02b92ee0747f3'
            area = "人生"
            areaID = "45"
            data = {
                "apiKey":apikey,
                "area":area,
                "areaID":areaID,
                }
            wb_data = requests.get(url,apikey,data)
        '''
        try:
            wb_data = requests.get(url,params=paramters)
            result = wb_data.json()
            logs.info("",f"{url} load successful!!!","test")
            return result
        except Exception as e:
            logs.info("", f"error:{e}", "test")


# if __name__ == '__main__':
#     view = View()
#     paramters = {'appid':'52766586','appsecret':'o1bLGo6t','version':'v61'}
#     url = 'https://v0.yiketianqi.com/api'
#     data = view.obtain_jsion(url,paramters)
#     print(data)

    
    
    
    
    
    
    
    
    
#     def main(self):
#         try:
#             appkey = ''
#             secret = ''
#             url = ''
#             port = ''
#             client = top.api.UserOpenidGetRequest(url,port)
#             client.set_app_info(top.appinfo(appkey,secret))
#         except ValueError:
#             print('Error!!!')
            
#     def get_(selef,domain,port,appkey,secret,sessionkey):
#         req=top.api.TradeFullinfoGetRequest(domain,port)

#         req.set_app_info(top.appinfo(appkey,secret))

#         req.fields="tid,type,status,payment,orders,promotion_details"

#         req.tid=123456789

#         try:

#             resp= req.getResponse(sessionkey) 
#             resp = resp.json()
#             return resp

#         except Exception as e:
#             print(e)
                    
            
# SYSTEM_GENERATE_VERSION = "taobao-sdk-python-20151217"

# P_APPKEY = "app_key"

# P_API = "method"

# P_SESSION = "session"

# P_ACCESS_TOKEN = "access_token"

# P_VERSION = "v"

# P_FORMAT = "format"

# P_TIMESTAMP = "timestamp"

# P_SIGN = "sign"

# P_SIGN_METHOD = "sign_method"

# P_PARTNER_ID = "partner_id"

# P_CODE = 'code'

# P_SUB_CODE = 'sub_code'

# P_MSG = 'msg'

# P_SUB_MSG = 'sub_msg'

# N_REST = '/router/rest'

# writer = codecs.lookup('utf-8')[3]

# def sign(secret, parameters):

#     if hasattr(parameters, "items"):
#         # keys = parameters.keys()
#         keys = list(parameters.keys()) # sudoz: Py3
#         keys.sort()
#         parameters = "%s%s%s" % (secret,str().join('%s%s' % (key,parameters[key]) for key in keys), secret)
#         # sign = hashlib.md5(parameters).hexdigest().upper()
#         sign = hashlib.md5(parameters.encode('utf8')).hexdigest().upper() # sudoz: Py3
#     return sign

# def mixStr(pstr):

#     if (isinstance(pstr, str)):
#         return pstr
#     elif (isinstance(pstr, bytes)): # sudoz: Py3
#         return ascii(pstr)
#     else:
#         return str(pstr)

# class FileItem(object):

#     def __init__(self, filename=None, content=None):
#         self.filename = filename
#         self.content = content

# class MultiPartForm(object):

#     """Accumulate the data to be used when posting a form."""

#     def __init__(self):

#         self.form_fields = []

#         self.files = []

#         self.boundary = "PYTHON_SDK_BOUNDARY"

#         return

#     def get_content_type(self):

#         return 'multipart/form-data; boundary=%s' % self.boundary

#     def add_field(self, name, value):

#         """Add a simple field to the form data."""

#         self.form_fields.append((name,str(value)))

#         return

#     def add_file(self, fieldname, filename, fileHandle, mimetype=None):

#         """Add a file to be uploaded."""

#         if mimetype is None:

#             mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'

#             self.files.append((fieldname, filename,fileHandle, mimetype))

#             return

