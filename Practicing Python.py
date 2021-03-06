# Name: Akram El-Gaouny 
# year 2019

import math
import turtle


 ###################################################################
 # Question 1
 ################################################################### 

def pythagorean_pair(a,b):
    '''
    (int, int) -> (boolean)
    Checks whether the two sides of the triangle a,b form a phythogorean pair"
    '''

    total = a**2 + b**2
    c = round(math.sqrt(total))
    Check = ((c**2)== total)
    return Check

 ##################################################################
 # Question 2
 ################################################################### 

def mh2kh(s):
    '''
    (float) -> (float)
    Returns the given speed -m/h- s in -km/h
    preconditions: Inputs must be non-negative integers
    '''
    Skmh = s*(1.60934)
    return (Skmh)

 ###################################################################
 # Question 3
 ###################################################################

def in_out(xs,ys,side):
    '''
    (float,float,float) -> (boolean)
    Returns true or false whether the input point that the user inputs is within the square defined by the coordinates of the bottom-left corner (xs,ys)as well as the length of one of the sides, side.
    Precondition: side is a non-negative number
    '''
    xf_position = xs+side
    yf_position = ys + side
    x_input = float(input("Enter a number for the x coordinate of a query point: "))
    y_input = float(input("Enter a number for the y coordinate of a query point: "))
    
    confirmx = ( x_input>= xs and x_input<= xf_position)
    confirmy = ( y_input>= ys and y_input<= yf_position)
    final = (confirmx==True and confirmy==True)
    print (final)

 

 ###################################################################
 # Question 4
 ###################################################################

def safe(n):
    '''
    (int) -> (boolean)
    Checks if the input number is a safe number (does not contain 9 or is divisible by 9)
    Preconditions: The input integer has to be 2 digits
    '''
    Div9 = n%9
    content9 = "9" in str(n)
    safe_number_checker = not(Div9==0 or content9 ==True)
    return safe_number_checker

 ###################################################################
 # Question 5
 ###################################################################

def quote_maker(quote, name, year):

    '''
    (str, str,str) -> (str)
    Integerates the quote given the quote, name, and the year date
    Preconditions: The parameters are logical components of a properly formated quote
    '''
    sp = " "
    final_str = "In" + sp + str(year) +", a person called" +sp + name + sp + "said:" + "\"" + quote + "\""
    return final_str

 ###################################################################
 # Question 6
 ###################################################################

def quote_displayer():
    '''
    () -> (str)
    Integerates the quote given the quote, name, and the year date
    Preconditions: The parameters are logical components of a properly formated quote
    '''
    quote = input ("Give me a quote: ")
    name = input ("Who said that? ")
    year = input ("What year did he/she say that? ")
    final_str = quote_maker(quote, name, year)
    print(final_str)               
 ###################################################################
 # Question 7
 ###################################################################


def rps_winner():
    '''
    ()-> Nonetype
    Asks two user for a choice between "rock, paper, scissors" and determines the winner based on the input of both users
    preconditions: the input must be all written in lowercase 
    '''
   
    player1_input = input("what choice did player 1 make?\nType one of the following options: rock, paper, scissors: ")
    player2_input = input("what choice did player 2 make?\nType one of the following options: rock, paper, scissors: ")
    player1_win = (player1_input=="rock" and player2_input=="scissors") or (player1_input=="paper" and player2_input=="rock") or (player1_input=="scissors" and player2_input=="paper")
    tie_check = "not " + str((player1_input != player2_input))
    print("Player 1 wins. That is" ,player1_win)
    print("It is a tie. That is" ,tie_check)



 ###################################################################
 # Question 8
 ###################################################################
def fun(x):
    '''
    (float)-> (float)
    Returns a y-value to the equation 10^(4y) = x+3
    Preconditions: The input x must be a positive integer
    '''
    
    y = (math.log((x+3),10))/4
    return y

 ###################################################################
 # Question 9
 ###################################################################

def ascii_name_plaque(name):

    '''
    (str) -> Nonetype
    Creates a name plaque with the string input of the user
    '''
    name= "*"+ " " + "_" + name+ "_" + " "+"*"
    beg_end = "*"* len(name)
    spacing = "\n*" + (" "*(len(beg_end)-2))+"*"
    print (beg_end+ spacing + "\n" + name + spacing + "\n"+beg_end)

 ###################################################################
 # Question 10
 ###################################################################

