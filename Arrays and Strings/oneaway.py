# pale, ple -> True

def oneAway(a, b):

    # check if strings are equal or 1 letter away

    lendiff = len(a) - len(b)

    alen = len(a)
    blen = len(b)

    # if the words are more than 1 character length apart False
    if lendiff < -1 or lendiff > 1:

        return False

    equalcount = 0

    # if the words are equal length
    if alen == blen:


        for x in range(0, alen):

            if a[x] == b[x]:

                equalcount += 1
        
        if abs(equalcount - alen) == 1:

            return True

    # if the words are different length
    else:      

        if alen > blen:    

            return checkLetters(b, a)

        else:

            return checkLetters(a, b)

def checkLetters(little, big):

    equalcount = 0

    for x in little:

        if x in big:

            equalcount += 1

    if equalcount == len(little):

        return True

    else:

        return False

def main():

    test1 = "pale"
    test2 = "ple"
    print (oneAway(test1, test2))

    test1 = "pales"
    test2 = "pale"
    print (oneAway(test1, test2))

    test1 = "pale"
    test2 = "bale"
    print (oneAway(test1, test2))

    test1 = "aa"
    test2 = "bbbbbale"
    print (oneAway(test1, test2))

if __name__ == '__main__':
    
    main()