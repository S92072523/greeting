import datetime
while True: 
    print("***********************Menu************************")
    print("1. Create Customer: ")
    print("2. Create Account: ")
    print("3. Exit: ")
    print("4. View Customer Balance Details: ")
    print("***************************************************")

    choice = int(input("Enter your choice(1 - 4: )"))

    if choice == 1:
         print("Hello")
    elif choice == 2:
        #Input for Account:
        Acc_Id = input('Enter the account ID: [eg: A_000101]')
        Acc_Type = input('Enter the account type: [Current, Saving, Fixed]')
        Cus_Id = input('Enter the Custome ID: [eg: C_0001]')
        balance = float(input("Enter the balacne: "))
        date = datetime.datetime.now()
        file = open("Account.txt", 'a')
        file.write(f"{Acc_Id}\t{Acc_Type}\t{Cus_Id}\t{date}\n")
        file.close()
        file = open("BalanceSheet.txt", 'a')
        file.write(f"{Acc_Id}\t{Cus_Id}\t{balance}\t{date}\t")
        file.close()
    elif choice == 3:
        exit()

    elif choice == 4:
        global Acc_Type_l, Cus_Id_l, balance_l, Cus_Name_l
        Acc_Id_input = input("Enter Account ID to view details: ")
        
        file = open("Account.txt", "r")
        for line in file:
            word = line.strip().split('\t')
            if word[0] == Acc_Id_input:
                Acc_Type_l = word[1]
                Cus_Id_l = word[2]
        file.close()

        file = open("BalanceSheet.txt", "r")
        for line in file:
            word = line.strip().split('\t')
            if word[0] == Acc_Id_input:
                balance_l = word[2]
        file.close()

        file = open("Customers.txt","r")
        for line in file:
            word = line.strip().split('\t')
            if word[0] == Cus_Id_l:
                Cus_Name_l = word[1]
        file.close()
        print("*********************Balance Statement****************************************************")
        print(f"{'Name':<10}{'Account Type':<10}{'Balance':<10}{'Date&Time':<10}")
        print(f"{Cus_Name_l:<10}{Acc_Type_l:<10}{balance_l:<10}{datetime.datetime.now()}")


