__#6014__

```python
a = input()
print(3 * (a + '\n'))
```

기본적으로 print(3 * 변수) 하면 변수변수변수 로 출력된다. 그래서 줄바꿈 해주는것



__#6015__

```python
a, b = inpu().split()
print(a, '\n' + b)
```

print(a + '\n', b)랑 다르다. 후자로 할 경우, 뒤 입력 숫자 앞에 띄어쓰기가 적용된다.

__쉼표가 공백이라고 생각하면 print문을 이해하기 쉽다__



__#6017__

```python
a = input()
print(3 * (a + ' '))
```



__#6018__

```python
a, b = input().split(':') # :로 나누어진 두 입력값을 받겠다
print(a, b, sep=':') # a와 b를 받는데, 구분은 :로 할거다. (기본 sep = ' ')
```



help(print)를 입력하면 디폴트 값을 알 수 있다.

```
sep(구분) : ' ' (공백)
end(마지막) : '\n' (줄바꿈)
```