def draw_train():
    '''
    ()->(Nonetype)
    This function draws a train using turtle graphics
    '''

    frame = turtle.Screen()
    train = turtle.Turtle()
    train.begin_fill()
    train.color("black", "yellow")
    train.penup()
    train.goto(-5, 30)
    train.pendown()
    train.circle(10)
    train.penup()
    train.end_fill()
    train.begin_fill()
    train.color("black", "green")
    train.goto(0,0)
    train.pendown()
    train.forward(100)
    train.left(90)
    train.forward(50)
    train.left(90)
    train.forward(100)
    train.left(90)
    train.forward(50)
    train.end_fill()
    train.goto(100,0)
    train.begin_fill()
    train.color("black", "green")
    train.left(90)
    train.forward(75)
    train.left(90)
    train.forward(150)
    train.right(90)
    train.forward(5)
    train.left(90)
    train.forward(10)
    train.left(90)
    train.forward(85)
    train.left(90)
    train.forward(10)
    train.left(90)
    train.forward(5)
    train.right(90)
    train.forward(150)
    train.penup()
    train.end_fill()
    train.goto(160,140)
    train.begin_fill()
    train.color("black", "blue")
    train.pendown()
    train.forward(25)
    train.right(90)
    train.forward(40)
    train.right(90)
    train.forward(25)
    train.right(90)
    train.forward(40)
    train.end_fill()
    train.penup()
    train.goto(0,0)
    train.begin_fill()
    train.color("black", "grey")
    train.pendown()
    train.right(90)
    train.forward(10)
    train.right(90)
    train.forward(40)
    train.right(145)
    train.forward(55)
    train.right(35)
    train.end_fill()
    train.begin_fill()
    train.color("black", "black")
    train.penup()
    train.goto(40,-20)
    train.pendown()
    train.circle(15)
    train.end_fill()
    train.penup()
    train.goto(70,-20)
    train.begin_fill()
    train.color("black", "black")
    train.pendown()
    train.circle(15)
    train.end_fill()
    train.penup()
    train.goto(40,-5)
    train.begin_fill()
    train.color("black", "grey")
    train.pendown()
    train.forward(30)
    train.left(90)
    train.forward(2)
    train.left(90)
    train.forward(30)
    train.left(90)
    train.forward(2)
    train.penup()
    train.end_fill()
    train.goto(10,98)
    train.begin_fill()
    train.color("black", "red")
    train.pendown()
    train.forward(50)
    train.left(90)
    train.forward(20)
    train.left(90)
    train.forward(50)
    train.right(20)
    train.forward(20)
    train.left(110)
    train.forward(40)
    train.left(120)
    train.forward(30)
    train.end_fill()
    train.penup()
    train.goto(120, -10)
    train.begin_fill()
    train.color("black", "black")
    train.pendown()
    train.circle(25)
    train.end_fill()
    frame.exitonclick()
    
    
    

 ###################################################################
 # Question 11
 ###################################################################

def alogical(n):
    '''
    (float) -> (int)
    Returns the number of times that the input n needs to be divided by 2 to get a value that is equal or less than 1
    preconditions: The input n must be greater or equal to 1
    '''

    x= math.log(n,2)
    x = math.ceil(x)
    return x

 ###################################################################
 # Question 12
 ###################################################################

def time_format(h,m):
    '''
    (int,int) -> (str)
    Returns a string telling the user the time based on the hour h input and minutes m input
    Preconditions: inputs must be positive integers, h must be a value between and including 0 and 24, m input must be a value between 0 and 60
    '''
    m = 5* round(m/5)

    if m ==60:
        m=0
        h=h+1

    if h==24:
        h=0
    if (m==0):
        str_final =  str(h) + " " + "o'clock"

    elif (m<30):
        str_final = str(m) + " " + "minutes past" + " " + str(h) + " " + "o'clock"
    elif (m>30):
        h= h+1
        if h==24:
            h=0
        str_final = str (60-m) +" " + "minutes to" + " " + str(h) + " " + "o'clock"
    elif (m==30):
        str_final = "half past" + " " + str(h) + " " + "o'clock"
        

    return str_final

     

 ###################################################################
 # Question 13
 ###################################################################
 
def cad_cashier(price, payment):
    '''
    (float,float)-> (float)
    Given two inputs, price and payment, this functions returns the amount of change owed back after rounding each number to the nearest 0.05 or 0 cents
    Predconditions: inputs price and payment must be positive, Payment must be greater or equal to price
    '''
    price = 0.05 * round(price/0.05)
    payment = 0.05 * round(payment/0.05)
    money_to_return = round((payment - price),2)
    return money_to_return
 ###################################################################
 # Question 14
 ###################################################################

def min_CAD_coins(price, payment):
    '''
    (float,float) -> (int,int,int,int)
    Given the two inputs price and payment this function will return the minimum number of coins required to provide change
    Predconditions: inputs price and payment must be positive, Payment must be greater or equal to price
    '''
    change = int(100*cad_cashier(price,payment)) +1
    t = change//200
    change = change - (t*200) 
    l = change // 100
    change = change - (l*100)
    q = change // 25
    change = change - (q*25)
    d = change//10
    change = change - (d*10)
    n = change//5
    return(t,l,q,d,n)

##################################################
###############Part 2 - Question 1################
##################################################


def min_enclosing_rectangle(radius, x, y):
    '''
    (float,float,float) -> (float,float) or (None)
    This function provides The coordinates of the bottom left corner of a rectangle that encloses a circle with a centre coordinate of (x,y) and a given radius
    '''
    if radius < 0:
        return None
    else:
        X = x-radius
        Y= y - radius
        return (X,Y)

