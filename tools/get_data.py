import pandas as pd
from tools.project_path import *


class GetData(object):
    Cookie = None
    # 从excel中读取数据
    NoRegTel = pd.read_excel(test_data_path, sheet_name='init').iloc[0, 0]
    normal_tel = pd.read_excel(test_data_path, sheet_name='init').iloc[1, 0]
    admin_tel = pd.read_excel(test_data_path, sheet_name='init').iloc[2, 0]
    loan_member_id = pd.read_excel(test_data_path, sheet_name='init').iloc[3, 0]
    memberID = pd.read_excel(test_data_path, sheet_name='init').iloc[4, 0]


# print(GetData.NoRegTel)
