'''
Assume we have list like this
[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
Basically a list of zero’s and one’s.
Write a python function to the number of maximum consecutive  one’s present in the array. 
E.g output for the above array would be 4
'''


def maxConOnes(l):
    ones = maxOnes = 0
    for i in range(len(l)):
        if(int(l[i]) == 0):
            ones = 0
        else:
            ones = ones + 1
            if(ones > maxOnes):
                maxOnes = ones
    return maxOnes


# Main Program
l = input().split()
print(maxConOnes(l))
