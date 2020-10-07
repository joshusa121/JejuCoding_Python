# 1부
#주석, 컨트롤 슬러쉬!
'''
주석
'''

#타입
a=10
b=10.1
c='hello'
d=-1
e='lee'
f='hj'
g=10 + 2j
h=0b1001
i=0o1001
j=0x1001

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
print(name2.strip())

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
print('제 나이는 '.age'입니다.')
print('제 나이는 {0}입니다. 제 이름은 {1}입니다.'.format(age, name))

#f-string

age = 10
name = 'josh'
print('제 나이는 '.age'입니다.)
print('제 나이는 {age}입니다. 제 이름은 {name}입니다.')

#구구단
for i in ragne(2, 10):
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j})

