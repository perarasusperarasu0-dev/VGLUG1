def ispolyndrom():
    num = int(input("ENTER THE NUMBER  :"))
    tem = num
    result = 0

    while(num > 0):
        result = result*10
        result += (num%10)
        num = num//10

    if tem == result:
        return "true"
    else:
        return "false"
    
print(ispolyndrom())