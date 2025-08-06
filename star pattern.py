def block1():
 for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=' ')
    print()
#'this program is to print the stars in reverse order
'''
* * * * *
* * * *
* * *
* *
*
'''
def block2():
 for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''
output
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
def block3():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print("*", end=' ')
        print()
'''
output
* 
* * 
* * * 
* * * * 
* * * * *
'''
if __name__ == "__main__":
    block3()
    block2()
    block1()