# test if given strings permutation can be a palidrome

# return list of permutations of a given string
def returnpermutations(s, start):

    slist = list(s)
    swap = start + 1

    print (start)

    if start == len(s):

        return

    '''
    temp = slist[start]
    slist[start] = slist[swap]
    slist[swap] = temp
    '''

    newstring = ''.join(slist)

    for x in range(0, len(s)-1):

        swap = x + 1

        temp = slist[x]
        slist[x] = slist[swap]
        slist[swap] = temp
    
        newstring = ''.join(slist)

        print (newstring)

    '''
    if newstring == s:

        return
    '''

    returnpermutations(newstring, start+1)


        

def returnpalidrome(s):

    pass


def main(test):



    returnpermutations(test, 0)


if __name__ == '__main__':
    
    test = "abc"
    main(test)