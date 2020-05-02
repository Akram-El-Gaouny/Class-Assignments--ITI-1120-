# Name: Akram El-Gaouny 
# year 2019

import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    
    stop = True
    while stop:
        try:
            file = input("Please Enter The Name of The File: ").strip()
            opened = open(file)
            return opened
        except FileNotFoundError:
            print("There is no file with that name. Try again.")
            stop=True
        
            
            
            
   

def read_file(fp):
    '''file object->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    final_dict={}
    lines = fp.read().split("\n")
    line_number = 1
    for x in range (len(lines)):
        s_words = lines_to_words(lines[x].lower())
        for x in s_words:
            if x in final_dict:
                final_dict[x].add(line_number)
            else:
                new_set = {line_number}
                final_dict[x]= new_set
        line_number +=1
    return final_dict
    

    
    
def remove_punctuation(string):
    '''
    str -> str
    returns a new string of the same word without any punctuation
    '''
    l = list(string)
    new_string = ""
    
    for x in l:
        if x not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~': ##### contents of string.punctuation
            new_string+=x
    return new_string
    
def lines_to_words(line):
    '''
    str-> set
    Returns a set of the words that exist in the given sentence (str)
    '''
    l=line.split()
    
    for x in range (len(l)):
        l[x] = remove_punctuation(l[x])

    for x in range (len(l)-1,-1,-1):
        if len(l[x]) == 1 or l[x].isalpha()==False:
            l.pop(x)
    return set(l) 
    
def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    l = format_query(query)
    for x in range (len(l)):
        if x==0:
            co_existed = D[l[x]]
        else:
            co_existed = co_existed.intersection(D[l[x]])
    
    lst = list(co_existed)
    lst.sort()
    return lst

def format_query(query):
    '''
    (str) -> list
    The following function return a formatted list of the user input ( it removes punctuatuon in the user input)
    '''
    l = query.split()
    for x in range(len(l)):
        l[x]= remove_punctuation(l[x])

    for x in range(len(l)-1,-1,-1):
        if len(l[x])==0:
            l.pop(x)
            
    return l

    
def all_found(d, query):
    '''
    (dict, list) -> bool
    The function return True if all the words in list query esist in dictionary and false otherwise
    '''
    if len(query)==0 or "" in query:
        print("The word \"\" is not in the dictionary")
        return False
    
    for x in range (len(query)):
        if query[x] not in d:
            print("The word " +"\'"+ query[x] +"\'"+ " is not in the file")
            return False
    return True
    
    

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
# YOUR CODE GOES HERE

while query!='q':
    lq = format_query(query)
    found = all_found(d,lq)
    if found == True:
        if len(find_coexistance(d,query))==0:
            print( "The one or more words you entered does not coexist in a same line of the file.")
        else:
            print("The one or more words you entered co-existed In The Following Lines of The file:")
            print(remove_punctuation(str(find_coexistance(d,query))))
        found == False
        query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
        
    else:
        query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    lq = format_query(query)
        
    
    
    
    

