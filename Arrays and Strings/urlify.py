
#  replace all spaces in string with '%20'

def url(s, l):

    s = s.strip()
    s = s.replace(" ", "%20")

    return s


def main():

    test = "aa bbb"
    print (url(test, 6))

    test = "bbb  ccc"
    print (url(test, 8))


if __name__ == '__main__':
    
    main()