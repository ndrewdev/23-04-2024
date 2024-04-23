def primary_check(s):   #Проверка количества
    if s.count('(') != s.count(')'):    return False
    if s.count('{') != s.count('}'):    return False
    if s.count('[') != s.count(']'):    return False
    if s.count('<') != s.count('>'):    return False
    return True

def secondary_check(s): #Проверка порядка
    o = '([{<'
    c = ')]}>'

    i = 1
    prev = ''
    
    for L in s:
        if i == 1 and L not in o:   #Кто писал этот код?
            return False
        if prev in o:
            if not (L in o or L == c[o.index(prev)]):
                return False
        prev = L
        i -= 1
    
    return True

def check(s):
    s = s.replace(' ', '')
    return primary_check(s) and secondary_check(s)

print(check(input()))   #Ввод с клавиатуры
