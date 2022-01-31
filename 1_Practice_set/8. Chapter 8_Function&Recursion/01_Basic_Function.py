# Find the percentage of marks 
def percentage(marks):
    total_marks = 0
    for i in range(len(marks)):
        total_marks = marks[i] + total_marks
    _percentage = ((total_marks/len(marks))/100)*100
    return _percentage

marks = []
total_sub = int(input("Enter total number of subjects: "))
for i in range(total_sub):
    subm = int(input(f"enter the {i+1}st subject's marks: "))
    marks.append(subm)
result = percentage(marks)
print(f"Your percentage of marks is: {result}%")