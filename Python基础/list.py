# -*- coding: utf-8 -*-
# @Author: caijw 573301753@qq.com
# @Date:   2017-02-28 14:12:59
# @Last Modified by:   Administrator
# @Last Modified time: 2017-02-28 14:12:59
classmates = ['cjw2','cjwe3','cjw2'];
print(classmates[0]);
print(len(classmates));
classmates.append('adam');
classmates.insert(1, 'jack');
print(classmates[len(classmates)-1]);
classmates.pop();
print(classmates[len(classmates)-1]);
classmates.pop(0);
print(classmates[0]);


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0]);
print(L[1][1]);
print(L[2][2]);

