#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/8 18:49
# @Author  : YeTao
import pytest
from test.calculate import Calculate
from test_cal.libs.get_yaml import YAMLUtils


class TestCase001:
    datas = YAMLUtils.utils_get_test_data('test_cal.yml', 'test_cal_01')
    ww = ['dd','as','11','aa']
    @pytest.mark.parametrize('datas', datas[1], ids=datas[0])
    def test_cal_01(self, datas):
        re = Calculate()
        assert re.cal(datas['a'], datas['b'], datas['c']) == datas['epx']


if __name__ == '__main__':
    pytest.main(['-sv'])
