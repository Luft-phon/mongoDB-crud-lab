from menu_definition import add_menu, list_menu, menu_main
from db_connection import Session, SessionLocal

import functions
def list_objects(sess: Session):
    list_action: str = ''
    while list_action != list_menu.last_action():
        list_action = list_menu.menu_prompt()
        exec(list_action)
def add_objects(sess: Session):
    add_action: str = ''
    while add_action != add_menu.last_action():
        add_action = add_menu.menu_prompt()
        exec(add_action)
def main():
    sessLoc = SessionLocal()
    sess = sessLoc.mongo_session        
    with sess.start_transaction():              #mở transaction và tự động đóng sau khi commit 
        main_action = ''
        while main_action != menu_main.last_action():
            main_action = menu_main.menu_prompt()
            exec(main_action)

if __name__ == "__main__":
    main()