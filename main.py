class Geometry:

    def displayRectangle(self,l,b):
        print("perimeter of rectangle is:"+str(2*(l+b)))
        print("area of rectangle is:"+str(l*b))
    def displayCircle(self,r):
        print("perimeter of a circle is:"+str(2*3.14*r))
        print("area of circle is:"+str(3.14*r*r))
    def displayTriangle(self,a,h):
        print("perimeter of triangle is :"+str(3*a))
        print("area of triangle is "+str((1/2)*a*h))
obj=Geometry()
ch=int(input("enter input:"))
if(ch==1):
    obj.displayTriangle(1,3)
elif(ch==2):
    obj.displayCircle(4)
elif (ch==3):
    obj.displayRectangle(3,4)


