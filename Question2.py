'''
Question2 
Setup a dict structure like this in python
Dict1: (this is a key, value pair of user id and username)
{
   “1” : “name1”,
   “2” : “name2”,
   “3” : “name3”
} etc.. 
Dict2: (this is a key value pair of user id and exam score) 
{
   “1” : 50,
   “2” : 60
   “3” : 70
}
These are just sample data assume there are hundreds of users 

Write a function in python, which will return maximum i.e function should return dictionary like
{
  “3” : 70
}
'''
# function to find out the maximum


def findMax(students):
    maxMarks = -1
    objKey = -1
    for key, value in students.items():
        if value > maxMarks:
            maxMarks = value
            objKey = key
    return {objKey: students[objKey]}


# Main program
numOfElements = int(input("Enter the number of elements: "))
students = {}
for i in range(numOfElements):
    k = input("Enter key: ")
    v = int(input("ENter the marks: "))
    students.update({k: v})

print(findMax(students))
