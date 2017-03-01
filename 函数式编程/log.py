# -*- coding: utf-8 -*-
# @Author: caijw 573301753@qq.com
# @Date:   2017-03-01 15:02:31
# @Last Modified by:   Administrator
# @Last Modified time: 2017-03-01 15:02:31
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('test')
def now():
    print('2015-3-25')

now();