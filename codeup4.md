__정수나 실수 두 개를 받고 싶을 때!__

```python
a, b = int(input().split())
c = a - b
print(c)

# 안되는 이유는 생각해보면 당연하다.
# 예를 들어 input을 3과 4로 넣었다면 int(3, 4)인 셈이다.
# 그렇기 때문에
a, b = input().split() # 먼저 입력값을 문자열로 받아준 다음
int(a), int(b) # 이렇게 따로 처리해주어야 한다.
```

