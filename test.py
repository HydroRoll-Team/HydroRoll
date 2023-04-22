import random

# 生成一个随机整数
num = random.randint(1, 10)
print(num)

# 从序列中随机选择一个元素
fruits = ['apple', 'banana', 'orange']
fruit = random.choice(fruits)
print(fruit)

# 打乱序列中元素的顺序
random.shuffle(fruits)
print(fruits)

# 生成一个 0 到 1 之间的随机小数
r = random.uniform(1,2)
print('%.2f' % r)
