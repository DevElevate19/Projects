Library – simple CLI
A small command-line script to manage a tiny “library”: add books, lend them out, and see due dates. Data is saved locally using pickle files.

How to run
Python 3 required

Run: python3 Library(Completed).py

What it does
Load Books: add numbered titles to the library

Take Books: pick by index or name; saves taken date and due date

Check Status: shows borrowed entries with dates

Change Days: set loan period

Save & Exit

Files created
data.pkl (available books and count)

taken_books.pkl (borrowed records with dates)

Notes
First run: use “Load Books” to seed the list

File format is pickle; don’t edit by hand



Run following code for sample dataset:

import pickle

update_file=open("data.txt",'wb')

pickle.dump([10,"1.The Alchemist", "2.Sapiens: A Brief History of Humankind", "3.The Kite Runner", "4.The Pragmatic Programmer", "5.The Name of the Wind", "6.The Hitchhiker’s Guide to the Galaxy", "7.The Count of Monte Cristo", "8.Atomic Habits", "9.Norse Mythology", "10.Deep Work"],update_file)
