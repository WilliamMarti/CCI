
#  binary search
# return position in list

def binarysearch(list, search, low, high):

    if (low > high):
        return -1

    #print (list)

    #print (str(low) + " " + str(high))

    middle = int((low + high) / 2)

    #print (middle)
    #print (list[middle])

    if (list[middle] < search):

        return binarysearch(list, search, middle + 1, high)

    elif (list[middle] > search):

        return binarysearch(list, search, low, middle - 1)

    else:

        return middle
    


def main():

    list = [1, 2, 5, 20, 30, 32, 45, 99, 300]
    print (binarysearch(list, 32, 0, len(list)))

    print (binarysearch(list, 2, 0, len(list)))

    print (binarysearch(list, 99, 0, len(list)))

if __name__ == '__main__':
    
    main()