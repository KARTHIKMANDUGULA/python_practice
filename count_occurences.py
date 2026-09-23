values=input("give values to count of a number:").split(",")
x=int(input("give the number you want to count:"))
new_list=[int(y) for y in values]
print("count:",new_list.count(x))