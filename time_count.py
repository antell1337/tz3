import time
from datetime import datetime
import count
import matplotlib.pyplot as plt

file_one = 'file_1.txt'
file_two = 'file_2.txt'
file_three = 'file_3.txt'


def test_one():
    t1 = time.time()
    for i in range(5):
        count.start(file_one)
    t2 = time.time()
    result_one = (t2 - t1) / 5
    return result_one


def test_two():
    t1 = time.time()
    for i in range(5):
        count.start(file_two)
    t2 = time.time()
    result_two = (t2 - t1) / 5
    return result_two


def test_three():
    t1 = time.time()
    for i in range(5):
        count.start(file_three)
    t2 = time.time()
    result_three = (t2 - t1) / 5
    return result_three


###### сохраняем время работы по 3 разным файлам
time_one = test_one()
time_two = test_two()
time_three = test_three()

###### строим график по времени, чтобы увидеть
###### зависимость
data = {'Test 1': time_one, 'Test 2': time_two, 'Test 3': time_three}
names = list(data.keys())
values = list(data.values())
fig, axs = plt.subplots()
axs.plot(names, values)
plt.savefig(f'data/grafik_{datetime.now():%d-%m_%Y_%H_%M_%S}.jpg')
