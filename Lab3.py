
# filename: Team5Lab3
# Author: Angelos Toutsios
# Date: 07/31/2023

# Program Description:
#    This program will create a warehouse system for keeping the quantity of various items
#    and inform the user about these values. It will also allow the user to update a product or even delete it.


def main():
    inventory_list = [] # Initialize the inventory list

    welcome_message = '\nWelcome to the Warehouse Management System!'
    print(welcome_message)

    # While True and Break in order to emulate a do..while loop.
    while True:
        print('\n'+'*'*len(welcome_message)+'\n')  # Separate each iteration with a visual effect!
        action = input("Choose a number [1-3] for the following actions:\n"
                   "    1 - Print the quantity of an item\n"
                   "    2 - Insert/Update an item\n"
                   "    3 - Exit the programm\n"
                   )
        if action == '1':
            item = input('Type the item your are looking for: ')
            quantity = get_quantity(inventory_list, item)
            if quantity != -1: # quantity == -1 means that the items does not exist in warehouse
                print(f'The quantity for {item} is {quantity} !')
        elif action == '2':
            item = input('Type the item your want to update/insert : ')
            new_quantity = int(input(f'Type the new quantity for {item} : ')) # quantity must be an integer
            if new_quantity < 0:
                print('The quantity cannot be a negative number, please try again!')
            else:
                set_quantity(inventory_list, item, new_quantity)
        elif action == '3':
            # Print the available products and their quantity
            print(f'Warehouse inventory consists of: ')
            for i in range(0, len(inventory_list), 2):
                print(f'Item: {inventory_list[i]}, with Quantity: {inventory_list[i+1]}')
            break # break to end the while loop
        else: # other inputs instead of 1-3
            print('Your inputs should be numbers from 1 to 3. Please try again!')


# Insert a new items, updates the quantity of an existing one, delete an item
def set_quantity(inventory_list, item, quantity):
    if item in inventory_list:  # Check if item is in the inventory
        index = inventory_list.index(item)
        if quantity == 0:  # If new quantity is 0 then delete the item
            del inventory_list[index:index+2]
            print(f'The item: {item} deleted successfully!')
        else:
            inventory_list[index + 1] = quantity  # Update the quantity
    else:  # item does not exist, so add it to list
        if quantity > 0:  # Check that the new item does not have a 0 quantity
            new_item = [item, quantity]
            inventory_list.extend(new_item) # extend is used to add a list in the end of an already existed one
        else:
            print('You cannot add a new item with 0 quantity!')
            return  # This return is used in order not to print done!
    print('done!')


def get_quantity(inventory_list, item):
    if item in inventory_list:
        index = inventory_list.index(item)
        return inventory_list[index+1]
    else:
        print('Item you searched for does not exist in inventory!\n'
              'You have to insert it first!')
        return -1


main()
