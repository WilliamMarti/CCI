# does a given string have all unique characters?

def isUnique(s):


    # assuming ascii charaters
    # if there are more than 256 chars, there must be repeats
    if len(s) > 256:

        return False

    output = True

    checkedletters = {}

    for letter in s:

        if letter in checkedletters:

            output = False
            break

        else:

            checkedletters[letter] = 1


    return output

def main():

    test = "test"
    print (isUnique(test))

    test = "abc"
    print (isUnique(test))


    test = "atta"
    print (isUnique(test))

if __name__ == '__main__':
    
    main()