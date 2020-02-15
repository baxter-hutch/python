# Complete the staircase function below.
def staircase(n):
    cor_x = 0
    cor_y = 0 #cor_y = 1: top
    while cor_y < n:
        while cor_x < n:
            if(cor_x < (n - cor_y - 1)):
                print(" ", end='')
            else:
                print("#", end='')
            cor_x+=1
        cor_x = 0
        print('')
        cor_y+=1

if __name__ == '__main__':
    n = 6

    staircase(n)
