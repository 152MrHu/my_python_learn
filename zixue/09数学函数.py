import math

# abs(x) - 绝对值
print(abs(-10))          # 输出: 10

# ceil(x) - 上入整数（向上取整）
print(math.ceil(4.1))    # 输出: 5
print(math.ceil(-2.3))   # 输出: -2

# cmp(x, y) - Python3已废弃，用 (x>y)-(x<y) 替代
x, y = 5, 3
print((x > y) - (x < y))  # 输出: 1

# exp(x) - e的x次幂
print(math.exp(1))       # 输出: 2.718281828459045

# fabs(x) - 浮点型绝对值
print(math.fabs(-10))    # 输出: 10.0

# floor(x) - 下舍整数（向下取整）
print(math.floor(4.9))   # 输出: 4
print(math.floor(-2.3))  # 输出: -3

# log(x) - 自然对数
print(math.log(math.e))  # 输出: 1.0
print(math.log(100, 10)) # 输出: 2.0

# log10(x) - 以10为底的对数
print(math.log10(100))   # 输出: 2.0

# max(x1, x2, ...) - 最大值
print(max(3, 7, 2, 9))   # 输出: 9
print(max([5, 1, 8]))    # 输出: 8

# min(x1, x2, ...) - 最小值
print(min(3, 7, 2, 9))   # 输出: 2
print(min([5, 1, 8]))    # 输出: 1

# modf(x) - 拆分整数和小数部分
print(math.modf(4.7))    # 输出: (0.7000000000000002, 4.0)
print(math.modf(-2.3))   # 输出: (-0.30000000000000027, -2.0)

# pow(x, y) - x的y次幂
print(math.pow(2, 3))    # 输出: 8.0
print(pow(2, 3))         # 输出: 8（内置pow返回int，math.pow返回float）

# round(x [,n]) - 四舍五入
print(round(4.7))        # 输出: 5
print(round(4.736, 2))   # 输出: 4.74

# sqrt(x) - 平方根
print(math.sqrt(16))     # 输出: 4.0