student=[] #Creating an empty list
n=int(input ("Enter the no of students:"))  #Taking n number of input from user
for _ in range(n):#Taking input
    name=input("Enter the student name:")
    grade=float(input("Enter the student grade:"))
    student.append([name,grade])
unique_grade=sorted(set([score for name,score in student])) #Identifying unique values by removing the duplicate one and ordering in ascending order
second_unique_grade=unique_grade[1]

name_1 = sorted (set ([name for name,score in student if score==second_unique_grade]))

print(name_1)