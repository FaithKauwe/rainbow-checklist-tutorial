# https://github.com/FaithKauwe/rainbow-checklist-tutorial.git

# print("Hello World")

checklist = list()
checklist.append('Blue')

checklist.append('Orange')


# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

checklist = ['Blue', 'Orange']
checklist[1] = 'Cats'
print(checklist)

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

# ADDS CHECKMARK
def mark_completed(index):
    checklist[index] = ("{} {}".format("√", checklist[index]))

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
    # Read item
    elif function_code == "R":
        item_index = int(user_input("Index Number?"))
        # Remember that item_index must actually exist or our program will crash.
        read(item_index)
    # Print all items
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
        # This is where we want to stop our loop
        return False
    # Catch all
    else:
        print("Unknown Option")

running = True
while running:
    selection = user_input(f"Enter a letter: \nC adds to the list\n U replaces an item\n D deletes an item\n R prints an item from an index number\n P displays the list\n Q exits the loop, \n Enter here:")
    running = select(selection)
    if user_input not in ['C', 'U', 'D', 'R', 'P', 'Q']:
        print("{}Not an option{}")
    else:
        os.system('clear')

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(read(1))

    list_all_items()

# call the test funciton
test()

