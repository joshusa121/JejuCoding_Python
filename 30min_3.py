#반복문(while, for) 조건문(if, elif, else)
a = 10
while a < 15:
    print('hello world')

a = 1
while True:
    print('hello world')
    if a > 9:
        break
    a += 1
else:
    print('good job')

a = 1
while False:
    print('hello world')
    if a > 9:
        break
    a += 1
else:
    print('good job')

#set은 중복을 허락하지 않는다
l = [10, 20, 30, 40]
S = {10, 20, 30, 40, 10, 10, 20}
for i in l:
    print(i)

for i in S:
    print(i)

for i in range(10):
    print(i)

print(list(range(10)))

print(1, list(range(10)))
print(2, list(range(5, 10)))
print(3, list(range(2, 10, 2)))
print(4, list(range(10, 5, -1)))
print(5, list(range(-10)))

for i in 'hello world':
    print(i)

for i in range(10):
    print(i)   
else:
    print('good job')

#일반 포맷 리스트
for i in range(2, 10):
    for j in range(1, 10):
        print('{} X {} = {}'.format(i, j, i*j))
#지능형리스트
lll = ['{} X {} = {}'.format(i, j, i*j) for i in range(2, 10) for j in range(1, 10)]

#벗기기 스킬
l = [(1, 10), (2, 20), (3, 30)]
for i, j in l:
    print(i, j)
print(l[2][1])

#넘버링함수
for i, j in enumerate(range(100, 1000, 100), 1):
    print(i, j)

#pass랑 continue부터 할 차례
#할 수 있다. 포기하지 말자. 
#파이썬 문법 열심히 배워서 코딩테스트 꼭 통과해보자!
