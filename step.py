def step_of_zero():
    number = int(input("ENTER THE NUMBER  :"))
    step_cunt = 0
    while(number > 0):
        if number%2 == 0:
           number= number//2
        else:
           number= number-1

        step_cunt +=1

    return step_cunt

print(step_of_zero())









