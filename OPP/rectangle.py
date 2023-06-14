class Rectangle:
    def __init__(self,x,y,color) -> None:
        self._x = x
        self._y = y
        self._color = color
    def perimeter(self):
        return (self._x+self._y)*2
    def area(self):
        return self._x*self._y
    def color(self):
        return self._color.title()
a = input().split()
r = Rectangle(int(a[0]), int(a[1]), (a[2]))
if int(a[0]) <=0 or int(a[1])<=0:
    print("INVALID")
else:
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))