
import decimal

accuracyOfDigitsYouWant = 1000

def calPi(accuracyOfDigits):
    work_context = decimal.getcontext()
    work_context.prec = accuracyOfDigitsYouWant+20
    loop = int((accuracyOfDigitsYouWant+20)*1.6590389016018308)
    
    ## accuracy = [(loopTime, correctDigit)]
    
    side = decimal.Decimal(1)
    r = decimal.Decimal(1)
    n = 6
    for i in range(loop):
        n = n*2
        part1Square = (side/2)**2
        part2Square = (r-(r**2-(side/2)**2).sqrt())**2
        side = (part1Square+part2Square).sqrt()
    myPi = str(side*n/2)
    myPi = myPi[:accuracyOfDigitsYouWant+2]
    print(myPi)
    return myPi

myPi = calPi(accuracyOfDigitsYouWant)
