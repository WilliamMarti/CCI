
#  bubble sort, n**2

def bubble(list):

    for x in range(0, len(list)):

        for y in range(0, len(list)):

            try:

                if list[x] < list[y]:

                    list[x], list[y] = list[y], list[x]

            except IndexError:

                continue

    return list


def main():

    list = [10, 11, 20, 50, 100, 1, 20, 3, 20]
    print (bubble(list))


if __name__ == '__main__':
    
    main()