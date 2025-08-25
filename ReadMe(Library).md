Use the following command to have sample dataset or you can just start from fresh
import pickle
update_file=open("data.txt",'wb')
pickle.dump([10,"1.The Alchemist", "2.Sapiens: A Brief History of Humankind", "3.The Kite Runner", "4.The Pragmatic Programmer", "5.The Name of the Wind", "6.The Hitchhiker’s Guide to the Galaxy", "7.The Count of Monte Cristo", "8.Atomic Habits", "9.Norse Mythology", "10.Deep Work"],update_file)
