import random
def creadit(number,number2): # this a the number depending on what you will choose
    '''
    this program will ask you an input and you will pay  100 or 500 if you pay 500 it will give you a 15 digit number or if you pay 100 it will giv you a 10 digit number 
    '''
    a = int(input("pls pay the amout:"))
    if a == 100:
        return random.randint(0,1000000000000) #<- this will give you a 10 digit number
        print("that is FOR YOUR CREADIT CARD FOR 100 KSH")
    elif a == 500:
        return random.randint(0,1000000000000000) #<- this will give you a 15 digit number
        print("that is FOR YOUR CREADIT CARD FOR 500 KSH")
creadit(1000000000000,1000000000000000)