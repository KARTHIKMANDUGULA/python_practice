m=int(input("marks in maths:"))
s=int(input("marks in science:"))
e=int(input("marks in english:"))
total_marks =m+s+e
average_marks =total_marks /3
percentage = (total_marks /300)*100
if percentage >90:
    grade ="A+"
elif percentage>80 and percentage<=90:
    grade="A"
elif percentage >70 and percentage <=80:
    grade ="B"

print(f"total marks:{total_marks}  \naverage marks:{average_marks} \ngrade:{grade}")