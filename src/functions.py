from datetime import datetime
from configparser import ConfigParser       # so that I can read in parameters
import random
from pymongo import MongoClient
from db_connection import get_db_name


def add_order(sess): 
    customers = sess.client[get_db_name()]['customers']
    orders = sess.client[get_db_name()]['orders']
    products = sess.client[get_db_name()]['products']

    # ---- CUSTOMER ----
    while True:
        customer = input("Enter customer name: ")
        customer_doc = customers.find_one(
            {'customername': customer}
        )
        
        if customer_doc is None:
            print(f'\tError, customer "{customer}" does not exist')
        else:
            break

    orderdate = datetime.now()

    # ---- REQUIREDDATE ----
    while True:
        try:
            requireddate = input("Enter required date (YYYY-MM-DD): ")
            required_date = datetime.strptime(requireddate, "%Y-%m-%d")
        except:
            print("\tInvalid date format.")
            continue

        if required_date < orderdate:
            print('\tError, required date cannot be before order date')
        else:
            break

    status = "In Process"
    shippeddate = None
    comments = ""
    details = []

    # ---- ADD PRODUCTS LOOP ----
    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        if product_name.lower() == "done":
            break

        product_doc = products.find_one(
            {'productname': product_name}
        )

        if product_doc is None:
            print(f'\tError: product "{product_name}" does not exist.')
            continue

        # duplicate check
        if any(d["product"]["productcode"] == product_doc["_id"] for d in details):
            print(f'\tError, product "{product_name}" already added.')
            continue

        product_code = product_doc["_id"]
        quantityinstock = product_doc["quantityinstock"]

        # quantity loop
        while True:
            quantityordered = int(input("Enter quantity ordered: "))
            if quantityordered > quantityinstock:
                print(f'\tError, only {quantityinstock} items in stock.')
            else:
                break

        # price each random
        msrp = product_doc["msrp"]
        priceeach = random.uniform(1.5 * msrp, 2.0 * msrp)

        detail = {
            "product": {
                "productcode": product_code,
                "productname": product_name
            },
            "quantityordered": quantityordered,
            "priceeach": priceeach
        }

        details.append(detail)

    # ---- CREATE ORDER DOCUMENT ----
    order_doc = {
        "customer": {
            "customernumber": customer_doc["_id"],
            "customername": customer_doc["customername"]
        },
        "orderdate": orderdate,
        "requireddate": required_date,
        "status": status,
        "shippeddate": shippeddate,
        "comments": comments,
        "details": details
    }

    print("\n--- ORDER PREVIEW ---")
    display_order(order_doc["details"])

    orders.insert_one(order_doc, session = sess)  # insert_one là syntax của session nhưng hiện tại session đang dc dùng trong transaction
    # sau khi insert thì sẽ vào transaction và chỉ commit sau khi thoát vòng lặp main menu trong main => lúc đó transaction sẽ tự closed

    print("\tOrder inserted successfully.\n")

def add_employees(sess):
    employees = sess.client[get_db_name()]['employees']
    customers = sess.client[get_db_name()]['customers']
    offices = sess.client[get_db_name()]['offices']
    managers = sess.client[get_db_name()]['managers']
    sale_reps = sess.client[get_db_name()]['sales_representatives']

    firstname = input("Enter employee's firstname: ").strip()
    lastname = input("Enter employee's lastname: ").strip()
    extension = input("Enter extension: ").strip()
    email = input("Enter email: ").strip()

    while True:
        try:
            officecode = int(input("Enter office code [1-7]: ").strip())
            if 1 <= officecode <= 7:
                break
            print("Code must be between 1 and 7.")
        except ValueError:
            print("Please enter a number.")
    office = offices.find_one({"_id": str(officecode)})
    office_doc = {
        "officecode": office["_id"],
        "city":  office["city"],
        "state": office["state"],
        "country": office["country"],
    }
    
    # ask whether this employee is manager or sale rep
    while True:
        print("Will this employee be a Manager or Sales Representative?")
        role = input("\tEnter role (m/s): ").strip()
        if role in ["m", "s"]: 
            break
        else: 
            print("\tError: Invalid choice. Enter 'm' or 's'")
    jobtitle = "Manager" if role == "m" else "Sales Representative"

    reportsto = None

    #_id
    last_employee = employees.find_one(sort=[("_id", -1)])
    new_id = last_employee["_id"] + 1 if last_employee else 1000

    new_employee = {
        "_id": new_id,
        "firstname": firstname,
        "lastname": lastname,
        "extension": extension,
        "email": email,
        "officecode": str(officecode),
        "office": office_doc,
        "jobtitle": jobtitle,
        "reportsto": reportsto
    }

    #insert employee
    employees.insert_one(new_employee)
    print(f"\nEmployee {firstname} {lastname} added with ID {new_id}.")

    #add to manager and sale rep collections
    if role == "m":
        managers.insert_one(
            {
                "_id": new_id,
                "firstname": firstname,
                "lastname": lastname,
                "extension": extension,
                "email": email,
                "officecode": str(officecode),
                "office": office_doc,
                "jobtitle": jobtitle,
                "reportsto": reportsto  
            }
        )        
        print("Added to MANAGERS collection.")
    else:
        sale_reps.insert_one({
            "_id": new_id,
            "firstname": firstname,
            "lastname": lastname,
            "extension": extension,
            "email": email,
            "officecode": str(officecode),
            "office": office_doc,
            "jobtitle": jobtitle,
            "reportsto": reportsto
        })
        print("Added to SALE REPRESENTATIVE collection.\n")

    # assign which employees is supervised by manager
    if role == "m":
        print("===Assign a subordinate to this manager===")
        while True:
            employee_name = input("Enter employee's firstname (or 'done' to exit): ")
            if employee_name == "done":
                break
            employee_doc = employees.find_one({"firstname": employee_name})
            if not employee_doc:
                print("\tError: Employee {employee_name} does not exist")

            employees.update_one(
                {"_id": employee_doc["_id"]},
                {"$set": {"reportsto": {
                        "_id": new_id,
                        "lastname": lastname,
                        "firstname": firstname
                    }}}, session = sess
            )
            
            print(f"\t{employee_doc['firstname']} {employee_doc['lastname']} now reports to {firstname} {lastname}.")

    # assign which customer is supervised by sale rep
    if role == "s":
        print("===Assign a customer to this sale representative\n")
        while True:
            cust_name = input("Enter customer's firstname (or 'done' to exit): ")
            if cust_name == "done":
                break
            cust_doc = customers.find_one({"contactfirstname": cust_name})

            if not cust_doc:
                print("\tError: Customer {cust_name} does not exist")

            customers.update_one(
                {"_id": cust_doc["_id"]},
                {"$set": {"salesrep": {
                            "employeenumber": new_id, 
                            "lastname": lastname,
                            "firstname": firstname
                        }
                }}
            )
            print(f"\t{cust_doc['contactfirstname']} {cust_doc['contactlastname']} now has {firstname} {lastname} as their sale rep.")
    