##################################################
###############Part 2 - Question 2################
##################################################
def series_sum():
    '''
    ()-> (float) or (None)
    finds the sum of series starting with a 1000 and increases by increments of (1/n^2) where n is a number that ranges between 1 and the input digit
    '''
    n = int(input("Please Enter a non-negative integer: "))
    if (n<0):
        return None
    else:
        sum_of_series = 1000

        for x in range (1,n):
            sum_of_series = sum_of_series + (1/(x)**2)
        return sum_of_series
##################################################
###############Part 2 - Question 3################
##################################################

def pell(n):
    '''
    (int)-> (int) or (None)
    This function return the nth - given through paramater n- pell number
    '''
    if (n<0):
        return None
    elif(n==0):
        return 0
    elif (n==1):
        return 1
    else:
        n_added = 0
        n_squared =1
        value=2
        for x in range(1,n):
            value = (n_squared)*2 + n_added
            n_added = n_squared
            n_squared = value
        return value
##################################################
###############Part 2 - Question 4################
##################################################
def countMembers(s):
    '''
    (str) -> (int)
    This function takes a string input and returns the number of ocuurences of the character in 'efghijFIJKLMNOPQRSTUVWX23456!,\\' in the given string parametr (s)
    '''
    counter = 0
    for x in s:
        if  x in 'efghijFIJKLMNOPQRSTUVWX23456!,\\':
            counter+=1

    return counter

##################################################
###############Part 2 - Question 5################
##################################################

def casual_number(s):
    '''
    (str)-> (int) or (None)
    The function takes a string and picks out the numbers in a sequence that mathematically represent an actual value 
    '''
    number=''
    counter_neg=0
    counter_str=0
    for x in s:

        if x.lower() in 'abcdefghijklmnopqrstuv':
            counter_str+=1
        elif x in "-":
            counter_neg+=1
            number = number + x
        elif x in "1234567890-":
            number = number + x
       
                 

    if (counter_neg>=2)or number==''or number=="-" or counter_str>0 :
        return None
    else:
        return int(number)
##################################################
###############Part 2 - Question 6################
##################################################
def alienNumbers(s):
    '''
    (str)-> (int)
     Calculates the sum of a string given values to specific characters
    '''
    
    sumT = (s.count('T')*1024)+ (s.count('y')*598)+ (s.count('!')*121)+ (s.count('a')*42)+(s.count('N')*6) +s.count('U')       
    return sumT


##################################################
###############Part 2 - Question 7################
##################################################
def alienNumbersAgain(s):
    '''
    (str)-> (int)
     Calculates the sum of a string given values to specific characters
    '''

    sumT =0
    for x in s:
        
        if x =="T":
            sumT= sumT + 1024
        elif x=="y":
            sumT= sumT + 598
        elif x=="!":
            sumT= sumT + 121
        elif x == "a":
            sumT= sumT + 42
        elif x=="N":
            sumT= sumT + 6
        elif x=="U":
            sumT= sumT + 1
    return sumT
    
##################################################
###############Part 2 - Question 8################
##################################################
def encrypt(s):
    '''
    (str) -> (str)
    The function encrypts the given string s and returns a new encrypted string. It reverses it and changes positions of characters.
    '''
    n_s = s[::-1]
    loop_var =0
    extra_letter=''
    if (len(n_s)%2==1):
        loop_var = int((len(n_s)-1)/2)
        extra_letter = n_s[-loop_var-1]
    else:
        loop_var = int(len(n_s)/2)
    
    
    encrypted_s =''

    for x in range(1,loop_var+1):
        encrypted_s =  encrypted_s + n_s[x-1] + n_s[-x]
    encrypted_s= encrypted_s + extra_letter
    return encrypted_s

##################################################
###############Part 2 - Question 9################
##################################################
def oPify(s):
    '''
    (str)->(str)
    This function place the sub string op alphabatic characters. the string op is formatted based on the capitalization of the preceding and following alphabatic character
    '''

    output =''
    if len(s) == 1:
        return s
    for x in range (0,len(s)):
        output= output+s[x]
        if s[x] not in "0123456789" and x<len(s)-1 and s[x+1] not in '0123456789':


            if(s[x].isupper() and s[x+1].isupper()):
                output = output+ "op".upper()
            elif(s[x+1].islower() and s[x].islower()):
                output = output+ "op".lower()
            elif(s[x].islower() and s[x+1].isupper()):
                output = output+ "oP"
            elif(s[x+1].islower() and s[x].isupper()):
                output = output+ "Op"
            
                
    return output

##################################################
###############Part 2 - Question 10###############
##################################################
def nonrepetitive(s):
    '''
    (str) -> (bool)
    This fundtion takes a string input (s) and returns True if the string is nonrepertive or false otherwise
    
    '''
    word =''
    for x in range (math.floor(len(s)/2),0,-1):
        for y in range (0, len(s)):
            if (word=='' and len(s)+1>(2*x)+y and s[y:x+y] == s[x+y:2*x+y]):
                word = s[y:x+y]
    return word == ''
    
                
                
            
           
            
            
   

    
