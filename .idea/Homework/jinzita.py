n=int(input("请输入层数："))
for i in range(n):
    print(' ' * (n-i-1) + '*' * (2*i+1) )#算几个空格几个*
for j in range(n):
    print( ' ' * (j+1)+'*' * (2*(n-j-1)-1) )











'''
str=input("请输入层数：")
n=int(str)
for i in range(1,n+1):
    for j in range(i,n+1):
            print(" ")
            for k in range(1,i):
                    print("*")
                    print("\n")

                    '''