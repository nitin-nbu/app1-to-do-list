"""
##### To Print
print("Enter a Todo:")

###########################

####### To get user input
print("Enter a todo")
userinput = input()
print(userinput)

# or
user_prompt = input("Enter to do: ")
print(user_prompt)

# or
user_prompt = ("Enter to do: ")
user_input = input(user_prompt)
print(user_input)
"""
##########################
####Store user input in list
"""
user_prompt = "Enter todos: "
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3]
print(todos)
"""
## Print length of inpu
"""
userprompt = input("Enter your todo: ")
print(len(userprompt))
"""

#or
"""
userprompt = input("Enter a title: ")
length = len(userprompt)
print("The lenght of userprompt is:",length)

"""
###############################################################################################################################################################
#  Day 2
####################################################################################################
# Batch Operations ## While loop

""""
user_prompt = ("Enter your todo: ")
todos = []
while True:
    todo = (input(user_prompt))
    todos.append(todo)
    print(todos)
"""

################################################################################################################################
##############################  DAY 3  #########################################################################################
################################################################################################################################

######  To Do List view and program Exit  #########################
# Match case
"""
todos = []

while True:
    user_action = input("Type add or show or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
print("Bye")
"""
#### Use for loop in above code  ####
"""
todos = []

while True:
    user_action = input("Type add or show or exit: ")
    user_action = user_action.strip() #strip function remove space

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case _: # case for invalid values ( other than add show and exit
            print("You entered wrong value")
print("Bye See you later")

"""

#### Add extrea function edit in the program
"""
todos = []

while True:
    user_action = input("Type Add, Show, Edit or Exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    match user_action:
        case 'add':
            todo = input("Enter your todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            change = int(input("What number you want to edit: "))
            change = change - 1
            print(todos[change])
            newtodo = input("Enter new todo: ")
            todos[change] = newtodo
        case 'exit':
            break
print("Bye")
"""

#### 1. To Add number or sr number infront of item in tod list use function enumerate with for loop############
#### 2. Add complete feature in the program so once you complete item will get delete from list#########
#### 3. Storing Item in text file #######
#### Day 7. remove extra space in items when use show feature
### DAY 8. Make change in code (make the code more readable) using "with context manager"
### DAY 9. Add if else condition
### DAY 10 create functions
### DAY 11 Add Argument to the function
#todos = [] ## 3. commanted so todos stores in text file and not in temp list
"""
def get_todos(filepath="todos.txt"): # Day 10 # Day 11 Added 'filepath'
    with open(filepath, 'r') as file_local:  # DAY 10 # Day 11 Added 'filepath'
        todos_local = file_local.readlines()  # DAY 10
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file:  ## DAY 11
        file.writelines(todos_arg)  ## DAY 11
"""
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

#    match user_action: ## Day 9 Match case dosent work in if else
#        case 'add': ## DAY 9
#    if 'add' in user_action: ## Day 9
    if user_action.startswith('add'): # Day 9
    #    todo = input("Enter your todo: ") + '\n' ## Day 9
        todo = user_action[4:] + '\n'# Day 9

    #    file = open('todos.txt', 'r') ##3. to open file todos.txt for reading ## DAY 8
    #    todos = file.readlines() ##3. to read todos.txt ## DAY 8
    #    file.close() ## DAY 8

    #    with open('todos.txt', 'r') as file: # DAY 8 ## Day 10
    #        todos = file.readlines() # DAY 8 ## Day 10
        todos = functions.get_todos() # Day 11

        todos.append(todo)

    #    file = open('todos.txt', 'w') ##3. to open file todos.txt for writing ## DAY 8
    #    file.writelines(todos) ##3. to write in todos.txt ## DAY 8
    #    file.close() ## DAY 8

 #       with open('todos.txt', 'w') as file: # DAY 8 ## Day 11
 #           file.writelines(todos) # DAY 8 ##Day 11
        functions.write_todos(todos) # Day 11

    #case 'show': ## DAY 9
    #    file = open('todos.txt', 'r')  ##3. to open file todos.txt for reading ## DAY 8
    #    todos = file.readlines()  ##3. to read todos.txt ## DAY 8
    #    file.close() ## DAY 8
    elif 'show' in user_action:

    #    with open ('todos.txt', 'r') as file: # DAY 8, ## Day 10
    #        todos = file.readlines() # DAY 8, Day 10
        todos = functions.get_todos() # Day 10 #Day 11
### commented process is lengthy
    #    new_todos = [] ## Day 7 create new empty list

     #   for item in todos: ## Day 7 for loop to itrate items in todos
      #      new_item = item.strip('\n') ## Day 7 strip the itrated item to remove extra space
      #      new_todos.append(new_item)### appended in the new list

        for index, item in enumerate(todos):
            item = item.strip('\n') ## Day 7. this code is similer to the above commented process
            row = (f"{index +1}. {item}")
            print(row)
   # case 'edit': ## Day 9
 #   elif 'edit' in user_action: ## Day 9
    elif user_action.startswith('edit'): # Day 9


#        change = int(input("What number you want to edit: "))## Day 9
        try: # Day 9
            change = int(user_action[5:])
            print(change)
            change = change - 1
            print(todos[change])

        #    with open ('todos.txt', 'r') as file: # DAY 8, ##Day 10
        #        todos = file.readlines() # DAY 8, ##Day 10
            todos = functions.get_todos()


            newtodo = input("Enter new todo: ")
            todos[change] = newtodo + '\n'

#            with open ('todos.txt', 'w') as file: # DAY 8 ## Day 11
#                file.writelines(todos) # DAY 8 ## Day 11
            functions.write_todos(todos) # Day 11
        except ValueError:
            print("command is not valid")
            continue

    #case 'complete': ## 2. added complete feature ## Day 9
 #   elif 'complete' in user_action: ## Day 9
    elif user_action.startswith('complete'): # Day 9
#        done = int(input("What number you want to complete: ")) ## Day 9
        try: ## Day 9
            done = int(user_action[9:])

        #    with open ('todos.txt', 'r') as file: # DAY 8, ##Day10
        #        todos = file.readlines() # DAY 8, ##Day10
            todos = functions.get_todos()

            print(todos.pop(done-1))

        #    with open ('todos.txt', 'w') as file: # DAY 8 ##Day 11
        #        file.writelines(todos) ## DAY 8 ##Day 11
            functions.write_todos(todos) # Day 11
        except IndexError: # Day 9
            print("there is no item with this number")
            continue # Day 9
#     case 'exit': ## Day 9
 #   elif 'exit' in user_action: ## Day 9
    elif user_action.startswith('exit'): # Day 9
        break
    else:
        print("Command is not valid")
print("Bye")








