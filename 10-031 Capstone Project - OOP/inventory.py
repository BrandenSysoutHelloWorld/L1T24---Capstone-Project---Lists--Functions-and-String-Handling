
#========The beginning of the class==========
class Shoe:
    # Initialize shoe class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    # Return the current cost of the shoes
    def get_cost(self):
        return float(self.cost)
    
    # Return the Quantity of the shoes
    def get_quantity(self):
        return int(self.quantity)

    # Update a shoe's quantity
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    # Output format
    def __str__(self):
        output = f'''
Shoe Product: {self.product}
    Origin Country: {self.country} | Code: {self.code}
    Remaining Stock: {self.quantity}
    Shoe's Cost: R {self.cost}
----------------------------------------------------------- '''
        return output

# Shoe list used to store Shoe objects
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list.
    '''
    with open('inventory.txt', 'r') as shoe_inventory:
        # Read data from text file
        shoes = shoe_inventory.readlines()
        
        # Append shoe objects to list
        for shoe in shoes:
            shoe_data = shoe.strip().split(',')
            # Test for headers
            if shoe_data[0].lower() != 'country':
                # Create the shoe object
                _shoe = Shoe(
                    country=shoe_data[0],
                    code = shoe_data[1],
                    product=shoe_data[2],
                    cost=shoe_data[3],
                    quantity=shoe_data[4])
        
                # Append the shoe object to list
                shoe_list.append(_shoe)    

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    # Capture shoes details
    captured_shoe = Shoe(
        country=input('Enter a shoes country:\n> '),
        code=input('Enter shoe code:\n> '), 
        product=input('Enter shoe product:\n> '),
        cost=input('Enter a shoe cost:\n> '),
        quantity=input('Enter a shoe quantity:\n> '))
    
    # Append shoe object to list
    shoe_list.append(captured_shoe)

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function.
    '''
    # Loop over shoe list and print each object
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # Use lambda - Order by Quantity
    shoe_list.sort(key=lambda _shoe: _shoe.get_quantity(), reverse=True)

    # Get the lowest quantity shoe object by calling the the last object within the list
    print('Consider Restocking the Following...\n')
    print(shoe_list[-1])
    

    # Prompt user to update the shoe quantity now
    print('Restock the shoe now?\nType "yes" or "no" to continue:')
    option_selected = input('> ')
    
    # Update shoe quantity
    if option_selected.lower() == 'yes':
        try:
            # Get new shoe quantity
            new_quantity = int(input('Your new shoe quantity:\n> '))
            
            # Update the shoe
            shoe_list[-1].update_quantity(new_quantity)

            # Write updated shoes data
            with open('inventory.txt', 'w') as write_shoe:
                write_shoe.write('Country,Code,Product,Cost,Quantity')
                for shoe in shoe_list:
                    write_shoe.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
        except Exception as e:
            print(f'Error: {e}')

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

    print('Search for Shoe/s in Inventory(Shoe Name, Country or Code)')
    # Prompt user for search term
    search_term = input('> ')

    # Lambda function nested in a filter class - NOTE I know this is complicated but it was the quickest way to get through this task for myself. I do not expect students to even know about lambda initially...
    search_results = list(filter(
        lambda _shoe: 
        _shoe.product.lower() == search_term.lower() or
        _shoe.code.lower() == search_term.lower() or
        _shoe.country.lower() == search_term.lower(), shoe_list))

    # Print search results out
    print(f'\nSEARCH RESULTS ({len(search_results)})')
    for shoe in search_results:
        print(shoe)

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

    # Loop over shoes list
    for shoe in shoe_list:
        # Calculate shoe inventory value
        _value = shoe.get_cost() * shoe.get_quantity()
        # Print the shoe at hand with the total value at the end
        print(shoe, end=f'Shoe Inventory Value: R {round(_value, 2)}\n')

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

    # Use lambda - Order by Quantity
    shoe_list.sort(key=lambda _shoe: _shoe.get_quantity(), reverse=True)

    # Get the lowest quantity shoe object by calling the the first object within the list
    print('Shoe for Sale...\n')
    print(shoe_list[0])
    
# Always load shoe inventory before displaying menu/output
read_shoes_data()

#==========Main Menu=============
while True:
    print('Please select(NUMBER) an option below:')
    print('(0) --- Refresh')
    print('(1) --- Capture shoe data')
    print('(2) --- Check shoe quantity data(returns lowest and gives option to restock the shoe)')
    print('(3) --- Check shoe quantity data(returns shoe with the highest quantity)')
    print('(4) --- Search for a shoe')
    print('(5) --- Calculate and view inventory value of each shoe')
    print('(-1) --- Exit')

    option_selected =  int(input('> '))
    # Match the selected option with the relevant function
    match option_selected:
        case 0:
            read_shoes_data()
        case 1:
            capture_shoes()
        case 2:
            re_stock()
        case 3:
            search_shoe()
        case 4:
            value_per_item()
        case 5:
            highest_qty()
        case -1:
            exit()
        case _:
            print('Invalid Option! Please try again...')
            continue