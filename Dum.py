customers = {}
i = 0
while i < 2:
    Cus_NIC = input('Enter the NIC: ')
    Cus_Id = input('Enter the Custome ID: [eg: C_0001]')
    Cus_Name = input('Enter the customers Name: [eg: M.Jhon]')
    Cus_Location = input('Enter the customers Location: [eg: Jaffna]')
    customers[Cus_NIC] = {Cus_Id,Cus_Name,Cus_Location}
    i += 1

print(customers)

