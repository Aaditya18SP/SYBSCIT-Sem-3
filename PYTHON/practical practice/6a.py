'''
try:
    f=open("D:\\backup\\Aditya\\file2.txt","r+")
    print(f.read())
    f.write(" this is newline1")
    f.close()
    f=open("D:\\backup\\Aditya\\file2.txt","r+")
    print(f.read())
except:
    print("an error occured")
finally:
    f.close()
'''


f=open("D:\\backup\\Aditya\\file2.txt","w+")

f.write(" this is newline2")
f.close()
f=open("D:\\backup\\Aditya\\file2.txt","r+")
print(f.read())

f.close()
'''

f=open("D:\\backup\\Aditya\\file2.txt","a+")
print(f.read())
f.write(" this is newline3")
f.close()
f=open("D:\\backup\\Aditya\\file2.txt","r+")
print(f.read())

f.close()

'''
'''
helllooooo this is my new file
this is line 1 
this is line 2 
this is line 3 
this is line 4 
this is line 5 
'''
