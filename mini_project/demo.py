def edit_phone():
    index = int(input("enter the record you want to edit"))
        
    phone = phones[index-1]
    print("Enter the data for a new phone. Press <enter> to leave unchanged.")
    
    print(phone[1])
    newname = input("Enter phone name to change or press return: ")
    if newname == "":
        newname = phone[0]
        
    print(phone[0])    
    newphone_num = input("Enter new phone number to change or press return: ")
    if newphone_num == "":
        newphone_num = phone[1]
            
    phone = [newname, newphone_num]
    phones[index-1] = phone