# python algorithm

# Fibonacci Sequence by math

def fibonacciSequence():
    firstNum = 0
    secondNum = 0
    total = 0
    sequence = []

    for i in range(0, 20):
        if(firstNum == 0):
            sequence.append(firstNum)
            secondNum = 1
            sequence.append(secondNum)
        total = firstNum + secondNum
        # print(total)
        sequence.append(total)
        firstNum = secondNum
        secondNum = total
        
    return sequence
    
print("The Fibonacci sequence in list format after 20 iterations")
print(fibonacciSequence())


