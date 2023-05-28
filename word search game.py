import time
def find (search):
    
    for i in search:
        i = ""
        x = 0
        y = 3
     
        while i != "t" and x != 3 and y > 0:
            x+=1
            y = y - 1
            i = input ("Enter the letter to find: ")
            print ("You have " + str(y) + " trials left")

        if i == "t":
            return "Found the word"
        else:
            return "Better luck next time"
        
           
help = find ("hello world welcome")
print (help)
time.sleep(3)
