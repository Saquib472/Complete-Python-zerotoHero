# Write a program to find out whether a student is pass or fail, if it requires total 40% and atleast 33% in one of the subjects to pass. Assume 3 subjects and take marks from the user.

sub1 = int(input("Enter first subject's marks: "))
sub2 = int(input("Enter second subject's marks: "))
sub3 = int(input("Enter third subject's marks: "))

if sub1<33 or sub2<33 or sub3<33:
    print("You are fail because you have less then 33% in one off the subjects")
elif (sub1+sub2+sub3)/3 <40:
    print("You are fail due to total percentage is less then 40%")
else:
    print("Congratulations!! You successfully passed the examination!!")
