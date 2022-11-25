def cash_machine(option, value, balance):

    if option == 1:
        if value <= balance:
            balance = balance - value
            print(f"You withdrew a R$ {value}. Your balance now is R$ {balance}.")
            return balance
        else:
            print(f"Failed. Your balance is {balance}, try other value.")

    elif option == 2:
        if value > 0:
            balance = balance + value
            print(f"You deposited R$ {value}. Your balance now is R$ {balance}.")
            return balance
        else:
            print(f"Failed. Try other value.")


    else:
        print("Inválid option. Try 1 for withdrew or 2 for deposit.")



