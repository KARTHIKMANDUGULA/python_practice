class student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.avg=(m1+m2+m3)/3


    def average(self):

        print(f"{self.name} got an avg of {self.avg}")

s1=student("karthik",96,97,98)
s1.average()