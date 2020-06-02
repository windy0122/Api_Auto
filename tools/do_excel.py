from openpyxl import load_workbook
from tools.read_config import ReadConfig
from tools.project_path import *


class DoExcel(object):
    @staticmethod
    def get_data(file_name):
        wb = load_workbook(file_name)

        mode = eval(ReadConfig.get_config(test_config_path, 'MODE', 'mode'))

        test_data = []
        for key in mode:
            sheet = wb[key]
            for i in range(2, sheet.max_row + 1):
                row_data = dict()
                row_data['case_id'] = sheet.cell(i, 1).value
                row_data['url'] = sheet.cell(i, 2).value
                row_data['data'] = sheet.cell(i, 3).value
                row_data['title'] = sheet.cell(i, 4).value
                row_data['http_method'] = sheet.cell(i, 5).value
                row_data['header'] = sheet.cell(i, 6).value
                test_data.append(row_data)
        return test_data



    @staticmethod
    def write_back(file_name, sheet_name, i, result, TestResult):
        wb = load_workbook(file_name)
        sheet = wb[sheet_name]
        sheet.cell(i, 7).value = result
        sheet.cell(i, 8).value = TestResult
        wb.save(file_name)


if __name__ == '__main__':
    res = DoExcel.get_data('D:/Api_Auto/test_data/test.xlsx')
    print(res)

