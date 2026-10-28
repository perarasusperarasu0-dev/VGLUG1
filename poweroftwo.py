def powerof_two():
    n = int(input("ENTER THE NUMBER  :"))

    if n<=0:
        return "False"
    
    while(n>1):
        if n%2 !=0:
           return "false"
        n = n//2
    return "true"


print(powerof_two())
        
   