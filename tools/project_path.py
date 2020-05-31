# 专门读取路径的值

import os

# project_path = os.path.realpath(__file__)  # D:\Api_Auto\tools\project_path.py
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]    # D:\Api_Auto

# 测试用例路径
test_data_path = os.path.join(project_path, 'test_data', 'test.xlsx')     # D:\Api_Auto\test_data\test.xlsx

# 测试报告路径
test_report_path = os.path.join(project_path, 'test_result', 'html_report', 'test_report.html')

print(test_data_path)




