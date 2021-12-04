def F():
    a = dict()
    _s = input()
    while _s != '':
        s = _s.split()
        a[s[0] + ' ' + s[1]] = int(s[2])
        _s = input()
    return a

count = int(input()) #кол-во олимпиад
b=[]
for i in range(count):
    b.append(F())
for j in b:
    print(j)