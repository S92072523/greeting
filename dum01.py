customers = {}
i = 0
while i < 2:
    Cus_NIC = input('Enter the NIC: ')
    Cus_Id = input('Enter the Custome ID: [eg: C_0001]')
    Cus_Name = input('Enter the customers Name: [eg: M.Jhon]')
    Cus_Location = input('Enter the customers Location: [eg: Jaffna]')
    customers[Cus_NIC] = {Cus_Id, Cus_Name, Cus_Location}
    i += 1

# Print to console
print(customers)

# Write to a file
with open("customers.txt", "w") as file:
    for nic, details in customers.items():
        file.write(f"{nic}\t")
        for item in details:
            file.write(f"{item}\t")
        file.write("\n")