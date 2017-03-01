# -*- coding: utf-8 -*-
# @Author: caijw 573301753@qq.com
# @Date:   2017-03-01 15:18:25
# @Last Modified by:   Administrator
# @Last Modified time: 2017-03-01 15:18:25
'a test module';

__author__ = 'cjw';

import sys;

def test():
	args = sys.argv;
	if len(args)==1:
		print('hello,world!')
	elif len(args)==2:
		print('hello,%s!'%args[1])
	else:
		print('too many arguments');

if __name__=='__main__':
	test()