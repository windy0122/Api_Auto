from tools.do_excel import DoExcel
from ddt import ddt, data   # 数据类型必须是列表嵌套列表，或者列表嵌套字典
import unittest
from tools.http_request import HttpRequest
import json
import tools.project_path as tool_path

test_data = DoExcel.get_data(tool_path.test_data_path, 'login')


@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_api(self, item):
        res = HttpRequest.http_request(item['url'], json.dumps(eval(item['data'])),
                                       item['http_method'], eval(item['header']))
        self.assertEqual('0', res.json()['success'])
        print('获取的结果是：{0}'.format(res.json()))


