# -*- coding: utf-8 -*-
# @Author: caijw 573301753@qq.com
# @Date:   2017-02-28 15:12:06
# @Last Modified by:   Administrator
# @Last Modified time: 2017-02-28 15:12:06
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5));