# Написать функцию, которая принимает строку и возвращает словарь
# вида:{'upper': N1, 'lower': N2}, где N1 и N2 кол-во символов
# верхнего и нижнего регистров соответственно.
# Вывести результат.
q = input()
def foo (a):
    b = {}
    c = 0
    d = 0
    for i in a:
        print(i)
        if i.islower() == True:
            c += 1
        else:
            d += 1
    b.update({'upper': d})
    b.update({'lower': c})
    print(b)
foo(q)
print(print(4))