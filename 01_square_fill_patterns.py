'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

'''

# pattern using one loop

n = int(input())
for i in range(1,n+1):
    print('* '*n)

# pattern using nested loop

n = int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        print('*',end=' ')
    print()
