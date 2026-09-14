a=input()
x,y,z=a.split(",")
x=int(x)
y=int(y)
z=int(z)
if x>y:
    if x>z:
        greater=x
    else:
        greater=z
    
elif y>x:
    if y>z:
        greater=y
    else:
        greater=z
elif x==y==z:
    greater="none"

print(f"THE LARGEST NUMBER IS:{greater}")
