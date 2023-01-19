#Question 2
class Triangle():
    def __init__(self):
        pass
    def validate_triangle(self,l):

        #number of sides must be 3
        if len(l)!=3:
            return 'Invalid Triangle'
        #sum of first 2 sides of the triangle must be greater than the 3rd side
        self.p=True
        for i in l:
            if sum(l)-i>i:
                self.p=True
            else :
                self.p=False
                break
        if self.p==False:
            return 'Invalid Triangle'
        else:
            return "Valid Triangle"
class Rectangle():
    def __init__(self):
        pass
    def validate_rectangle(self,l):
        #number of sides must be 4
        if len(l)!=4:
            return 'Invalid Rectangle'

        #inputs should be in correct order i.e, (l,b,l,b)
        if  l[0]==l[2] and l[1]==l[3]:
            return "Valid Rectangle"         
        else:
            return "Invalid Rectangle"

tri_sides=list(map(int,input("Enter the sides of Triangle : ").split()))
obj1=Triangle()       
print(obj1.validate_triangle(tri_sides))
rect_sides=list(map(int,input("Enter the sides of Rectangle in the correct order : ").split()))
obj2=Rectangle()
print(obj2.validate_rectangle(rect_sides))