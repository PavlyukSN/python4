# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

n = int(input('Сколько кустов в Вашем фермерском хозяйстве? - '))
luck = []
for i in range(n):
     luck.append(randint(0,10))
print("Всего поспело",luck,"едениц черники (список по кустам).")

event = 0
for i in range(n):
     crop = luck[i-2] + luck[i-1] + luck[i]
     print(crop,"=",luck[i-2],  luck[i-1],  luck[i])
     if crop > event:
          event = crop
     
print("Максимальный сбор за 1 заход:",event)
