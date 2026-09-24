with open ("practice2.txt","w") as f :
    f.write("1,4,6,8,9,34")



with open ("practice2.txt","r") as f :
    data=f.read()
    num=data.split(",")
    print(num)
    even_num=[int(x) for x in num if int(x) % 2 ==0]
    print(len(even_num))