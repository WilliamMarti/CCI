# small string = s
# bing string = b
# find permuations of s inside b.


def toString(List):
    return ''.join(List)


def permute(listofstring, start, end):




    if start==end:


        print (toString(listofstring))

        print ("______________________")

    else:


        #print ("start: " + str(start))

        for i in range(start,end+1):

           # print ("start")
            #print(listofstring)

            print ("i:" + str(i) + " " + "start: " + str(start)  + " " + "end: " + str(end))

            temp = listofstring[start] # first char
            listofstring[start] = listofstring[i] 
            #print (listofstring[start])
            listofstring[i] = temp
           # print (listofstring[i])
            


            #print ("after")
           # print(listofstring)

            #a[l], a[i] = a[i], a[l]

            permute(listofstring, start+1, end)

            print("Out")

            print ("i:" + str(i) + " " + "start: " + str(start)  + " " + "end: " + str(end))

            #print("Start: " + str(start))

            temp = listofstring[start]
            listofstring[start] = listofstring[i]
            listofstring[i] = temp

            #print ("temp: " + str(temp))


            #a[l], a[i] = a[i], a[l] # backtrack

def findString(s, b):

    lists = list(s)
    listb = list(b)

    print (lists)
    print (listb)

    for letterb in b:

        for lettera in s:

            pass



def main(a, l, r):

    permute(a, l, r)


    #findString(s, b)


if __name__ == '__main__':

    string = "abc"
    listofstring = list(string)
    end = len(string)
    
    permute(listofstring, 0, end-1)