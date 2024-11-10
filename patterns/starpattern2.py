# *
# **
# ***
# ****
# *****

n = int(input("enter"))

for i in range(1,n+1):
    for j in range(1,i+1):
        # print(j,end='')
        print("*",end=' ')
    print('')

for i in range(5):
    for j in range(i+1):
        print("*",end=' ')
    print('')