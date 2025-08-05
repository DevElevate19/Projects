Expense_Tracker=[]

while (True):
    print("Welcome to Expense Tracker!")
    print("1. Add Expense\n2. View Summary\n3. Search Expense\n4. Save & Exit")
    try:
        Input=int(input("Enter your choice : "))
        if Input==1:
            Amount_Adding=int(input("Enter amount : "))
            Category=input("Enter Category : ")
            Date=input("Enter date (YYYY-MM-DD) : ")
            Note=input("Enter notes (optional) : ")
            print("\nExpense Added\n\n")
            Expense_Tracker.append([Amount_Adding,Category,Date,Note])
        elif Input==2:
            print(Expense_Tracker,"\n")
        elif Input==3:
            Search_Category=input("Category of Expense : ")
            for i in range(0,len(Expense_Tracker)):
                if Search_Category in Expense_Tracker[i]:
                    print(Expense_Tracker[i])
            print("\n")
        elif Input==4:
            print("Saved!\n")
        else:
            print("Write a valid choice")
    except:
        print("Write numbers in Choice Selection and Amount")
