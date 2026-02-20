import random

# 1. choice(seq)：从序列中随机选一个元素
seq = ['apple', 'banana', 'cherry']
print(random.choice(seq))  # 可能输出 'banana'

# 2. randrange([start,] stop[, step])：从指定范围按步长取随机整数
print(random.randrange(10))       # 0-9 之间的随机整数
print(random.randrange(1, 10, 2)) # 1,3,5,7,9 中的一个

# 3. random()：生成 [0,1) 之间的随机浮点数
print(random.random())  # 例如 0.573214

# 4. seed([x])：设置随机种子，让结果可复现
random.seed(42)
print(random.random())  # 每次运行都会得到相同的结果

# 5. shuffle(lst)：将列表随机打乱顺序
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst)  # 例如 [3, 1, 5, 2, 4]

# 6. uniform(x, y)：生成 [x, y] 之间的随机浮点数
print(random.uniform(1, 10))  # 例如 3.7892