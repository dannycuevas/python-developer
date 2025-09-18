# Exercise 1: For loops

# Think back to the previous exercise of creating a program to classify students' grades.

# Recall that the classification is as follows:

#     It will print 'A' if the mark is between 8..10 (inclusive).

#     It will print 'B'  if the mark is between 5..7 (inclusive).

#     It will print 'C' if the mark is between 4..6 (inclusive).

#     It will print 'F' if the mark is between 1..3 (inclusive).

#     It will print 'Wrong input' if anything else is provided.

# The problem you need to solve

# The teacher wants you to extend this program now to allow them to read all the numbers of the class and print the mean of the class as well. So your program should print the grade for each student, but it should use a loop to do this for 10 students and also print the mean of the class at the end.

#     Assume there are 10 students in the class.

#     At the end, the program should also print the mean of the class. The mean is the total marks of the class divided by the number of students. That is, if the total of all marks from all the students is 75 and there are 10 students, the mean will be 7.5 (75 divided by 10). 

total = 0

for i in range(1, 11):
    mark = float(input(f'Please provide the mark of student {i}: '))

    total += mark

    if mark >= 8 and mark <= 10:
        print(f'Student {i} grade: A')
    elif mark >= 5 and mark <= 7:
        print(f'Student {i} grade: B')
    elif mark >= 4 and mark <= 6:
        print(f'Student {i} grade: C')
    elif mark >= 1 and mark <= 3:
        print(f'Student {i} grade: F')

mean = total / 10
print(f'The mean of the class is {mean}')
