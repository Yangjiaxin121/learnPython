#!/use/bin/env python3
# -*- coding:utf-8 -*-

def product(*numbers):
    sum = 1
    for n in numbers:
        sum = sum * n;
    return sum


print(product(3, 4, 5, 6))
print('product()', product())
print('product(5) =', product(5))
print('product(5,6) =', product(5, 6))
print('product(5,6,7) =', product(5, 6, 7))
print('product(5,6,7,9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
