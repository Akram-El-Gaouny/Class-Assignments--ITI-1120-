# Name: Akram El-Gaouny 
# year 2019


class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:
    'Class Rectangle represents a rectangle in a plane'
    def __init__(self, point1, point2, color):
        '''
        (Rectangle, point,point, str) -> None
        Initilizes the bottom right and top left points of the rectangle and initillizes the color and intillizes the width and length of the rectangle
        '''
        self.point1 = point1
        self.point2 = point2
        self.color = color.lower()
        self.lenx =abs(self.point2.x - self.point1.x)
        self.leny=abs(self.point2.y - self.point1.y)

    def __repr__(self):
        '''
        (Rectangle)->  str
        Returns a representation of object Rectangle Rectangle(Point(x,y), Point(x,y), 'color')
        '''
        return "Rectangle(" + str(self.point1) + "," + str(self.point2) + ",'" + self.color+ "')"

    def __str__(self):
        '''
        (Rectangle)-> str
        Return a user-friendly representation of an object rectangle stating bottom-left, top-right, and color features
        '''
        return "I am a " + self.color + " rectangle with bottom left corner at("+ str(self.point1.x)+"," +str(self.point1.y) + ") and top right corner at (" + str(self.point2.x)+"," +str(self.point2.y) + ")."
    def get_bottom_left(self):
        '''
        (Rectangle)-> Point
        Return the bottom left coordinate of the rectangle
        '''
        return self.point1
    
    def get_top_right(self):
        '''
        (Rectangle)-> Point
        Return the top right coordinate of the rectangle
        '''
        return self.point2
        
    def get_color(self):
        '''
        (Rectangle)-> str
        Return the color of the rectangle
        '''
        return self.color
    def reset_color(self, color):
        '''
        (Rectangle, str)-> None
        Return the color of the rectangle
        '''
        self.color = color.lower()
    def get_perimeter(self):
        '''
        (Rectangle)-> number
        Return the peremiter of the Rectangle
        '''
        return 2*self.lenx + 2*self.leny
    def get_area(self):
        '''
        (Rectangle)-> number
        Return the area of the rectangle
        '''
        return self.lenx*self.leny
    def move(self,dx,dy):
        '''
        (Rectangle, number,number) -> None
        Moves the rectangle by moving the bottom-left and top-right coordinates
        '''
        self.point1.move(dx,dy)
        self.point2.move(dx,dy)
    def __eq__(self, other):
        '''
        (Rectangle,Rectangle) -> bool
        Return True if both objects have the same bottom-left, top-right coordinates and same color
        '''
        return self.point1 == other.point1 and self.point2 == other.point2 and self.color == other.color
    def intersects(self, other):
        '''
        (Rectangle,Rectangle) -> bool
        Return True if the two objects of type rectangle intersect one another and False otherwise
        '''
        if self.point1.x<=other.point1.x:
            condition_x = self.point1.x <= other.point1.x <= self.point2.x 
            condition_y = self.point1.y <= other.point1.y <= self.point2.y or (other.point1.y<=self.point1.y and other.point2.y>=self.point2.y)
            return condition_x and condition_y
            
        else:
            condition_x = other.point1.x <= self.point1.x <= other.point2.x 
            condition_y = other.point1.y <= self.point1.y <= other.point2.y or (other.point1.y>=self.point1.y and other.point2.y<=self.point2.y)
            return condition_x and condition_y
        
    def contains(self, x, y):
        '''
        (Rectangle,number,number) -> bool
        Return True the coordinate (x,y) is in the object rectangle
        '''
        return self.point1.x<=x<=self.point2.x and self.point1.y<=y<=self.point2.y
    

class Canvas:
    ' Class Canvas represent a collection of rectamgles in a plane'
    def __init__(self):
        '''
        (Canvas) -> None
        Initilizes a list to contain the collection of rectangles in the canvas
        '''
        self.l = [] #### THE FOLLOWING LIST WILL HOLD RECTANGLE OBJECTS
    def __repr__(self):
        '''
        (Canvas) ->  str
        Returns a representation of the canvas in the form Canvas([list])
        '''
        return "Canvas(" + str(self.l)+" )"
   
    def add_one_rectangle(self, rectangle):
        '''
        (Canvas, Rectangle) ->  None
        Adds an Object Rectangle to the canvas - appends it to the list.
        '''
        self.l.append(rectangle)
    def count_same_color(self, color):
        '''
        (Canvas, str) ->  int
        Counts the number of rectangle that have the same color as the string color
        '''
        
        counter =0
        for x in range (len(self.l)):
            if self.l[x].get_color() == color:
                counter+=1
        return counter

    def __len__(self):
        '''
        (Canvas) ->  int
        Returns the number of rectangles that exist in the passed canvas
        '''
        return len(self.l)
    
    def total_perimeter(self):
        '''
        (Canvas) ->  number
        Returns the total perimeter of all rectangles that exist in the passed canvas
        '''
        total = 0
        for x in range (len(self.l)):
            total +=self.l[x].get_perimeter()
        return total
    def min_enclosing_rectangle(self):
        '''
        (Canvas) ->  Rectangle
        Returns a rectangle that can enclose the entire collection of rectangles
        Precondition: Canvas is not empty
        '''
        
        
        minx = self.l[0].get_bottom_left().x
        miny = self.l[0].get_bottom_left().y
        maxx =self.l[0].get_top_right().x
        maxy =self.l[0].get_top_right().x

        
        for x in range (len(self.l)):
            if self.l[x].get_top_right().x>maxx:
                maxx = self.l[x].get_top_right().x
            if self.l[x].get_top_right().y>maxy:
                maxy = self.l[x].get_top_right().y
            if self.l[x].get_bottom_left().x<minx:
                minx = self.l[x].get_bottom_left().x
            if self.l[x].get_bottom_left().y < miny:
                miny = self.l[x].get_bottom_left().y
        return Rectangle(Point(minx,miny), Point(maxx,maxy), "red")
            
            
                
    def common_point(self):
        '''
        (Canvas) ->  bool
        Returns true if there exists a point between all rectangles - in other words if all rectangles intersect each other- and false otherwise
        Precondition: Canvas is not empty
        '''
        for x in range (len(self.l)):
            for y in range (len(self.l)):
                
                if self.l[x].intersects(self.l[y])==False:
                    return False
        return True
        
                    
        
    
