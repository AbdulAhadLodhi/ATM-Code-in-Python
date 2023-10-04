print("Welcome to Islamic Bank\n\nInsert your card")

password=1234
balance=10000
choice=0

pin=int(input("Enter your Four digit pin\n"))

if pin==password:
    while choice != 4:

        print("\n\n**** Menu ****")
        print("1 == balance")
        print("2 == deposite")
        print("3 == withdraw")
        print("4 == cancel\n")

        choice=int(input("\nEnter your option:\n"))

        if choice==1:
            print("Balance = Rs", balance)

        elif choice==2:
            dep=int(input("Enter your deposite: Rs"))
            balance += dep
            print("\n deposited amount: Rs", dep)
            print("balance = Rs", balance)

        elif choice==3:
            wit=int(input("Enter the amount to withdraw: Rs"))
            balance -= wit
            print("\nwithdrawn amount : Rs", wit)
            print("balance = Rs", balance)

        elif choice==4:
            print("\n Session Ended!! Goodbye ")

        else:
            print("\nInvalid Entry !!")            

else:
    print("Pin Incorrect!! Try again")    