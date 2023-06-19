for i in range(1, 10):
    for j in range(2, 6):
        if i%4==0:
            print(j , '*' , i, '=' , i * j, end=' ')
        else:
            print(end='')
    print()
print()
for i in range(1, 10):
    for j in range(6, 10):
        if i%4!=0:
            print(j , '*' , i, '=' , i * j, end='  ')
    print()