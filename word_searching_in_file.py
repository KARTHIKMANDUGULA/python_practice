word=input("give a word to find in the file:")
with open("practice.txt","r") as f:
    new_data_2 = f.read()
    if word in new_data_2:
        print("found")
    else:
        print("not found")


def finding_line():
    word="learning"
    with open ("practice.txt","r") as f:
        line_no=1
        new_data_3 = True
        while new_data_3:
            new_data_3=f.readline()
            if word in new_data_3:
                return line_no
            line_no+=1
    return -1

print(finding_line())