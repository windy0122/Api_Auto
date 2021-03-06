from ddt import ddt, data   # 数据类型必须是列表嵌套列表，或者列表嵌套字典
import unittest
from tools.http_request import HttpRequest
import json
import tools.project_path as tool_path
from tools.do_excel import DoExcel
from test_result.log.api_logging import MyLog

my_logger = MyLog()
test_data = DoExcel.get_data(tool_path.test_data_path)


@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_api(self, item):
        res = HttpRequest.http_request(item['url'], json.dumps(eval(item['data'])), item['http_method'], eval(item['header']))
        try:
            self.assertEqual('0', res.json()['success'])
            TestResult = 'PASS'
        except AssertionError as e:
            TestResult = 'FAILED'
            my_logger.info('执行出错：{0}'.format(e))
            raise e
        finally:
            DoExcel.write_back(tool_path.test_data_path, item['sheet_name'], int(item['case_id'])+1, str(res.json()), TestResult)
            print('获取的结果是：{0}'.format(res.json()['msg']))



