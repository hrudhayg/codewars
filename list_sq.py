def atm_withdrawal():
    acct_balance = 10000

    try:
        amt = int(input("Enter money to withdraw: "))
        
        if amt < 0:
            print("Amount can't be negative.")
        elif amt <= acct_balance:
            bal_fwd = acct_balance - amt
            print("Your balance after withdrawal is:", bal_fwd)
        else:
            print("Your available balance is:", acct_balance)
            print("Insufficient funds. Please try again!")

    except ValueError:
        print("Enter a valid numeric amount.")

atm_withdrawal()
