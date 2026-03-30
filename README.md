🗂️ performace test- students management systems

A command-line students management system built in Python. It allows users to create, read, search, save, and reload students using a CSV file for persistent storage.
📁 Project Structure

prueba_joshua/
├── App.py        #Csv save/load logic
├── main.py       # place where start the code
├── menu.py       # Menu and program flow
├── models.py     # where i import and save the list
├── services.py   # Input validation functions
└── data/
    └── data.csv    # Persistent storage file

⚙️ How It Works

The program starts from main.py and execute a menu who have a loop that shows the user a menu with 8 options:

    create a student — asks for name, age, grade and status, then appends it to the students list.
    Show students — prints all registered students with their values
    search students — asks for the students that you want to seacrh and why you searching this one.
    uptaded students — this one change one think of the student register previusly
    delete student — ask for the name of one student and delete it 
    save students — writes the current inventory to data/data.csv.
    Upload inventory — reads data/data.csv and loads it back into memory.
    Exit — closes the program.

🧩 Modules
models.py

Defines the shared inventory list used across all modules.
services.py

Contains input validation functions:

    name() — validates that the students name contains only letters.
    new_name() — validates the new students name.
    age() — validates that the age is a positive integer.
    new_age() — validates the new age.
    grade_selected() — print a list and validate de option that user choose.
    new_grade_selected() — validate the new grade.
    status() — print a list with 2 options and validate the option.
    options() — validate the options that the user choose un the menu
    options_to_delete() — validate the options that you choose in the delete menu.
    search_1 () — validate the index that you want to search the student
    search_id() — validate the Id that you put in is posible and positive.
    uptade_students() — ask for what index you want to uptade the student
    show_students() — search in the list the students and print then.

app.py

Handles CSV operations:

    save_student() — writes the students list to data/data.csv.
    read_register() — reads the CSV and returns a list of dictionaries.
    upload_students() — loads CSV data back into the students list.

main.py

Main entry point. Runs the menu loop and connects all modules together.
▶️ How to Run

python main.py

Make sure all files are in the same folder before running.
📋 Requirements

    Python 3.x
    No external libraries — uses only built-in csv module.

💾 Data Format

Products are stored in data/data.csv with the following columns:
ID-name_age-grade-status
303-joshua-18--11°-active

👤 Author

Joshua Quintero Reguillo 
Coder from Riwi
