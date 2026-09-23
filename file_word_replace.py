with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing java.\nI like programming in java.")



with open ("practice.txt","r") as f:
    data=f.read()

new_data=data.replace("java","python")

with open ("practice.txt","w") as f:
    f.write(new_data)