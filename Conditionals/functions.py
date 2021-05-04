# a file that contains a function
def conditional_decided(currentStatus, lowGallonQt):
    if (currentStatus >= 12 and currentStatus <= 15):
        print('You are good, and I would probably say that you are perfect')
    elif (currentStatus >= 3 and currentStatus <= 11):
        print('We think you should be thinking about some replenishment')
    elif (currentStatus > lowGallonQt and currentStatus < 3):
        print('My friend, you are about to start running on fumes')
    elif (currentStatus  == lowGallonQt):
        print('Low fuel warning has been turned on')
    else:
        print('Oh my God, my car just stopped in the middle of the highway')


def printHello(text):
    print(f'This is the text from the other file: {text}')

def printAddition(num1, num2):
    addition = num1 + num2
    return addition


def printTest():
    print('Test')