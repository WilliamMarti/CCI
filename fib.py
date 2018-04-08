# print fib sequence
# 1 1 2 3 5 8 13

from functools import lru_cache

@lru_cache(maxsize = 1000)
def fib(n):

    if n == 0:

        value = 0
    
    elif n == 1:

        value =  1

    elif n == 2:

        value =  1
    
    elif n > 2:

        value =  fib(n-1) + fib(n-2)

    return value

def main(n):

    print (fib(n))

if __name__ == '__main__':
    
    
    for i in range (1,100):
        main(i)