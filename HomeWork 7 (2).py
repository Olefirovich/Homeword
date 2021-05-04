#2. Написать функцию, которая принимает строку и возвращает
# True либо False, в зависимости от того, является ли строка
# палиндромом.
# Например: "Never odd or even", "Able was I ere I saw Elba".
# Обратите внимание, что "палиндромность" строки не зависит
# от знаков препинания и пробелов.
file = 'Never odd or even'
def foo (a):
    x = True
    v = []
    g = v.append(a.lower().replace('\n', '').replace(' ',''))
    m = [i[::-1] for i in v]
    print(m)
    print(v)
    for ui in v:
        for iu in m:
            if ui == iu:
                print(x)
            else:
                print(not x)
foo(file)
