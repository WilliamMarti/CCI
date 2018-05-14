
#  compress strings
# aaaabbbcccc = a4b3c4

def compress(s):

    count = 1

    for x in range(0, len(s)):

        # first letter is a starting point
        if x == 0:

            newstring = s[x]
        
        else:

            if s[x] == s[x-1]:

                count += 1
            
            else:

                newstring += str(count)
                count = 1
                newstring += str(s[x])

    newstring += str(count)


    if len(newstring) == len(s):

        return s

    return newstring


def main():

    if compress("aabbcc") == "aabbcc":
        print (True)
    else:
        print (False)

    if compress("aaaaabbbccc") == "a5b3c3":
        print (True)
    else:
        print (False)


    if compress("aabcccccaaa") == "a2b1c5a3":
        print (True)
    else:
        print (False)

if __name__ == '__main__':
    
    main()