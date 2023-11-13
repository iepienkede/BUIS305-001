number1= int(input("Enter number:"))
if (number1%3==0 and number1%5==0):
    print("Tic Tac")
elif (number1%5==0):
    print("Tac")
elif (number1%3==0):
    print("Tic")
