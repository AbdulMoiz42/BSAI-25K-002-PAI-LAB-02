# # 1. A university maintains student names and their marks in different subjects. You need to develop a program that
# can store the data, calculate each student’s average, identify the highest-performing student, and generate a list of
# students who achieved an average above a specified threshold. Requirement: The solution should handle multiple
# students and multiple subjects efficiently.

no_of_students=int(input("Enter number of students:"))
info={}
high_achievers = {}

highest_average = 0.0
highest_achiever = ""

threshold = float(input("Enter the average threshold: "))

for i in range(1,no_of_students+1):
    name=input("Enter your name:")
    no_of_subjects=int(input("Entyer no. of subjects:"))
    marks=[]
    avg=0
    for f in range(1,no_of_subjects+1):
        
        mark=int(input(f"Enter number of subject {f}:"))
        marks.append(mark)
    
    total=sum(marks)    
    
    average=total/no_of_subjects
    if average > highest_average:
        highest_average = average
        highest_achiever = name

   
    if average > threshold:
        high_achievers[name] = average

    info[name]={"marks":marks,"average":average}




print("\nStudent Information:")
print(info)

print("\nHighest Performing Student:")
print(highest_achiever)
print("Average:", highest_average)

print("\nHigh Achievers:")
print(high_achievers)
        