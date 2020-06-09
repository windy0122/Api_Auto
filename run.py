from tools.http_request import HttpRequest
from tools.do_excel import DoExcel
import json
from tools.http_request_ddt import TestHttpRequest
import unittest
import tools.project_path as tool_path
import HTMLTestRunner_cn
from tools.do_email import DoEmail


# def run(test_data):
#     for item in test_data:
#         # print(item['case_id'])
#         print('现在正在执行的测试用例是:{0}'.format(item['title']))
#         res = HttpRequest().http_request(item['url'], json.dumps(eval(item['data'])),
#                                          item['http_method'], eval(item['header']))
#         print('请求的结果是：{0}'.format(res.json()))
#         DoExcel().write_back('D:/Api_Auto/test_data/test.xlsx', 'login', int(item['case_id'])+1, str(res.json()))
#
#
# test_data_login = DoExcel.get_data('D:/Api_Auto/test_data/test.xlsx', 'login')
# run(test_data_login)

suite = unittest.TestSuite()
loder = unittest.TestLoader()
suite.addTest(loder.loadTestsFromTestCase(TestHttpRequest))

with open(tool_path.test_report_path, 'wb') as file:
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=file, title='单元测试', description='测试报告', tester='吴迪')
    runner.run(suite)

DoEmail().send_email()

