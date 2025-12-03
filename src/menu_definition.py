from menu import Menu
from option import Option
 # The main options for operating on Departments and Courses.
menu_main = Menu('main', 'Please select one of the following options:', [
    Option("Add", "add_objects(sess)"),
    Option("List", "list_objects(sess)"),
    Option("Abort", "sess.abort_transaction()"),   #
    Option("Exit this application", "pass")
])
add_menu = Menu('add', 'Please indicate what you want to add:', [
    Option("Order", "functions.add_order(sess)"),
    Option("Employee", "functions.add_employees(sess)"),
    Option("Exit", "pass")
 ])
list_menu = Menu('list', 'Please indicate what you want to list:', [
    Option("Order", "functions.list_order(sess)"),
    Option("Employee", "functions.list_employee_hierarchy(sess)"),
    Option("Exit", "pass")
 ])
debug_select = Menu('debug select', 'Please select a debug level:', [
    Option("Informational", "logging.INFO"),
    Option("Debug", "logging.DEBUG"),
    Option("Error", "logging.ERROR")
 ])