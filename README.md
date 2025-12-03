<h1 align="center"> MongoDB CRUD Lab </h1>

```javascript
=== WELCOME TO CATEGORIZATION OF BILL MATERIAL ===

Please select one of the following options:
  1 - Add
  2 - List
  3 - Abort
  4 - Exit this application
Enter your choice: ...
```

## 🌐 What is this lab project?
This lab is a menu-driven command-line application that demonstrates how to work with MongoDB using Python.
The goal is to practice:
- Connecting to MongoDB
- Executing CRUD-like operations
- Using MongoDB sessions and transactions
- Building a simple interactive menu system
- The project focuses on customers, products, orders, employees, and office relationships

## ⭐ It allows user to:
 INSERT data
- Add orders for existing customers
- Add employees (Managers or Sales Representatives)
- Automatically link employees to offices, subordinates, or customers

LIST data
- Show a detailed summary of a selected order, including line items and total price
- Display a full employee hierarchy starting with any chosen employee

ABORT changes
- Abort the active MongoDB transaction to undo all changes made during the session

EXIT the application
- Cleanly exit the program and end the session

## 🗂 Data Model Overview

The project uses the following MongoDB collections:

customers, products, orders, employees, offices, managers, sales_representatives
 
## 🛠 Setup
1. Clone this repository
```
https://github.com/Luft-phon/mongoDB-crud-lab.git
```

2. Open the project folder
   
3. Install dependencies
```
pip install pymongo

```
4. Create config.ini file, we must defind  
```
[server]
host = 
port = 
database = 

[operational]
rollback = False
restart = True

```

5. Run the program
```
python main.py
```
## ⚝ Tools
- Visual Studio Code
- Datagrip
- MongoDB Compass

## 📁 Project Structure

```
Project/
├── config.ini            # MongoDB connection & operational flags
├── db_connection.py      # MongoDB client + session utilities
├── functions.py          # Core operations: add/list orders & employees
├── main.py               # Entry point; transaction + menu loop
├── menu_definition.py    # Main/Add/List menu structures
├── menu.py               # Menu class: input/validation logic
└── option.py             # Option class for menu prompts
    
```

## 🧭 Using the Application

### ▶️ Add Menu

<details>
  <summary align="left"><strong>Add Order</strong></summary>

  - Select customer  
  - Choose products & quantities  
  - App validates stock and builds an order record  

</details>

<details>
  <summary align="left"><strong>Add Employee</strong></summary>

  - Enter employee info  
  - Choose role (Manager / Sales Rep)  
  - Optionally assign subordinate employees or customers  

</details>

### ▶️ List Menu

**List Order**

- Enter customer name and order date  
- The program prints a fully formatted invoice-style view  

**List Employee**

- Select an employee  
- Displays a recursive hierarchy of subordinates  

### ▶️ Abort  
Rolls back the active MongoDB transaction — useful for testing.

### ▶️ Exit  
Safely exits the program.
