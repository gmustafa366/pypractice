# input json module
import json

# Create input file for MakeModel.json
# Create output file for csv
input_file_car = 'MakeModel.json'
output_file_favorites = 'favorites.csv'

try:
    input_file_handle = open(input_file_car, 'r')  # create door handle --> open file for reading
except OSError:
    print('Could not open', input_file_car)
    # 1 is the error if code is not working, where 0 is working.
    exit(1)

# Create a dictionary called car collections
car_collections = json.load(input_file_handle)

# convert the dict into a list
car_list = car_collections.get('CarMake')

# Create an empty list for adding favorite car/model
favorite_cars = list()

# Create loop: ask user to add favorite vehicle to list
while True:
    print('\nHere are current inventory of cars:')
    counter = 1
    for single_car in car_list:
        print(str(counter) + '. ', single_car.get("make"), single_car.get("model"))
        counter += 1

    # Make prompt to ask users to add their favorite vehicles list
    car_num = int(input('\nEnter the number of your favorite car: '))

# Create the outer and inner lists
    sub_list = list()
    sub_list.append(car_list[car_num - 1].get("make"))
    sub_list.append(car_list[car_num - 1].get("model"))

# display message of chosen of make and model after picking a number
    print('\nYou have chosen the', sub_list[0], sub_list[1])
    favorite_cars.append(sub_list)

# Enter a break in loop by asking user to add again favorite
    add_again = input('\nDo you want to add another vehicle in favorite list - Y or N: ')
    if add_again.upper() == 'N' and add_again.lower() == 'n':
        # print out each make and model from favorite list
        print('Following are the cars selected for favorite list:')
        for c in favorite_cars:
            print(c[0], '-', c[1])
        # print favorite car list into CSV file
        # Open file - make door handle
        output_file_handle = open(output_file_favorites, 'w')
        # In CSV file, make three column of Number, Make, and Model
        output_file_handle.write('NUMBER,MAKE,MODEL\n')
        counter = 1
        for c in favorite_cars:
            output_file_handle.write(str(counter) + ',' + c[0] + ',' + c[1] + '\n')
            counter += 1
        print('\nNow find your favorite car list and open it in Excel!')
        break