def display_order(details):
    number = 0

    # Header
    print("+" + "-"*6 +"+" + "-"*14 + "+" + "-"*41 + "+" + "-"*10 + "+" + "-"*12 + "+")
    print(f"|  {'#' : <2}  | {'ProductCode':<12} | {'Product Name':<39} | {'Quantity':<8} | {'PriceEach':<10} |")
    print("+" + "-"*6 +"+" + "-"*14 + "+" + "-"*41 + "+" + "-"*10 + "+" + "-"*12 + "+")

    for d in details:
        number += 1
        product = d["product"]
        code = product["productcode"]
        name = product["productname"]
        quantity = d["quantityordered"]
        price = round(d["priceeach"], 2)

        print(f"|  {number: <2}  | {code:<12} | {name:<39} | {quantity:<8} | {price:<10} |")

    print("+" + "-"*6 +"+" + "-"*14 + "+" + "-"*41 + "+" + "-"*10 + "+" + "-"*12 + "+")

def list_order(sess):
    db = sess.client[get_db_name()] 
    customers = db["customers"] 
    orders = db["orders"] 
    # 1. Input 
    customer_name = input("Enter customer name: ").lower() 
    order_date_str = input("Enter order date (YYYY-MM-DD): ") 
    # # Convert string → datetime 
    order_date = datetime.strptime(order_date_str, "%Y-%m-%d") 
    # 2. Find customer 
    customer = customers.find_one({
        "customername": {
            "$regex": f"^{customer_name}$", 
            "$options": "i" } 
            }
        ) 
    if not customer: 
        print("\tError: Customer not found.") 
        return 
    
    cust_number = customer["_id"] 
    # 3. Find the order on that date 
    order = orders.find_one({ "customer.customernumber": cust_number, "orderdate": order_date }, session = sess) 
    if not order:
        print("\tError: No order found for that customer on that date.") 
        return 
    
    # 4. Display order details
    details = order.get("details", []) 
    details_sorted = sorted(details, key=lambda x: x["product"]["productcode"]) 
    if not details: 
        print("No order details found.") 
        return
    display_order(details_sorted) 
    # Total 
    total = sum(d["quantityordered"] * d["priceeach"] for d in details_sorted) 
    print(f"Total Amount: {total:.2f}") 
    print("+" + "-"*14 + "+" + "-"*41 + "+" + "-"*10 + "+" + "-"*12 + "+") 
    print()

def list_employee_hierarchy(sess):
    db = sess.client[get_db_name()]
    employees = db["employees"]

    while True:
        emp_name = input("Enter employee to start with: ").strip()
        emp_doc = employees.find_one(
            {"firstname": {"$regex": f"^{emp_name}$", "$options": "i"}}, session = sess
        )
        if not emp_doc:
            print("\tError: Employee not found.")
        else: 
            break
    
    def print_hierarchy(manager_id, indent=0):

        manager = employees.find_one({"_id": manager_id}, session = sess)
        if manager is None:
            return

        print(" " * indent + f"{manager_id} {manager['firstname']} {manager['lastname']}")

        subordinates = employees.find({"reportsto._id": manager_id}, session = sess)

        for emp in subordinates:
            print_hierarchy(emp["_id"], indent + 4)

    # ---- START PRINTING ----
    print("\n--- Employee Hierarchy ---")
    print_hierarchy(emp_doc["_id"])
    print()


