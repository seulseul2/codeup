def get_strong_word(a, b):
    result_a = 0
    result_b = 0
    for i in a:
        result_a += ord(i)
    for i in b:
        result_b += ord(i)
    if result_a > result_b:
        return a
    else:
        return b
        
print(get_strong_word('z', 'a'))
print(get_strong_word('tom', 'john'))