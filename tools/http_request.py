import requests
from test_result.log.api_logging import MyLog
my_logger = MyLog()


class HttpRequest(object):
    @staticmethod
    def http_request(url, data, http_method, header, verfiry=False):
        try:
            if http_method.lower() == 'get':
                res = requests.get(url=url, data=data, headers=header)
            elif http_method.lower() == 'post':
                res = requests.post(url=url, data=data, headers=header)
            else:
                print('输入的请求方法不正确')
        except Exception as e:
            my_logger.error('请求报错了：{}'.format(e))
            raise e
        return res




