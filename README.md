# 🐍 30 Days of Python Challenge

Welcome to the **30 Days of Python Challenge** repository! This project serves as a step-by-step guide to mastering Python, starting from foundational concepts and moving towards building complex applications.

Each day focuses on a core Python topic accompanied by a hands-on project/task and automated test scripts to verify the implementation.

---

## 📂 Project Structure

The repository is organized by days, with each directory containing a task description, the implementation file, and a corresponding test suite.

```text
python-30-day/
├── day1/                  # Day 1: Variables & Data Types
│   ├── day01_calculator.py  # Basic CLI Calculator
│   ├── task.md              # Problem Description
│   └── test_day01.py        # Calculator Test Suite
├── day2/                  # Day 2: Control Flow
│   ├── day02_guessing_game.py # Text-based Guessing Game
│   ├── task.md              # Problem Description
│   └── test_day02.py        # Guessing Game Test Suite
├── day3/                  # Day 3: Lists & Tuples
│   ├── day03_inventory.py   # Inventory List Manager
│   ├── task.md              # Problem Description
│   └── test_day03.py        # Inventory Test Suite
├── day4/                  # Day 4: Dictionaries
│   ├── day04_profile.py     # User Profile Generator
│   ├── task.md              # Problem Description
│   └── test_day04.py        # Profile Test Suite
└── README.md              # This guide
```

---

## 📋 Challenge Progress

Here is a summary of the topics and projects implemented so far:

| Day | Topic | Project | Status |
| :--- | :--- | :--- | :---: |
| **Day 1** | Variables & Data Types | [CLI Calculator](day1/day01_calculator.py) | Completed |
| **Day 2** | Control Flow (`if`/`elif`/`else`) | [Text Guessing Game](day2/day02_guessing_game.py) | Completed |
| **Day 3** | Lists & Tuples | [Inventory Manager](day3/day03_inventory.py) | Completed |
| **Day 4** | Dictionaries | [User Profile Generator](day4/day04_profile.py) | Completed |
| **Days 5-30**| Functions, OOP, File I/O, Web, etc. | Upcoming Tasks | In Progress |

---

## 🚀 How to Run the Scripts

To run the script for a specific day, navigate into that day's directory and execute the script using Python:

```bash
# Example for running Day 1 Calculator
cd day1
python day01_calculator.py
```

---

## 🧪 Running the Tests

Each day includes a test runner to automate verification of your code. 

> [!IMPORTANT]
> **Directory Scope Warning:**  
> The test scripts execute the main exercise scripts using a relative path (e.g. `day0X_inventory.py`). Because of this, **you must execute the tests from within the specific day's directory**. Running them from the repository root will cause a "File Not Found" error.

### Correct Way to Run Tests:
```bash
# Navigate to the specific day's folder
cd day3

# Run the test script
python test_day03.py
```

### Example Test Outputs:

- **Day 1 Calculator:**
  ```text
  Running 10 Test Cases for Day 1 Calculator...
  --------------------------------------------------
  [PASS] Test 1 PASSED: 10 + 5 -> expected 'Output:  15.0'
  [PASS] Test 2 PASSED: 10 - 5 -> expected 'Output:  5.0'
  ...
  Results: 10/10 Tests Passed.
  ```

---

## 🛠 Prerequisites

Make sure you have Python 3.x installed. You can check your version by running:
```bash
python --version
```
