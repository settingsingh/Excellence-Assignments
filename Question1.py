'''
Question1
Use python lists and make an list of numbers.
Write a function which returns sum of the list of numbers
'''

# Function to find the max from the list


def findMax(l):
    max = -1
    for i in l:
        if i > max:
            max = i
    return max


# Main Program
l = []
numOfElements = int(input())
for i in range(numOfElements):
    l.append(int(input()))

print(findMax(l))
