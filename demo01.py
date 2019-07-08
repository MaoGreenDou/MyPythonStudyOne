# -*- coding:utf-8 -*

#注意开头

# 1 first program

print('Hello World!')

# float data
PI = 3.14159
pi = 3.14159
PI is pi

id(PI)
id(pi)

# 2 integer data

p = 3
q = 3
q is p

id(q)
id(p)

# 3 big integer data

a = 257
b = 257

a is b

id(a)
id(b)

# 4 string data

x = 'Hello World!'
y = 'Hello World'

x is y
id(x)
id(y)


# 5 数据类型：新增的：单引号/双引号/三引号字符串，元组，字典

data={'cos':'cos_value','sin':'sin_value'}
print(data['cos'])

# 6 运算符操作


x = int(input("Input x: "))       #输入语句
y = int(input("Input y: "))

print("x+y =", x + y)
print("x-y =", x - y)
print("x*y =", x * y)
print("x/y =", x / y)
print("x//y =", x // y)

# 7 r/R 运算符

print(r'this is a test\n')
print(R'this is a test\n')
print('this is a test\n')
print('this is a test')
print('this is a test')   # print语句 默认加一个换行符

# 8 输入输出语句小练习

firstname = input('请输入你的姓')
secondname = input('请输入你的名')
print('你的姓是',firstname)
print('你的名字',secondname)

# 9 python当中的 包  库 模块 之间的关系 以及两种导入方式

# 10 条件结构

a = 1
b = 2
c = 3
d = 1

if a>b:
    print('a>b')
elif b>c:
    print('b>c')
elif c<d:
    print('c<d')
else:
    print('a = d')

# 11 range 函数

list(range(10))

print(range(10))      #这输出的是啥

list = range(5,10)
print(list)          #同上，这输出的是啥

list = range(5,10,2)
print(list)

print(list[2])

# 12 while循环，for循环，列表解析，生成器