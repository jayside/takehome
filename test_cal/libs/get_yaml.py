#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/8 18:53
# @Author  : YeTao
import yaml
from test_cal.libs.params import test_datas_path


class YAMLUtils:
    @staticmethod
    def utils_get_test_data(file_name, case_name):
        """
        :param file_name: 测试数据文件名
        :param case_name: 文件的用例标号
        :return: 测试数据的优先级，及对应测试数据
        """
        file_path = test_datas_path + file_name
        with open(file_path, mode="r", encoding="utf-8") as f:
            data = yaml.load(stream=f, Loader=yaml.FullLoader)[case_name]
            datas = []
            levels = []
            for i in list(data.keys()):
                datas += data[i]
                nums = len(data[i])
                levels.append(i)
                if nums != 1:
                    for ii in range(1, nums):
                        levels.append(i)
            return levels, datas
