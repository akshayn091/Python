f = open('number.txt','w')
while True:
    a = input("Enter a number=")
    a = str(a)
    print(a)
    m = a.isdigit()
    if m == False :
        print( ' Error in number')
        continue
    else:
        
        
        f.write(a + "\n")
        
        
        Ans=input('Press Yes to continue and No to stop=')
        if Ans == 'No':
            break
        else:
            continue
f.close()
        
        
    
    
