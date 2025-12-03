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
It is going to make some alterations to that model, and build a CRUD application to perform some updates to it.

## ⭐ It allows user to:
- Insert new rows into each of the tables.
- Report out the data in a selected row from each of the tables.
- Delete a selected row, or give them an error message if such a deletion would leave orphaned rows.
- Update a selected row
  
## 📌 An abbreviated BOM for an idealized motorcycle
 <img alt="Fav Icon Png" src="https://github.com/Luft-phon/cecs323_orm_sqlalchemy_lab/blob/list/photos/BOM.png"/>

 <details>
   <summary align="center">VIEW MORE PHOTOS HERE</summary>
    <img alt="Fav Icon Png" src="https://github.com/Luft-phon/cecs323_orm_sqlalchemy_lab/blob/list/photos/ERD.png" />
    <img alt="Fav Icon Png" src="https://github.com/Luft-phon/cecs323_orm_sqlalchemy_lab/blob/list/photos/Enterprise%20description.jpg"/>
 </details>
 
## 🛠 Setup
1. Clone this repository
```
https://github.com/Luft-phon/cecs323_orm_sqlalchemy_lab.git
```

2. Open the project folder
   
3. Create config.ini file, we must defind  
```
[credentials]
userid = your-database-userid
password: your-database-password
host = localhost
port = ...
database = your-database-management-system
```

4. Run the program
```
python main.py
```

5. The program will ask to enter the database schema
   - Enter "Public"

## 📁 Project Structure

```
Project/
├── db_connection.py/        # configuration to connect postgres
├── functions.py/            # methods  
├── main.py/       
├── menu_definition.py/      
├── menu.py/
├── option.py/    
├── part.py/                 # Mapped class
├── usage.py/                # Mapped class
├── vendor.py/               # Mapped class
├── piecePart.py/            # Mapped class
├── SQLAlchemyUltilities.py/ # Check constraints
├── orm_base.py/      
```
