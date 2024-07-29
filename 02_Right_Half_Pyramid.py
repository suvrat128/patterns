'''
*
* *
* * *
* * * *
* * * * *
'''

# using one loop

n = int(input())

for i in range(1,n+1):
    print('* '*i)

# pattern using nested loop

n = int(input())
for row in range(1,n+1):
    for col in range(1,row+1):
        print('*',end=' ')
    print()

# generic aproch

n = int(input())
star = 1
for row in range(1,n+1):
    for st in range(1,star+1):
        print('*',end=' ')
    print()
    star+=1
