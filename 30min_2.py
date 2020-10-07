#리스트
l = [100, 200, 300, 400]
print(l)
print(type(l))
#print(dir(l))
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


