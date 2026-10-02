# 🐍 Python Projects Collection

A collection of beginner-to-intermediate **Python programming projects** organized into five learning units.  
These projects demonstrate fundamental Python concepts such as input/output, conditional statements, loops, functions, randomization, object-oriented programming, and CSV file handling.

## 📌 Project Overview

| Unit | Project | Main Concepts |
|---|---|---|
| Unit 1 | ATM System | Input/Output, Conditions, Loops |
| Unit 1 | Simple MCQ Quiz | Variables, Conditions, Score Calculation |
| Unit 2 | Number Guess Game | Loops, Binary Search Logic, User Input |
| Unit 2 | Stronger Password Checker | Strings, Loops, Character Validation |
| Unit 3 | Mini Library Management | Classes, Objects, Functions, Lists |
| Unit 3 | Rock Paper Scissors | Functions, Dictionary, Random Module |
| Unit 4 | Dice Game | Random Module, Functions, Loops, Animation |
| Unit 4 | Hangman | OOP, Sets, Random Module, Game Logic |
| Unit 5 | CSV Files Accessing | CSV Module, File Handling, CRUD Operations |

---

## 📂 Folder Structure

```text
python-projects/
│
├── Unit_1/
│   ├── ATM System.py
│   └── Simple MCQ Quiz.py
│
├── Unit_2/
│   ├── number guess game.py
│   └── stronger password checker.py
│
├── Unit_3/
│   ├── Mini Library Management.py
│   └── Rock Paper Scissors.py
│
├── Unit_4/
│   ├── Dice Game.py
│   └── Hangman.py
│
└── Unit_5/
    ├── CSV Files Accessing.py
    └── Santhosh.csv
```

---

# 🚀 Projects

## 1. 🏧 ATM System

A console-based ATM simulation that allows users to:

- Check account balance
- Deposit money
- Withdraw money
- Maintain a minimum balance
- Exit the ATM system

### Concepts Used
- Variables
- `input()` and `print()`
- `while` loop
- `if-elif-else`
- Arithmetic operations
- User input validation

---

## 2. 📝 Simple MCQ Quiz

A command-line multiple-choice quiz containing questions from different topics.

### Features
- Takes the user's name
- Displays multiple-choice questions
- Accepts answers
- Calculates the score
- Displays the final result

### Concepts Used
- Variables
- Conditional statements
- User input
- Score calculation
- Loops and basic control flow

---

## 3. 🔢 Number Guess Game

A number guessing program where the computer determines the user's number using a binary-search-style approach.

### Features
- Number range from 1 to 50
- Yes/No based interaction
- Reduces the search range after every answer
- Displays the number of questions asked

### Concepts Used
- `while` loop
- Integer calculations
- Conditional statements
- User input
- Binary search logic

---

## 4. 🔐 Stronger Password Checker

A password strength checker that evaluates a password based on five criteria.

### Checks
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

The program provides a score out of 5 and suggestions for improving weak passwords.

### Concepts Used
- Strings
- Loops
- Character checking
- `isupper()`
- `islower()`
- `isdigit()`
- Conditional statements

---

## 5. 📚 Mini Library Management

A console-based library management system implemented using **Object-Oriented Programming**.

### Features
- Display available books
- Display registered users
- Borrow books
- Return books
- Display borrowed books
- Validate users and books

### Concepts Used
- Classes and objects
- Constructors
- Methods
- Lists
- Functions
- Object state management
- OOP principles

### Main Classes
```text
Book
User
```

---

## 6. ✊ Rock Paper Scissors

A command-line Rock Paper Scissors game where the player competes against the computer.

### Features
- Rock, Paper, Scissors choices
- Computer-generated random choice
- Best-of-5 gameplay
- Round-by-round score
- Final result

### Concepts Used
- Functions
- Dictionary
- Lists
- `random` module
- Loops
- Conditional statements

---

## 7. 🎲 Dice Game

A Best-of-5 dice game between the player and computer.

### Features
- Random dice rolls
- ASCII-style dice display
- Roll animation
- Round-based scoring
- First player to win 3 rounds wins
- Replay option

### Concepts Used
- `random` module
- `time` module
- Functions
- Dictionaries
- Loops
- Conditional statements

---

## 8. 🎮 Hangman

A console-based Hangman word guessing game.

### Features
- Random word selection
- Word hints
- Six available lives
- Tracks guessed letters
- Prevents duplicate guesses
- Win/loss detection
- Replay option

### Concepts Used
- Classes and objects
- Sets
- Dictionaries
- Lists
- `random` module
- Loops
- String processing

---

## 9. 🏥 CSV Hospital Management

A CSV-based console application for managing patient records.

### Features
- View patient data
- Add a patient
- Search for a patient
- Delete a patient
- Access a specific row
- Access a specific column

### Patient Information
The program works with fields such as:

```text
Patient ID
Name
Age
Gender
Disease
Doctor
Department
Admission Date
Discharge Date
Bill Amount
```

### Concepts Used
- File handling
- `csv` module
- Reading and writing CSV files
- CRUD-style operations
- Lists
- Functions
- User input

> **Important:** Before running this project, update the `file_path` inside `CSV Files Accessing.py` so that it points to the `Santhosh.csv` file on your computer.

For example:

```python
file_path = "Santhosh.csv"
```

Using a relative path is generally more convenient when the CSV file is stored in the same folder as the Python program.

---

# 🛠️ Technologies Used

- **Python 3**
- Python Standard Library
- `random`
- `time`
- `csv`

No external packages are required for these projects.

---

# 💻 Requirements

Before running the projects, install:

### Python

Python 3.8 or later is recommended.

Check your Python installation:

```bash
python --version
```

or:

```bash
py --version
```

---

# ▶️ How to Run

### 1. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

### 2. Open the Project Folder

```bash
cd python-projects
```

### 3. Navigate to a Unit

For example:

```bash
cd Unit_1
```

### 4. Run a Python Program

```bash
python "ATM System.py"
```

You can run any project by providing its filename.

Example:

```bash
python "Hangman.py"
```

---

# 🎯 Learning Objectives

These projects were created to practice and understand:

- Python syntax and programming fundamentals
- Variables and data types
- Input and output
- Conditional statements
- Loops
- Functions
- Lists, dictionaries, and sets
- String operations
- Random number generation
- File handling
- CSV processing
- Object-Oriented Programming
- Basic problem-solving and algorithmic thinking

---

# 📈 Concepts Progression

```text
Unit 1
   ↓
Python Basics
Input → Conditions → Loops
   ↓
Unit 2
   ↓
Problem Solving
Algorithms → Strings → Validation
   ↓
Unit 3
   ↓
Functions & OOP
Functions → Classes → Objects
   ↓
Unit 4
   ↓
Interactive Programs
Randomization → Game Logic → OOP
   ↓
Unit 5
   ↓
File Handling
CSV → Read → Write → Search → Delete
```

---

# 🔮 Future Improvements

Possible enhancements for these projects include:

- Graphical user interfaces using Tkinter
- Better input validation
- Persistent data storage
- Improved exception handling
- More quiz questions and categories
- Difficulty levels for games
- High-score tracking
- Search and filter options
- Modular Python files
- Unit testing
- Database integration for larger applications

---

# 👨‍💻 Author

**Santhosh**

A collection of Python practice projects developed to strengthen programming fundamentals and problem-solving skills.

---

## ⭐ Repository

If you find these projects useful for learning Python, consider giving the repository a ⭐ on GitHub.
