# print all positive solutions to a^3 + b^3 = c^3 + d^4
# a,b,c,d < 1000


for a in range (1, 1000):

    for b in range (1, 1000):

        for c in range (1, 1000):

            for d in range (1, 1000):

                if a**3 + b**3 == c**3 + d**3:

                    print (str(a) + " " + str(b) +  " " + str(c) + " " + str(d))

                    break
