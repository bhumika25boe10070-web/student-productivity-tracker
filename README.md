PROJECT: Student Productivity Tracker
AUTHOR: BHUMIKA SHARMA 

INTRODUCTION
The Student Productivity Tracker is a simple Python-based program designed to help students manage their daily tasks in an organized way. In day-to-day student life, it is easy to forget assignments or delay work due to poor planning. I created this project to solve that problem by building a basic system where tasks can be added, tracked, and completed easily.

PROBLEM STATEMENT

Students often have multiple responsibilities such as assignments, studying, and personal work. Without a proper system to track these tasks, it becomes difficult to manage time effectively. As a result, some tasks are missed or completed late, which affects productivity.


SOLUTION DEVELOPED

This project provides a simple solution by allowing users to:

* Add new tasks
* View all tasks with their status
* Mark tasks as completed
* Track overall progress based on completed tasks

This helps users stay organized and understand how much work they have completed.

WORKING

The program is menu-driven and runs in the terminal. When the program starts, it displays a list of options. The user selects an option by entering a number.

Based on the user’s choice:

* A task can be added to the list
* Existing tasks can be displayed
* A task can be marked as completed
* The overall progress is calculated and shown

Each task is stored using a dictionary with two values:

* Task name
* Completion status (Done or Pending)

All tasks are stored inside a list, which allows multiple tasks to be managed at once.

TECHNOLOGIES USED

* Python
* Concepts used:

  * Lists
  * Dictionaries
  * Functions
  * Loops
  * Conditional statements

HOW TO RUN

1. Make sure Python is installed on your system
2. Open the project folder in terminal or command prompt
3. Run the following command: python main.py
4. Follow the on-screen menu to use the program

EXAMPLE 

If a user adds tasks like:

* Complete assignment
* Study for exam

The program will display them along with their status (Pending or Done). Once marked complete, the progress will update automatically.


LEARNING OUTCOME

Through this project, I learned how to apply basic Python concepts to create a real-world application. I also understood how to take user input, manage data using lists and dictionaries, and design a simple menu-driven program.


FUTURE IMPROVEMENTS

This project can be improved further by:

* Saving tasks in a file so they are not lost after closing the program
* Creating a graphical user interface (GUI)
* Adding features like deadlines or reminders
