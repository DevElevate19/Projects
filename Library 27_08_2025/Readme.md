# 📚 Library – Simple CLI

A lightweight command-line tool to manage a tiny library:  
**Add books, lend them out, and track due dates.**  
All data is stored locally using pickle files for persistence.

---

## 🚀 Quick Start

1. **Requires:** Python 3
2. **Run:**  
   ```bash
   python3 Library(Completed).py
   ```

---

## 🛠️ Features

- **Load Books:**  
  Add numbered titles to your library collection.
- **Take Books:**  
  Borrow a book by index or name; records taken date and due date.
- **Check Status:**  
  View all borrowed books and their loan/due dates.
- **Change Days:**  
  Set or modify the loan period for borrowed books.
- **Save & Exit:**  
  Persist all changes and close the program.

---

## 📁 Files Created

- `data.pkl` — stores available books and count  
- `taken_books.pkl` — stores records of borrowed books and dates

---

## 📝 Notes

- **First Run:**  
  Use “Load Books” to add your initial list of titles.
- **File Format:**  
  All data is saved as pickle files (`.pkl`).  
  **Do not edit these files by hand!**

---

## 🧪 Sample Dataset

Use the code below to seed your library with example books:

```python
import pickle

update_file = open("data.pkl", 'wb')
pickle.dump([
    10,
    "1. The Alchemist",
    "2. Sapiens: A Brief History of Humankind",
    "3. The Kite Runner",
    "4. The Pragmatic Programmer",
    "5. The Name of the Wind",
    "6. The Hitchhiker’s Guide to the Galaxy",
    # ... add more titles as needed
], update_file)
update_file.close()
```

---

## 💡 Tip

- For best results, always use the CLI to manage your library.
- Explore each menu option to learn the workflow.

---

## 🏷️ License

This project is for educational purposes.
