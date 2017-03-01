# -*- coding: utf-8 -*-
# @Author: caijw 573301753@qq.com
# @Date:   2017-03-01 14:25:57
# @Last Modified by:   Administrator
# @Last Modified time: 2017-03-01 14:25:57
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count();

print(f1());
print(f2());
print(f3());