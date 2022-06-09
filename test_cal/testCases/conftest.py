#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/8 18:49
# @Author  : YeTao
import pytest


@pytest.fixture(scope='class', autouse=True)
def c_start():
    print('测试开始')
    yield
    print('测试结束')


@pytest.fixture(scope='function', autouse=True)
def f_start():
    print('计算开始')
    yield
    print('计算结束')


def pytest_collection_modifyitems(items):
    """
    对收集好的用例根据id判断加上自定义标记
    """
    for item in items:
        if "P0" in item.nodeid:
            item.add_marker(pytest.mark.P0)
        if "P1" in item.nodeid:
            item.add_marker(pytest.mark.P1)
        print(item)
