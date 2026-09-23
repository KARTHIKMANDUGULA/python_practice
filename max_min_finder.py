input_list=input("GIVE NUMBERS TO FIND MAX AND MIN:").split(",")
new_list=[int(x) for x in input_list]
new_list.sort()
print("max:",new_list[-1],"MIN:",new_list[0])