import sqlite3

# global variable
db_name = "car_inventory.db"


# write a line that allow user to connect to the database
# (establishing a connection)
def connect_to_db():
    db_conn = sqlite3.connect(db_name) # opening (doorknob)
    db_cursor = db_conn.cursor()
    print('Successfully connected to DB!')
    return db_conn, db_cursor


# create
def create_table(db_cursor):
    sql_create = 'CREATE TABLE car' \
                 '(vin INTEGER, make TEXT, model TEXT, ' \
                 'mileage INTEGER, price REAL, color TEXT)'
    db_cursor.execute(sql_create)
    print('Successfully created table.')


def drop_table(db_cursor):
    sql_drop = 'DROP TABLE IF EXISTS  car'
    db_cursor.execute(sql_drop)
    print('Successfully dropped table.')


def select_all(db_cursor):
    sql_select_all = 'SELECT * FROM car'
    result_set = db_cursor.execute(sql_select_all)
    print("\nThe data is: ")
    for row in result_set:
        print(row)



def ask_for_int(field):
    while True:
        try:
            x = int(input('Enter the ' + field))
            return x
        except:
            print('You have entered an invalid int. Please try again')


def ask_for_float(field):
    while True:
        try:
            x = float(input('Enter the ' + field))
            return x
        except:
            print('You have entered an invalid int. Please try again')


def insert_row(db_cursor):
    # order must match the order given when creating the table
    sql_insert = 'INSERT INTO car VALUES' \
                 '(?,?,?,?,?,?)'
    while True:
        # add user for each value
        vin = ask_for_int("vin number: ")
        make = input('Enter make: ')
        model = input('Enter model: ')
        mileage = ask_for_int("mileage: ")
        price = ask_for_float('price: ')
        color = input('Enter color: ')
        tuple_of_values = (vin, make, model, mileage, price, color)
        db_cursor.execute(sql_insert, tuple_of_values)
        print('Successfully inserted one row')
        loop_again = input('Do you want to insert another row? Y or N: ')
        if loop_again.upper() == 'N':
            break

        select_all(db_cursor)


def select_row(db_cursor):
    sql_row = 'SELECT * FROM car WHERE vin = ?'
    vin = int(input('Which vehicle would you like to select?\nEnter VIN: '))
    tuple_of_values = (vin, )
    result_set = db_cursor.execute(sql_row, tuple_of_values)
    print('The data returned is:')
    for row in result_set:
        print(row)


def update_row(db_cursor):
    sql_update = 'UPDATE car SET price = ?, mileage = ?' \
                 ' WHERE vin = ?'
    vin = int(input('Which of the vehicle would you like to update, so enter the VIN: '))
    mileage = int(input('What is the new mileage on the vehicle?'))
    price = float(input('What is the new price of the vehicle?'))
    print('Updated row with the VIN of', vin)
    print('The new price is', price, "according to the new mileage -", mileage)
    tuple_of_values = (vin, price, mileage)
    db_cursor.execute(sql_update, tuple_of_values)


def delete_row(db_cursor):
    sql_delete = "DELETE FROM car" \
                 " WHERE vin = ?"
    vin = int(input('Which car would you like do delete?\nEnter VIN: '))
    tuple_of_values = (vin, )
    db_cursor.execute(sql_delete, tuple_of_values)
    print('Successfully deleted row with VIN', vin)


def display_menu(db_conn, db_cursor):
    while True:
        print('\nMain Menu:\n')
        print('Enter \'S\' to get started and create/refresh the table')
        print('Enter \'C\' create a new row')
        print('Enter \'R\' to retrieve data')
        print('Enter \'U\' to update a row')
        print('Enter \'D\' to delete a row')
        print('Enter \'Q\' to quit the program')

        choice = input('\nEnter choice: ').upper()
        if choice == 'S':
            drop_table(db_cursor)
            create_table(db_cursor)
        elif choice == 'C':
            insert_row(db_cursor)
        elif choice == 'R':
            select_row(db_cursor)
        elif choice == 'U':
            update_row(db_cursor)
        elif choice == 'D':
            delete_row(db_cursor)
        elif choice == 'Q':
            print('Thank you for using the car inventory program!')
            break
        else:
            print('Invalid option have been chosen, please try again!', choice)

        # to commit (save) all the changes
        db_conn.commit()
        select_all(db_cursor)


def main():
    db_conn, db_cursor = connect_to_db()
    display_menu(db_conn, db_cursor)


main()