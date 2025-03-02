class student:
    
    def __init__(self,name, physics, chemistry, bio):
        self.n1 = name
        self.m1 = physics
        self.m2 = chemistry 
        self.m3 = bio
    
    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3
        
s1 = student("rajul", 22,32,45)

print("the name of first student is: ",s1.n1,s1.m1, s1.m2, s1.m3)
print("the average of stud 1 is: ",s1.average())

s2 = student("tia", 45.3,56.2,89.1)
print("the average of", s2.n1,"is: ",s2.average())
        