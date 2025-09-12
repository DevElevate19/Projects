import pickle
from datetime import *

class Books:
    def __init__(self,nof,naof):
        self.no_of_books= nof
        self.name_of_books=naof
while True:
    func=int(input("Select Function you wanna perform:\n1.Take Books\n2.Load Books\n3.Check Status of Books given to others\n4.Change the number of days for books to be held by someone\n5.Save and Exit  \n"))
    if func==1:
        file=open("data.txt","rb")
        list_saved=pickle.load(file)
        k=Books(list_saved[0],list_saved[1:])
        nouwt=int(input("\nNumber of books u wanna withdraw: "))
        booksrn=list_saved[0]-nouwt
        file.close()
        update_file=open("data.txt",'wb')
#pickle.dump([10,"1.The Alchemist", "2.Sapiens: A Brief History of Humankind", "3.The Kite Runner", "4.The Pragmatic Programmer", "5.The Name of the Wind", "6.The Hitchhiker’s Guide to the Galaxy", "7.The Count of Monte Cristo", "8.Atomic Habits", "9.Norse Mythology", "10.Deep Work"],update_file)
        nodbtbh=30
        print(k.name_of_books)
        reserved_book=open("taken_books.txt",'wb')
        books_list_reserved=[]
        for i in range(0,nouwt):
            naouwt=input("\nName of the book u wanna take or enter the index no.(starting from 1)")
            try:
                #(Done)Solve indexing problem today
                books_list_reserved.append((k.name_of_books)[int(naouwt)-1-i]+(f',{date.today()}-{date.today()+timedelta(days=nodbtbh)}'))
                (k.name_of_books).pop(int(naouwt)-1-i)
            except:
                for j in range(1,11):
                    if f'{j}.{naouwt}' in k.name_of_books:
                        books_list_reserved.append(f'{j}.{naouwt},{date.today()},-,{date.today()+timedelta(days=nodbtbh)}')
                        (k.name_of_books).remove(f'{j}.{naouwt}')
        list_tobesaved=k.name_of_books
        list_tobesaved.insert(0,booksrn)
        pickle.dump(list_tobesaved,update_file)
        pickle.dump(books_list_reserved,reserved_book)
        reserved_book.close()
    elif func==2:
        loading=open("data.txt","wb")
        previous_data=open("data.txt","rb")
        list_for_op=pickle.load(previous_data)
        nobuwl=int(input("\nNo. of books you wanna load"))
        for i in range(0,nobuwl):
            book_loading=input("\nName of book you want to add (syntax:position.nameofbook)")
            list_for_op.insert(book_loading[0:2],book_loading[2:])
        pickle.dump(list_for_op)
    elif func==3:
        rrbf=open('taken_books.txt','rb')
        print('\n',pickle.load(rrbf))
        rrbf.close()

    elif func==5:
        print("\nYour data has been saved")
        break
    else:
        nodbtbh=int(input("\nEnter the number of days:"))
#(Checked)Add system to load books in library
#(Checked)Add due dates and date at which u took the book
#update_file=open("data.txt",'wb')
#pickle.dump([10,"1.The Alchemist", "2.Sapiens: A Brief History of Humankind", "3.The Kite Runner", "4.The Pragmatic Programmer", "5.The Name of the Wind", "6.The Hitchhiker’s Guide to the Galaxy", "7.The Count of Monte Cristo", "8.Atomic Habits", "9.Norse Mythology", "10.Deep Work"],update_file)


