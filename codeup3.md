__#6014__

실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.

```python
a = input()
print(3 * (a + '\n'))
```

왜 float으로 하면 안될까요?



__##6017__

정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자.

예시
s = input()
print(s, s, s) #공백으로 구분해 한 줄로 출력한다.
와 같은 방법으로 3번 출력할 수 있다.

```python
a = input()
print(3 * (a + ' '))
```

왜 print(3 * (a, sep=' '))로 하면 안될까요?



__##6027~6030##__ 

%x -> 16진수(소문자)

%X -> 16진수(대문자)

16진수로 입력받는 방법 => a = int(input(), 16)

%o -> 8진수(숫자)

ord(x) : x를 10진수로 변환한 값 [ 문자 -> 숫자 ]