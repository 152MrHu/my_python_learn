import random
random_num = random.randint(1, 100)
print(random_num)
num = int(input('请输入一个数字： '))

if num == random_num:
    print('恭喜你一次，猜对了！')
else:
    if num > random_num:
        print('你猜的数字太大了！')
    else:
        print('你猜的数字太小了！')
    num = int(input('请再试一次： '))
    if num == random_num:
        print('恭喜你二次，猜对了！')
    else:
        if num > random_num:
            print('你猜的数字太大了！')
        else:
            print('你猜的数字太小了！')
        num = int(input('请再试一次： '))
        if num == random_num:
            print('恭喜你三次，猜对了！')
        else:
            print('很遗憾，你三次都没有猜对！')

