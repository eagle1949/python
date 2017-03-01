###map/reduce
```
def f(x):
	return x*x;

r = map(f, [1,2,3,4,5,6,7]);
print(list(r));
```
###返回函数
```
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
```
####装饰器
```
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
```