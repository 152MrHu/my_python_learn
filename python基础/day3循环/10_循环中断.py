# 只作用在所属最近的循环中
for i in range(10):
    if i == 5:
        break
    print(i, end=' ')
print()

for i in range(10):
    if i == 5:
        continue
    print(i, end=' ')
print()

for i in range(10):
    if i == 5:
        pass
    print(i, end=' ')