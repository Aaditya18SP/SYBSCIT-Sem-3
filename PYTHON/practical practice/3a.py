def pan_chk():
    sen=input("enter a sentence:")
    sen2=sen.lower()
    d=0
    s1="abcdefghijklmnopqrstuvwxyz"
   
    for letter3 in s1:
        if (letter3 in sen2):
            d=d+1
    if(d==len(s1)):
        print("the sentence is pangram")
    else:
        print("the sentence is not pangram")
pan_chk()
    
    
            
