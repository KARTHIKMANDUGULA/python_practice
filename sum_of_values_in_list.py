input_list=input("give numbers to add:").split(",")
new_list=sum([int(x) for x in input_list])
print("SUM OF ELEMENTS:",new_list)