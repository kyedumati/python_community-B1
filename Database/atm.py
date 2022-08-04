try:
    withdrawAmount = int(input("Please enter amount to withdraw "))
    currentbal = 2000
    remainingAmount=currentbal-withdrawAmount
    print(remainingAmount)
except:
    print("Please enter valid amount")
