#print('hello data', end='\n') 

print(type(a))

name = 'joshaaaaa'
print(a[3])
print(a[3:8])
print(a[3:8:2])
print(a[3:8:-1])

print(a.upper())
print(a.lower())
print(a.count())

name2 = '     joshaaaaa'
print(name2.strip()) #공백 없애기

aa=2020 
bb=12
cc=11
print(a, b, c, sep='/', end=' ')
#end=' ' 는 엔터 안치겠다는 뜻

#형변환
int(aa)
str(aa)

print(bool(' '))
print(bool(''))
print(bool('0'))
print(bool('1'))
print(bool('-1'))
print(bool('None'))

#할당연산
a = 10
a = a + 10
a += 10
print(a)

#함수!
def f(x, y):
    z = x + y
    return z
print(f(3, 5))

#함수의 순서
def ff():
    print('1')
    print('2')
    print('3')    
print(4)
ff()

def circle(r):
    width = r*r*3.14
    return width
print(circle(10))

#함수 안의 인자는 밖에서 불러오지 못한다. 단, 글로벌을 쓰면 가능
a = 10
def aplus():
    global a
    a += 10
    return a
print(aplus())

#format
age = 10
name = 'josh'

print('제 나이는 {0}입니다. 제 이름은 {1}입니다.'.format(age, name))

#f-string
age = 10
name = 'josh'
print('제 나이는 '.age'입니다.')
print('제 나이는 {age}입니다. 제 이름은 {name}입니다.')

#구구단
for i in ragne(2, 10):
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j})

#리스트
l = [100, 200, 300, 400]
print(l)
#print(dir(l))
print(type(l))
#변경이 가능한 자료형
#순서가 있는 자료형
print(l[1])
l[1] = 1000
print(l)

print(dir(l))
l.append(300) #하나만 추가
print(l)
#l.clear() 비우는 애
print(l.count(300))

l.extend([100, 200, 300])
l.insert(3, 1000)
l.pop(3)
l.remove(100)
l.reverse()
l.sort()
# sorted()
# reversed()

print(l[::-1])
# start:stop:step의 순서다

print(set('aabbbeeedd')) #중복제거

#딕셔너리
d = {'one':10, 'two':20}
#순서가 없고 키 중복을 허락하지 않는다
print(type(d))
print(dir(d))
print(d.values(d))
print(d.items(d))

l = list(d.items())
print(l[0][1]) #다중 리스트

#.copy -> 원 인자는 그대로 나두고 복사인자만 변경

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