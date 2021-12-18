import random
s = '1'
for i in range(1, 4000):
    s += ',' + str(random.randint(1, 10))
with open('file_1.txt', 'w') as failik:
    failik.write(s)
    failik.close()
s = '1'
for i in range(1, 8000):
    s += ',' + str(random.randint(1, 10))
with open('file_2.txt', 'w') as failik:
    failik.write(s)
    failik.close()
s = '1'
for i in range(1, 16000):
    s += ',' + str(random.randint(1, 10))
with open('file_3.txt', 'w') as failik:
    failik.write(s)
    failik.close()
