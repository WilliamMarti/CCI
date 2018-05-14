
#  selection sort, n**2

def selection(list):

    
    for x in range(0, len(list)):
        
        lowest = x

        for y in range(x+1, len(list)):

            if list[y] < list[lowest]:

                lowest = y

        list[x], list[lowest] = list[lowest], list[x]

    return list


def main():

    list = [10, 11, 20, 50, 100, 1, 20, 3, 20]
    print (selection(list))


if __name__ == '__main__':
    
    main()